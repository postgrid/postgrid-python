import requests

pm_base = 'https://api.postgrid.com/print-mail/v1/'
av_base = 'https://api.postgrid/com/v1/'

pm_key = None
av_key = None

MAX_LIMIT = 100
KNOWN_ABBREVS = {'HTML', 'URL', 'ID'}


def _is_file_like(f):
    return hasattr(f, 'read')


def _camel_to_snake(s):
    new_s = ''

    # Turn keys like frontHTML to frontHtml so it converts to front_html
    # instead of front_hTML
    for abbrev in KNOWN_ABBREVS:
        s = s.replace(abbrev, abbrev[0] + abbrev[1:].lower())

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


def _map_keys_recursive(d, fn):
    if isinstance(d, list):
        return list(map(lambda v: _map_keys_recursive(v, fn), d))
    elif not isinstance(d, dict):
        return d

    new_d = {}

    for key, value in d.items():
        new_d[fn(key)] = _map_keys_recursive(value, fn)

    return new_d


def _request(base, endpoint, method='GET', **kwargs):
    assert base in [pm_base, av_base]

    kwargs = _map_keys_recursive(kwargs, _snake_to_camel)

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

        res = requests.post(base + endpoint, data=data,
                            files=files, headers=headers)
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
            key: value for key, value in locals_.items() if key != 'kwargs' and key != 'cls'
        }

        return _pm_post(cls.endpoint, **locals_except_kwargs_and_cls, **locals_['kwargs'])

    @classmethod
    def _progress(cls, id):
        return _pm_post(f'{cls.endpoint}/{id}/progressions')

    @classmethod
    def list(cls, skip=0, limit=10):
        return _pm_get(cls.endpoint, skip=skip, limit=limit)

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
               bank_secondary_line=None, **kwargs):
        return cls._create(locals())


class Letter(PMResource):
    endpoint = 'letters'

    @classmethod
    def create(cls, to, from_, template=None, html=None, pdf=None, extra_service=None,
               express=None, address_placement=None, perforated_page=None, envelope_type=None,
               color=None, double_sided=None, return_envelope=None, send_date=None, merge_variables=None,
               **kwargs):
        return cls._create(locals())

    
    @classmethod
    def progress(cls, id):
        return cls._progress(id)


class Postcard(PMResource):
    endpoint = 'postcards'

    @classmethod
    def create(cls, to, size, from_=None, front_template=None, back_template=None, 
               front_html=None, back_html=None, pdf=None, express=None, send_date=None, 
               merge_variables=None, **kwargs):
        return cls._create(locals())

    @classmethod
    def progress(cls, id):
        return cls._progress(id)


PM_OBJECT_TO_CLASS = {
    'contact': Contact,
    'template': Template,
    'bank_account': BankAccount,
    'letter': Letter,
    'postcard': Postcard,
    'list': List
}


def _pm_convert_json_value(value):
    for key, inner_value in value.items():
        if key != 'metadata' and isinstance(inner_value, dict) and 'object' in inner_value:
            value[_camel_to_snake(key)] = _pm_convert_json_value(inner_value)

    return PM_OBJECT_TO_CLASS[value['object']](**_map_keys_recursive(value, _camel_to_snake))
