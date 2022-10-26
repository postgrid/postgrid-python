import requests
import jwt
import os

pm_base = 'https://api.postgrid.com/print-mail/v1/'
av_base = 'https://api.postgrid/com/v1/'

pm_key = None
av_key = None

MAX_LIMIT = 100
KNOWN_ABBREVS = {'HTML', 'URL', 'ID', 'PDF'}


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

    return new_s.lower()


def _snake_to_camel(s):
    new_s = ''

    # Convert e.g. letter_html to letter_HTML so that
    # we transmit letterHTML as intended. We match on the '_' + abbrev
    # so that we don't replace e.g. double_sided with double_sIDed.
    for abbrev in KNOWN_ABBREVS:
        lower_abbrev = f'_{abbrev.lower()}'
        lower_abbrev_index = s.find(lower_abbrev)

        if lower_abbrev_index > 0:
            s = s.replace(lower_abbrev, abbrev.upper())

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
        # HACK We should not mess with the camel/snake casing of merge variables/metadata
        new_d[fn(key)] = value if key == 'metadata' or key == 'merge_variables' \
            else _map_keys_recursive(value, fn)

    return new_d


class UnsupportedFileTypeError(Exception):
    def __init__(self, ext):
        self.ext = ext


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
            nonlocal files

            if _is_file_like(value):
                if not files:
                    files = {}

                path, ext = os.path.splitext(value.name)

                if ext == '.pdf':
                    content_type = 'application/pdf'
                elif ext == '.png':
                    content_type = 'image/png'
                elif ext == '.jpeg':
                    content_type = 'image/jpeg'
                else:
                    # TODO Make sure we don't expect any other file types
                    raise UnsupportedFileTypeError(ext)

                files[key] = (os.path.basename(path), value, content_type)
            elif isinstance(value, dict):
                for inner_key, inner_value in value.items():
                    flatten(f'{key}[{inner_key}]', inner_value)
            elif isinstance(value, list):
                for inner_value in value:
                    flatten(f'{key}[]', inner_value)
            elif isinstance(value, bool):
                data.append((key, 'true' if value else 'false'))
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


class CreateableResource:
    @classmethod
    def create(cls, locals_, parent_resource_id=None):
        assert 'cls' in locals_
        assert 'kwargs' in locals_

        locals_except_kwargs_and_cls = {
            key: value for key, value in locals_.items() if key != 'kwargs' and key != 'cls'
        }

        return _pm_post(cls.endpoint.format(parent_resource_id), **locals_except_kwargs_and_cls, **locals_['kwargs'])


class ProgressableResource:
    @classmethod
    def progress(cls, id):
        return _pm_post(f'{cls.endpoint}/{id}/progressions')


class ListableResource:
    @classmethod
    def list(cls, skip=0, limit=10, parent_resource_id=None, search=None):
        return _pm_get(cls.endpoint.format(parent_resource_id), skip=skip, limit=limit, search=search)

    @classmethod
    def list_autopaginate(cls, max=None, parent_resource_id=None, search=None):
        # We call the derived class's list method repeatedly

        # FIXME: Wasteful because we request MAX_LIMIT always and then potentially discard
        # a certain number of contacts.
        data = []
        last_total_count = None

        while True:
            list_ = cls.list(skip=len(data),
                             limit=MAX_LIMIT,
                             parent_resource_id=parent_resource_id,
                             search=search)

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


class RetrieveableResource:
    @classmethod
    def retrieve(cls, id, parent_resource_id=None, **kwargs):
        return _pm_get(f'{cls.endpoint.format(parent_resource_id)}/{id}', **kwargs)


class UpdatableResource:
    @classmethod
    def update(cls, id, locals_, parent_resource_id=None, **kwargs):
        # HACK This is copied from create, the only difference is the endpoint
        assert 'cls' in locals_
        assert 'kwargs' in locals_

        locals_except_kwargs_and_cls = {
            key: value for key, value in locals_.items() if key != 'kwargs' and key != 'cls'
        }

        return _pm_post(f'{cls.endpoint.format(parent_resource_id)}/{id}', **locals_except_kwargs_and_cls, **locals_['kwargs'])


class DeleteableResource:
    @classmethod
    def delete(cls, id, parent_resource_id=None):
        return _pm_delete(f'{cls.endpoint.format(parent_resource_id)}/{id}')


class BaseResource:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class List:
    def __init__(self, object, total_count, skip, limit, data):
        self.object = object
        self.total_count = total_count
        self.skip = skip
        self.limit = limit

        if len(data) > 0 and isinstance(data[0], dict):
            data = list(map(_pm_convert_json_value, data))

        self.data = data


class Contact(BaseResource,
              CreateableResource,
              RetrieveableResource,
              ListableResource,
              DeleteableResource):
    endpoint = 'contacts'

    @classmethod
    def create(cls, address_line1, country_code, first_name=None, last_name=None,
               company_name=None, address_line2=None, city=None,
               province_or_state=None, email=None, phone_number=None,
               job_title=None, postal_or_zip=None, **kwargs):
        return super().create(locals())


class Template(BaseResource,
               CreateableResource,
               RetrieveableResource,
               ListableResource,
               DeleteableResource):
    endpoint = 'templates'

    @classmethod
    def create(cls, html, **kwargs):
        return super().create(locals())


