# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types import (
    AddressVerificationVerifyResponse,
    AddressVerificationAutocompleteResponse,
    AddressVerificationGetLookupInfoResponse,
    AddressVerificationParseAnAddressResponse,
    AddressVerificationSuggestAddressesResponse,
    AddressVerificationBatchVerificationResponse,
    AddressVerificationGetAutocompletePreviewsResponse,
    AddressVerificationLookupZipCodeFromCityOrStateResponse,
    AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete(self, client: PostGrid) -> None:
        address_verification = client.address_verification.autocomplete(
            partial_street="partialStreet",
        )
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_with_all_params(self, client: PostGrid) -> None:
        address_verification = client.address_verification.autocomplete(
            partial_street="partialStreet",
            filter_exact=True,
            geocode=True,
            include_details=True,
            index=0,
            limit=0,
            proper_case=True,
            query_verified_only=True,
            verify=True,
            city_filter="cityFilter",
            country_filter="countryFilter",
            pc_filter="pcFilter",
            state_filter="stateFilter",
            body_verified_only=True,
        )
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.autocomplete(
            partial_street="partialStreet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.autocomplete(
            partial_street="partialStreet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_verification(self, client: PostGrid) -> None:
        address_verification = client.address_verification.batch_verification(
            addresses=[{"address": "address"}],
        )
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_verification_with_all_params(self, client: PostGrid) -> None:
        address_verification = client.address_verification.batch_verification(
            addresses=[{"address": "address"}],
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_verification(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.batch_verification(
            addresses=[{"address": "address"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_verification(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.batch_verification(
            addresses=[{"address": "address"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_previews(self, client: PostGrid) -> None:
        address_verification = client.address_verification.get_autocomplete_previews(
            partial_street="partialStreet",
        )
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_previews_with_all_params(self, client: PostGrid) -> None:
        address_verification = client.address_verification.get_autocomplete_previews(
            partial_street="partialStreet",
            city_filter="cityFilter",
            country_filter="countryFilter",
            filter_exact=True,
            limit=0,
            pc_filter="pcFilter",
            proper_case=True,
            prov_instead_of_pc=True,
            state_filter="stateFilter",
            verified_only=True,
        )
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_autocomplete_previews(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.get_autocomplete_previews(
            partial_street="partialStreet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_autocomplete_previews(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.get_autocomplete_previews(
            partial_street="partialStreet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(
                AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_lookup_info(self, client: PostGrid) -> None:
        address_verification = client.address_verification.get_lookup_info()
        assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_lookup_info(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.get_lookup_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_lookup_info(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.get_lookup_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_city_or_state_from_postal_or_zip_code(self, client: PostGrid) -> None:
        address_verification = client.address_verification.lookup_city_or_state_from_postal_or_zip_code(
            postal_or_zip="postalOrZip",
        )
        assert_matches_type(
            AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_city_or_state_from_postal_or_zip_code(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.lookup_city_or_state_from_postal_or_zip_code(
            postal_or_zip="postalOrZip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(
            AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_city_or_state_from_postal_or_zip_code(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.lookup_city_or_state_from_postal_or_zip_code(
            postal_or_zip="postalOrZip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(
                AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_zip_code_from_city_or_state(self, client: PostGrid) -> None:
        address_verification = client.address_verification.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        )
        assert_matches_type(
            AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup_zip_code_from_city_or_state(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(
            AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup_zip_code_from_city_or_state(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(
                AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_parse_an_address(self, client: PostGrid) -> None:
        address_verification = client.address_verification.parse_an_address(
            address="address",
        )
        assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_parse_an_address(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.parse_an_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_parse_an_address(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.parse_an_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_suggest_addresses_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.suggest_addresses(
            address="address",
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_suggest_addresses_with_all_params_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.suggest_addresses(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_suggest_addresses_overload_1(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.suggest_addresses(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_suggest_addresses_overload_1(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.suggest_addresses(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_suggest_addresses_overload_2(self, client: PostGrid) -> None:
        address_verification = client.address_verification.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_suggest_addresses_with_all_params_overload_2(self, client: PostGrid) -> None:
        address_verification = client.address_verification.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "line2": "line2",
                "recipient": "recipient",
            },
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_suggest_addresses_overload_2(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_suggest_addresses_overload_2(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address="address",
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_overload_1(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_overload_1(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.verify(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_overload_2(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params_overload_2(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "line2": "line2",
                "recipient": "recipient",
            },
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_overload_2(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_overload_2(self, client: PostGrid) -> None:
        with client.address_verification.with_streaming_response.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = response.parse()
            assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAddressVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.autocomplete(
            partial_street="partialStreet",
        )
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_with_all_params(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.autocomplete(
            partial_street="partialStreet",
            filter_exact=True,
            geocode=True,
            include_details=True,
            index=0,
            limit=0,
            proper_case=True,
            query_verified_only=True,
            verify=True,
            city_filter="cityFilter",
            country_filter="countryFilter",
            pc_filter="pcFilter",
            state_filter="stateFilter",
            body_verified_only=True,
        )
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.autocomplete(
            partial_street="partialStreet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.autocomplete(
            partial_street="partialStreet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationAutocompleteResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_verification(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.batch_verification(
            addresses=[{"address": "address"}],
        )
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_verification_with_all_params(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.batch_verification(
            addresses=[{"address": "address"}],
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_verification(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.batch_verification(
            addresses=[{"address": "address"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_verification(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.batch_verification(
            addresses=[{"address": "address"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationBatchVerificationResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.get_autocomplete_previews(
            partial_street="partialStreet",
        )
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_previews_with_all_params(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.get_autocomplete_previews(
            partial_street="partialStreet",
            city_filter="cityFilter",
            country_filter="countryFilter",
            filter_exact=True,
            limit=0,
            pc_filter="pcFilter",
            proper_case=True,
            prov_instead_of_pc=True,
            state_filter="stateFilter",
            verified_only=True,
        )
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.get_autocomplete_previews(
            partial_street="partialStreet",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.get_autocomplete_previews(
            partial_street="partialStreet",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(
                AddressVerificationGetAutocompletePreviewsResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_lookup_info(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.get_lookup_info()
        assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_lookup_info(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.get_lookup_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_lookup_info(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.get_lookup_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationGetLookupInfoResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_city_or_state_from_postal_or_zip_code(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.lookup_city_or_state_from_postal_or_zip_code(
            postal_or_zip="postalOrZip",
        )
        assert_matches_type(
            AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_city_or_state_from_postal_or_zip_code(self, async_client: AsyncPostGrid) -> None:
        response = (
            await async_client.address_verification.with_raw_response.lookup_city_or_state_from_postal_or_zip_code(
                postal_or_zip="postalOrZip",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(
            AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_city_or_state_from_postal_or_zip_code(
        self, async_client: AsyncPostGrid
    ) -> None:
        async with (
            async_client.address_verification.with_streaming_response.lookup_city_or_state_from_postal_or_zip_code(
                postal_or_zip="postalOrZip",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(
                AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_zip_code_from_city_or_state(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        )
        assert_matches_type(
            AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup_zip_code_from_city_or_state(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(
            AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup_zip_code_from_city_or_state(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.lookup_zip_code_from_city_or_state(
            city="city",
            country_code="countryCode",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(
                AddressVerificationLookupZipCodeFromCityOrStateResponse, address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_parse_an_address(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.parse_an_address(
            address="address",
        )
        assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_parse_an_address(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.parse_an_address(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_parse_an_address(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.parse_an_address(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationParseAnAddressResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_suggest_addresses_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.suggest_addresses(
            address="address",
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_suggest_addresses_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.suggest_addresses(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_suggest_addresses_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.suggest_addresses(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_suggest_addresses_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.suggest_addresses(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_suggest_addresses_overload_2(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_suggest_addresses_with_all_params_overload_2(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "line2": "line2",
                "recipient": "recipient",
            },
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_suggest_addresses_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_suggest_addresses_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.suggest_addresses(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationSuggestAddressesResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address="address",
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.verify(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params_overload_2(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "line2": "line2",
                "recipient": "recipient",
            },
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.address_verification.with_streaming_response.verify(
            address={
                "city": "city",
                "country": "ca",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_verification = await response.parse()
            assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True
