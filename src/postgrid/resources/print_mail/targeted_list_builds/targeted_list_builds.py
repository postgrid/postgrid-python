# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .filters import (
    FiltersResource,
    AsyncFiltersResource,
    FiltersResourceWithRawResponse,
    AsyncFiltersResourceWithRawResponse,
    FiltersResourceWithStreamingResponse,
    AsyncFiltersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ....types.print_mail import (
    targeted_list_build_list_params,
    targeted_list_build_create_params,
    targeted_list_build_update_params,
)
from ....types.print_mail.targeted_list_build_list_response import TargetedListBuildListResponse
from ....types.print_mail.targeted_list_build_create_response import TargetedListBuildCreateResponse
from ....types.print_mail.targeted_list_build_delete_response import TargetedListBuildDeleteResponse
from ....types.print_mail.targeted_list_build_update_response import TargetedListBuildUpdateResponse
from ....types.print_mail.targeted_list_build_confirm_response import TargetedListBuildConfirmResponse
from ....types.print_mail.targeted_list_build_retrieve_response import TargetedListBuildRetrieveResponse

__all__ = ["TargetedListBuildsResource", "AsyncTargetedListBuildsResource"]


class TargetedListBuildsResource(SyncAPIResource):
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
    def filters(self) -> FiltersResource:
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
        return FiltersResource(self._client)

    @cached_property
    def with_raw_response(self) -> TargetedListBuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return TargetedListBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetedListBuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return TargetedListBuildsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        us_companies: targeted_list_build_create_params.UsCompanies | Omit = omit,
        us_consumers: targeted_list_build_create_params.UsConsumers | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildCreateResponse:
        """Create a new targeted list build.

        A quote will be generated asynchronously based
        on the provided filters.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          limit: Maximum number of contacts to include in the built mailing list. If omitted, all
              matching contacts are included.

          metadata: See the section on Metadata.

          us_companies: Filters used to target US companies (B2B) when building a list.

          us_consumers: Filters used to target US consumers (B2C) when building a list.

              The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
              exclusive — you may supply at most one of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/print-mail/v1/targeted_list_builds",
            body=maybe_transform(
                {
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "us_companies": us_companies,
                    "us_consumers": us_consumers,
                },
                targeted_list_build_create_params.TargetedListBuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildCreateResponse,
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
    ) -> TargetedListBuildRetrieveResponse:
        """
        Retrieve a specific targeted list build by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        us_companies: targeted_list_build_update_params.UsCompanies | Omit = omit,
        us_consumers: targeted_list_build_update_params.UsConsumers | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildUpdateResponse:
        """Update an existing targeted list build.

        Only builds that have not yet been
        confirmed may be updated. Updating the filters or `limit` will reset the build's
        status back to `generating_quote` and a new quote will be generated.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          limit: Maximum number of contacts to include in the built mailing list. If omitted, all
              matching contacts are included.

          metadata: See the section on Metadata.

          us_companies: Filters used to target US companies (B2B) when building a list.

          us_consumers: Filters used to target US consumers (B2C) when building a list.

              The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
              exclusive — you may supply at most one of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "us_companies": us_companies,
                    "us_consumers": us_consumers,
                },
                targeted_list_build_update_params.TargetedListBuildUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildUpdateResponse,
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
    ) -> SyncSkipLimit[TargetedListBuildListResponse]:
        """
        Retrieve a paginated list of targeted list builds for the authenticated
        organization, ordered from most recently updated to least recently updated.

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
            "/print-mail/v1/targeted_list_builds",
            page=SyncSkipLimit[TargetedListBuildListResponse],
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
                    targeted_list_build_list_params.TargetedListBuildListParams,
                ),
            ),
            model=TargetedListBuildListResponse,
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
    ) -> TargetedListBuildDeleteResponse:
        """Delete a targeted list build.

        List builds can only be deleted before they have
        been confirmed — once a build has transitioned to `creating_list` or `completed`
        it cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildDeleteResponse,
        )

    def confirm(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildConfirmResponse:
        """Confirm a targeted list build whose quote is ready.

        This deducts the appropriate
        amount of list build credits from the organization (in live mode) and kicks off
        the asynchronous creation of the underlying mailing list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/targeted_list_builds/{id}/confirm", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildConfirmResponse,
        )


