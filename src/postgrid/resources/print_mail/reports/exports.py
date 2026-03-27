# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.print_mail.reports import export_create_params
from ....types.print_mail.deleted_response import DeletedResponse
from ....types.print_mail.reports.report_export import ReportExport

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    """
    The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
     Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
     Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

     You can request access to this to this feature by reaching out to support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        report_id: str,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        params: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportExport:
        """Create a new export job for a saved report.

        This runs the report's query
        asynchronously and generates a downloadable CSV file with the full results. Your
        queries can run for up to 13 minutes the resulting file can be up to 100mb
        large.

        Args:
          description: An optional user-friendly description for the export.

          metadata: Optional key-value metadata associated with the export.

          params: Optional parameters to bind to the SQL query of the associated report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._post(
            path_template("/print-mail/v1/reports/{report_id}/exports", report_id=report_id),
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "params": params,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportExport,
        )

    def retrieve(
        self,
        export_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportExport:
        """Retrieve the status and details of a specific report export job.

        Check the
        `outputURL` property for the download link once generation is complete.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._get(
            path_template(
                "/print-mail/v1/reports/{report_id}/exports/{export_id}", report_id=report_id, export_id=export_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportExport,
        )

    def delete(
        self,
        export_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedResponse:
        """
        Delete a completed or failed report export job and its associated output file
        (if any). This action cannot be undone. You cannot delete an export that is
        still generating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._delete(
            path_template(
                "/print-mail/v1/reports/{report_id}/exports/{export_id}", report_id=report_id, export_id=export_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedResponse,
        )


class AsyncExportsResource(AsyncAPIResource):
    """
    The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
     Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
     Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

     You can request access to this to this feature by reaching out to support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        report_id: str,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        params: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportExport:
        """Create a new export job for a saved report.

        This runs the report's query
        asynchronously and generates a downloadable CSV file with the full results. Your
        queries can run for up to 13 minutes the resulting file can be up to 100mb
        large.

        Args:
          description: An optional user-friendly description for the export.

          metadata: Optional key-value metadata associated with the export.

          params: Optional parameters to bind to the SQL query of the associated report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._post(
            path_template("/print-mail/v1/reports/{report_id}/exports", report_id=report_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "params": params,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportExport,
        )

    async def retrieve(
        self,
        export_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportExport:
        """Retrieve the status and details of a specific report export job.

        Check the
        `outputURL` property for the download link once generation is complete.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._get(
            path_template(
                "/print-mail/v1/reports/{report_id}/exports/{export_id}", report_id=report_id, export_id=export_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportExport,
        )

    async def delete(
        self,
        export_id: str,
        *,
        report_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedResponse:
        """
        Delete a completed or failed report export job and its associated output file
        (if any). This action cannot be undone. You cannot delete an export that is
        still generating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._delete(
            path_template(
                "/print-mail/v1/reports/{report_id}/exports/{export_id}", report_id=report_id, export_id=export_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedResponse,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            exports.delete,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            exports.delete,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            exports.delete,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            exports.delete,
        )
