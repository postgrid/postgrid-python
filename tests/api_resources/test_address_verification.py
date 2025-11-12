# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types import AddressVerificationVerifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address="address",
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_with_all_params_overload_1(self, client: PostGrid) -> None:
        address_verification = client.address_verification.verify(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify_overload_1(self, client: PostGrid) -> None:
        response = client.address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address="address",
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        address_verification = await async_client.address_verification.verify(
            address="address",
            geocode=True,
            include_details=True,
            proper_case=True,
        )
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.address_verification.with_raw_response.verify(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_verification = await response.parse()
        assert_matches_type(AddressVerificationVerifyResponse, address_verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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
