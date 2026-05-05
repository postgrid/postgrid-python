# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

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
from ....types.print_mail.virtual_mailboxes import item_list_params, item_create_params
from ....types.print_mail.virtual_mailboxes.item_list_response import ItemListResponse
from ....types.print_mail.virtual_mailboxes.item_create_response import ItemCreateResponse
from ....types.print_mail.virtual_mailboxes.item_retrieve_response import ItemRetrieveResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
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
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        matched_letter: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateResponse:
        """Create a test item for a virtual mailbox.

        This is only available in test mode,
        an error will be returned if you attempt this call in live mode.

        Args:
          description: The description of the item.

          matched_letter: The ID of a letter to match this test item to.

          metadata: The metadata of the item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "matched_letter": matched_letter,
                    "metadata": metadata,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    def retrieve(
        self,
        item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveResponse:
        """
        Retrieves a single item for a virtual mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items/{item_id}", id=id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrieveResponse,
        )

    def list(
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
    ) -> SyncSkipLimit[ItemListResponse]:
        """
        Lists items for a virtual mailbox.

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
        return self._get_api_list(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items", id=id),
            page=SyncSkipLimit[ItemListResponse],
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
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )


class AsyncItemsResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        matched_letter: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemCreateResponse:
        """Create a test item for a virtual mailbox.

        This is only available in test mode,
        an error will be returned if you attempt this call in live mode.

        Args:
          description: The description of the item.

          matched_letter: The ID of a letter to match this test item to.

          metadata: The metadata of the item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "matched_letter": matched_letter,
                    "metadata": metadata,
                },
                item_create_params.ItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemCreateResponse,
        )

    async def retrieve(
        self,
        item_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemRetrieveResponse:
        """
        Retrieves a single item for a virtual mailbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items/{item_id}", id=id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemRetrieveResponse,
        )

    def list(
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
    ) -> AsyncPaginator[ItemListResponse, AsyncSkipLimit[ItemListResponse]]:
        """
        Lists items for a virtual mailbox.

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
        return self._get_api_list(
            path_template("/print-mail/v1/virtual_mailboxes/{id}/items", id=id),
            page=AsyncSkipLimit[ItemListResponse],
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
                    item_list_params.ItemListParams,
                ),
            ),
            model=ItemListResponse,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            items.retrieve,
        )
        self.list = to_raw_response_wrapper(
            items.list,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_raw_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            items.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            items.list,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.create = to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            items.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            items.list,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.create = async_to_streamed_response_wrapper(
            items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            items.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
