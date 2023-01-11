import postgrid
import os


def setup_module():
    # Use live key to test
    postgrid.av_key = os.environ.get('AV_API_KEY')


def test_lookup_info():
    info = postgrid.Address.lookup_info()

    assert info['status'] == 'success'
    assert 'data' in info


def test_verify_freeform():
    res = postgrid.Address.verify('22-20 bay st, floor 11, toronto, on')

    assert res['status'] == 'success'
    assert 'data' in res
    assert res['data']['country'] == 'ca'
    assert res['data']['postalOrZip'] == 'M5J 2N8'
    assert res['data']['line1'] == '22-20 BAY ST FLOOR 11'


def test_autocomplete_previews():
    res = postgrid.Address.autocomplete_previews(partial_street='77 bloor st', country_filter='CA', prov_instead_of_pc='false')
    assert res['status'] == 'success'
    assert 'data' in res
    assert len(res['data']) >= 1


def test_autocomplete_address():
    res = postgrid.Address.autocomplete_address('20 bay st', 'Toronto')

    assert res['status'] == 'success'
    assert 'data' in res
    assert res['data']['address']['address'] == '20 BAY ST'


def test_batch_verify_address():
    addresses = {
        "addresses": [
            {
                "line1": "145 mulberry st ph d",
                "city": "new york",
                "provinceOrState": "new york",
                "postalOrZip": "10013",
                "country": "US"
            },
            {
                "line1": "90 canal st",
                "city": "boston",
                "provinceOrState": "ma",
                "country": "US"
            },
            "22-20 bay st, floor 11, toronto on, ca"
        ]
    }
    res = postgrid.Address.batch_verify(addresses)
    assert res['status'] == 'success'
    assert 'data' in res
    assert len(res['data']['results']) == 3
    assert res['data']['results'][0]['verifiedAddress']['line1'] == '145 Mulberry St Ph D'

def test_verify_structured():
    address = {
        "recipient": "Milk Bar",
        "line1": "251 E 13th St",
        "city": "new york city",
        "provinceOrState": "ny",
        "country": "us"
    }
    res = postgrid.Address.verify(address)

    assert res['status'] == 'success'
    assert 'data' in res
    assert res['data']['country'] == 'us'
    assert res['data']['postalOrZip'] == '10003'
    assert res['data']['line1'] == '251 E 13TH ST'


def test_suggest_address():
    address = {
        "line1": "2220 lakeshore blvd",
        "city": "toronto",
        "provinceOrState": "on",
        "country": "ca"
    }
    res = postgrid.Address.suggest_addresses(address)

    assert res['status'] == 'success'
    assert 'data' in res
    assert res['data'][0]['country'] == 'ca'
    assert res['data'][0]['postalOrZip'] == 'M8V 0E3'
    assert res['data'][0]['line1'] == '2220 LAKE SHORE BLVD W'


def test_parse_address():
    res = postgrid.Address.parse_address('20 bay st toronto, on m9v4v1, canada')
    assert res['status'] == 'success'
    assert res['message'] == 'Success.'


def test_lookup_city():
    res = postgrid.Address.lookup_city_state('m9v4v1')

    assert res['status'] == 'success'
    assert 'data' in res
    assert res['data'][0]['provinceOrState'] == 'ON'
