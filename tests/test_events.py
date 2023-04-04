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
        html='Hello, {{to.firstName}}',
        double_sided=True,
        color=True,
        merge_variables={
            'testCamel': 1,
            'test_snake': 1
        }
    )


def test_list_events():
    letter = create_test_letter()
    events = postgrid.Event.list(['letter.created'])

    assert isinstance(events, postgrid.List)
    assert events.total_count >= 1
    assert events.skip == 0
    assert events.limit == 10
    assert isinstance(events.data[0], postgrid.Event)
    assert events.data[0].data.html == letter.html
    assert events.data[0].type == 'letter.created'
