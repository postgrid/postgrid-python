# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import Postgrid, AsyncPostgrid
from tests.utils import assert_matches_type
from postgrid.types import Contact, ContactDeleteResponse
from postgrid.pagination import SyncList, AsyncList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Postgrid) -> None:
        contact = client.contacts.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Postgrid) -> None:
        contact = client.contacts.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
            address_line2="addressLine2",
            city="city",
            company_name="companyName",
            description="description",
            email="email",
            force_verified_status=True,
            job_title="jobTitle",
            last_name="lastName",
            metadata={"foo": "bar"},
            phone_number="phoneNumber",
            postal_or_zip="postalOrZip",
            province_or_state="provinceOrState",
            skip_verification=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Postgrid) -> None:
        response = client.contacts.with_raw_response.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Postgrid) -> None:
        with client.contacts.with_streaming_response.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Postgrid) -> None:
        contact = client.contacts.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Postgrid) -> None:
        contact = client.contacts.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
            address_line2="addressLine2",
            city="city",
            description="description",
            email="email",
            first_name="firstName",
            force_verified_status=True,
            job_title="jobTitle",
            last_name="lastName",
            metadata={"foo": "bar"},
            phone_number="phoneNumber",
            postal_or_zip="postalOrZip",
            province_or_state="provinceOrState",
            skip_verification=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Postgrid) -> None:
        response = client.contacts.with_raw_response.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Postgrid) -> None:
        with client.contacts.with_streaming_response.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Postgrid) -> None:
        contact = client.contacts.retrieve(
            "id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Postgrid) -> None:
        response = client.contacts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Postgrid) -> None:
        with client.contacts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Postgrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Postgrid) -> None:
        contact = client.contacts.list()
        assert_matches_type(SyncList[Contact], contact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Postgrid) -> None:
        contact = client.contacts.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncList[Contact], contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Postgrid) -> None:
        response = client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SyncList[Contact], contact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Postgrid) -> None:
        with client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SyncList[Contact], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Postgrid) -> None:
        contact = client.contacts.delete(
            "id",
        )
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Postgrid) -> None:
        response = client.contacts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Postgrid) -> None:
        with client.contacts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactDeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Postgrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contacts.with_raw_response.delete(
                "",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
            address_line2="addressLine2",
            city="city",
            company_name="companyName",
            description="description",
            email="email",
            force_verified_status=True,
            job_title="jobTitle",
            last_name="lastName",
            metadata={"foo": "bar"},
            phone_number="phoneNumber",
            postal_or_zip="postalOrZip",
            province_or_state="provinceOrState",
            skip_verification=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPostgrid) -> None:
        response = await async_client.contacts.with_raw_response.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPostgrid) -> None:
        async with async_client.contacts.with_streaming_response.create(
            address_line1="addressLine1",
            country_code="countryCode",
            first_name="firstName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
            address_line2="addressLine2",
            city="city",
            description="description",
            email="email",
            first_name="firstName",
            force_verified_status=True,
            job_title="jobTitle",
            last_name="lastName",
            metadata={"foo": "bar"},
            phone_number="phoneNumber",
            postal_or_zip="postalOrZip",
            province_or_state="provinceOrState",
            skip_verification=True,
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPostgrid) -> None:
        response = await async_client.contacts.with_raw_response.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPostgrid) -> None:
        async with async_client.contacts.with_streaming_response.create(
            address_line1="addressLine1",
            company_name="companyName",
            country_code="countryCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.retrieve(
            "id",
        )
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostgrid) -> None:
        response = await async_client.contacts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(Contact, contact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostgrid) -> None:
        async with async_client.contacts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(Contact, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostgrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.list()
        assert_matches_type(AsyncList[Contact], contact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncList[Contact], contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostgrid) -> None:
        response = await async_client.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(AsyncList[Contact], contact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostgrid) -> None:
        async with async_client.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(AsyncList[Contact], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPostgrid) -> None:
        contact = await async_client.contacts.delete(
            "id",
        )
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostgrid) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactDeleteResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostgrid) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactDeleteResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostgrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                "",
            )
