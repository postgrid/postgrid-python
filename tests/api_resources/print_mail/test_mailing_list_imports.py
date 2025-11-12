# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    MailingListImportResponse,
    MailingListImportDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMailingListImports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
            description="description",
            metadata={"foo": "bar"},
            receiver_merge_variable_mapping={"foo": "string"},
            sender_address_mapping={"foo": "string"},
            sender_merge_variable_mapping={"foo": "string"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_list_imports.with_raw_response.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.mailing_list_imports.with_streaming_response.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.retrieve(
            "id",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_list_imports.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.mailing_list_imports.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_list_imports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.update(
            id="id",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.update(
            id="id",
            description="Corrected description",
            metadata={"batch": "spring_sale"},
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_list_imports.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: PostGrid) -> None:
        with client.print_mail.mailing_list_imports.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_list_imports.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.list()
        assert_matches_type(SyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_list_imports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = response.parse()
        assert_matches_type(SyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.mailing_list_imports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = response.parse()
            assert_matches_type(SyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        mailing_list_import = client.print_mail.mailing_list_imports.delete(
            "id",
        )
        assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.mailing_list_imports.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = response.parse()
        assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.mailing_list_imports.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = response.parse()
            assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.mailing_list_imports.with_raw_response.delete(
                "",
            )


class TestAsyncMailingListImports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
            description="description",
            metadata={"foo": "bar"},
            receiver_merge_variable_mapping={"foo": "string"},
            sender_address_mapping={"foo": "string"},
            sender_merge_variable_mapping={"foo": "string"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_list_imports.with_raw_response.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = await response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_list_imports.with_streaming_response.create(
            file="https://signed-upload-url.csv",
            file_type="csv",
            receiver_address_mapping={
                "description": "Description",
                "firstName": "First Name",
                "lastName": "Last Name",
                "email": "Email",
                "addressLine1": "Address",
                "city": "City",
                "postalOrZip": "Postal Code",
                "provinceOrState": "State",
                "countryCode": "Country",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = await response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.retrieve(
            "id",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_list_imports.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = await response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_list_imports.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = await response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_list_imports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.update(
            id="id",
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.update(
            id="id",
            description="Corrected description",
            metadata={"batch": "spring_sale"},
        )
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_list_imports.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = await response.parse()
        assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_list_imports.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = await response.parse()
            assert_matches_type(MailingListImportResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_list_imports.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.list()
        assert_matches_type(AsyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_list_imports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = await response.parse()
        assert_matches_type(AsyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_list_imports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = await response.parse()
            assert_matches_type(AsyncSkipLimit[MailingListImportResponse], mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        mailing_list_import = await async_client.print_mail.mailing_list_imports.delete(
            "id",
        )
        assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.mailing_list_imports.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mailing_list_import = await response.parse()
        assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.mailing_list_imports.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mailing_list_import = await response.parse()
            assert_matches_type(MailingListImportDeleteResponse, mailing_list_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.mailing_list_imports.with_raw_response.delete(
                "",
            )
