# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import Event

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        event = client.print_mail.events.list()
        assert_matches_type(SyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        event = client.print_mail.events.list(
            limit=0,
            skip=0,
            type=["letter.created"],
        )
        assert_matches_type(SyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncSkipLimit[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        event = await async_client.print_mail.events.list()
        assert_matches_type(AsyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        event = await async_client.print_mail.events.list(
            limit=0,
            skip=0,
            type=["letter.created"],
        )
        assert_matches_type(AsyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncSkipLimit[Event], event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncSkipLimit[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True
