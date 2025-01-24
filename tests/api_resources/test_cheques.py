# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types import Cheque
from postgrid._utils import parse_datetime
from postgrid.pagination import SyncList, AsyncList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheques:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        cheque = client.cheques.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        cheque = client.cheques.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
            currency_code="USD",
            description="description",
            digital_only={"watermark": "watermark"},
            envelope="standard",
            logo_url="https://example.com",
            mailing_class="first_class",
            memo="memo",
            merge_variables={"foo": "bar"},
            message="message",
            metadata={"foo": "bar"},
            number=123456,
            redirect_to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.cheques.with_raw_response.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.cheques.with_streaming_response.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        cheque = client.cheques.retrieve(
            "id",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.cheques.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.cheques.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cheques.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        cheque = client.cheques.list()
        assert_matches_type(SyncList[Cheque], cheque, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        cheque = client.cheques.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncList[Cheque], cheque, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.cheques.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = response.parse()
        assert_matches_type(SyncList[Cheque], cheque, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.cheques.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = response.parse()
            assert_matches_type(SyncList[Cheque], cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: PostGrid) -> None:
        cheque = client.cheques.cancel(
            "id",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: PostGrid) -> None:
        response = client.cheques.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: PostGrid) -> None:
        with client.cheques.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cheques.with_raw_response.cancel(
                "",
            )


class TestAsyncCheques:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
            currency_code="USD",
            description="description",
            digital_only={"watermark": "watermark"},
            envelope="standard",
            logo_url="https://example.com",
            mailing_class="first_class",
            memo="memo",
            merge_variables={"foo": "bar"},
            message="message",
            metadata={"foo": "bar"},
            number=123456,
            redirect_to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.cheques.with_raw_response.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = await response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.cheques.with_streaming_response.create(
            amount=1000,
            bank_account="bank_123",
            from_="contact_123",
            to="contact_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = await response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.retrieve(
            "id",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.cheques.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = await response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.cheques.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = await response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cheques.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.list()
        assert_matches_type(AsyncList[Cheque], cheque, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncList[Cheque], cheque, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.cheques.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = await response.parse()
        assert_matches_type(AsyncList[Cheque], cheque, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.cheques.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = await response.parse()
            assert_matches_type(AsyncList[Cheque], cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncPostGrid) -> None:
        cheque = await async_client.cheques.cancel(
            "id",
        )
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.cheques.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cheque = await response.parse()
        assert_matches_type(Cheque, cheque, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPostGrid) -> None:
        async with async_client.cheques.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cheque = await response.parse()
            assert_matches_type(Cheque, cheque, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cheques.with_raw_response.cancel(
                "",
            )
