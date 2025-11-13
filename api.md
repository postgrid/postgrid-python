# AddressVerification

Types:

```python
from postgrid.types import Errors, Status, AddressVerificationVerifyResponse
```

Methods:

- <code title="post /v1/addver/verifications">client.address_verification.<a href="./src/postgrid/resources/address_verification.py">verify</a>(\*\*<a href="src/postgrid/types/address_verification_verify_params.py">params</a>) -> <a href="./src/postgrid/types/address_verification_verify_response.py">AddressVerificationVerifyResponse</a></code>

# IntlAddressVerification

Types:

```python
from postgrid.types import IntlAddressVerificationVerifyResponse
```

Methods:

- <code title="post /v1/intl_addver/verifications">client.intl_address_verification.<a href="./src/postgrid/resources/intl_address_verification.py">verify</a>(\*\*<a href="src/postgrid/types/intl_address_verification_verify_params.py">params</a>) -> <a href="./src/postgrid/types/intl_address_verification_verify_response.py">IntlAddressVerificationVerifyResponse</a></code>

# PrintMail

Types:

```python
from postgrid.types import ContactCreateWithCompanyName, ContactCreateWithFirstName
```

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
- <code title="get /print-mail/v1/cheques/{id}/url">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque_retrieve_url_response.py">ChequeRetrieveURLResponse</a></code>
- <code title="get /print-mail/v1/cheques/{id}/with_deposit_ready_pdf">client.print_mail.cheques.<a href="./src/postgrid/resources/print_mail/cheques.py">retrieve_with_deposit_ready_pdf</a>(id) -> <a href="./src/postgrid/types/print_mail/cheque.py">Cheque</a></code>

## Contacts

Types:

```python
from postgrid.types.print_mail import Contact, ContactCreate, ContactDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/contacts">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/contact_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/contact.py">Contact</a></code>
- <code title="get /print-mail/v1/contacts/{id}">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/contact.py">Contact</a></code>
- <code title="get /print-mail/v1/contacts">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/contact_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/contact.py">SyncSkipLimit[Contact]</a></code>
- <code title="delete /print-mail/v1/contacts/{id}">client.print_mail.contacts.<a href="./src/postgrid/resources/print_mail/contacts.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/contact_delete_response.py">ContactDeleteResponse</a></code>

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
- <code title="get /print-mail/v1/letters/{id}/url">client.print_mail.letters.<a href="./src/postgrid/resources/print_mail/letters.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/letter_retrieve_url_response.py">LetterRetrieveURLResponse</a></code>

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

## OrderProfiles

### Cheques

Types:

```python
from postgrid.types.print_mail.order_profiles import (
    ChequeProfile,
    CurrencyCode,
    ChequeListResponse,
    ChequeDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/order_profiles/cheques">client.print_mail.order_profiles.cheques.<a href="./src/postgrid/resources/print_mail/order_profiles/cheques.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/cheque_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/cheque_profile.py">ChequeProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/cheques/{id}">client.print_mail.order_profiles.cheques.<a href="./src/postgrid/resources/print_mail/order_profiles/cheques.py">retrieve</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/cheque_retrieve_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/cheque_profile.py">ChequeProfile</a></code>
- <code title="post /print-mail/v1/order_profiles/cheques/{id}">client.print_mail.order_profiles.cheques.<a href="./src/postgrid/resources/print_mail/order_profiles/cheques.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/cheque_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/cheque_profile.py">ChequeProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/cheques">client.print_mail.order_profiles.cheques.<a href="./src/postgrid/resources/print_mail/order_profiles/cheques.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/cheque_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/cheque_list_response.py">SyncSkipLimit[ChequeListResponse]</a></code>
- <code title="delete /print-mail/v1/order_profiles/cheques/{id}">client.print_mail.order_profiles.cheques.<a href="./src/postgrid/resources/print_mail/order_profiles/cheques.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/order_profiles/cheque_delete_response.py">ChequeDeleteResponse</a></code>

### Letters

Types:

```python
from postgrid.types.print_mail.order_profiles import LetterProfile, LetterDeleteResponse
```

Methods:

- <code title="post /print-mail/v1/order_profiles/letters">client.print_mail.order_profiles.letters.<a href="./src/postgrid/resources/print_mail/order_profiles/letters.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/letter_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/letter_profile.py">LetterProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/letters/{id}">client.print_mail.order_profiles.letters.<a href="./src/postgrid/resources/print_mail/order_profiles/letters.py">retrieve</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/letter_retrieve_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/letter_profile.py">LetterProfile</a></code>
- <code title="post /print-mail/v1/order_profiles/letters/{id}">client.print_mail.order_profiles.letters.<a href="./src/postgrid/resources/print_mail/order_profiles/letters.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/letter_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/letter_profile.py">LetterProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/letters">client.print_mail.order_profiles.letters.<a href="./src/postgrid/resources/print_mail/order_profiles/letters.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/letter_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/letter_profile.py">SyncSkipLimit[LetterProfile]</a></code>
- <code title="delete /print-mail/v1/order_profiles/letters/{id}">client.print_mail.order_profiles.letters.<a href="./src/postgrid/resources/print_mail/order_profiles/letters.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/order_profiles/letter_delete_response.py">LetterDeleteResponse</a></code>

### Postcards

Types:

```python
from postgrid.types.print_mail.order_profiles import (
    PostcardProfile,
    PostcardSize,
    PostcardDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/order_profiles/postcards">client.print_mail.order_profiles.postcards.<a href="./src/postgrid/resources/print_mail/order_profiles/postcards.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/postcard_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/postcard_profile.py">PostcardProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/postcards/{id}">client.print_mail.order_profiles.postcards.<a href="./src/postgrid/resources/print_mail/order_profiles/postcards.py">retrieve</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/postcard_retrieve_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/postcard_profile.py">PostcardProfile</a></code>
- <code title="post /print-mail/v1/order_profiles/postcards/{id}">client.print_mail.order_profiles.postcards.<a href="./src/postgrid/resources/print_mail/order_profiles/postcards.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/postcard_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/postcard_profile.py">PostcardProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/postcards">client.print_mail.order_profiles.postcards.<a href="./src/postgrid/resources/print_mail/order_profiles/postcards.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/postcard_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/postcard_profile.py">SyncSkipLimit[PostcardProfile]</a></code>
- <code title="delete /print-mail/v1/order_profiles/postcards/{id}">client.print_mail.order_profiles.postcards.<a href="./src/postgrid/resources/print_mail/order_profiles/postcards.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/order_profiles/postcard_delete_response.py">PostcardDeleteResponse</a></code>

### SelfMailers

Types:

```python
from postgrid.types.print_mail.order_profiles import (
    SelfMailerProfile,
    SelfMailerSize,
    SelfMailerDeleteResponse,
)
```

Methods:

- <code title="post /print-mail/v1/order_profiles/self_mailers">client.print_mail.order_profiles.self_mailers.<a href="./src/postgrid/resources/print_mail/order_profiles/self_mailers.py">create</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/self_mailer_create_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/self_mailer_profile.py">SelfMailerProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/self_mailers/{id}">client.print_mail.order_profiles.self_mailers.<a href="./src/postgrid/resources/print_mail/order_profiles/self_mailers.py">retrieve</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/self_mailer_retrieve_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/self_mailer_profile.py">SelfMailerProfile</a></code>
- <code title="post /print-mail/v1/order_profiles/self_mailers/{id}">client.print_mail.order_profiles.self_mailers.<a href="./src/postgrid/resources/print_mail/order_profiles/self_mailers.py">update</a>(id, \*\*<a href="src/postgrid/types/print_mail/order_profiles/self_mailer_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/self_mailer_profile.py">SelfMailerProfile</a></code>
- <code title="get /print-mail/v1/order_profiles/self_mailers">client.print_mail.order_profiles.self_mailers.<a href="./src/postgrid/resources/print_mail/order_profiles/self_mailers.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/order_profiles/self_mailer_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/order_profiles/self_mailer_profile.py">SyncSkipLimit[SelfMailerProfile]</a></code>
- <code title="delete /print-mail/v1/order_profiles/self_mailers/{id}">client.print_mail.order_profiles.self_mailers.<a href="./src/postgrid/resources/print_mail/order_profiles/self_mailers.py">delete</a>(id) -> <a href="./src/postgrid/types/print_mail/order_profiles/self_mailer_delete_response.py">SelfMailerDeleteResponse</a></code>

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
- <code title="get /print-mail/v1/postcards/{id}/url">client.print_mail.postcards.<a href="./src/postgrid/resources/print_mail/postcards.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/postcard_retrieve_url_response.py">PostcardRetrieveURLResponse</a></code>

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
- <code title="get /print-mail/v1/self_mailers/{id}/url">client.print_mail.self_mailers.<a href="./src/postgrid/resources/print_mail/self_mailers.py">retrieve_url</a>(id) -> <a href="./src/postgrid/types/print_mail/self_mailer_retrieve_url_response.py">SelfMailerRetrieveURLResponse</a></code>

## SubOrganizations

Types:

```python
from postgrid.types.print_mail import (
    EmailPreferences,
    SubOrganization,
    SubOrganizationUpdateResponse,
    SubOrganizationRetrieveUsersResponse,
)
```

Methods:

- <code title="get /print-mail/v1/sub_organizations/{id}">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">retrieve</a>(id) -> <a href="./src/postgrid/types/print_mail/sub_organization.py">SubOrganization</a></code>
- <code title="post /print-mail/v1/sub_organizations">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">update</a>(\*\*<a href="src/postgrid/types/print_mail/sub_organization_update_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization_update_response.py">SubOrganizationUpdateResponse</a></code>
- <code title="get /print-mail/v1/sub_organizations">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">list</a>(\*\*<a href="src/postgrid/types/print_mail/sub_organization_list_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization.py">SyncSkipLimit[SubOrganization]</a></code>
- <code title="get /print-mail/v1/sub_organizations/{id}/users">client.print_mail.sub_organizations.<a href="./src/postgrid/resources/print_mail/sub_organizations.py">retrieve_users</a>(id, \*\*<a href="src/postgrid/types/print_mail/sub_organization_retrieve_users_params.py">params</a>) -> <a href="./src/postgrid/types/print_mail/sub_organization_retrieve_users_response.py">SubOrganizationRetrieveUsersResponse</a></code>

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