class AsyncTargetedListBuildsResource(AsyncAPIResource):
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
    def filters(self) -> AsyncFiltersResource:
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
        return AsyncFiltersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTargetedListBuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetedListBuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetedListBuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncTargetedListBuildsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        us_companies: targeted_list_build_create_params.UsCompanies | Omit = omit,
        us_consumers: targeted_list_build_create_params.UsConsumers | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildCreateResponse:
        """Create a new targeted list build.

        A quote will be generated asynchronously based
        on the provided filters.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          limit: Maximum number of contacts to include in the built mailing list. If omitted, all
              matching contacts are included.

          metadata: See the section on Metadata.

          us_companies: Filters used to target US companies (B2B) when building a list.

          us_consumers: Filters used to target US consumers (B2C) when building a list.

              The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
              exclusive — you may supply at most one of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/print-mail/v1/targeted_list_builds",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "us_companies": us_companies,
                    "us_consumers": us_consumers,
                },
                targeted_list_build_create_params.TargetedListBuildCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildCreateResponse,
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
    ) -> TargetedListBuildRetrieveResponse:
        """
        Retrieve a specific targeted list build by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        limit: int | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        us_companies: targeted_list_build_update_params.UsCompanies | Omit = omit,
        us_consumers: targeted_list_build_update_params.UsConsumers | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildUpdateResponse:
        """Update an existing targeted list build.

        Only builds that have not yet been
        confirmed may be updated. Updating the filters or `limit` will reset the build's
        status back to `generating_quote` and a new quote will be generated.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          limit: Maximum number of contacts to include in the built mailing list. If omitted, all
              matching contacts are included.

          metadata: See the section on Metadata.

          us_companies: Filters used to target US companies (B2B) when building a list.

          us_consumers: Filters used to target US consumers (B2C) when building a list.

              The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
              exclusive — you may supply at most one of them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "limit": limit,
                    "metadata": metadata,
                    "us_companies": us_companies,
                    "us_consumers": us_consumers,
                },
                targeted_list_build_update_params.TargetedListBuildUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildUpdateResponse,
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
    ) -> AsyncPaginator[TargetedListBuildListResponse, AsyncSkipLimit[TargetedListBuildListResponse]]:
        """
        Retrieve a paginated list of targeted list builds for the authenticated
        organization, ordered from most recently updated to least recently updated.

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
            "/print-mail/v1/targeted_list_builds",
            page=AsyncSkipLimit[TargetedListBuildListResponse],
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
                    targeted_list_build_list_params.TargetedListBuildListParams,
                ),
            ),
            model=TargetedListBuildListResponse,
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
    ) -> TargetedListBuildDeleteResponse:
        """Delete a targeted list build.

        List builds can only be deleted before they have
        been confirmed — once a build has transitioned to `creating_list` or `completed`
        it cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/print-mail/v1/targeted_list_builds/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildDeleteResponse,
        )

    async def confirm(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetedListBuildConfirmResponse:
        """Confirm a targeted list build whose quote is ready.

        This deducts the appropriate
        amount of list build credits from the organization (in live mode) and kicks off
        the asynchronous creation of the underlying mailing list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/targeted_list_builds/{id}/confirm", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetedListBuildConfirmResponse,
        )


class TargetedListBuildsResourceWithRawResponse:
    def __init__(self, targeted_list_builds: TargetedListBuildsResource) -> None:
        self._targeted_list_builds = targeted_list_builds

        self.create = to_raw_response_wrapper(
            targeted_list_builds.create,
        )
        self.retrieve = to_raw_response_wrapper(
            targeted_list_builds.retrieve,
        )
        self.update = to_raw_response_wrapper(
            targeted_list_builds.update,
        )
        self.list = to_raw_response_wrapper(
            targeted_list_builds.list,
        )
        self.delete = to_raw_response_wrapper(
            targeted_list_builds.delete,
        )
        self.confirm = to_raw_response_wrapper(
            targeted_list_builds.confirm,
        )

    @cached_property
    def filters(self) -> FiltersResourceWithRawResponse:
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
        return FiltersResourceWithRawResponse(self._targeted_list_builds.filters)


class AsyncTargetedListBuildsResourceWithRawResponse:
    def __init__(self, targeted_list_builds: AsyncTargetedListBuildsResource) -> None:
        self._targeted_list_builds = targeted_list_builds

        self.create = async_to_raw_response_wrapper(
            targeted_list_builds.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            targeted_list_builds.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            targeted_list_builds.update,
        )
        self.list = async_to_raw_response_wrapper(
            targeted_list_builds.list,
        )
        self.delete = async_to_raw_response_wrapper(
            targeted_list_builds.delete,
        )
        self.confirm = async_to_raw_response_wrapper(
            targeted_list_builds.confirm,
        )

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithRawResponse:
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
        return AsyncFiltersResourceWithRawResponse(self._targeted_list_builds.filters)


class TargetedListBuildsResourceWithStreamingResponse:
    def __init__(self, targeted_list_builds: TargetedListBuildsResource) -> None:
        self._targeted_list_builds = targeted_list_builds

        self.create = to_streamed_response_wrapper(
            targeted_list_builds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            targeted_list_builds.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            targeted_list_builds.update,
        )
        self.list = to_streamed_response_wrapper(
            targeted_list_builds.list,
        )
        self.delete = to_streamed_response_wrapper(
            targeted_list_builds.delete,
        )
        self.confirm = to_streamed_response_wrapper(
            targeted_list_builds.confirm,
        )

    @cached_property
    def filters(self) -> FiltersResourceWithStreamingResponse:
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
        return FiltersResourceWithStreamingResponse(self._targeted_list_builds.filters)


class AsyncTargetedListBuildsResourceWithStreamingResponse:
    def __init__(self, targeted_list_builds: AsyncTargetedListBuildsResource) -> None:
        self._targeted_list_builds = targeted_list_builds

        self.create = async_to_streamed_response_wrapper(
            targeted_list_builds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            targeted_list_builds.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            targeted_list_builds.update,
        )
        self.list = async_to_streamed_response_wrapper(
            targeted_list_builds.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            targeted_list_builds.delete,
        )
        self.confirm = async_to_streamed_response_wrapper(
            targeted_list_builds.confirm,
        )

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithStreamingResponse:
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
        return AsyncFiltersResourceWithStreamingResponse(self._targeted_list_builds.filters)
