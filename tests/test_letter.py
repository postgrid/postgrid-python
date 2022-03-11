import postgrid
import os


def setup_module():
    postgrid.pm_key = os.environ.get('PM_API_KEY')


def create_test_letter():
    return postgrid.Letter.create(
        to={
            'first_name': 'Test',
            'last_name': 'Contact',
            'company_name': 'Test Company',
            'address_line1': '20 Bay St, Toronto, ON M9V 4V1',
            'country_code': 'CA',
            'job_title': 'Test',
            'metadata': {
                'test': [10, 20]
            }
        },
        from_={
            'company_name': 'PostGrid',
            'address_line1': '20 Bay St, Toronto, ON M9V 4V1',
            'country_code': 'CA'
        },
        html='Hello, {{to.firstName}}'
    )


def test_create():
    letter = create_test_letter()

    assert isinstance(letter, postgrid.Letter)
    assert isinstance(letter.html, str)


def test_list():
    letter = create_test_letter()
    list_ = postgrid.Letter.list()

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Letter)
    assert list_.data[0].html == letter.html


def test_delete():
    letter = create_test_letter()
    res = postgrid.Letter.delete(letter.id)

    assert isinstance(res, postgrid.Letter)
