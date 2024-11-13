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