class BankAccount(BaseResource,
                  CreateableResource,
                  RetrieveableResource,
                  ListableResource,
                  DeleteableResource):
    endpoint = 'bank_accounts'

    @classmethod
    def create(cls, bank_name, account_number, bank_primary_line,
               bank_country_code, transit_number=None, route_number=None,
               routing_number=None, signature_image=None, signature_text=None,
               bank_secondary_line=None, **kwargs):
        return super().create(locals())


class Letter(BaseResource,
             CreateableResource,
             RetrieveableResource,
             ListableResource,
             ProgressableResource,
             DeleteableResource):
    endpoint = 'letters'

    @classmethod
    def create(cls, to, from_, template=None, html=None, pdf=None, extra_service=None,
               express=None, address_placement=None, perforated_page=None, envelope_type=None,
               color=None, double_sided=None, return_envelope=None, send_date=None, merge_variables=None,
               **kwargs):
        return super().create(locals())


class Postcard(BaseResource,
               CreateableResource,
               RetrieveableResource,
               ListableResource,
               ProgressableResource,
               DeleteableResource):
    endpoint = 'postcards'

    @classmethod
    def create(cls, to, size, from_=None, front_template=None, back_template=None,
               front_html=None, back_html=None, pdf=None, express=None, send_date=None,
               merge_variables=None, **kwargs):
        return super().create(locals())


class Cheque(BaseResource,
             CreateableResource,
             RetrieveableResource,
             ListableResource,
             ProgressableResource,
             DeleteableResource):
    endpoint = 'cheques'

    @classmethod
    def create(cls, to, from_, bank_account, amount, number=None, message=None, memo=None,
               letter_html=None, letter_template=None, letter_pdf=None, extra_service=None,
               express=None, send_date=None, redirect_to=None, logo=None, currency_code=None,
               merge_variables=None, **kwargs):
        return super().create(locals())


class ReturnEnvelopeOrder(BaseResource,
                          CreateableResource,
                          RetrieveableResource,
                          ListableResource,
                          DeleteableResource):
    endpoint = 'return_envelopes/{}/orders'

    @classmethod
    def create(cls, return_envelope_id, quantity_ordered, **kwargs):
        return super().create(locals(), parent_resource_id=return_envelope_id)

    @classmethod
    def retrieve(cls, return_envelope_id, id):
        return super().retrieve(id, return_envelope_id)

    @classmethod
    def list(cls, return_envelope_id, skip=0, limit=10, search=None):
        return super().list(skip, limit, return_envelope_id, search=search)

    @classmethod
    def list_autopaginate(cls, return_envelope_id, max=None, search=None):
        return super().list_autopaginate(max, return_envelope_id, search=search)

    @classmethod
    def fill(cls, return_envelope_id, id):
        return _pm_post(f'{cls.endpoint.format(return_envelope_id)}/{id}/fills')

    @classmethod
    def delete(cls, return_envelope_id, id):
        return super().delete(id, return_envelope_id)


class ReturnEnvelope(BaseResource,
                     CreateableResource,
                     RetrieveableResource,
                     ListableResource):
    endpoint = 'return_envelopes'

    @classmethod
    def create(cls, to, **kwargs):
        return super().create(locals())


class WebhookEvent:
    def __init__(self, type_, data):
        self.type = type_
        self.data = data


class SignatureVerificationError(Exception):
    pass


class WebhookInvocation(BaseResource,
                        ListableResource):
    endpoint = 'webhooks/{}/invocations'

    @classmethod
    def list(cls, webhook_id, skip=0, limit=0, search=None):
        return super().list(skip, limit, webhook_id, search=search)

    @classmethod
    def list_autopaginate(cls, webhook_id, max=None, search=None):
        return super().list_autopaginate(max, webhook_id, search=search)


class Webhook(BaseResource,
              CreateableResource,
              RetrieveableResource,
              ListableResource,
              UpdatableResource,
              DeleteableResource):
    endpoint = 'webhooks'

    @classmethod
    def create(cls, enabled_events, url, **kwargs):
        return cls.create(locals())

    @classmethod
    def update(cls, id, enabled_events, url, **kwargs):
        return cls.update(id, locals())

    @ classmethod
    def construct_event(cls, payload, secret):
        try:
            event = jwt.decode(payload, secret, algorithms='HS256')

            type_ = event['type']
            event['data']['object'] = type_.split('.')[0]

            return WebhookEvent(
                type_=type_,
                data=_pm_convert_json_value(event['data'])
            )
        except jwt.exceptions.InvalidSignatureError:
            raise SignatureVerificationError()
        except jwt.exceptions.InvalidTokenError:
            raise ValueError()


PM_OBJECT_TO_CLASS = {
    'contact': Contact,
    'template': Template,
    'bank_account': BankAccount,
    'letter': Letter,
    'postcard': Postcard,
    'cheque': Cheque,
    'webhook': Webhook,
    'webhook_invocation': WebhookInvocation,
    'return_envelope': ReturnEnvelope,
    'return_envelope_order': ReturnEnvelopeOrder,
    'list': List
}


def _pm_convert_json_value(value):
    new_value = {}

    for key, inner_value in value.items():
        # HACK We convert mergeVariables to merge_variables but we
        # do not convert the inner value
        if key == 'mergeVariables' and isinstance(inner_value, dict):
            new_value[_camel_to_snake(key)] = inner_value
            continue

        if key != 'metadata' and isinstance(inner_value, dict) and 'object' in inner_value:
            new_value[_camel_to_snake(key)] = _pm_convert_json_value(inner_value)
            continue

        new_value[key] = inner_value

    return PM_OBJECT_TO_CLASS[new_value['object']](**_map_keys_recursive(new_value, _camel_to_snake))
