import postgrid
import os
import random


def setup_module():
    postgrid.pm_key = os.environ.get('PM_API_KEY')


def create_test_return_envelope(retrieve_existing):
    try:
        return postgrid.ReturnEnvelope.create(
            to={
                'first_name': 'Test',
                'last_name': 'Contact',
                'company_name': 'Test Company',
                'address_line1': '20 Bay St, Toronto, ON M9V 4V1',
                'country_code': 'CA',
                'job_title': 'Test',
                'metadata': {
                    'dedup': 0 if retrieve_existing else random.random()
                }
            },
            description='SDK Test'
        )
    except postgrid.PMError:
        # Ideally we would only hit this codepath if we're retrieving an existing return envelope
        assert retrieve_existing

        return postgrid.ReturnEnvelope.list().data[0]


def test_create():
    res = create_test_return_envelope(False)

    assert isinstance(res, postgrid.ReturnEnvelope)
    assert res.available == 0


def test_create_order():
    res = create_test_return_envelope(True)
    order_res = postgrid.ReturnEnvelopeOrder.create(res.id, 10000)

    assert isinstance(order_res, postgrid.ReturnEnvelopeOrder)
    assert order_res.quantity_ordered == 10000


def test_list_orders():
    res = create_test_return_envelope(True)
    order_res = postgrid.ReturnEnvelopeOrder.create(res.id, 10000)
    orders = postgrid.ReturnEnvelopeOrder.list(res.id)

    assert isinstance(orders, postgrid.List)
    assert len(orders.data) >= 1


def test_fill_order():
    res = create_test_return_envelope(True)
    order_res = postgrid.ReturnEnvelopeOrder.create(res.id, 10000)

    order = postgrid.ReturnEnvelopeOrder.fill(res.id, order_res.id)
    res = postgrid.ReturnEnvelope.retrieve(res.id)

    assert isinstance(order, postgrid.ReturnEnvelopeOrder)
    assert order.status == 'filled'
    assert res.available >= 10000


def test_cancel_order():
    res = create_test_return_envelope(True)
    order_res = postgrid.ReturnEnvelopeOrder.create(res.id, 10000)

    order = postgrid.ReturnEnvelopeOrder.delete(res.id, order_res.id)

    assert isinstance(order, postgrid.ReturnEnvelopeOrder)
    assert order.status == 'cancelled'
