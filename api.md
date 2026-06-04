# AddressVerification

Types:

```python
from postgrid.types import (
    Errors,
    Status,
    AddressVerificationAutocompleteResponse,
    AddressVerificationBatchVerificationResponse,
    AddressVerificationGetAutocompletePreviewsResponse,
    AddressVerificationGetLookupInfoResponse,
    AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse,
    AddressVerificationLookupZipCodeFromCityOrStateResponse,
    AddressVerificationParseAnAddressResponse,
    AddressVerificationSuggestAddressesResponse,
    AddressVerificationVerifyResponse,
)
```

Methods:

- <code title="post /v1/addver/completions">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">autocomplete</a>(\*\*<a href="src/postgrid/types/address_verification_autocomplete_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_autocomplete_response.py">AddressVerificationAutocompleteResponse</a></code>
- <code title="post /v1/addver/verifications/batch">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">batch_verification</a>(\*\*<a href="src/postgrid/types/address_verification_batch_verification_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_batch_verification_response.py">AddressVerificationBatchVerificationResponse</a></code>
- <code title="get /v1/addver/completions">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">get_autocomplete_previews</a>(\*\*<a href="src/postgrid/types/address_verification_get_autocomplete_previews_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_get_autocomplete_previews_response.py">AddressVerificationGetAutocompletePreviewsResponse</a></code>
- <code title="get /v1/addver/">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">get_lookup_info</a>() -> <a href="./src/postgrid/types/address_verification_get_lookup_info_response.py">AddressVerificationGetLookupInfoResponse</a></code>
- <code title="post /v1/addver/city_states">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">lookup_city_or_state_from_postal_or_zip_code</a>(\*\*<a href="src/postgrid/types/address_verification_lookup_city_or_state_from_postal_or_zip_code_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_lookup_city_or_state_from_postal_or_zip_code_response.py">AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse</a></code>
- <code title="post /v1/addver/zip_codes">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">lookup_zip_code_from_city_or_state</a>(\*\*<a href="src/postgrid/types/address_verification_lookup_zip_code_from_city_or_state_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_lookup_zip_code_from_city_or_state_response.py">AddressVerificationLookupZipCodeFromCityOrStateResponse</a></code>
- <code title="post /v1/addver/parses">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">parse_an_address</a>(\*\*<a href="src/postgrid/types/address_verification_parse_an_address_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_parse_an_address_response.py">AddressVerificationParseAnAddressResponse</a></code>
- <code title="post /v1/addver/suggestions">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">suggest_addresses</a>(\*\*<a href="src/postgrid/types/address_verification_suggest_addresses_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_suggest_addresses_response.py">AddressVerificationSuggestAddressesResponse</a></code>
- <code title="post /v1/addver/verifications">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">verify</a>(\*\*<a href="src/postgrid/types/address_verification_verify_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_verify_response.py">AddressVerificationVerifyResponse</a></code>

# IntlAddressVerification

Types:

```python
from postgrid.types import (
    IntlAddressVerificationAutocompleteResponse,
    IntlAddressVerificationBatchVerificationResponse,
    IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
    IntlAddressVerificationGetAutocompletePreviewsResponse,
    IntlAddressVerificationVerifyResponse,
)
```

Methods:

- <code title="post /v1/intl_addver/completions">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">autocomplete</a>(\*\*<a href="src/postgrid/types/intl_address_verification_autocomplete_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_autocomplete_response.py">IntlAddressVerificationAutocompleteResponse</a></code>
- <code title="post /v1/intl_addver/verifications/batch">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">batch_verification</a>(\*\*<a href="src/postgrid/types/intl_address_verification_batch_verification_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_batch_verification_response.py">IntlAddressVerificationBatchVerificationResponse</a></code>
- <code title="get /v1/intl_addver/completions">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">get_autocomplete_advanced_previews</a>(\*\*<a href="src/postgrid/types/intl_address_verification_get_autocomplete_advanced_previews_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_get_autocomplete_advanced_previews_response.py">IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse</a></code>
- <code title="get /v1/intl_addver/completions">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">get_autocomplete_previews</a>(\*\*<a href="src/postgrid/types/intl_address_verification_get_autocomplete_previews_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_get_autocomplete_previews_response.py">IntlAddressVerificationGetAutocompletePreviewsResponse</a></code>
- <code title="post /v1/intl_addver/verifications">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">verify</a>(\*\*<a href="src/postgrid/types/intl_address_verification_verify_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_verify_response.py">IntlAddressVerificationVerifyResponse</a></code>

