# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    VirtualMailboxListResponse,
    VirtualMailboxCreateResponse,
    VirtualMailboxRetrieveResponse,
    VirtualMailboxRetrieveAddressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVirtualMailboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.create(
            country_code="US",
        )
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.create(
            country_code="US",
            capabilities={
                "envelope_scans": True,
                "forward_mail_to": "contact_pxd7wnnD1xY6H6etKNvjb4",
            },
        )
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.virtual_mailboxes.with_raw_response.create(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = response.parse()
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.virtual_mailboxes.with_streaming_response.create(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = response.parse()
            assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.retrieve(
            "id",
        )
        assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.virtual_mailboxes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = response.parse()
        assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.virtual_mailboxes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = response.parse()
            assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.virtual_mailboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.list()
        assert_matches_type(SyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.virtual_mailboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = response.parse()
        assert_matches_type(SyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.virtual_mailboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = response.parse()
            assert_matches_type(SyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_address(self, client: PostGrid) -> None:
        virtual_mailbox = client.print_mail.virtual_mailboxes.retrieve_address(
            "id",
        )
        assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_address(self, client: PostGrid) -> None:
        response = client.print_mail.virtual_mailboxes.with_raw_response.retrieve_address(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = response.parse()
        assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_address(self, client: PostGrid) -> None:
        with client.print_mail.virtual_mailboxes.with_streaming_response.retrieve_address(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = response.parse()
            assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_address(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.virtual_mailboxes.with_raw_response.retrieve_address(
                "",
            )


class TestAsyncVirtualMailboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.create(
            country_code="US",
        )
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.create(
            country_code="US",
            capabilities={
                "envelope_scans": True,
                "forward_mail_to": "contact_pxd7wnnD1xY6H6etKNvjb4",
            },
        )
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.virtual_mailboxes.with_raw_response.create(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = await response.parse()
        assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.virtual_mailboxes.with_streaming_response.create(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = await response.parse()
            assert_matches_type(VirtualMailboxCreateResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.retrieve(
            "id",
        )
        assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.virtual_mailboxes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = await response.parse()
        assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.virtual_mailboxes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = await response.parse()
            assert_matches_type(VirtualMailboxRetrieveResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.virtual_mailboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.list()
        assert_matches_type(AsyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.virtual_mailboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = await response.parse()
        assert_matches_type(AsyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.virtual_mailboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = await response.parse()
            assert_matches_type(AsyncSkipLimit[VirtualMailboxListResponse], virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_address(self, async_client: AsyncPostGrid) -> None:
        virtual_mailbox = await async_client.print_mail.virtual_mailboxes.retrieve_address(
            "id",
        )
        assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_address(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.virtual_mailboxes.with_raw_response.retrieve_address(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_mailbox = await response.parse()
        assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_address(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.virtual_mailboxes.with_streaming_response.retrieve_address(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_mailbox = await response.parse()
            assert_matches_type(VirtualMailboxRetrieveAddressResponse, virtual_mailbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_address(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.virtual_mailboxes.with_raw_response.retrieve_address(
                "",
            )
