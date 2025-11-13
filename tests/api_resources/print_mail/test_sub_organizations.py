# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    SubOrganization,
    SubOrganizationUpdateResponse,
    SubOrganizationRetrieveUsersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.retrieve(
            "id",
        )
        assert_matches_type(SubOrganization, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.sub_organizations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = response.parse()
        assert_matches_type(SubOrganization, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.sub_organizations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = response.parse()
            assert_matches_type(SubOrganization, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.sub_organizations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        )
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
            phone_number="9059059059",
        )
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.sub_organizations.with_raw_response.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = response.parse()
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.sub_organizations.with_streaming_response.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = response.parse()
            assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.list()
        assert_matches_type(SyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.sub_organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = response.parse()
        assert_matches_type(SyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.sub_organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = response.parse()
            assert_matches_type(SyncSkipLimit[SubOrganization], sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_users(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.retrieve_users(
            id="id",
        )
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_users_with_all_params(self, client: PostGrid) -> None:
        sub_organization = client.print_mail.sub_organizations.retrieve_users(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_users(self, client: PostGrid) -> None:
        response = client.print_mail.sub_organizations.with_raw_response.retrieve_users(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = response.parse()
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_users(self, client: PostGrid) -> None:
        with client.print_mail.sub_organizations.with_streaming_response.retrieve_users(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = response.parse()
            assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_users(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.sub_organizations.with_raw_response.retrieve_users(
                id="",
            )


class TestAsyncSubOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.retrieve(
            "id",
        )
        assert_matches_type(SubOrganization, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.sub_organizations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = await response.parse()
        assert_matches_type(SubOrganization, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.sub_organizations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = await response.parse()
            assert_matches_type(SubOrganization, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.sub_organizations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        )
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
            phone_number="9059059059",
        )
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.sub_organizations.with_raw_response.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = await response.parse()
        assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.sub_organizations.with_streaming_response.update(
            country_code="CA",
            email="suborg@postgrid.com",
            name="Calvin",
            organization_name="PostGrid",
            password="very-strong-password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = await response.parse()
            assert_matches_type(SubOrganizationUpdateResponse, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.list()
        assert_matches_type(AsyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.sub_organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = await response.parse()
        assert_matches_type(AsyncSkipLimit[SubOrganization], sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.sub_organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = await response.parse()
            assert_matches_type(AsyncSkipLimit[SubOrganization], sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_users(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.retrieve_users(
            id="id",
        )
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_users_with_all_params(self, async_client: AsyncPostGrid) -> None:
        sub_organization = await async_client.print_mail.sub_organizations.retrieve_users(
            id="id",
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_users(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.sub_organizations.with_raw_response.retrieve_users(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_organization = await response.parse()
        assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_users(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.sub_organizations.with_streaming_response.retrieve_users(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_organization = await response.parse()
            assert_matches_type(SubOrganizationRetrieveUsersResponse, sub_organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_users(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.sub_organizations.with_raw_response.retrieve_users(
                id="",
            )
