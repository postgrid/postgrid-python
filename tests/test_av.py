import postgrid
import os


def setup_module():
    # Use live key to test
    postgrid.av_key = os.environ.get('AV_API_KEY')


def test_lookup_info():
    info = postgrid.Address.lookup_info()

    assert info.status == 'success'
    assert hasattr(info, 'data')


def test_verify_freeform():
    res = postgrid.Address.verify('22-20 bay st, floor 11, toronto, on')

    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data.country == 'ca'
    assert res.data.postal_or_zip == 'M5J 2N8'
    assert res.data.line1 == '22-20 BAY ST FLOOR 11'


def test_autocomplete_previews():
    res = postgrid.Address.autocomplete_previews(
        partial_street='77 bloor st', country_filter='CA', prov_instead_of_pc='false')
    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert len(res.data) >= 1


def test_autocomplete_address():
    res = postgrid.Address.autocomplete_address('20 bay st', 'Toronto')

    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data.address.address == '20 BAY ST'
    assert res.data.address.pc == 'M5H 4A6'


def test_batch_verify_address():
    addresses = {
        "addresses": [
            {
                "line1": "145 mulberry st ph d",
                "city": "new york",
                "province_or_state": "new york",
                "postal_or_zip": "10013",
                "country": "US"
            },
            {
                "line1": "90 canal st",
                "city": "boston",
                "province_or_state": "ma",
                "country": "US"
            },
            "22-20 bay st, floor 11, toronto on, ca"
        ]
    }
    res = postgrid.Address.batch_verify(addresses)
    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert len(res.data.results) == 3
    assert res.data.results[0].verified_address.line1 == '145 Mulberry St Ph D'


def test_verify_structured():
    address = {
        "recipient": "Milk Bar",
        "line1": "251 E 13th St",
        "city": "new york city",
        "province_or_state": "ny",
        "country": "us"
    }
    res = postgrid.Address.verify(address)

    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data.country == 'us'
    assert res.data.postal_or_zip == '10003'
    assert res.data.line1 == '251 E 13TH ST'


def test_suggest_address():
    address = {
        "line1": "2220 lakeshore blvd",
        "city": "toronto",
        "province_or_state": "on",
        "country": "ca"
    }
    res = postgrid.Address.suggest_addresses(address)
    print(res)
    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data[0].country == 'ca'
    assert res.data[0].postal_or_zip == 'M8V 0E3'
    assert res.data[0].line1 == '2220 LAKE SHORE BLVD W'


def test_parse_address():
    res = postgrid.Address.parse_address(
        '20 bay st toronto, on m9v4v1, canada')
    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data.city == 'toronto'
    assert res.data.country == 'canada'
    assert res.data.road == 'bay st'


def test_lookup_city():
    res = postgrid.Address.lookup_city_state('m9v4v1')

    assert res.status == 'success'
    assert hasattr(res, 'data')
    assert res.data[0].province_or_state == 'ON'
