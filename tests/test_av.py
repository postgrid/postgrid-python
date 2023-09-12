import postgrid
import os


def setup_module():
    # Use live key to test
    postgrid.av_key = os.environ.get("AV_API_KEY")


def test_lookup_info():
    res = postgrid.LookupInfo.lookup_info()
    assert isinstance(res, postgrid.LookupInfo)
    assert res.status == "success"
    assert hasattr(res, "data")


def test_verify_freeform():
    res = postgrid.Verification.verify("22-20 bay st, floor 11, toronto, on")

    assert isinstance(res, postgrid.Verification)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert res.data.country == "ca"
    assert res.data.postal_or_zip == "M5J 2N8"
    assert res.data.line1 == "22-20 BAY ST FLOOR 11"


def test_autocomplete_previews():
    res = postgrid.Autocomplete.previews(
        partial_street="77 bloor st", country_filter="CA", prov_instead_of_pc=False
    )

    assert isinstance(res, postgrid.Autocomplete)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert len(res.data) >= 1


def test_autocomplete_address():
    res = postgrid.Autocomplete.address("20 bay st", "Toronto")

    assert isinstance(res, postgrid.Autocomplete)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert res.data[0].address.address == "20 BAY ST"
    assert res.data[0].address.pc == "M5H 4A6"


def test_batch_verify_address():
    addresses = {
        "addresses": [
            {
                "line1": "145 mulberry st ph d",
                "city": "new york",
                "province_or_state": "new york",
                "postal_or_zip": "10013",
                "country": "US",
            },
            {
                "line1": "90 canal st",
                "city": "boston",
                "province_or_state": "ma",
                "country": "US",
            },
            "22-20 bay st, floor 11, toronto on, ca",
        ]
    }
    res = postgrid.Verification.batch_verify(addresses, False, True, False)

    assert isinstance(res, postgrid.Verification)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert len(res.data.results) == 3
    assert res.data.results[0].verified_address.line1 == "145 Mulberry St Ph D"


def test_verify_structured():
    address = {
        "recipient": "Milk Bar",
        "line1": "251 E 13th St",
        "city": "new york city",
        "province_or_state": "ny",
        "country": "us",
    }
    res = postgrid.Verification.verify(address)

    assert isinstance(res, postgrid.Verification)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert res.data.country == "us"
    assert res.data.postal_or_zip == "10003"
    assert res.data.line1 == "251 E 13TH ST"


def test_suggest_address():
    address = {
        "line1": "2220 lakeshore blvd",
        "city": "toronto",
        "province_or_state": "on",
        "country": "ca",
    }
    res = postgrid.Suggestion.suggest_addresses(address, True, False, False)

    assert isinstance(res, postgrid.Suggestion)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert hasattr(res.data[0], "details")
    assert res.data[0].city == "TORONTO"
    assert res.data[0].country == "ca"
    assert res.data[0].country_name == "CANADA"
    assert res.data[0].postal_or_zip == "M8V 0E3"
    assert res.data[0].line1 == "2220 LAKE SHORE BLVD W"


def test_parse_address():
    res = postgrid.Parse.parse_address("20 bay st toronto, on m9v4v1, canada")

    assert isinstance(res, postgrid.Parse)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert res.data.city == "toronto"
    assert res.data.country == "canada"
    assert res.data.road == "bay st"


def test_lookup_city():
    res = postgrid.CityState.lookup_city_state("m9v4v1")

    assert isinstance(res, postgrid.CityState)
    assert res.status == "success"
    assert hasattr(res, "data")
    assert res.data[0].province_or_state == "ON"
