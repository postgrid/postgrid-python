# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSkipLimit, AsyncSkipLimit
from ..._base_client import AsyncPaginator, make_request_options
from ...types.print_mail import (
    sub_organization_list_params,
    sub_organization_update_params,
    sub_organization_retrieve_users_params,
)
from ...types.print_mail.sub_organization import SubOrganization
from ...types.print_mail.sub_organization_update_response import SubOrganizationUpdateResponse
from ...types.print_mail.sub_organization_retrieve_users_response import SubOrganizationRetrieveUsersResponse

__all__ = ["SubOrganizationsResource", "AsyncSubOrganizationsResource"]


class SubOrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return SubOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return SubOrganizationsResourceWithStreamingResponse(self)

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
    ) -> SubOrganization:
        """
        Get a sub-organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/sub_organizations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubOrganization,
        )

    def update(
        self,
        *,
        country_code: str,
        email: str,
        name: str,
        organization_name: str,
        password: str,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubOrganizationUpdateResponse:
        """
        When creating a user through the API, the verifiedEmail field will automatically
        be set to true. However, if public signups are used, the email will need to be
        verified by the user.

        Args:
          country_code: The country code of the sub-organization.

          email: The email of the user to be created alongside the sub-organization.

          name: The name of the user to be created alongside the sub-organization.

          organization_name: The name of the sub-organization.

          password: The password of the user to be created alongside the sub-organization.

          phone_number: The phone number of the user to be created alongside the sub-organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/sub_organizations",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "email": email,
                    "name": name,
                    "organization_name": organization_name,
                    "password": password,
                    "phone_number": phone_number,
                },
                sub_organization_update_params.SubOrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubOrganizationUpdateResponse,
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
    ) -> SyncSkipLimit[SubOrganization]:
        """
        List sub-organizations.

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
            "/print-mail/v1/sub_organizations",
            page=SyncSkipLimit[SubOrganization],
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
                    sub_organization_list_params.SubOrganizationListParams,
                ),
            ),
            model=SubOrganization,
        )

    def retrieve_users(
        self,
        id: str,
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
    ) -> SubOrganizationRetrieveUsersResponse:
        """
        List users for a sub-organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/sub_organizations/{id}/users",
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
                    sub_organization_retrieve_users_params.SubOrganizationRetrieveUsersParams,
                ),
            ),
            cast_to=SubOrganizationRetrieveUsersResponse,
        )


class AsyncSubOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncSubOrganizationsResourceWithStreamingResponse(self)

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
    ) -> SubOrganization:
        """
        Get a sub-organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/sub_organizations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubOrganization,
        )

    async def update(
        self,
        *,
        country_code: str,
        email: str,
        name: str,
        organization_name: str,
        password: str,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubOrganizationUpdateResponse:
        """
        When creating a user through the API, the verifiedEmail field will automatically
        be set to true. However, if public signups are used, the email will need to be
        verified by the user.

        Args:
          country_code: The country code of the sub-organization.

          email: The email of the user to be created alongside the sub-organization.

          name: The name of the user to be created alongside the sub-organization.

          organization_name: The name of the sub-organization.

          password: The password of the user to be created alongside the sub-organization.

          phone_number: The phone number of the user to be created alongside the sub-organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/sub_organizations",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "email": email,
                    "name": name,
                    "organization_name": organization_name,
                    "password": password,
                    "phone_number": phone_number,
                },
                sub_organization_update_params.SubOrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubOrganizationUpdateResponse,
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
    ) -> AsyncPaginator[SubOrganization, AsyncSkipLimit[SubOrganization]]:
        """
        List sub-organizations.

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
            "/print-mail/v1/sub_organizations",
            page=AsyncSkipLimit[SubOrganization],
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
                    sub_organization_list_params.SubOrganizationListParams,
                ),
            ),
            model=SubOrganization,
        )

    async def retrieve_users(
        self,
        id: str,
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
    ) -> SubOrganizationRetrieveUsersResponse:
        """
        List users for a sub-organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/sub_organizations/{id}/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "search": search,
                        "skip": skip,
                    },
                    sub_organization_retrieve_users_params.SubOrganizationRetrieveUsersParams,
                ),
            ),
            cast_to=SubOrganizationRetrieveUsersResponse,
        )


class SubOrganizationsResourceWithRawResponse:
    def __init__(self, sub_organizations: SubOrganizationsResource) -> None:
        self._sub_organizations = sub_organizations

        self.retrieve = to_raw_response_wrapper(
            sub_organizations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sub_organizations.update,
        )
        self.list = to_raw_response_wrapper(
            sub_organizations.list,
        )
        self.retrieve_users = to_raw_response_wrapper(
            sub_organizations.retrieve_users,
        )


class AsyncSubOrganizationsResourceWithRawResponse:
    def __init__(self, sub_organizations: AsyncSubOrganizationsResource) -> None:
        self._sub_organizations = sub_organizations

        self.retrieve = async_to_raw_response_wrapper(
            sub_organizations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sub_organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            sub_organizations.list,
        )
        self.retrieve_users = async_to_raw_response_wrapper(
            sub_organizations.retrieve_users,
        )


class SubOrganizationsResourceWithStreamingResponse:
    def __init__(self, sub_organizations: SubOrganizationsResource) -> None:
        self._sub_organizations = sub_organizations

        self.retrieve = to_streamed_response_wrapper(
            sub_organizations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sub_organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            sub_organizations.list,
        )
        self.retrieve_users = to_streamed_response_wrapper(
            sub_organizations.retrieve_users,
        )


class AsyncSubOrganizationsResourceWithStreamingResponse:
    def __init__(self, sub_organizations: AsyncSubOrganizationsResource) -> None:
        self._sub_organizations = sub_organizations

        self.retrieve = async_to_streamed_response_wrapper(
            sub_organizations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sub_organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sub_organizations.list,
        )
        self.retrieve_users = async_to_streamed_response_wrapper(
            sub_organizations.retrieve_users,
        )
