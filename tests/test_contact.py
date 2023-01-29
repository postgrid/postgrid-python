import postgrid
import os
import uuid


def setup_module():
    postgrid.pm_key = os.environ.get('PM_API_KEY')


def create_test_contact(idempotency_key=None):
    return postgrid.Contact.create(
        first_name='Test',
        last_name='Contact',
        company_name='Test Company',
        address_line1='20 Bay St, Toronto, ON M9V 4V1',
        country_code='CA',
        job_title='Test',
        metadata={
            'test': [10, 20]
        },
        idempotency_key=idempotency_key
    )


def test_create():
    contact = create_test_contact()

    assert isinstance(contact, postgrid.Contact)
    assert contact.company_name == 'Test Company'


def test_idempotency():
    idempotency_key = str(uuid.uuid4())

    contact = create_test_contact(idempotency_key=idempotency_key)
    contact_duplicate = create_test_contact(idempotency_key=idempotency_key)

    # The second call should not result in a new contact being created
    assert contact.id == contact_duplicate.id


def test_list():
    contact = create_test_contact()
    list_ = postgrid.Contact.list()

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Contact)
    assert list_.data[0].company_name == contact.company_name


def test_delete():
    contact = create_test_contact()
    res = postgrid.Contact.delete(contact.id)

    assert isinstance(res, postgrid.Contact)
