# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    TrackerListResponse,
    TrackerCreateResponse,
    TrackerDeleteResponse,
    TrackerUpdateResponse,
    TrackerRetrieveResponse,
    TrackerRetrieveVisitsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrackers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        )
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.retrieve(
            "id",
        )
        assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.trackers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        )
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.trackers.with_raw_response.update(
                id="",
                redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
                url_expire_after_days=90,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.list()
        assert_matches_type(SyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(SyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(SyncSkipLimit[TrackerListResponse], tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.delete(
            "id",
        )
        assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.trackers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_visits(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.retrieve_visits(
            id="id",
        )
        assert_matches_type(SyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_visits_with_all_params(self, client: PostGrid) -> None:
        tracker = client.print_mail.trackers.retrieve_visits(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_visits(self, client: PostGrid) -> None:
        response = client.print_mail.trackers.with_raw_response.retrieve_visits(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = response.parse()
        assert_matches_type(SyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_visits(self, client: PostGrid) -> None:
        with client.print_mail.trackers.with_streaming_response.retrieve_visits(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = response.parse()
            assert_matches_type(SyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_visits(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.trackers.with_raw_response.retrieve_visits(
                id="",
            )


class TestAsyncTrackers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        )
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.create(
            redirect_url_template="https://postgrid.com?name={{to.firstName}}",
            url_expire_after_days=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(TrackerCreateResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.retrieve(
            "id",
        )
        assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(TrackerRetrieveResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.trackers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        )
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.update(
            id="id",
            redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
            url_expire_after_days=90,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(TrackerUpdateResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.trackers.with_raw_response.update(
                id="",
                redirect_url_template="https://postgrid.com?firstName={{to.firstName}}",
                url_expire_after_days=90,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.list()
        assert_matches_type(AsyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(AsyncSkipLimit[TrackerListResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(AsyncSkipLimit[TrackerListResponse], tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.delete(
            "id",
        )
        assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(TrackerDeleteResponse, tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.trackers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_visits(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.retrieve_visits(
            id="id",
        )
        assert_matches_type(AsyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_visits_with_all_params(self, async_client: AsyncPostGrid) -> None:
        tracker = await async_client.print_mail.trackers.retrieve_visits(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_visits(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.trackers.with_raw_response.retrieve_visits(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracker = await response.parse()
        assert_matches_type(AsyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_visits(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.trackers.with_streaming_response.retrieve_visits(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracker = await response.parse()
            assert_matches_type(AsyncSkipLimit[TrackerRetrieveVisitsResponse], tracker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_visits(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.trackers.with_raw_response.retrieve_visits(
                id="",
            )
