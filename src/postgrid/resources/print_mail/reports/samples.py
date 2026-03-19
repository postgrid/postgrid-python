# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.print_mail.reports import sample_create_params
from ....types.print_mail.reports.report_sample import ReportSample

__all__ = ["SamplesResource", "AsyncSamplesResource"]


class SamplesResource(SyncAPIResource):
    """
    The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
     Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
     Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

     You can request access to this to this feature by reaching out to support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> SamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return SamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return SamplesResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
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
        Run the query associated with a saved report and get a sample of the results.
        This allows getting up to 1000 rows of resutls but the runtime of the query is
        limited to 30 seconds. If you need more rows or longer runtime, you should
        create an export from this report.

        Args:
          limit: Maximum number of rows to return in the sample.

          params: Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
              $1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/reports/{id}/samples", id=id),
            body=maybe_transform(
                {
                    "limit": limit,
                    "params": params,
                },
                sample_create_params.SampleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSample,
        )


class AsyncSamplesResource(AsyncAPIResource):
    """
    The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
     Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
     Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

     You can request access to this to this feature by reaching out to support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> AsyncSamplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSamplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSamplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncSamplesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
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
        Run the query associated with a saved report and get a sample of the results.
        This allows getting up to 1000 rows of resutls but the runtime of the query is
        limited to 30 seconds. If you need more rows or longer runtime, you should
        create an export from this report.

        Args:
          limit: Maximum number of rows to return in the sample.

          params: Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
              $1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/reports/{id}/samples", id=id),
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "params": params,
                },
                sample_create_params.SampleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportSample,
        )


class SamplesResourceWithRawResponse:
    def __init__(self, samples: SamplesResource) -> None:
        self._samples = samples

        self.create = to_raw_response_wrapper(
            samples.create,
        )


class AsyncSamplesResourceWithRawResponse:
    def __init__(self, samples: AsyncSamplesResource) -> None:
        self._samples = samples

        self.create = async_to_raw_response_wrapper(
            samples.create,
        )


class SamplesResourceWithStreamingResponse:
    def __init__(self, samples: SamplesResource) -> None:
        self._samples = samples

        self.create = to_streamed_response_wrapper(
            samples.create,
        )


class AsyncSamplesResourceWithStreamingResponse:
    def __init__(self, samples: AsyncSamplesResource) -> None:
        self._samples = samples

        self.create = async_to_streamed_response_wrapper(
            samples.create,
        )
