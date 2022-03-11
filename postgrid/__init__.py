import requests

pm_base = 'https://api.postgrid.com/print-mail/v1/'
av_base = 'https://api.postgrid/com/v1/'

pm_key = None
av_key = None

MAX_LIMIT=100

def _is_file_like(f):
    return hasattr(f, 'read')

def _camel_to_snake(s):
    new_s = ''

    for i, ch in enumerate(s):
        if i > 0 and ch.isupper() and s[i - 1].islower():
            new_s += '_' + ch.lower()
        else:
            new_s += ch

    return new_s

def _snake_to_camel(s):
    new_s = ''

    for i, ch in enumerate(s):
        if s[i] == '_':
            continue

        if i > 0 and s[i - 1] == '_':
            new_s += ch.upper()
        else:
            new_s += ch
        
    return new_s

def _camel_to_snake_dict_keys_recursive(d):
    if isinstance(d, list):
        return list(map(_camel_to_snake_dict_keys_recursive, d))
    elif not isinstance(d, dict):
        return d

    new_d = {}

    for key, value in d.items():
        new_d[_camel_to_snake(key)] = _camel_to_snake_dict_keys_recursive(value)

    return new_d

def _request(base, endpoint, method='GET', **kwargs):
    assert base in [pm_base, av_base]
    
    headers = {'x-api-key': pm_key if base == pm_base else av_key}

    if method == 'GET':
        res = requests.get(base + endpoint, params=kwargs, headers=headers)
    elif method == 'POST':
        data = []
        files = None

        def flatten(key, value):
            if _is_file_like(value):
                if not files:
                    files = {}

                files[key] = value
            elif isinstance(value, dict):
                for inner_key, inner_value in value.items():
                    flatten(f'{key}[{inner_key}]', inner_value)
            elif isinstance(value, list):
                for inner_value in value:
                    flatten(f'{key}[]', inner_value)
            elif value is not None:
                data.append((key, value))

        for key, value in kwargs.items():
            flatten(key, value)
        
        res = requests.post(base + endpoint, data=data, files=files, headers=headers)
    elif method == 'DELETE':
        res = requests.delete(base + endpoint, params=kwargs, headers=headers)
    else:
        raise NotImplementedError()

    value = res.json()

    try:
        res.raise_for_status()
    except requests.HTTPError as e:
        if base == pm_base:
            raise PMError(status_code=res.status_code,
                          object=value['object'],
                          type=value['error']['type'],
                          message=value['error']['message'])
        else:
            raise NotImplementedError()

    if base == pm_base:
        return _pm_convert_json_value(value)
    else:
        raise NotImplementedError()

def _pm_get(endpoint, **kwargs):
    return _request(pm_base, endpoint, method='GET', **kwargs)

def _pm_post(endpoint, **kwargs):
    return _request(pm_base, endpoint, method='POST', **kwargs)

def _pm_delete(endpoint, **kwargs):
    return _request(pm_base, endpoint, method='DELETE', **kwargs)

class PMError(Exception):
    def __init__(self, status_code, object, type, message):
        super().__init__(message)

        self.status_code = status_code
        self.object = object
        self.type = type
        self.message = message

class PMResource:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def _create(cls, locals_):
        assert 'cls' in locals_
        assert 'kwargs' in locals_

        locals_except_kwargs_and_cls = {
            _snake_to_camel(key): value for key, value in locals_.items() if key != 'kwargs' and key != 'cls'
        }

        return _pm_post(cls.endpoint, **locals_except_kwargs_and_cls, **locals_['kwargs'])

    @classmethod
    def list(cls, skip=0, limit=10):
        return _pm_get('contacts', skip=skip, limit=limit)
    
    @classmethod
    def list_autopaginate(cls, max=None):
        # We call the derived class's list method repeatedly
        
        # FIXME: Wasteful because we request MAX_LIMIT always and then potentially discard
        # a certain number of contacts.
        data = []
        last_total_count = None

        while True:
            list_ = cls.list(skip=len(data),
                             limit=MAX_LIMIT)

            data.extend(list_.data)
            last_total_count = list_.total_count

            if len(data) >= list_.total_count or \
               (max and len(data) >= max):
                break
        
        if max:
            data = data[:max]

        return List(
            object='list',
            total_count=last_total_count,
            skip=0,
            limit=max if max else len(data),
            data=data
        )

    @classmethod
    def retrieve(cls, id):
        return _pm_get(f'{cls.endpoint}/{id}')

    @classmethod
    def delete(cls, id):
        return _pm_delete(f'{cls.endpoint}/{id}')
 
    def to_dict(self):
        return vars(self)

class List(PMResource):
    def __init__(self, object, total_count, skip, limit, data):
        self.object = object
        self.total_count = total_count
        self.skip = skip
        self.limit = limit

        if len(data) > 0 and isinstance(data[0], dict):
            data = list(map(_pm_convert_json_value, data))

        self.data = data

class Contact(PMResource):
    endpoint = 'contacts'

    @classmethod
    def create(cls, address_line1, country_code, first_name=None, last_name=None,
               company_name=None, address_line2=None, city=None,
               province_or_state=None, email=None, phone_number=None,
               job_title=None, postal_or_zip=None, **kwargs):
        return cls._create(locals())

class Template(PMResource):
    endpoint = 'templates'

    @classmethod
    def create(cls, html, **kwargs):
        return cls._create(locals())

class BankAccount(PMResource):
    endpoint = 'bank_accounts'

    @classmethod
    def create(cls, bank_name, account_number, bank_primary_line,
                    bank_country_code, transit_number=None, route_number=None, 
                    routing_number=None, signature_image=None, signature_text=None,
                    bank_secondary_line=None):
        cls._create(locals())

PM_OBJECT_TO_CLASS = {
    'contact': Contact,
    'template': Template,
    'list': List
}

def _pm_convert_json_value(value):
    for key, inner_value in value.items():
        if key != 'metadata' and isinstance(inner_value, dict) and 'object' in inner_value:
            value[_camel_to_snake(key)] = _pm_convert_json_value(inner_value)

    return PM_OBJECT_TO_CLASS[value['object']](**_camel_to_snake_dict_keys_recursive(value))