# PrintMail

## Contacts

Types:

```python
from postgrid.types.print_mail import (
    Contact,
    ContactCreate,
    ContactCreateWithCompanyName,
    ContactCreateWithFirstName,
    ContactDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/contacts">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/contact_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/contact.py">Contact</a></code>
- <code title="get /print-mail/v1/contacts/{id}">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/contact.py">Contact</a></code>
- <code title="get /print-mail/v1/contacts">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/contact_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/contact.py">SyncSkipLimit[Contact]</a></code>
- <code title="delete /print-mail/v1/contacts/{id}">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/contact_delete_response.py">ContactDeleteResponse</a></code>

## Templates

Types:

```python
from postgrid.types.print_mail import Template, TemplateDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/templates">client.print_mail.templates.<a href="./src/postgrid/resources/print_mail/templates.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/template_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/template.py">Template</a></code>
- <code title="get /print-mail/v1/templates/{id}">client.print_mail.templates.<a href="./src/postgrid/resources/print_mail/templates.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/template.py">Template</a></code>
- <code title="post /print-mail/v1/templates/{id}">client.print_mail.templates.<a href="./src/postgrid/resources/print_mail/templates.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/template_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/template.py">Template</a></code>
- <code title="get /print-mail/v1/templates">client.print_mail.templates.<a href="./src/postgrid/resources/print_mail/templates.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/template_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/template.py">SyncSkipLimit[Template]</a></code>
- <code title="delete /print-mail/v1/templates/{id}">client.print_mail.templates.<a href="./src/postgrid/resources/print_mail/templates.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/template_delete_response.py">TemplateDeleteResponse</a></code>

## Trackers

Types:

```python
from postgrid.types.print_mail import (
    TrackerCreateResponse,
    TrackerRetrieveResponse,
    TrackerUpdateResponse,
    TrackerListResponse,
    TrackerDeleteResponse,
    TrackerRetrieveVisitsResponse,
)
```

Methods:

