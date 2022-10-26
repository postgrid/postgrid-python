# PostGrid Python Library

The PostGrid Python library enables you to access the PostGrid Print & Mail API
conveniently from applications written in Python. It contains classes representing
every resource in the PostGrid Print & Mail API and methods which create and operate
on these resources.

## Installation

In order to install this package, run

```bash
pip install --upgrade postgrid-python
```

### Requirements

- Python 3.6+

## Usage

You must have a PostGrid Print & Mail Account (you can sign up at https://dashboard.postgrid.com/signup) and access to your API key which you can retrieve from the [settings page](https://dashboard.postgrid.com/settings).

```python
import postgrid

# Swap this out for your live API key to create live orders
postgrid.pm_key = 'test_sk_...'

# Send a letter
letter = postgrid.Letter.create(
    to={
        'first_name': 'Apaar',
        'last_name': 'Madan',
        'address_line1': '145 Mulberry St, Apt PH D, New York NY 10013',
        'country_code': 'US'
    },
    from_={
        'first_name': 'Kevin',
        'last_name': 'Villena',
        'address_line1': '90 Canal St',
        'address_line2': '2nd Floor',
        'city': 'Boston',
        'province_or_state': 'MA',
        'postal_or_zip': '02114',
        'country_code': 'US'
    },
    html='''
        <html>
            <body>
                <p>Hi, {{to.firstName}}</p>
                <p>Welcome to PostGrid.</p>
                <p>Yours Truly,</p>
                <p>{{from.firstName}} {{from.lastName}}</p>
            </body>
        </html>
    '''
)

# Prints 'ready'
print(letter.status)

# Cancel the letter
letter = postgrid.Letter.delete(letter.id)

# Prints 'cancelled'
print(letter.status)
```

Note that API parameters map one-to-one with the underlying [REST API](https://docs.postgrid.com).
However, instead of `camelCase`, this library uses `snake_case`. For example, a `letterHTML` parameter
in the original API would be `letter_html` in this library.

### Handling Exceptions

Errors produced by the API will raise a `PMError` exception. The `PMError` object has a
`type` field that can be used to determine what the error was. It also has a `message` field
which provides a human readable message describing the error in detail.

```python
import postgrid

postgrid.pm_key = 'test_sk_...'

try:
    template = postgrid.Template.create(
        description='SDK Template',
        html='''
            <html>
                <body>
                    <p>Hi, {{to.firstName}}</p>
                    <p>Welcome to PostGrid.</p>
                    <p>Yours Truly,</p>
                    <p>{{from.firstName}} {{from.lastName}}</p>
                </body>
            </html>
        ''',
    )
except postgrid.PMError as e:
    print(e.status_code)
    print(e.type)
    print(e.message)

    raise e
```

## Support

Email `support@postgrid.com` if you face any errors with the API or create issues in the
`postgrid-python` GitHub if you face issues with the SDK itself.
