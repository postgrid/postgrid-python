# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid._utils import parse_datetime
from postgrid.pagination import SyncSkipLimit, AsyncSkipLimit
from postgrid.types.print_mail import (
    Letter,
    LetterRetrieveURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLetters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="description",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            perforated_page=1,
            plastic_card={
                "size": "standard",
                "double_sided": {
                    "back_html": "backHTML",
                    "back_template": "backTemplate",
                    "front_html": "frontHTML",
                    "front_template": "frontTemplate",
                    "pdf": "https://example.com",
                },
                "single_sided": {
                    "html": "html",
                    "pdf": "https://example.com",
                    "template": "template",
                },
            },
            return_envelope="returnEnvelope",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.create(
            template="template",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.create(
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.create(
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="description",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            perforated_page=1,
            plastic_card={
                "size": "standard",
                "double_sided": {
                    "back_html": "backHTML",
                    "back_template": "backTemplate",
                    "front_html": "frontHTML",
                    "front_template": "frontTemplate",
                    "pdf": "https://example.com",
                },
                "single_sided": {
                    "html": "html",
                    "pdf": "https://example.com",
                    "template": "template",
                },
            },
            return_envelope="returnEnvelope",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.retrieve(
            "id",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.letters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.list()
        assert_matches_type(SyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(SyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(SyncSkipLimit[Letter], letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.delete(
            "id",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.letters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_url(self, client: PostGrid) -> None:
        letter = client.print_mail.letters.retrieve_url(
            "id",
        )
        assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_url(self, client: PostGrid) -> None:
        response = client.print_mail.letters.with_raw_response.retrieve_url(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = response.parse()
        assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_url(self, client: PostGrid) -> None:
        with client.print_mail.letters.with_streaming_response.retrieve_url(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = response.parse()
            assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_url(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.letters.with_raw_response.retrieve_url(
                "",
            )


class TestAsyncLetters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="description",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            perforated_page=1,
            plastic_card={
                "size": "standard",
                "double_sided": {
                    "back_html": "backHTML",
                    "back_template": "backTemplate",
                    "front_html": "frontHTML",
                    "front_template": "frontTemplate",
                    "pdf": "https://example.com",
                },
                "single_sided": {
                    "html": "html",
                    "pdf": "https://example.com",
                    "template": "template",
                },
            },
            return_envelope="returnEnvelope",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            html="html",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.create(
            template="template",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.create(
            template="template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.create(
            template="template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
                "address_line2": "addressLine2",
                "city": "city",
                "company_name": "companyName",
                "description": "description",
                "email": "email",
                "force_verified_status": True,
                "job_title": "jobTitle",
                "last_name": "lastName",
                "metadata": {"foo": "bar"},
                "phone_number": "phoneNumber",
                "postal_or_zip": "postalOrZip",
                "province_or_state": "provinceOrState",
                "skip_verification": True,
            },
            address_placement="top_first_page",
            attached_pdf={
                "file": "https://example.com",
                "placement": "before_template",
            },
            color=True,
            description="description",
            double_sided=True,
            envelope="envelope",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            perforated_page=1,
            plastic_card={
                "size": "standard",
                "double_sided": {
                    "back_html": "backHTML",
                    "back_template": "backTemplate",
                    "front_html": "frontHTML",
                    "front_template": "frontTemplate",
                    "pdf": "https://example.com",
                },
                "single_sided": {
                    "html": "html",
                    "pdf": "https://example.com",
                    "template": "template",
                },
            },
            return_envelope="returnEnvelope",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            size="us_letter",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.retrieve(
            "id",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.letters.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.list()
        assert_matches_type(AsyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(AsyncSkipLimit[Letter], letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(AsyncSkipLimit[Letter], letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.delete(
            "id",
        )
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(Letter, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(Letter, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.letters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_url(self, async_client: AsyncPostGrid) -> None:
        letter = await async_client.print_mail.letters.retrieve_url(
            "id",
        )
        assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_url(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.letters.with_raw_response.retrieve_url(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        letter = await response.parse()
        assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_url(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.letters.with_streaming_response.retrieve_url(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            letter = await response.parse()
            assert_matches_type(LetterRetrieveURLResponse, letter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_url(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.letters.with_raw_response.retrieve_url(
                "",
            )