- <code title="post /print-mail/v1/trackers">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/tracker_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/tracker_create_response.py">TrackerCreateResponse</a></code>
- <code title="get /print-mail/v1/trackers/{id}">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/tracker_retrieve_response.py">TrackerRetrieveResponse</a></code>
- <code title="post /print-mail/v1/trackers/{id}">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/tracker_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/tracker_update_response.py">TrackerUpdateResponse</a></code>
- <code title="get /print-mail/v1/trackers">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/tracker_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/tracker_list_response.py">SyncSkipLimit[TrackerListResponse]</a></code>
- <code title="delete /print-mail/v1/trackers/{id}">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/tracker_delete_response.py">TrackerDeleteResponse</a></code>
- <code title="get /print-mail/v1/trackers/{id}/visits">client.print_mail.trackers.<a href="./src/postgrid/resources/print_mail/trackers.py">retrieve_visits</a>(id, \*\*<a href="src/postgrid/types/print_mail/tracker_retrieve_visits_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/tracker_retrieve_visits_response.py">SyncSkipLimit[TrackerRetrieveVisitsResponse]</a></code>

## Webhooks

Types:

```python
from postgrid.types.print_mail import Webhook, WebhookInvocation, WebhookDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/webhooks">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/webhook_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/webhook.py">Webhook</a></code>
- <code title="get /print-mail/v1/webhooks/{id}">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/webhook.py">Webhook</a></code>
- <code title="post /print-mail/v1/webhooks/{id}">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/webhook_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/webhook.py">Webhook</a></code>
- <code title="get /print-mail/v1/webhooks">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/webhook_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/webhook.py">SyncSkipLimit[Webhook]</a></code>
- <code title="delete /print-mail/v1/webhooks/{id}">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /print-mail/v1/webhooks/{id}/invocations">client.print_mail.webhooks.<a href="./src/postgrid/resources/print_mail/webhooks.py">list_invocations</a>(id, \*\*<a href="src/postgrid/types/print_mail/webhook_list_invocations_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/webhook_invocation.py">SyncSkipLimit[WebhookInvocation]</a></code>

## Events

Types:

```python
from postgrid.types.print_mail import Event
```

Methods:

- <code title="get /print-mail/v1/events">client.print_mail.events.<a href="./src/postgrid/resources/print_mail/events.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/event_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/event.py">SyncSkipLimit[Event]</a></code>

## Letters

Types:

```python
from postgrid.types.print_mail import (
    AddressPlacement,
    AttachedPdf,
    Letter,
    LetterSize,
    PlasticCard,
    LetterRetrieveURLResponse,
)
```

Methods:

- <code title="post /print-mail/v1/letters">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/letter_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/letter.py">Letter</a></code>
- <code title="get /print-mail/v1/letters/{id}">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/letter.py">Letter</a></code>
- <code title="get /print-mail/v1/letters">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/letter_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/letter.py">SyncSkipLimit[Letter]</a></code>
- <code title="delete /print-mail/v1/letters/{id}">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/letter.py">Letter</a></code>
- <code title="post /print-mail/v1/letters/{id}/cancellation">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">cancel</a>(id, \*\*<a href="src/postgrid/types/print_mail/letter_cancel_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/letter.py">Letter</a></code>
- <code title="post /print-mail/v1/letters/{id}/progressions">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">progress</a>(id) -> <a href="./src/postgrid/types/print_mail/letter.py">Letter</a></code>
- <code title="get /print-mail/v1/letters/{id}/url">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/letter_retrieve_url_response.py">LetterRetrieveURLResponse</a></code>

## Postcards

Types:

```python
from postgrid.types.print_mail import Postcard, PostcardRetrieveURLResponse
```

Methods:

- <code title="post /print-mail/v1/postcards">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/postcard_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/postcard.py">Postcard</a></code>
- <code title="get /print-mail/v1/postcards/{id}">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/postcard.py">Postcard</a></code>
- <code title="get /print-mail/v1/postcards">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/postcard_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/postcard.py">SyncSkipLimit[Postcard]</a></code>
- <code title="delete /print-mail/v1/postcards/{id}">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/postcard.py">Postcard</a></code>
- <code title="post /print-mail/v1/postcards/{id}/cancellation">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">cancel</a>(id, \*\*<a href="src/postgrid/types/print_mail/postcard_cancel_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/postcard.py">Postcard</a></code>
- <code title="post /print-mail/v1/postcards/{id}/progressions">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">progress</a>(id) -> <a href="./src/postgrid/types/print_mail/postcard.py">Postcard</a></code>
- <code title="get /print-mail/v1/postcards/{id}/url">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/postcard_retrieve_url_response.py">PostcardRetrieveURLResponse</a></code>

## BankAccounts

Types:

```python
from postgrid.types.print_mail import BankAccount, BankAccountCountryCode, BankAccountDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/bank_accounts">client.print_mail.bank_accounts.<a href="./src/postgrid/resources/print_mail/bank_accounts.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/bank_account_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/bank_account.py">BankAccount</a></code>
- <code title="get /print-mail/v1/bank_accounts/{id}">client.print_mail.bank_accounts.<a href="./src/postgrid/resources/print_mail/bank_accounts.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/bank_account.py">BankAccount</a></code>
- <code title="get /print-mail/v1/bank_accounts">client.print_mail.bank_accounts.<a href="./src/postgrid/resources/print_mail/bank_accounts.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/bank_account_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/bank_account.py">SyncSkipLimit[BankAccount]</a></code>
- <code title="delete /print-mail/v1/bank_accounts/{id}">client.print_mail.bank_accounts.<a href="./src/postgrid/resources/print_mail/bank_accounts.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/bank_account_delete_response.py">BankAccountDeleteResponse</a></code>

## Cheques

Types:

```python
from postgrid.types.print_mail import Cheque, ChequeSize, DigitalOnly, ChequeRetrieveURLResponse
```

Methods:

- <code title="post /print-mail/v1/cheques">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/cheque_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>
- <code title="get /print-mail/v1/cheques/{id}">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>
- <code title="get /print-mail/v1/cheques">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/cheque_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/cheque.py">SyncSkipLimit[Cheque]</a></code>
- <code title="delete /print-mail/v1/cheques/{id}">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>
- <code title="post /print-mail/v1/cheques/{id}/cancellation">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">cancel</a>(id, \*\*<a href="src/postgrid/types/print_mail/cheque_cancel_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>
- <code title="post /print-mail/v1/cheques/{id}/progressions">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">progress</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>
- <code title="get /print-mail/v1/cheques/{id}/url">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque_retrieve_url_response.py">ChequeRetrieveURLResponse</a></code>
- <code title="get /print-mail/v1/cheques/{id}/with_deposit_ready_pdf">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">retrieve_with_deposit_ready_pdf</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>

## SelfMailers

Types:

```python
from postgrid.types.print_mail import SelfMailer, SelfMailerRetrieveURLResponse
```

Methods:

- <code title="post /print-mail/v1/self_mailers">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/self_mailer_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/self_mailer.py">SelfMailer</a></code>
- <code title="get /print-mail/v1/self_mailers/{id}">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/self_mailer.py">SelfMailer</a></code>
- <code title="get /print-mail/v1/self_mailers">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/self_mailer_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/self_mailer.py">SyncSkipLimit[SelfMailer]</a></code>
- <code title="delete /print-mail/v1/self_mailers/{id}">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/self_mailer.py">SelfMailer</a></code>
- <code title="post /print-mail/v1/self_mailers/{id}/progressions">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">progress</a>(id) -> <a href="./src/postgrid/types/print_mail/self_mailer.py">SelfMailer</a></code>
- <code title="get /print-mail/v1/self_mailers/{id}/url">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/self_mailer_retrieve_url_response.py">SelfMailerRetrieveURLResponse</a></code>

## Campaigns

Types:

```python
from postgrid.types.print_mail import Campaign, CampaignDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/campaigns">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/campaign_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/campaign.py">Campaign</a></code>
- <code title="get /print-mail/v1/campaigns/{id}">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/campaign.py">Campaign</a></code>
- <code title="post /print-mail/v1/campaigns/{id}">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/campaign_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/campaign.py">Campaign</a></code>
- <code title="get /print-mail/v1/campaigns">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/campaign_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/campaign.py">SyncSkipLimit[Campaign]</a></code>
- <code title="delete /print-mail/v1/campaigns/{id}">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/campaign_delete_response.py">CampaignDeleteResponse</a></code>
- <code title="post /print-mail/v1/campaigns/{id}/send">client.print_mail.campaigns.<a href="./src/postgrid/resources/print_mail/campaigns.py">send</a>(id, \*\*<a href="src/postgrid/types/print_mail/campaign_send_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/campaign.py">Campaign</a></code>

## MailingListImports

Types:

```python
from postgrid.types.print_mail import (
    FileType,
    MailingListImportResponse,
    VerificationStatusCount,
    MailingListImportDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/mailing_list_imports">client.print_mail.mailing_list_imports.<a href="./src/postgrid/resources/print_mail/mailing_list_imports.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/mailing_list_import_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list_import_response.py">MailingListImportResponse</a></code>
- <code title="get /print-mail/v1/mailing_list_imports/{id}">client.print_mail.mailing_list_imports.<a href="./src/postgrid/resources/print_mail/mailing_list_imports.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/mailing_list_import_response.py">MailingListImportResponse</a></code>
- <code title="post /print-mail/v1/mailing_list_imports/{id}">client.print_mail.mailing_list_imports.<a href="./src/postgrid/resources/print_mail/mailing_list_imports.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/mailing_list_import_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list_import_response.py">MailingListImportResponse</a></code>
- <code title="get /print-mail/v1/mailing_list_imports">client.print_mail.mailing_list_imports.<a href="./src/postgrid/resources/print_mail/mailing_list_imports.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/mailing_list_import_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list_import_response.py">SyncSkipLimit[MailingListImportResponse]</a></code>
- <code title="delete /print-mail/v1/mailing_list_imports/{id}">client.print_mail.mailing_list_imports.<a href="./src/postgrid/resources/print_mail/mailing_list_imports.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/mailing_list_import_delete_response.py">MailingListImportDeleteResponse</a></code>

## MailingLists

Types:

```python
from postgrid.types.print_mail import MailingList, MailingListUpdate, MailingListDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/mailing_lists">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/mailing_list_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list.py">MailingList</a></code>
- <code title="get /print-mail/v1/mailing_lists/{id}">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/mailing_list.py">MailingList</a></code>
- <code title="post /print-mail/v1/mailing_lists/{id}">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/mailing_list_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list_update.py">MailingListUpdate</a></code>
- <code title="get /print-mail/v1/mailing_lists">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/mailing_list_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list.py">SyncSkipLimit[MailingList]</a></code>
- <code title="delete /print-mail/v1/mailing_lists/{id}">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/mailing_list_delete_response.py">MailingListDeleteResponse</a></code>
- <code title="post /print-mail/v1/mailing_lists/{id}/jobs">client.print_mail.mailing_lists.<a href="./src/postgrid/resources/print_mail/mailing_lists.py">jobs</a>(id, \*\*<a href="src/postgrid/types/print_mail/mailing_list_jobs_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/mailing_list.py">MailingList</a></code>

## Reports

Types:

```python
from postgrid.types.print_mail import DeletedResponse, Report
```

Methods:

- <code title="post /print-mail/v1/reports">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/report_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/report.py">Report</a></code>
- <code title="get /print-mail/v1/reports/{id}">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/report.py">Report</a></code>
- <code title="post /print-mail/v1/reports/{id}">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/report_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/report.py">Report</a></code>
- <code title="get /print-mail/v1/reports">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/report_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/report.py">SyncSkipLimit[Report]</a></code>
- <code title="delete /print-mail/v1/reports/{id}">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/deleted_response.py">DeletedResponse</a></code>
- <code title="post /print-mail/v1/reports/samples">client.print_mail.reports.<a href="./src/postgrid/resources/print_mail/reports/reports.py">sample</a>(\*\*<a href="src/postgrid/types/print_mail/report_sample_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/reports/report_sample.py">ReportSample</a></code>

### Samples

Types:

```python
from postgrid.types.print_mail.reports import ReportSample, ReportSampleCreateBase
```

Methods:

- <code title="post /print-mail/v1/reports/{id}/samples">client.print_mail.reports.samples.<a href="./src/postgrid/resources/print_mail/reports/samples.py">create</a>(id, \*\*<a href="src/postgrid/types/print_mail/reports/sample_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/reports/report_sample.py">ReportSample</a></code>

### Exports

Types:

```python
from postgrid.types.print_mail.reports import ReportExport
```

Methods:

- <code title="post /print-mail/v1/reports/{reportID}/exports">client.print_mail.reports.exports.<a href="./src/postgrid/resources/print_mail/reports/exports.py">create</a>(report_id, \*\*<a href="src/postgrid/types/print_mail/reports/export_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/reports/report_export.py">ReportExport</a></code>
- <code title="get /print-mail/v1/reports/{reportID}/exports/{exportID}">client.print_mail.reports.exports.<a href="./src/postgrid/resources/print_mail/reports/exports.py">retrieve</a>(export_id, \*, report_id) -> <a href="./src/postgrid/types/print_mail/reports/report_export.py">ReportExport</a></code>
- <code title="delete /print-mail/v1/reports/{reportID}/exports/{exportID}">client.print_mail.reports.exports.<a href="./src/postgrid/resources/print_mail/reports/exports.py">delete</a>(export_id, \*, report_id) -> <a href="./src/postgrid/types/print_mail/deleted_response.py">DeletedResponse</a></code>

## SubOrganizations

Types:

```python
from postgrid.types.print_mail import (
    EmailPreferences,
    SubOrganization,
    SubOrganizationCreateResponse,
    SubOrganizationRetrieveUsersResponse,
)
```

Methods:

- <code title="post /print-mail/v1/sub_organizations">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/sub_organization_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization_create_response.py">SubOrganizationCreateResponse</a></code>
- <code title="get /print-mail/v1/sub_organizations/{id}">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/sub_organization.py">SubOrganization</a></code>
- <code title="get /print-mail/v1/sub_organizations">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/sub_organization_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization.py">SyncSkipLimit[SubOrganization]</a></code>
- <code title="get /print-mail/v1/sub_organizations/{id}/users">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">retrieve_users</a>(id, \*\*<a href="src/postgrid/types/print_mail/sub_organization_retrieve_users_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization_retrieve_users_response.py">SubOrganizationRetrieveUsersResponse</a></code>

## Boxes

Types:

```python
from postgrid.types.print_mail import (
    BoxCreateResponse,
    BoxRetrieveResponse,
    BoxListResponse,
    BoxDeleteResponse,
    BoxProgressionsResponse,
)
```

Methods:

- <code title="post /print-mail/v1/boxes">client.print_mail.boxes.<a href="./src/postgrid/resources/print_mail/boxes.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/box_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/box_create_response.py">BoxCreateResponse</a></code>
- <code title="get /print-mail/v1/boxes/{id}">client.print_mail.boxes.<a href="./src/postgrid/resources/print_mail/boxes.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/box_retrieve_response.py">BoxRetrieveResponse</a></code>
- <code title="get /print-mail/v1/boxes">client.print_mail.boxes.<a href="./src/postgrid/resources/print_mail/boxes.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/box_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/box_list_response.py">SyncSkipLimit[BoxListResponse]</a></code>
- <code title="delete /print-mail/v1/boxes/{id}">client.print_mail.boxes.<a href="./src/postgrid/resources/print_mail/boxes.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/box_delete_response.py">BoxDeleteResponse</a></code>
- <code title="post /print-mail/v1/boxes/{id}/progressions">client.print_mail.boxes.<a href="./src/postgrid/resources/print_mail/boxes.py">progressions</a>(id) -> <a href="./src/postgrid/types/print_mail/box_progressions_response.py">BoxProgressionsResponse</a></code>

## SnapPacks

Types:

```python
from postgrid.types.print_mail import (
    SnapPackCreateResponse,
    SnapPackRetrieveResponse,
    SnapPackListResponse,
    SnapPackDeleteResponse,
    SnapPackProgressionsResponse,
    SnapPackRetrieveCapabilitiesResponse,
)
```

Methods:

- <code title="post /print-mail/v1/snap_packs">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/snap_pack_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/snap_pack_create_response.py">SnapPackCreateResponse</a></code>
- <code title="get /print-mail/v1/snap_packs/{id}">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/snap_pack_retrieve_response.py">SnapPackRetrieveResponse</a></code>
- <code title="get /print-mail/v1/snap_packs">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/snap_pack_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/snap_pack_list_response.py">SyncSkipLimit[SnapPackListResponse]</a></code>
- <code title="delete /print-mail/v1/snap_packs/{id}">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/snap_pack_delete_response.py">SnapPackDeleteResponse</a></code>
- <code title="post /print-mail/v1/snap_packs/{id}/progressions">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">progressions</a>(id) -> <a href="./src/postgrid/types/print_mail/snap_pack_progressions_response.py">SnapPackProgressionsResponse</a></code>
- <code title="get /print-mail/v1/snap_packs/capabilities">client.print_mail.snap_packs.<a href="./src/postgrid/resources/print_mail/snap_packs.py">retrieve_capabilities</a>(\*\*<a href="src/postgrid/types/print_mail/snap_pack_retrieve_capabilities_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/snap_pack_retrieve_capabilities_response.py">SnapPackRetrieveCapabilitiesResponse</a></code>

## TargetedListBuilds

Types:

```python
from postgrid.types.print_mail import (
    TargetedListBuildCreateResponse,
    TargetedListBuildRetrieveResponse,
    TargetedListBuildUpdateResponse,
    TargetedListBuildListResponse,
    TargetedListBuildDeleteResponse,
    TargetedListBuildConfirmResponse,
)
```

Methods:

- <code title="post /print-mail/v1/targeted_list_builds">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/targeted_list_build_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_create_response.py">TargetedListBuildCreateResponse</a></code>
- <code title="get /print-mail/v1/targeted_list_builds/{id}">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_retrieve_response.py">TargetedListBuildRetrieveResponse</a></code>
- <code title="post /print-mail/v1/targeted_list_builds/{id}">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/targeted_list_build_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_update_response.py">TargetedListBuildUpdateResponse</a></code>
- <code title="get /print-mail/v1/targeted_list_builds">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/targeted_list_build_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_list_response.py">SyncSkipLimit[TargetedListBuildListResponse]</a></code>
- <code title="delete /print-mail/v1/targeted_list_builds/{id}">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_delete_response.py">TargetedListBuildDeleteResponse</a></code>
- <code title="post /print-mail/v1/targeted_list_builds/{id}/confirm">client.print_mail.targeted_list_builds.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/targeted_list_builds.py">confirm</a>(id) -> <a href="./src/postgrid/types/print_mail/targeted_list_build_confirm_response.py">TargetedListBuildConfirmResponse</a></code>

### Filters

Types:

```python
from postgrid.types.print_mail.targeted_list_builds import FilterAutocompleteResponse
```

Methods:

- <code title="post /print-mail/v1/targeted_list_builds/filters/autocomplete">client.print_mail.targeted_list_builds.filters.<a href="./src/postgrid/resources/print_mail/targeted_list_builds/filters.py">autocomplete</a>(\*\*<a href="src/postgrid/types/print_mail/targeted_list_builds/filter_autocomplete_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/targeted_list_builds/filter_autocomplete_response.py">FilterAutocompleteResponse</a></code>

## TemplateEditorSessions

Types:

```python
from postgrid.types.print_mail import (
    TemplateEditorSessionCreateResponse,
    TemplateEditorSessionListResponse,
    TemplateEditorSessionDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/template_editor_sessions">client.print_mail.template_editor_sessions.<a href="./src/postgrid/resources/print_mail/template_editor_sessions.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/template_editor_session_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/template_editor_session_create_response.py">TemplateEditorSessionCreateResponse</a></code>
- <code title="get /print-mail/v1/template_editor_sessions">client.print_mail.template_editor_sessions.<a href="./src/postgrid/resources/print_mail/template_editor_sessions.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/template_editor_session_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/template_editor_session_list_response.py">SyncSkipLimit[TemplateEditorSessionListResponse]</a></code>
- <code title="delete /print-mail/v1/template_editor_sessions/{id}">client.print_mail.template_editor_sessions.<a href="./src/postgrid/resources/print_mail/template_editor_sessions.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/template_editor_session_delete_response.py">TemplateEditorSessionDeleteResponse</a></code>

## VirtualMailboxes

Types:

```python
from postgrid.types.print_mail import (
    VirtualMailboxCreateResponse,
    VirtualMailboxRetrieveResponse,
    VirtualMailboxListResponse,
    VirtualMailboxRetrieveAddressResponse,
)
```

Methods:

- <code title="post /print-mail/v1/virtual_mailboxes">client.print_mail.virtual_mailboxes.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/virtual_mailboxes.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/virtual_mailbox_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/virtual_mailbox_create_response.py">VirtualMailboxCreateResponse</a></code>
- <code title="get /print-mail/v1/virtual_mailboxes/{id}">client.print_mail.virtual_mailboxes.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/virtual_mailboxes.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/virtual_mailbox_retrieve_response.py">VirtualMailboxRetrieveResponse</a></code>
- <code title="get /print-mail/v1/virtual_mailboxes">client.print_mail.virtual_mailboxes.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/virtual_mailboxes.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/virtual_mailbox_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/virtual_mailbox_list_response.py">SyncSkipLimit[VirtualMailboxListResponse]</a></code>
- <code title="get /print-mail/v1/virtual_mailboxes/{id}/address">client.print_mail.virtual_mailboxes.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/virtual_mailboxes.py">retrieve_address</a>(id) -> <a href="./src/postgrid/types/print_mail/virtual_mailbox_retrieve_address_response.py">VirtualMailboxRetrieveAddressResponse</a></code>

### Items

Types:

```python
from postgrid.types.print_mail.virtual_mailboxes import (
    ItemCreateResponse,
    ItemRetrieveResponse,
    ItemListResponse,
)
```

Methods:

- <code title="post /print-mail/v1/virtual_mailboxes/{id}/items">client.print_mail.virtual_mailboxes.items.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/items.py">create</a>(id, \*\*<a href="src/postgrid/types/print_mail/virtual_mailboxes/item_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/virtual_mailboxes/item_create_response.py">ItemCreateResponse</a></code>
- <code title="get /print-mail/v1/virtual_mailboxes/{id}/items/{itemID}">client.print_mail.virtual_mailboxes.items.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/items.py">retrieve</a>(item_id, \*, id) -> <a href="./src/postgrid/types/print_mail/virtual_mailboxes/item_retrieve_response.py">ItemRetrieveResponse</a></code>
- <code title="get /print-mail/v1/virtual_mailboxes/{id}/items">client.print_mail.virtual_mailboxes.items.<a href="./src/postgrid/resources/print_mail/virtual_mailboxes/items.py">list</a>(id, \*\*<a href="src/postgrid/types/print_mail/virtual_mailboxes/item_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/virtual_mailboxes/item_list_response.py">SyncSkipLimit[ItemListResponse]</a></code>
