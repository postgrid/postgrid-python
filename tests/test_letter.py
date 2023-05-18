import postgrid
import os
import time


def setup_module():
    postgrid.pm_key = os.environ.get("PM_API_KEY")


def create_test_letter():
    return postgrid.Letter.create(
        to={
            "first_name": "Test",
            "last_name": "Contact",
            "company_name": "Test Company",
            "address_line1": "20 Bay St, Toronto, ON M9V 4V1",
            "country_code": "CA",
            "job_title": "Test",
            "metadata": {"test": [10, 20]},
        },
        from_={
            "company_name": "PostGrid",
            "address_line1": "20 Bay St, Toronto, ON M9V 4V1",
            "country_code": "CA",
        },
        html="Hello, {{to.firstName}}",
        double_sided=True,
        color=True,
        merge_variables={"testCamel": 1, "test_snake": 1},
    )


def test_create():
    letter = create_test_letter()

    assert isinstance(letter, postgrid.Letter)
    assert isinstance(letter.html, str)
    assert letter.double_sided
    assert letter.color
    assert letter.merge_variables.get("testCamel") == "1"
    assert letter.merge_variables.get("test_snake") == "1"


def test_preview_generated():
    letter = create_test_letter()

    assert isinstance(letter, postgrid.Letter)

    time.sleep(5)

    letter = postgrid.Letter.retrieve(letter.id)

    assert isinstance(letter.url, str)


def test_list():
    letter = create_test_letter()
    list_ = postgrid.Letter.list()

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Letter)
    assert list_.data[0].html == letter.html


def test_list_search():
    letter = create_test_letter()
    list_ = postgrid.Letter.list(search=f'{{"_id": "{letter.id}"}}')

    assert list_.total_count >= 1
    assert list_.skip == 0
    assert isinstance(list_.data[0], postgrid.Letter)
    assert list_.data[0].html == letter.html


def test_delete():
    letter = create_test_letter()
    res = postgrid.Letter.delete(letter.id)

    assert isinstance(res, postgrid.Letter)
