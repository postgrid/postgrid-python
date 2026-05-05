# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.print_mail.targeted_list_builds import filter_autocomplete_params
from ....types.print_mail.targeted_list_builds.filter_autocomplete_response import FilterAutocompleteResponse

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    """
    **Beta:** the targeted list builds API is in beta and is subject to
     breaking changes. Endpoint shapes, status values, and filter fields may
     change without notice.

     The targeted list builds API lets you programmatically build mailing
     lists of US consumers (B2C) or US companies (B2B) that match a set of
     demographic, geographic, and firmographic filters.

     The lifecycle of a list build is:

     1. Create a list build by supplying either `usConsumers` or `usCompanies`
        filters. A quote is generated asynchronously — poll the resource or
        wait for its `status` to become `quote_ready`.
     2. Review the `quote` (total count and price per contact) and masked
        `previewRecords`. Adjust the filters with an update call if needed —
        this will regenerate the quote.
     3. Confirm the build. This deducts the appropriate amount of list build
        credits from your organization (in live mode) and begins constructing
        the mailing list. `buildProgressPercent` reflects progress from 0 to
        100.
     4. Once `status` is `completed`, the ID of the resulting mailing list is
        available in the `mailingList` field and can be used like any other
        mailing list in the PostGrid API.

     Targeted list builds must be enabled on your organization before they
     can be used. Contact PostGrid support to request access.
    """

    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return FiltersResourceWithStreamingResponse(self)

    def autocomplete(
        self,
        *,
        field: Literal["industry"],
        size: int | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterAutocompleteResponse:
        """
        Return a list of autocomplete suggestions for a given filter field (currently
        only `industry` is supported). Useful when building a UI around the `industries`
        company filter.

        Args:
          field: A field that can be autocompleted when configuring list build filters.

          size: Maximum number of suggestions to return. Between 1 and 100. Defaults to 25 if
              omitted.

          text: Optional text prefix to narrow the autocomplete suggestions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/targeted_list_builds/filters/autocomplete",
            body=maybe_transform(
                {
                    "field": field,
                    "size": size,
                    "text": text,
                },
                filter_autocomplete_params.FilterAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterAutocompleteResponse,
        )


class AsyncFiltersResource(AsyncAPIResource):
    """
    **Beta:** the targeted list builds API is in beta and is subject to
     breaking changes. Endpoint shapes, status values, and filter fields may
     change without notice.

     The targeted list builds API lets you programmatically build mailing
     lists of US consumers (B2C) or US companies (B2B) that match a set of
     demographic, geographic, and firmographic filters.

     The lifecycle of a list build is:

     1. Create a list build by supplying either `usConsumers` or `usCompanies`
        filters. A quote is generated asynchronously — poll the resource or
        wait for its `status` to become `quote_ready`.
     2. Review the `quote` (total count and price per contact) and masked
        `previewRecords`. Adjust the filters with an update call if needed —
        this will regenerate the quote.
     3. Confirm the build. This deducts the appropriate amount of list build
        credits from your organization (in live mode) and begins constructing
        the mailing list. `buildProgressPercent` reflects progress from 0 to
        100.
     4. Once `status` is `completed`, the ID of the resulting mailing list is
        available in the `mailingList` field and can be used like any other
        mailing list in the PostGrid API.

     Targeted list builds must be enabled on your organization before they
     can be used. Contact PostGrid support to request access.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncFiltersResourceWithStreamingResponse(self)

    async def autocomplete(
        self,
        *,
        field: Literal["industry"],
        size: int | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterAutocompleteResponse:
        """
        Return a list of autocomplete suggestions for a given filter field (currently
        only `industry` is supported). Useful when building a UI around the `industries`
        company filter.

        Args:
          field: A field that can be autocompleted when configuring list build filters.

          size: Maximum number of suggestions to return. Between 1 and 100. Defaults to 25 if
              omitted.

          text: Optional text prefix to narrow the autocomplete suggestions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/targeted_list_builds/filters/autocomplete",
            body=await async_maybe_transform(
                {
                    "field": field,
                    "size": size,
                    "text": text,
                },
                filter_autocomplete_params.FilterAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterAutocompleteResponse,
        )


class FiltersResourceWithRawResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.autocomplete = to_raw_response_wrapper(
            filters.autocomplete,
        )


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.autocomplete = async_to_raw_response_wrapper(
            filters.autocomplete,
        )


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.autocomplete = to_streamed_response_wrapper(
            filters.autocomplete,
        )


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.autocomplete = async_to_streamed_response_wrapper(
            filters.autocomplete,
        )
