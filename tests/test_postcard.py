import postgrid
import os


def setup_module():
    postgrid.pm_key = os.environ.get('PM_API_KEY')


def create_test_postcard():
    return postgrid.Postcard.create(
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
        frontHTML='Hello, {{to.firstName}}',
        backHTML='Goodbye, {{to.firstName}}',
        size='6x4'
    )


def test_create():
    res = create_test_postcard()

    print(res.to_dict())

    assert isinstance(res, postgrid.Postcard)
    assert isinstance(res.front_html, str)
    assert isinstance(res.back_html, str)


def test_list():
    postcard = create_test_postcard()
    list_ = postgrid.Postcard.list()

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Postcard)
    assert list_.data[0].front_html == postcard.front_html


def test_delete():
    postcard = create_test_postcard()
    res = postgrid.Postcard.delete(postcard.id)

    assert isinstance(res, postgrid.Postcard)
