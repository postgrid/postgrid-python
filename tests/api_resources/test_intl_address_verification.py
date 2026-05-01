# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types import (
    IntlAddressVerificationVerifyResponse,
    IntlAddressVerificationAutocompleteResponse,
    IntlAddressVerificationBatchVerificationResponse,
    IntlAddressVerificationGetAutocompletePreviewsResponse,
    IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntlAddressVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.autocomplete(
            id="id",
        )
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_with_all_params(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.autocomplete(
            id="id",
            include_details=True,
            proper_case=True,
            use_enhanced_china_dataset=True,
            verify=True,
        )
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.autocomplete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.autocomplete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(
                IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_verification(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        )
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_verification_with_all_params(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                        "city": "city",
                        "line2": "line2",
                        "line3": "line3",
                        "line4": "line4",
                    }
                }
            ],
            geo_data=True,
            include_details=True,
            proper_case=True,
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch_verification(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch_verification(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(
                IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_advanced_previews(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.get_autocomplete_advanced_previews()
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_advanced_previews_with_all_params(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.get_autocomplete_advanced_previews(
            advanced=True,
            city_filter="cityFilter",
            container="container",
            countries_filter="countriesFilter",
            disable_ip_biasing=True,
            language="language",
            limit=0,
            partial_street="partialStreet",
            postal_or_zip_filter="postalOrZipFilter",
            standard_fallback=True,
            street_filter="streetFilter",
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_autocomplete_advanced_previews(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.get_autocomplete_advanced_previews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_autocomplete_advanced_previews(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.get_autocomplete_advanced_previews() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(
                IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
                intl_address_verification,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_previews(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.get_autocomplete_previews()
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_autocomplete_previews_with_all_params(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.get_autocomplete_previews(
            advanced=True,
            city_filter="cityFilter",
            container="container",
            countries_filter="countriesFilter",
            disable_ip_biasing=True,
            language="language",
            limit=0,
            partial_street="partialStreet",
            postal_or_zip_filter="postalOrZipFilter",
            standard_fallback=True,
            street_filter="streetFilter",
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_autocomplete_previews(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.get_autocomplete_previews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_autocomplete_previews(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.get_autocomplete_previews() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(
                IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_overload_1(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params_overload_1(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "city": "city",
                "line2": "line2",
                "line3": "line3",
                "line4": "line4",
            },
            geo_data=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_overload_1(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_overload_1(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_overload_2(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.verify(
            address="address",
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_verify_with_all_params_overload_2(self, client: PostGrid) -> None:
        intl_address_verification = client.intl_address_verification.verify(
            address="address",
            geo_data=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_verify_overload_2(self, client: PostGrid) -> None:
        response = client.intl_address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = response.parse()
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_verify_overload_2(self, client: PostGrid) -> None:
        with client.intl_address_verification.with_streaming_response.verify(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = response.parse()
            assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntlAddressVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.autocomplete(
            id="id",
        )
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_with_all_params(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.autocomplete(
            id="id",
            include_details=True,
            proper_case=True,
            use_enhanced_china_dataset=True,
            verify=True,
        )
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.autocomplete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.intl_address_verification.with_streaming_response.autocomplete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(
                IntlAddressVerificationAutocompleteResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_verification(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        )
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_verification_with_all_params(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                        "city": "city",
                        "line2": "line2",
                        "line3": "line3",
                        "line4": "line4",
                    }
                }
            ],
            geo_data=True,
            include_details=True,
            proper_case=True,
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch_verification(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(
            IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch_verification(self, async_client: AsyncPostGrid) -> None:
        async with async_client.intl_address_verification.with_streaming_response.batch_verification(
            addresses=[
                {
                    "address": {
                        "country": "country",
                        "line1": "line1",
                        "postal_or_zip": "postalOrZip",
                        "province_or_state": "provinceOrState",
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(
                IntlAddressVerificationBatchVerificationResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_advanced_previews(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.get_autocomplete_advanced_previews()
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_advanced_previews_with_all_params(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.get_autocomplete_advanced_previews(
            advanced=True,
            city_filter="cityFilter",
            container="container",
            countries_filter="countriesFilter",
            disable_ip_biasing=True,
            language="language",
            limit=0,
            partial_street="partialStreet",
            postal_or_zip_filter="postalOrZipFilter",
            standard_fallback=True,
            street_filter="streetFilter",
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_autocomplete_advanced_previews(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.get_autocomplete_advanced_previews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(
            IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_autocomplete_advanced_previews(self, async_client: AsyncPostGrid) -> None:
        async with (
            async_client.intl_address_verification.with_streaming_response.get_autocomplete_advanced_previews()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(
                IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
                intl_address_verification,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.get_autocomplete_previews()
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_autocomplete_previews_with_all_params(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.get_autocomplete_previews(
            advanced=True,
            city_filter="cityFilter",
            container="container",
            countries_filter="countriesFilter",
            disable_ip_biasing=True,
            language="language",
            limit=0,
            partial_street="partialStreet",
            postal_or_zip_filter="postalOrZipFilter",
            standard_fallback=True,
            street_filter="streetFilter",
            use_enhanced_china_dataset=True,
        )
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.get_autocomplete_previews()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(
            IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_autocomplete_previews(self, async_client: AsyncPostGrid) -> None:
        async with (
            async_client.intl_address_verification.with_streaming_response.get_autocomplete_previews()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(
                IntlAddressVerificationGetAutocompletePreviewsResponse, intl_address_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "city": "city",
                "line2": "line2",
                "line3": "line3",
                "line4": "line4",
            },
            geo_data=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.intl_address_verification.with_streaming_response.verify(
            address={
                "country": "country",
                "line1": "line1",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.verify(
            address="address",
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params_overload_2(self, async_client: AsyncPostGrid) -> None:
        intl_address_verification = await async_client.intl_address_verification.verify(
            address="address",
            geo_data=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.intl_address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intl_address_verification = await response.parse()
        assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_verify_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.intl_address_verification.with_streaming_response.verify(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intl_address_verification = await response.parse()
            assert_matches_type(IntlAddressVerificationVerifyResponse, intl_address_verification, path=["response"])

        assert cast(Any, response.is_closed) is True
