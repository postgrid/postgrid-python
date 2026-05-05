# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.print_mail import virtual_mailbox_list_params, virtual_mailbox_create_params
from ....types.print_mail.virtual_mailbox_list_response import VirtualMailboxListResponse
from ....types.print_mail.virtual_mailbox_create_response import VirtualMailboxCreateResponse
from ....types.print_mail.virtual_mailbox_retrieve_response import VirtualMailboxRetrieveResponse
from ....types.print_mail.virtual_mailbox_retrieve_address_response import VirtualMailboxRetrieveAddressResponse

__all__ = ["VirtualMailboxesResource", "AsyncVirtualMailboxesResource"]


class VirtualMailboxesResource(SyncAPIResource):
    """
    Virtual mailboxes let you receive, scan, and forward your physical mail
     without needing a traditional physical mailbox. Each mailbox is fully
     digital, giving you a unique ID, status, and a set of capabilities such as
     forwarding mail to another address or viewing envelope scans. This allows you
     to manage physical correspondence entirely online.

     You can request access to this feature by reaching out to
     support@postgrid.com
    """

    @cached_property
    def items(self) -> ItemsResource:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VirtualMailboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return VirtualMailboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualMailboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return VirtualMailboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country_code: Literal["US"],
        capabilities: virtual_mailbox_create_params.Capabilities | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VirtualMailboxCreateResponse:
        """Creates a new virtual mailbox.

        In live mode, the virtual mailbox will be pending
        assignment and cannot be used until it has been assigned and activated by our
        team. You will be notified via email once the virtual mailbox has been
        activated. In test mode, the virtual mailbox will be activated immediately upon
        creation.

        Args:
          country_code: All of the supported countries for virtual mailboxes.

          capabilities: The capabilities the virtual mailbox should support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/virtual_mailboxes",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "capabilities": capabilities,
                },
                virtual_mailbox_create_params.VirtualMailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxCreateResponse,
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
    ) -> VirtualMailboxRetrieveResponse:
        """
        Retrieve Virtual Mailbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxRetrieveResponse,
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
    ) -> SyncSkipLimit[VirtualMailboxListResponse]:
        """Lists virtual mailboxes.

        You can use the `skip`, `limit`, and `search` query
        parameters to refine the list.

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
            "/print-mail/v1/virtual_mailboxes",
            page=SyncSkipLimit[VirtualMailboxListResponse],
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
                    virtual_mailbox_list_params.VirtualMailboxListParams,
                ),
            ),
            model=VirtualMailboxListResponse,
        )

    def retrieve_address(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VirtualMailboxRetrieveAddressResponse:
        """
        Retrieves the physical address of the virtual mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/address", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxRetrieveAddressResponse,
        )


class AsyncVirtualMailboxesResource(AsyncAPIResource):
    """
    Virtual mailboxes let you receive, scan, and forward your physical mail
     without needing a traditional physical mailbox. Each mailbox is fully
     digital, giving you a unique ID, status, and a set of capabilities such as
     forwarding mail to another address or viewing envelope scans. This allows you
     to manage physical correspondence entirely online.

     You can request access to this feature by reaching out to
     support@postgrid.com
    """

    @cached_property
    def items(self) -> AsyncItemsResource:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVirtualMailboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVirtualMailboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualMailboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncVirtualMailboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country_code: Literal["US"],
        capabilities: virtual_mailbox_create_params.Capabilities | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VirtualMailboxCreateResponse:
        """Creates a new virtual mailbox.

        In live mode, the virtual mailbox will be pending
        assignment and cannot be used until it has been assigned and activated by our
        team. You will be notified via email once the virtual mailbox has been
        activated. In test mode, the virtual mailbox will be activated immediately upon
        creation.

        Args:
          country_code: All of the supported countries for virtual mailboxes.

          capabilities: The capabilities the virtual mailbox should support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/virtual_mailboxes",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "capabilities": capabilities,
                },
                virtual_mailbox_create_params.VirtualMailboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxCreateResponse,
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
    ) -> VirtualMailboxRetrieveResponse:
        """
        Retrieve Virtual Mailbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxRetrieveResponse,
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
    ) -> AsyncPaginator[VirtualMailboxListResponse, AsyncSkipLimit[VirtualMailboxListResponse]]:
        """Lists virtual mailboxes.

        You can use the `skip`, `limit`, and `search` query
        parameters to refine the list.

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
            "/print-mail/v1/virtual_mailboxes",
            page=AsyncSkipLimit[VirtualMailboxListResponse],
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
                    virtual_mailbox_list_params.VirtualMailboxListParams,
                ),
            ),
            model=VirtualMailboxListResponse,
        )

    async def retrieve_address(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VirtualMailboxRetrieveAddressResponse:
        """
        Retrieves the physical address of the virtual mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/address", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualMailboxRetrieveAddressResponse,
        )


class VirtualMailboxesResourceWithRawResponse:
    def __init__(self, virtual_mailboxes: VirtualMailboxesResource) -> None:
        self._virtual_mailboxes = virtual_mailboxes

        self.create = to_raw_response_wrapper(
            virtual_mailboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            virtual_mailboxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            virtual_mailboxes.list,
        )
        self.retrieve_address = to_raw_response_wrapper(
            virtual_mailboxes.retrieve_address,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return ItemsResourceWithRawResponse(self._virtual_mailboxes.items)


class AsyncVirtualMailboxesResourceWithRawResponse:
    def __init__(self, virtual_mailboxes: AsyncVirtualMailboxesResource) -> None:
        self._virtual_mailboxes = virtual_mailboxes

        self.create = async_to_raw_response_wrapper(
            virtual_mailboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            virtual_mailboxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            virtual_mailboxes.list,
        )
        self.retrieve_address = async_to_raw_response_wrapper(
            virtual_mailboxes.retrieve_address,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncItemsResourceWithRawResponse(self._virtual_mailboxes.items)


class VirtualMailboxesResourceWithStreamingResponse:
    def __init__(self, virtual_mailboxes: VirtualMailboxesResource) -> None:
        self._virtual_mailboxes = virtual_mailboxes

        self.create = to_streamed_response_wrapper(
            virtual_mailboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            virtual_mailboxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            virtual_mailboxes.list,
        )
        self.retrieve_address = to_streamed_response_wrapper(
            virtual_mailboxes.retrieve_address,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return ItemsResourceWithStreamingResponse(self._virtual_mailboxes.items)


class AsyncVirtualMailboxesResourceWithStreamingResponse:
    def __init__(self, virtual_mailboxes: AsyncVirtualMailboxesResource) -> None:
        self._virtual_mailboxes = virtual_mailboxes

        self.create = async_to_streamed_response_wrapper(
            virtual_mailboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            virtual_mailboxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            virtual_mailboxes.list,
        )
        self.retrieve_address = async_to_streamed_response_wrapper(
            virtual_mailboxes.retrieve_address,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncItemsResourceWithStreamingResponse(self._virtual_mailboxes.items)
