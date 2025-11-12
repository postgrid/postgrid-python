# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    BankAccount,
    BankAccountDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBankAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.retrieve(
            "id",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.bank_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.list()
        assert_matches_type(SyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(SyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(SyncSkipLimit[BankAccount], bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        bank_account = client.print_mail.bank_accounts.delete(
            "id",
        )
        assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.bank_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = response.parse()
        assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.bank_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = response.parse()
            assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.bank_accounts.with_raw_response.delete(
                "",
            )


class TestAsyncBankAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_text="signatureText",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
            bank_primary_line="bankPrimaryLine",
            bank_secondary_line="bankSecondaryLine",
            ca_designation_number="caDesignationNumber",
            description="description",
            metadata={"foo": "bar"},
            route_number="routeNumber",
            routing_number="routingNumber",
            transit_number="transitNumber",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.create(
            account_number="accountNumber",
            bank_country_code="CA",
            bank_name="bankName",
            signature_image="U3RhaW5sZXNzIHJvY2tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.retrieve(
            "id",
        )
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccount, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccount, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.bank_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.list()
        assert_matches_type(AsyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(AsyncSkipLimit[BankAccount], bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(AsyncSkipLimit[BankAccount], bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        bank_account = await async_client.print_mail.bank_accounts.delete(
            "id",
        )
        assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.bank_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank_account = await response.parse()
        assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.bank_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank_account = await response.parse()
            assert_matches_type(BankAccountDeleteResponse, bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.bank_accounts.with_raw_response.delete(
                "",
            )
