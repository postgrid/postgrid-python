# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .exports import (
    ExportsResource,
    AsyncExportsResource,
    ExportsResourceWithRawResponse,
    AsyncExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
    AsyncExportsResourceWithStreamingResponse,
)
from .samples import (
    SamplesResource,
    AsyncSamplesResource,
    SamplesResourceWithRawResponse,
    AsyncSamplesResourceWithRawResponse,
    SamplesResourceWithStreamingResponse,
    AsyncSamplesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSkipLimit, AsyncSkipLimit
from ...._base_client import AsyncPaginator, make_request_options
from ....types.print_mail import report_list_params, report_create_params, report_sample_params, report_update_params
from ....types.print_mail.report import Report
from ....types.print_mail.deleted_response import DeletedResponse
from ....types.print_mail.reports.report_sample import ReportSample

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def samples(self) -> SamplesResource:
        return SamplesResource(self._client)

    @cached_property
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        sql_query: str,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """Create a new saved report definition.

        Saved reports are SQL queries that can be
        executed later to generate full exports or samples.

        If you just want to do ad-hoc queries, you should use the `/reports/samples`
        endpoint.

        Args:
          sql_query: The SQL query defining the report.

          description: An optional user-friendly description for the report.

          metadata: Optional key-value metadata associated with the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/reports",
            body=maybe_transform(
                {
                    "sql_query": sql_query,
                    "description": description,
                    "metadata": metadata,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieve the details of a specific saved report by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        sql_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """Update an existing saved report definition.

        You can change the query,
        description, or metadata.

        Args:
          description: An optional user-friendly description for the report. Set to null to remove.

          metadata: Optional key-value metadata associated with the report. Set to null to remove.

          sql_query: The SQL query defining the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/reports/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "sql_query": sql_query,
                },
                report_update_params.ReportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimit[Report]:
        """
        Retrieve a list of saved reports for your organization.

        Args:
          search: You can supply any string to help narrow down the list of resources. For
              example, if you pass `"New York"` (quoted), it will return resources that have
              that string present somewhere in their response. Alternatively, you can supply a
              structured search query. See the documentation on `StructuredSearchQuery` for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/print-mail/v1/reports",
            page=SyncSkipLimit[Report],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "search": search,
                        "skip": skip,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=Report,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedResponse:
        """Delete a saved report definition.

        This action cannot be undone. Associated
        exports are not automatically deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedResponse,
        )

    def sample(
        self,
        *,
        sql_query: str,
        limit: int | Omit = omit,
        params: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSample:
        """
        Run an ad-hoc SQL query against your data lake and get a sample of the results.
        This is useful for quickly testing queries without saving them as a report. The
        query execution time and result size are limited.

        Args:
          sql_query: The SQL query to execute for the sample.

          limit: Maximum number of rows to return in the sample.

          params: Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
              $1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/reports/samples",
            body=maybe_transform(
                {
                    "sql_query": sql_query,
                    "limit": limit,
                    "params": params,
                },
                report_sample_params.ReportSampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSample,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def samples(self) -> AsyncSamplesResource:
        return AsyncSamplesResource(self._client)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        sql_query: str,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """Create a new saved report definition.

        Saved reports are SQL queries that can be
        executed later to generate full exports or samples.

        If you just want to do ad-hoc queries, you should use the `/reports/samples`
        endpoint.

        Args:
          sql_query: The SQL query defining the report.

          description: An optional user-friendly description for the report.

          metadata: Optional key-value metadata associated with the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/reports",
            body=await async_maybe_transform(
                {
                    "sql_query": sql_query,
                    "description": description,
                    "metadata": metadata,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """
        Retrieve the details of a specific saved report by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        sql_query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Report:
        """Update an existing saved report definition.

        You can change the query,
        description, or metadata.

        Args:
          description: An optional user-friendly description for the report. Set to null to remove.

          metadata: Optional key-value metadata associated with the report. Set to null to remove.

          sql_query: The SQL query defining the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/reports/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "sql_query": sql_query,
                },
                report_update_params.ReportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        search: str | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Report, AsyncSkipLimit[Report]]:
        """
        Retrieve a list of saved reports for your organization.

        Args:
          search: You can supply any string to help narrow down the list of resources. For
              example, if you pass `"New York"` (quoted), it will return resources that have
              that string present somewhere in their response. Alternatively, you can supply a
              structured search query. See the documentation on `StructuredSearchQuery` for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/print-mail/v1/reports",
            page=AsyncSkipLimit[Report],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "search": search,
                        "skip": skip,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=Report,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletedResponse:
        """Delete a saved report definition.

        This action cannot be undone. Associated
        exports are not automatically deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedResponse,
        )

    async def sample(
        self,
        *,
        sql_query: str,
        limit: int | Omit = omit,
        params: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportSample:
        """
        Run an ad-hoc SQL query against your data lake and get a sample of the results.
        This is useful for quickly testing queries without saving them as a report. The
        query execution time and result size are limited.

        Args:
          sql_query: The SQL query to execute for the sample.

          limit: Maximum number of rows to return in the sample.

          params: Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
              $1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/reports/samples",
            body=await async_maybe_transform(
                {
                    "sql_query": sql_query,
                    "limit": limit,
                    "params": params,
                },
                report_sample_params.ReportSampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSample,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reports.retrieve,
        )
        self.update = to_raw_response_wrapper(
            reports.update,
        )
        self.list = to_raw_response_wrapper(
            reports.list,
        )
        self.delete = to_raw_response_wrapper(
            reports.delete,
        )
        self.sample = to_raw_response_wrapper(
            reports.sample,
        )

    @cached_property
    def samples(self) -> SamplesResourceWithRawResponse:
        return SamplesResourceWithRawResponse(self._reports.samples)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._reports.exports)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reports.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            reports.update,
        )
        self.list = async_to_raw_response_wrapper(
            reports.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reports.delete,
        )
        self.sample = async_to_raw_response_wrapper(
            reports.sample,
        )

    @cached_property
    def samples(self) -> AsyncSamplesResourceWithRawResponse:
        return AsyncSamplesResourceWithRawResponse(self._reports.samples)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._reports.exports)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            reports.update,
        )
        self.list = to_streamed_response_wrapper(
            reports.list,
        )
        self.delete = to_streamed_response_wrapper(
            reports.delete,
        )
        self.sample = to_streamed_response_wrapper(
            reports.sample,
        )

    @cached_property
    def samples(self) -> SamplesResourceWithStreamingResponse:
        return SamplesResourceWithStreamingResponse(self._reports.samples)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._reports.exports)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            reports.update,
        )
        self.list = async_to_streamed_response_wrapper(
            reports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reports.delete,
        )
        self.sample = async_to_streamed_response_wrapper(
            reports.sample,
        )

    @cached_property
    def samples(self) -> AsyncSamplesResourceWithStreamingResponse:
        return AsyncSamplesResourceWithStreamingResponse(self._reports.samples)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._reports.exports)
