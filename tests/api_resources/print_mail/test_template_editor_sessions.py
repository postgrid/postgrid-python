# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    TemplateEditorSessionListResponse,
    TemplateEditorSessionCreateResponse,
    TemplateEditorSessionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplateEditorSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        template_editor_session = client.print_mail.template_editor_sessions.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        )
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        template_editor_session = client.print_mail.template_editor_sessions.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
            back_url="https://postgrid.com",
            styles={
                "canvas": {"background_color": "backgroundColor"},
                "panel_text": {"color": "color"},
                "save_button": {
                    "background_color": "backgroundColor",
                    "text_color": "textColor",
                },
            },
            title="My Editor Session",
            trackers=["tracker_123456789abcdefghijklmnopqrstuvwxyz"],
        )
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.template_editor_sessions.with_raw_response.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = response.parse()
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.template_editor_sessions.with_streaming_response.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = response.parse()
            assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        template_editor_session = client.print_mail.template_editor_sessions.list()
        assert_matches_type(
            SyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        template_editor_session = client.print_mail.template_editor_sessions.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(
            SyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.template_editor_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = response.parse()
        assert_matches_type(
            SyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.template_editor_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = response.parse()
            assert_matches_type(
                SyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        template_editor_session = client.print_mail.template_editor_sessions.delete(
            "id",
        )
        assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.template_editor_sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = response.parse()
        assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.template_editor_sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = response.parse()
            assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.template_editor_sessions.with_raw_response.delete(
                "",
            )


class TestAsyncTemplateEditorSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        template_editor_session = await async_client.print_mail.template_editor_sessions.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        )
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        template_editor_session = await async_client.print_mail.template_editor_sessions.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
            back_url="https://postgrid.com",
            styles={
                "canvas": {"background_color": "backgroundColor"},
                "panel_text": {"color": "color"},
                "save_button": {
                    "background_color": "backgroundColor",
                    "text_color": "textColor",
                },
            },
            title="My Editor Session",
            trackers=["tracker_123456789abcdefghijklmnopqrstuvwxyz"],
        )
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.template_editor_sessions.with_raw_response.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = await response.parse()
        assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.template_editor_sessions.with_streaming_response.create(
            template="template_eYxcbMKPZEZPk71ZJPA6Yz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = await response.parse()
            assert_matches_type(TemplateEditorSessionCreateResponse, template_editor_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        template_editor_session = await async_client.print_mail.template_editor_sessions.list()
        assert_matches_type(
            AsyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        template_editor_session = await async_client.print_mail.template_editor_sessions.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(
            AsyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.template_editor_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = await response.parse()
        assert_matches_type(
            AsyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.template_editor_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = await response.parse()
            assert_matches_type(
                AsyncSkipLimit[TemplateEditorSessionListResponse], template_editor_session, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        template_editor_session = await async_client.print_mail.template_editor_sessions.delete(
            "id",
        )
        assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.template_editor_sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template_editor_session = await response.parse()
        assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.template_editor_sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template_editor_session = await response.parse()
            assert_matches_type(TemplateEditorSessionDeleteResponse, template_editor_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.template_editor_sessions.with_raw_response.delete(
                "",
            )
