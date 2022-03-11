import requests

pm_base = 'https://api.postgrid.com/print-mail/v1/'
av_base = 'https://api.postgrid/com/v1/'

pm_key = None
av_key = None

def _camel_to_snake(s):
    new_s = ''

    for i, ch in enumerate(s):
        if i > 0 and ch.isupper() and s[i - 1].islower():
            new_s += '_' + ch.lower()
        else:
            new_s += ch

    return new_s

def _camel_to_snake_dict_keys_recursive(d):
    if isinstance(d, list):
        return map(_camel_to_snake_dict_keys_recursive, d)
    elif not isinstance(d, dict):
        return d

    new_d = {}

    for key, value in d.items():
        new_d[_camel_to_snake(key)] = _camel_to_snake_dict_keys_recursive(value)

    return new_d

def _request(base, endpoint, method='GET', **kwargs):
    headers = {'x-api-key': pm_key if base == pm_base else av_key}

    if method == 'GET':
        res = requests.get(base + endpoint, params=kwargs, headers=headers)
    elif method == 'POST':
        res = requests.post(base + endpoint, json=kwargs, headers=headers)
    elif method == 'DELETE':
        res = requests.delete(base + endpoint, params=kwargs, headers=headers)
    else:
        raise NotImplementedError()

    res.raise_for_status()

    return _convert_json_value(res.json())

def _pm_get(endpoint, **kwargs):
    return _request(pm_base, endpoint, method='GET', **kwargs)

def _pm_post(endpoint, **kwargs):
    return _request(pm_base, endpoint, method='POST', **kwargs)

class PMResource:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def to_dict(self):
        return vars(self)

class List(PMResource):
    def __init__(self, total_count, skip, limit, data):
        self.total_count = total_count
        self.skip = skip
        self.limit = limit
        self.data = map(_convert_json_value, data)

class Contact(PMResource):
    @staticmethod
    def list(skip, limit):
        return _pm_get('contacts', skip, limit)

    @staticmethod
    def retrieve(id):
        return _pm_get('contacts/' + id)

    @staticmethod
    def create(address_line1, country_code, first_name=None, last_name=None,
               company_name=None, address_line2=None, city=None,
               province_or_state=None, email=None, phone_number=None,
               job_title=None, postal_or_zip=None, **kwargs):
        return _pm_post('contacts', 
                 addressLine1=address_line1,
                 addressLine2=address_line2,
                 city=city,
                 provinceOrState=province_or_state,
                 postalOrZip=postal_or_zip,
                 countryCode=country_code,
                 firstName=first_name,
                 lastName=last_name,
                 companyName=company_name,
                 email=email,
                 phoneNumber=phone_number,
                 jobTitle=job_title,
                 **kwargs)

OBJECT_TO_CLASS = {
    'contact': Contact
}

def _convert_json_value(value):
    return OBJECT_TO_CLASS[value['object']](**_camel_to_snake_dict_keys_recursive(value))
