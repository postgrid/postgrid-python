# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from postgrid import PostGrid, AsyncPostGrid
from tests.utils import assert_matches_type
from postgrid.types.print_mail import DeletedResponse
from postgrid.types.print_mail.reports import ReportExport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: PostGrid) -> None:
        export = client.print_mail.reports.exports.create(
            report_id="reportID",
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PostGrid) -> None:
        export = client.print_mail.reports.exports.create(
            report_id="reportID",
            description="October Orders Export",
            metadata={"foo": "string"},
            params=["2023-10-01T00:00:00Z"],
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PostGrid) -> None:
        response = client.print_mail.reports.exports.with_raw_response.create(
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PostGrid) -> None:
        with client.print_mail.reports.exports.with_streaming_response.create(
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ReportExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.print_mail.reports.exports.with_raw_response.create(
                report_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: PostGrid) -> None:
        export = client.print_mail.reports.exports.retrieve(
            export_id="exportID",
            report_id="reportID",
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: PostGrid) -> None:
        response = client.print_mail.reports.exports.with_raw_response.retrieve(
            export_id="exportID",
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: PostGrid) -> None:
        with client.print_mail.reports.exports.with_streaming_response.retrieve(
            export_id="exportID",
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ReportExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.print_mail.reports.exports.with_raw_response.retrieve(
                export_id="exportID",
                report_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            client.print_mail.reports.exports.with_raw_response.retrieve(
                export_id="",
                report_id="reportID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: PostGrid) -> None:
        export = client.print_mail.reports.exports.delete(
            export_id="exportID",
            report_id="reportID",
        )
        assert_matches_type(DeletedResponse, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: PostGrid) -> None:
        response = client.print_mail.reports.exports.with_raw_response.delete(
            export_id="exportID",
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(DeletedResponse, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: PostGrid) -> None:
        with client.print_mail.reports.exports.with_streaming_response.delete(
            export_id="exportID",
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(DeletedResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: PostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.print_mail.reports.exports.with_raw_response.delete(
                export_id="exportID",
                report_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            client.print_mail.reports.exports.with_raw_response.delete(
                export_id="",
                report_id="reportID",
            )


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPostGrid) -> None:
        export = await async_client.print_mail.reports.exports.create(
            report_id="reportID",
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPostGrid) -> None:
        export = await async_client.print_mail.reports.exports.create(
            report_id="reportID",
            description="October Orders Export",
            metadata={"foo": "string"},
            params=["2023-10-01T00:00:00Z"],
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.reports.exports.with_raw_response.create(
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.reports.exports.with_streaming_response.create(
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ReportExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.print_mail.reports.exports.with_raw_response.create(
                report_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPostGrid) -> None:
        export = await async_client.print_mail.reports.exports.retrieve(
            export_id="exportID",
            report_id="reportID",
        )
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.reports.exports.with_raw_response.retrieve(
            export_id="exportID",
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ReportExport, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.reports.exports.with_streaming_response.retrieve(
            export_id="exportID",
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ReportExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.print_mail.reports.exports.with_raw_response.retrieve(
                export_id="exportID",
                report_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            await async_client.print_mail.reports.exports.with_raw_response.retrieve(
                export_id="",
                report_id="reportID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPostGrid) -> None:
        export = await async_client.print_mail.reports.exports.delete(
            export_id="exportID",
            report_id="reportID",
        )
        assert_matches_type(DeletedResponse, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPostGrid) -> None:
        response = await async_client.print_mail.reports.exports.with_raw_response.delete(
            export_id="exportID",
            report_id="reportID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(DeletedResponse, export, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPostGrid) -> None:
        async with async_client.print_mail.reports.exports.with_streaming_response.delete(
            export_id="exportID",
            report_id="reportID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(DeletedResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPostGrid) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.print_mail.reports.exports.with_raw_response.delete(
                export_id="exportID",
                report_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            await async_client.print_mail.reports.exports.with_raw_response.delete(
                export_id="",
                report_id="reportID",
            )
