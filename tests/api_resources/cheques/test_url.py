# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types.cheques import URLRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        url = client.cheques.url.retrieve(
            "id",
        )
        assert_matches_type(URLRetrieveResponse, url, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.cheques.url.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = response.parse()
        assert_matches_type(URLRetrieveResponse, url, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.cheques.url.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = response.parse()
            assert_matches_type(URLRetrieveResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.cheques.url.with_raw_response.retrieve(
                "",
            )


class TestAsyncURL:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        url = await async_client.cheques.url.retrieve(
            "id",
        )
        assert_matches_type(URLRetrieveResponse, url, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.cheques.url.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url = await response.parse()
        assert_matches_type(URLRetrieveResponse, url, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.cheques.url.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url = await response.parse()
            assert_matches_type(URLRetrieveResponse, url, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.cheques.url.with_raw_response.retrieve(
                "",
            )
