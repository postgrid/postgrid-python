# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail.order_profiles import (
    SelfMailerProfile,
    SelfMailerDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSelfMailers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.create(
            size="8.5x11_bifold",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.create(
            size="8.5x11_bifold",
            expand=["string"],
            description="description",
            inside_template="insideTemplate",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            outside_template="outsideTemplate",
            pdf="https://example.com",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.self_mailers.with_raw_response.create(
            size="8.5x11_bifold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.self_mailers.with_streaming_response.create(
            size="8.5x11_bifold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.retrieve(
            id="id",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.retrieve(
            id="id",
            expand=["string"],
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.self_mailers.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.self_mailers.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.self_mailers.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.update(
            id="id",
            size="8.5x11_bifold",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.update(
            id="id",
            size="8.5x11_bifold",
            expand=["string"],
            description="description",
            inside_template="insideTemplate",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            outside_template="outsideTemplate",
            pdf="https://example.com",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.self_mailers.with_raw_response.update(
            id="id",
            size="8.5x11_bifold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.self_mailers.with_streaming_response.update(
            id="id",
            size="8.5x11_bifold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.self_mailers.with_raw_response.update(
                id="",
                size="8.5x11_bifold",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.list()
        assert_matches_type(SyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.self_mailers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = response.parse()
        assert_matches_type(SyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.self_mailers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = response.parse()
            assert_matches_type(SyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        self_mailer = client.print_mail.order_profiles.self_mailers.delete(
            "id",
        )
        assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.self_mailers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = response.parse()
        assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.self_mailers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = response.parse()
            assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.self_mailers.with_raw_response.delete(
                "",
            )


class TestAsyncSelfMailers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.create(
            size="8.5x11_bifold",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.create(
            size="8.5x11_bifold",
            expand=["string"],
            description="description",
            inside_template="insideTemplate",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            outside_template="outsideTemplate",
            pdf="https://example.com",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.self_mailers.with_raw_response.create(
            size="8.5x11_bifold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = await response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.self_mailers.with_streaming_response.create(
            size="8.5x11_bifold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = await response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.retrieve(
            id="id",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.retrieve(
            id="id",
            expand=["string"],
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.self_mailers.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = await response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.self_mailers.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = await response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.self_mailers.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.update(
            id="id",
            size="8.5x11_bifold",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.update(
            id="id",
            size="8.5x11_bifold",
            expand=["string"],
            description="description",
            inside_template="insideTemplate",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            outside_template="outsideTemplate",
            pdf="https://example.com",
        )
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.self_mailers.with_raw_response.update(
            id="id",
            size="8.5x11_bifold",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = await response.parse()
        assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.self_mailers.with_streaming_response.update(
            id="id",
            size="8.5x11_bifold",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = await response.parse()
            assert_matches_type(SelfMailerProfile, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.self_mailers.with_raw_response.update(
                id="",
                size="8.5x11_bifold",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.list()
        assert_matches_type(AsyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.self_mailers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = await response.parse()
        assert_matches_type(AsyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.self_mailers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = await response.parse()
            assert_matches_type(AsyncSkipLimit[SelfMailerProfile], self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        self_mailer = await async_client.print_mail.order_profiles.self_mailers.delete(
            "id",
        )
        assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.self_mailers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        self_mailer = await response.parse()
        assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.self_mailers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            self_mailer = await response.parse()
            assert_matches_type(SelfMailerDeleteResponse, self_mailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.self_mailers.with_raw_response.delete(
                "",
            )
