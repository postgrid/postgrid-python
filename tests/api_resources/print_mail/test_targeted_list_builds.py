# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    TargetedListBuildListResponse,
    TargetedListBuildCreateResponse,
    TargetedListBuildDeleteResponse,
    TargetedListBuildUpdateResponse,
    TargetedListBuildConfirmResponse,
    TargetedListBuildRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTargetedListBuilds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.create()
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.create(
            description="Q1 prospecting list",
            limit=1000,
            metadata={"campaign": "bar"},
            us_companies={
                "postal_codes": ["10001", "10002"],
                "company_types": ["public"],
                "employee_count": [10, 500],
                "founded_year": [1600, 1600],
                "industries": ["software"],
                "naics_codes": ["string"],
                "tags": ["string"],
            },
            us_consumers={
                "age_range": [18, 18],
                "city_states": ["string"],
                "education_levels": ["high_school"],
                "gender": "male",
                "home_value_range": [0, 0],
                "income_range": [0, 0],
                "num_children_range": [0, 0],
                "occupations": ["professional_technical"],
                "zip_codes": ["string"],
                "zip_codes_around": {
                    "radius_in_miles": 0.1,
                    "zip_code": "zipCode",
                },
            },
            idempotency_key="idempotency-key",
        )
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.retrieve(
            "id",
        )
        assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.targeted_list_builds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.update(
            id="id",
        )
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.update(
            id="id",
            description="description",
            limit=2000,
            metadata={"foo": "bar"},
            us_companies={
                "postal_codes": ["10001", "10002", "10003"],
                "company_types": ["public"],
                "employee_count": [50, 1000],
                "founded_year": [1600, 1600],
                "industries": ["software", "fintech"],
                "naics_codes": ["string"],
                "tags": ["string"],
            },
            us_consumers={
                "age_range": [18, 18],
                "city_states": ["string"],
                "education_levels": ["high_school"],
                "gender": "male",
                "home_value_range": [0, 0],
                "income_range": [0, 0],
                "num_children_range": [0, 0],
                "occupations": ["professional_technical"],
                "zip_codes": ["string"],
                "zip_codes_around": {
                    "radius_in_miles": 0.1,
                    "zip_code": "zipCode",
                },
            },
        )
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.targeted_list_builds.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.list()
        assert_matches_type(SyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(SyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(SyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.delete(
            "id",
        )
        assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.targeted_list_builds.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_confirm(self, client: PostGrid) -> None:
        targeted_list_build = client.print_mail.targeted_list_builds.confirm(
            "id",
        )
        assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_confirm(self, client: PostGrid) -> None:
        response = client.print_mail.targeted_list_builds.with_raw_response.confirm(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = response.parse()
        assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_confirm(self, client: PostGrid) -> None:
        with client.print_mail.targeted_list_builds.with_streaming_response.confirm(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = response.parse()
            assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_confirm(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.targeted_list_builds.with_raw_response.confirm(
                "",
            )


class TestAsyncTargetedListBuilds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.create()
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.create(
            description="Q1 prospecting list",
            limit=1000,
            metadata={"campaign": "bar"},
            us_companies={
                "postal_codes": ["10001", "10002"],
                "company_types": ["public"],
                "employee_count": [10, 500],
                "founded_year": [1600, 1600],
                "industries": ["software"],
                "naics_codes": ["string"],
                "tags": ["string"],
            },
            us_consumers={
                "age_range": [18, 18],
                "city_states": ["string"],
                "education_levels": ["high_school"],
                "gender": "male",
                "home_value_range": [0, 0],
                "income_range": [0, 0],
                "num_children_range": [0, 0],
                "occupations": ["professional_technical"],
                "zip_codes": ["string"],
                "zip_codes_around": {
                    "radius_in_miles": 0.1,
                    "zip_code": "zipCode",
                },
            },
            idempotency_key="idempotency-key",
        )
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(TargetedListBuildCreateResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.retrieve(
            "id",
        )
        assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(TargetedListBuildRetrieveResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.targeted_list_builds.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.update(
            id="id",
        )
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.update(
            id="id",
            description="description",
            limit=2000,
            metadata={"foo": "bar"},
            us_companies={
                "postal_codes": ["10001", "10002", "10003"],
                "company_types": ["public"],
                "employee_count": [50, 1000],
                "founded_year": [1600, 1600],
                "industries": ["software", "fintech"],
                "naics_codes": ["string"],
                "tags": ["string"],
            },
            us_consumers={
                "age_range": [18, 18],
                "city_states": ["string"],
                "education_levels": ["high_school"],
                "gender": "male",
                "home_value_range": [0, 0],
                "income_range": [0, 0],
                "num_children_range": [0, 0],
                "occupations": ["professional_technical"],
                "zip_codes": ["string"],
                "zip_codes_around": {
                    "radius_in_miles": 0.1,
                    "zip_code": "zipCode",
                },
            },
        )
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(TargetedListBuildUpdateResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.targeted_list_builds.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.list()
        assert_matches_type(AsyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(AsyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(AsyncSkipLimit[TargetedListBuildListResponse], targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.delete(
            "id",
        )
        assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(TargetedListBuildDeleteResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.targeted_list_builds.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_confirm(self, async_client: AsyncPostGrid) -> None:
        targeted_list_build = await async_client.print_mail.targeted_list_builds.confirm(
            "id",
        )
        assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.targeted_list_builds.with_raw_response.confirm(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        targeted_list_build = await response.parse()
        assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.targeted_list_builds.with_streaming_response.confirm(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            targeted_list_build = await response.parse()
            assert_matches_type(TargetedListBuildConfirmResponse, targeted_list_build, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.targeted_list_builds.with_raw_response.confirm(
                "",
            )
