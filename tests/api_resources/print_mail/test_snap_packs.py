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
    SnapPack,
    SnapPackCreateResponse,
    SnapPackRetrieveCapabilitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapPacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.retrieve(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.snap_packs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.list()
        assert_matches_type(SyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(SyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SyncSkipLimit[SnapPack], snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.delete(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.snap_packs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_progressions(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.progressions(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_progressions(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.progressions(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_progressions(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.progressions(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_progressions(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.print_mail.snap_packs.with_raw_response.progressions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_capabilities(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.retrieve_capabilities(
            return_country_code="returnCountryCode",
        )
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_capabilities_with_all_params(self, client: PostGrid) -> None:
        snap_pack = client.print_mail.snap_packs.retrieve_capabilities(
            return_country_code="returnCountryCode",
            destination_country_code="destinationCountryCode",
            mailing_list="mailingList",
        )
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_capabilities(self, client: PostGrid) -> None:
        response = client.print_mail.snap_packs.with_raw_response.retrieve_capabilities(
            return_country_code="returnCountryCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = response.parse()
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_capabilities(self, client: PostGrid) -> None:
        with client.print_mail.snap_packs.with_streaming_response.retrieve_capabilities(
            return_country_code="returnCountryCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = response.parse()
            assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSnapPacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_html="insideHTML",
            outside_html="outsideHTML",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            inside_template="insideTemplate",
            outside_template="outsideTemplate",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.create(
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
                "secret": True,
                "skip_verification": True,
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
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
                "secret": True,
                "skip_verification": True,
            },
            description="description",
            mailing_class="first_class",
            merge_variables={"foo": "bar"},
            metadata={"foo": "bar"},
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            idempotency_key="idempotency-key",
        )
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.create(
            from_={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
            pdf="https://example.com",
            size="8.5x11_bifold_v",
            to={
                "address_line1": "addressLine1",
                "country_code": "countryCode",
                "first_name": "firstName",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPackCreateResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.retrieve(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.snap_packs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.list()
        assert_matches_type(AsyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.list(
            limit=0,
            search="search",
            skip=0,
        )
        assert_matches_type(AsyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(AsyncSkipLimit[SnapPack], snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(AsyncSkipLimit[SnapPack], snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.delete(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.snap_packs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_progressions(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.progressions(
            "id",
        )
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_progressions(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.progressions(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPack, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_progressions(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.progressions(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPack, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_progressions(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.print_mail.snap_packs.with_raw_response.progressions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_capabilities(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.retrieve_capabilities(
            return_country_code="returnCountryCode",
        )
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_capabilities_with_all_params(self, async_client: AsyncPostGrid) -> None:
        snap_pack = await async_client.print_mail.snap_packs.retrieve_capabilities(
            return_country_code="returnCountryCode",
            destination_country_code="destinationCountryCode",
            mailing_list="mailingList",
        )
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_capabilities(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.snap_packs.with_raw_response.retrieve_capabilities(
            return_country_code="returnCountryCode",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snap_pack = await response.parse()
        assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_capabilities(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.snap_packs.with_streaming_response.retrieve_capabilities(
            return_country_code="returnCountryCode",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snap_pack = await response.parse()
            assert_matches_type(SnapPackRetrieveCapabilitiesResponse, snap_pack, path=["response"])

        assert cast(Any, response.is_closed) is True
