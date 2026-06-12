# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types import (
    BulkVerificationListResponse,
    BulkVerificationUploadResponse,
    BulkVerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        bulk_verification = client.bulk_verification.retrieve(
            "id",
        )
        assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.bulk_verification.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = response.parse()
        assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.bulk_verification.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = response.parse()
            assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bulk_verification.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        bulk_verification = client.bulk_verification.list()
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        bulk_verification = client.bulk_verification.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.bulk_verification.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = response.parse()
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.bulk_verification.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = response.parse()
            assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: PostGrid) -> None:
        bulk_verification = client.bulk_verification.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        )
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: PostGrid) -> None:
        bulk_verification = client.bulk_verification.upload(
            file=b"Example data",
            mappings={
                "line1": "line1",
                "city": "city",
                "country": "country",
                "first_name": "firstName",
                "full_name": "fullName",
                "last_name": "lastName",
                "line2": "line2",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
            name="name",
            default_country="defaultCountry",
            run_ccoa=True,
            run_ncoa=True,
            use_geocode=True,
            use_intl_verification=True,
            use_proper_case=True,
        )
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: PostGrid) -> None:
        response = client.bulk_verification.with_raw_response.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = response.parse()
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: PostGrid) -> None:
        with client.bulk_verification.with_streaming_response.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = response.parse()
            assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulkVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        bulk_verification = await async_client.bulk_verification.retrieve(
            "id",
        )
        assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.bulk_verification.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = await response.parse()
        assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.bulk_verification.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = await response.parse()
            assert_matches_type(BulkVerificationRetrieveResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bulk_verification.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        bulk_verification = await async_client.bulk_verification.list()
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        bulk_verification = await async_client.bulk_verification.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.bulk_verification.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = await response.parse()
        assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.bulk_verification.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = await response.parse()
            assert_matches_type(BulkVerificationListResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncPostGrid) -> None:
        bulk_verification = await async_client.bulk_verification.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        )
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncPostGrid) -> None:
        bulk_verification = await async_client.bulk_verification.upload(
            file=b"Example data",
            mappings={
                "line1": "line1",
                "city": "city",
                "country": "country",
                "first_name": "firstName",
                "full_name": "fullName",
                "last_name": "lastName",
                "line2": "line2",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
            },
            name="name",
            default_country="defaultCountry",
            run_ccoa=True,
            run_ncoa=True,
            use_geocode=True,
            use_intl_verification=True,
            use_proper_case=True,
        )
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.bulk_verification.with_raw_response.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_verification = await response.parse()
        assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncPostGrid) -> None:
        async with async_client.bulk_verification.with_streaming_response.upload(
            file=b"Example data",
            mappings={"line1": "line1"},
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_verification = await response.parse()
            assert_matches_type(BulkVerificationUploadResponse, bulk_verification, path=["response"])

        assert cast(Any, response.is_closed) is True
