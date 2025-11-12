# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid._utils import parse_datetime
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import Box

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBoxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "logo_url": "https://example.com",
                    "memo": "memo",
                    "merge_variables": {"foo": "bar"},
                    "message_template": "messageTemplate",
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.boxes.with_raw_response.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.boxes.with_streaming_response.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.retrieve(
            "id",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.boxes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.boxes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.list()
        assert_matches_type(SyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(SyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(SyncSkipLimit[Box], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        box = client.print_mail.boxes.delete(
            "id",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.boxes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.boxes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.boxes.with_raw_response.delete(
                "",
            )


class TestAsyncBoxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "logo_url": "https://example.com",
                    "memo": "memo",
                    "merge_variables": {"foo": "bar"},
                    "message_template": "messageTemplate",
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.boxes.with_raw_response.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.boxes.with_streaming_response.create(
            cheques=[
                {
                    "amount": 5000,
                    "bank_account": "bank_abc",
                    "number": 1042,
                    "from": "contact_456",
                    "to": "contact_123",
                }
            ],
            from_="contact_456",
            to="contact_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.retrieve(
            "id",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.boxes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.boxes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.list()
        assert_matches_type(AsyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(AsyncSkipLimit[Box], box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(AsyncSkipLimit[Box], box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        box = await async_client.print_mail.boxes.delete(
            "id",
        )
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.boxes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(Box, box, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.boxes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(Box, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.boxes.with_raw_response.delete(
                "",
            )
