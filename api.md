# Contacts

Types:

```python
from postgrid.types import Contact, ContactDeleteResponse
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/postgrid/resources/contacts.py">create</a>(\*\*<a href="src/postgrid/types/contact_create_params.py">params</a>) -> <a href="./src/postgrid/types/contact.py">Contact</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/postgrid/resources/contacts.py">retrieve</a>(id) -> <a href="./src/postgrid/types/contact.py">Contact</a></code>
- <code title="get /contacts">client.contacts.<a href="./src/postgrid/resources/contacts.py">list</a>(\*\*<a href="src/postgrid/types/contact_list_params.py">params</a>) -> <a href="./src/postgrid/types/contact.py">SyncList[Contact]</a></code>
- <code title="delete /contacts/{id}">client.contacts.<a href="./src/postgrid/resources/contacts.py">delete</a>(id) -> <a href="./src/postgrid/types/contact_delete_response.py">ContactDeleteResponse</a></code>

# Templates

Types:

```python
from postgrid.types import Template, TemplateList, TemplateDeleteResponse
```

Methods:

- <code title="post /templates">client.templates.<a href="./src/postgrid/resources/templates.py">create</a>(\*\*<a href="src/postgrid/types/template_create_params.py">params</a>) -> <a href="./src/postgrid/types/template.py">Template</a></code>
- <code title="get /templates/{id}">client.templates.<a href="./src/postgrid/resources/templates.py">retrieve</a>(id) -> <a href="./src/postgrid/types/template.py">Template</a></code>
- <code title="post /templates/{id}">client.templates.<a href="./src/postgrid/resources/templates.py">update</a>(id, \*\*<a href="src/postgrid/types/template_update_params.py">params</a>) -> <a href="./src/postgrid/types/template.py">Template</a></code>
- <code title="get /templates">client.templates.<a href="./src/postgrid/resources/templates.py">list</a>(\*\*<a href="src/postgrid/types/template_list_params.py">params</a>) -> <a href="./src/postgrid/types/template.py">SyncList[Template]</a></code>
- <code title="delete /templates/{id}">client.templates.<a href="./src/postgrid/resources/templates.py">delete</a>(id) -> <a href="./src/postgrid/types/template_delete_response.py">TemplateDeleteResponse</a></code>

# BankAccounts

Types:

```python
from postgrid.types import BankAccount, BankAccountList, BankAccountDeleteResponse
```

Methods:

- <code title="post /bank_accounts">client.bank_accounts.<a href="./src/postgrid/resources/bank_accounts.py">create</a>(\*\*<a href="src/postgrid/types/bank_account_create_params.py">params</a>) -> <a href="./src/postgrid/types/bank_account.py">BankAccount</a></code>
- <code title="get /bank_accounts/{id}">client.bank_accounts.<a href="./src/postgrid/resources/bank_accounts.py">retrieve</a>(id) -> <a href="./src/postgrid/types/bank_account.py">BankAccount</a></code>
- <code title="get /bank_accounts">client.bank_accounts.<a href="./src/postgrid/resources/bank_accounts.py">list</a>(\*\*<a href="src/postgrid/types/bank_account_list_params.py">params</a>) -> <a href="./src/postgrid/types/bank_account.py">SyncList[BankAccount]</a></code>
- <code title="delete /bank_accounts/{id}">client.bank_accounts.<a href="./src/postgrid/resources/bank_accounts.py">delete</a>(id) -> <a href="./src/postgrid/types/bank_account_delete_response.py">BankAccountDeleteResponse</a></code>

# Cheques

Types:

```python
from postgrid.types import Cheque, ChequeList
```

Methods:

- <code title="post /cheques">client.cheques.<a href="./src/postgrid/resources/cheques/cheques.py">create</a>(\*\*<a href="src/postgrid/types/cheque_create_params.py">params</a>) -> <a href="./src/postgrid/types/cheque.py">Cheque</a></code>
- <code title="get /cheques/{id}">client.cheques.<a href="./src/postgrid/resources/cheques/cheques.py">retrieve</a>(id) -> <a href="./src/postgrid/types/cheque.py">Cheque</a></code>
- <code title="get /cheques">client.cheques.<a href="./src/postgrid/resources/cheques/cheques.py">list</a>(\*\*<a href="src/postgrid/types/cheque_list_params.py">params</a>) -> <a href="./src/postgrid/types/cheque.py">SyncList[Cheque]</a></code>
- <code title="delete /cheques/{id}">client.cheques.<a href="./src/postgrid/resources/cheques/cheques.py">cancel</a>(id) -> <a href="./src/postgrid/types/cheque.py">Cheque</a></code>

## URL

Types:

```python
from postgrid.types.cheques import URLRetrieveResponse
```

Methods:

- <code title="get /cheques/{id}/url">client.cheques.url.<a href="./src/postgrid/resources/cheques/url.py">retrieve</a>(id) -> <a href="./src/postgrid/types/cheques/url_retrieve_response.py">URLRetrieveResponse</a></code>

## WithDepositReadyPdf

Methods:

- <code title="get /cheques/{id}/with_deposit_ready_pdf">client.cheques.with_deposit_ready_pdf.<a href="./src/postgrid/resources/cheques/with_deposit_ready_pdf.py">retrieve</a>(id) -> <a href="./src/postgrid/types/cheque.py">Cheque</a></code>

# Letters

Types:

```python
from postgrid.types import Letter, LetterList, LetterURLResponse
```

Methods:

- <code title="post /letters">client.letters.<a href="./src/postgrid/resources/letters.py">create</a>(\*\*<a href="src/postgrid/types/letter_create_params.py">params</a>) -> <a href="./src/postgrid/types/letter.py">Letter</a></code>
- <code title="get /letters/{id}">client.letters.<a href="./src/postgrid/resources/letters.py">retrieve</a>(id) -> <a href="./src/postgrid/types/letter.py">Letter</a></code>
- <code title="get /letters">client.letters.<a href="./src/postgrid/resources/letters.py">list</a>(\*\*<a href="src/postgrid/types/letter_list_params.py">params</a>) -> <a href="./src/postgrid/types/letter.py">SyncList[Letter]</a></code>
- <code title="delete /letters/{id}">client.letters.<a href="./src/postgrid/resources/letters.py">delete</a>(id) -> <a href="./src/postgrid/types/letter.py">Letter</a></code>
- <code title="get /letters/{id}/url">client.letters.<a href="./src/postgrid/resources/letters.py">url</a>(id) -> <a href="./src/postgrid/types/letter_url_response.py">LetterURLResponse</a></code>

# Postcards

Types:

```python
from postgrid.types import Postcard, PostcardList, PostcardURLResponse
```

Methods:

- <code title="post /postcards">client.postcards.<a href="./src/postgrid/resources/postcards.py">create</a>(\*\*<a href="src/postgrid/types/postcard_create_params.py">params</a>) -> <a href="./src/postgrid/types/postcard.py">Postcard</a></code>
- <code title="get /postcards/{id}">client.postcards.<a href="./src/postgrid/resources/postcards.py">retrieve</a>(id) -> <a href="./src/postgrid/types/postcard.py">Postcard</a></code>
- <code title="get /postcards">client.postcards.<a href="./src/postgrid/resources/postcards.py">list</a>(\*\*<a href="src/postgrid/types/postcard_list_params.py">params</a>) -> <a href="./src/postgrid/types/postcard.py">SyncList[Postcard]</a></code>
- <code title="delete /postcards/{id}">client.postcards.<a href="./src/postgrid/resources/postcards.py">delete</a>(id) -> <a href="./src/postgrid/types/postcard.py">Postcard</a></code>
- <code title="get /postcards/{id}/url">client.postcards.<a href="./src/postgrid/resources/postcards.py">url</a>(id) -> <a href="./src/postgrid/types/postcard_url_response.py">PostcardURLResponse</a></code>
