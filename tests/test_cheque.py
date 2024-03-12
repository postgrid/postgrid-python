import postgrid
import os
import time


def setup_module():
    postgrid.pm_key = os.environ.get("PM_API_KEY")


def create_test_cheque():
    bank_account = postgrid.BankAccount.create(
        bank_name="Test SDK",
        bank_primary_line="47 Park Ave",
        bank_secondary_line="New York NY 10013",
        bank_country_code="US",
        account_number="12345678",
        routing_number="002301323",
        signature_image=open("tests/assets/signature.png", "rb"),
    )

    return postgrid.Cheque.create(
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
        bank_account=bank_account.id,
        amount=10000,
        memo="Hello",
        letter_html="Hello, {{to.firstName}}",
    )


def test_create():
    cheque = create_test_cheque()

    assert isinstance(cheque, postgrid.Cheque)
    assert isinstance(cheque.letter_html, str)


def test_preview_generated():
    cheque = create_test_cheque()

    assert isinstance(cheque, postgrid.Cheque)

    time.sleep(10)

    cheque = postgrid.Cheque.retrieve(cheque.id)

    assert isinstance(cheque.url, str)


def test_delete():
    cheque = create_test_cheque()
    res = postgrid.Cheque.delete(cheque.id)

    assert isinstance(res, postgrid.Cheque)

def test_delete_with_note():
    cheque = create_test_cheque()
    note = "cancelled due to issues test"
    res = postgrid.Cheque.delete_with_note(cheque.id, note)

    assert isinstance(res, postgrid.Cheque)
    assert res.cancellation["note"] == note