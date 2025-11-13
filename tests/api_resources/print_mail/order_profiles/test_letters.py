# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail.order_profiles import (
    LetterProfile,
    LetterDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLetters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.create(
            size="us_letter",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.create(
            size="us_letter",
            expand=["string"],
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="Monthly Newsletter Profile",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"salutation": "bar"},
            metadata={"campaign": "Q1 Newsletter"},
            pdf="https://example.com",
            perforated_page=1,
            return_envelope="returnEnvelope",
            template="template_abc",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.letters.with_raw_response.create(
            size="us_letter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.letters.with_streaming_response.create(
            size="us_letter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.retrieve(
            id="id",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.retrieve(
            id="id",
            expand=["string"],
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.letters.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.letters.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.letters.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.update(
            id="id",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.update(
            id="id",
            expand=["string"],
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=False,
            description="Updated Newsletter Profile",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            pdf="https://example.com",
            perforated_page=1,
            return_envelope="returnEnvelope",
            template="template",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.letters.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.letters.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.letters.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.list()
        assert_matches_type(SyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.letters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(SyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.letters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(SyncSkipLimit[LetterProfile], letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        letter = client.print_mail.order_profiles.letters.delete(
            "id",
        )
        assert_matches_type(LetterDeleteResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.order_profiles.letters.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(LetterDeleteResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.order_profiles.letters.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(LetterDeleteResponse, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.order_profiles.letters.with_raw_response.delete(
                "",
            )


class TestAsyncLetters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.create(
            size="us_letter",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.create(
            size="us_letter",
            expand=["string"],
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="Monthly Newsletter Profile",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"salutation": "bar"},
            metadata={"campaign": "Q1 Newsletter"},
            pdf="https://example.com",
            perforated_page=1,
            return_envelope="returnEnvelope",
            template="template_abc",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.letters.with_raw_response.create(
            size="us_letter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.letters.with_streaming_response.create(
            size="us_letter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.retrieve(
            id="id",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.retrieve(
            id="id",
            expand=["string"],
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.letters.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.letters.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.letters.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.update(
            id="id",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.update(
            id="id",
            expand=["string"],
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=False,
            description="Updated Newsletter Profile",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "string"},
            pdf="https://example.com",
            perforated_page=1,
            return_envelope="returnEnvelope",
            template="template",
        )
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.letters.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(LetterProfile, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.letters.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(LetterProfile, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.letters.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.list()
        assert_matches_type(AsyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.letters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(AsyncSkipLimit[LetterProfile], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.letters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(AsyncSkipLimit[LetterProfile], letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.order_profiles.letters.delete(
            "id",
        )
        assert_matches_type(LetterDeleteResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.order_profiles.letters.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(LetterDeleteResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.order_profiles.letters.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(LetterDeleteResponse, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.order_profiles.letters.with_raw_response.delete(
                "",
            )
