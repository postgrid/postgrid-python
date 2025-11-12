# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    MailingList,
    MailingListUpdate,
    MailingListDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMailingLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.create()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.create(
            description="Test Mailing List",
            metadata={"campaign": "bar"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.retrieve(
            "id",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_lists.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.update(
            id="id",
        )
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.update(
            id="id",
            description="Updated Mailing List Description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_lists.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.list()
        assert_matches_type(SyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(SyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(SyncSkipLimit[MailingList], mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.delete(
            "id",
        )
        assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_jobs(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.jobs(
            id="id",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_jobs_with_all_params(self, client: PostGrid) -> None:
        mailing_list = client.print_mail.mailing_lists.jobs(
            id="id",
            add_contacts=["string"],
            add_mailing_list_imports=["string"],
            remove_contacts=["string"],
            remove_mailing_list_imports=["mailing_list_import_123", "mailing_list_import_456"],
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_jobs(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_lists.with_raw_response.jobs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_jobs(self, client: PostGrid) -> None:
        with client.print_mail.mailing_lists.with_streaming_response.jobs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_jobs(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_lists.with_raw_response.jobs(
                id="",
            )


class TestAsyncMailingLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.create()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.create(
            description="Test Mailing List",
            metadata={"campaign": "bar"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.retrieve(
            "id",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_lists.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.update(
            id="id",
        )
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.update(
            id="id",
            description="Updated Mailing List Description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(MailingListUpdate, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_lists.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.list()
        assert_matches_type(AsyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(AsyncSkipLimit[MailingList], mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(AsyncSkipLimit[MailingList], mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.delete(
            "id",
        )
        assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(MailingListDeleteResponse, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_jobs(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.jobs(
            id="id",
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_jobs_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list = await async_client.print_mail.mailing_lists.jobs(
            id="id",
            add_contacts=["string"],
            add_mailing_list_imports=["string"],
            remove_contacts=["string"],
            remove_mailing_list_imports=["mailing_list_import_123", "mailing_list_import_456"],
        )
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_jobs(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_lists.with_raw_response.jobs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list = await response.parse()
        assert_matches_type(MailingList, mailing_list, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_jobs(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_lists.with_streaming_response.jobs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list = await response.parse()
            assert_matches_type(MailingList, mailing_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_jobs(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_lists.with_raw_response.jobs(
                id="",
            )
