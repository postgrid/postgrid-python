# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail.return_envelopes import (
    ReturnEnvelopeOrder,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.create(
            id="id",
            quantity_ordered=5000,
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.create(
            id="id",
            quantity_ordered=5000,
            description="A batch of 5000",
            metadata={"foo": "bar"},
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.return_envelopes.orders.with_raw_response.create(
            id="id",
            quantity_ordered=5000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.return_envelopes.orders.with_streaming_response.create(
            id="id",
            quantity_ordered=5000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.create(
                id="",
                quantity_ordered=5000,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.retrieve(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.retrieve(
            order_id="orderID",
            id="id",
            expand=["returnEnvelope"],
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.return_envelopes.orders.with_streaming_response.retrieve(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
                order_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.list(
            id="id",
        )
        assert_matches_type(SyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.list(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.return_envelopes.orders.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(SyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.return_envelopes.orders.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(SyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.cancel(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.cancel(
            order_id="orderID",
            id="id",
            expand=["returnEnvelope"],
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: PostGrid) -> None:
        response = client.print_mail.return_envelopes.orders.with_raw_response.cancel(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: PostGrid) -> None:
        with client.print_mail.return_envelopes.orders.with_streaming_response.cancel(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.cancel(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.cancel(
                order_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fill(self, client: PostGrid) -> None:
        order = client.print_mail.return_envelopes.orders.fill(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fill(self, client: PostGrid) -> None:
        response = client.print_mail.return_envelopes.orders.with_raw_response.fill(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fill(self, client: PostGrid) -> None:
        with client.print_mail.return_envelopes.orders.with_streaming_response.fill(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fill(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.fill(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.print_mail.return_envelopes.orders.with_raw_response.fill(
                order_id="",
                id="id",
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.create(
            id="id",
            quantity_ordered=5000,
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.create(
            id="id",
            quantity_ordered=5000,
            description="A batch of 5000",
            metadata={"foo": "bar"},
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.return_envelopes.orders.with_raw_response.create(
            id="id",
            quantity_ordered=5000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.return_envelopes.orders.with_streaming_response.create(
            id="id",
            quantity_ordered=5000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.create(
                id="",
                quantity_ordered=5000,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.retrieve(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.retrieve(
            order_id="orderID",
            id="id",
            expand=["returnEnvelope"],
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.return_envelopes.orders.with_streaming_response.retrieve(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.retrieve(
                order_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.list(
            id="id",
        )
        assert_matches_type(AsyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.list(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.return_envelopes.orders.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(AsyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.return_envelopes.orders.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(AsyncSkipLimit[ReturnEnvelopeOrder], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.cancel(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.cancel(
            order_id="orderID",
            id="id",
            expand=["returnEnvelope"],
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.return_envelopes.orders.with_raw_response.cancel(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.return_envelopes.orders.with_streaming_response.cancel(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.cancel(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.cancel(
                order_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fill(self, async_client: AsyncPostGrid) -> None:
        order = await async_client.print_mail.return_envelopes.orders.fill(
            order_id="orderID",
            id="id",
        )
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fill(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.return_envelopes.orders.with_raw_response.fill(
            order_id="orderID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fill(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.return_envelopes.orders.with_streaming_response.fill(
            order_id="orderID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(ReturnEnvelopeOrder, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fill(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.fill(
                order_id="orderID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.print_mail.return_envelopes.orders.with_raw_response.fill(
                order_id="",
                id="id",
            )
