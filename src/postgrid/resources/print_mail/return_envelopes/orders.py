# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

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
from ....types.print_mail.return_envelopes import (
    order_list_params,
    order_cancel_params,
    order_create_params,
    order_retrieve_params,
)
from ....types.print_mail.return_envelopes.return_envelope_order import ReturnEnvelopeOrder

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    """
    You can use the return envelopes API to create and manage return envelopes.
     These are envelopes that are sent along with your mail (if specified) and
     allow your recipients to send mail to a particular address without having to
     purchase their own envelopes/stamps.

     Note that you must order return envelopes and wait for the order to be
     filled before you can use them. You can manage these return envelope orders
     via the API as well as the dashboard.
    """

    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return OrdersResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        quantity_ordered: int,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """Creates a batch order of return envelopes.

        The minimum order quantity is 5000.

        Args:
          quantity_ordered: The quantity of return envelopes ordered. Minimum 5000.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/return_envelopes/{id}/orders", id=id),
            body=maybe_transform(
                {
                    "quantity_ordered": quantity_ordered,
                    "description": description,
                    "metadata": metadata,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelopeOrder,
        )

    def retrieve(
        self,
        order_id: str,
        *,
        id: str,
        expand: List[Literal["returnEnvelope"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Gets a specific return envelope order by return envelope ID as `id` and return
        envelope order ID as `orderID`.

        Args:
          expand: Pass `expand[]=returnEnvelope` to expand the order's `returnEnvelope` field into
              the full return envelope object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, order_retrieve_params.OrderRetrieveParams),
            ),
            cast_to=ReturnEnvelopeOrder,
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
    ) -> SyncSkipLimit[ReturnEnvelopeOrder]:
        """
        Gets a list of orders for the return envelope by `id`.

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
            path_template("/print-mail/v1/return_envelopes/{id}/orders", id=id),
            page=SyncSkipLimit[ReturnEnvelopeOrder],
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
                    order_list_params.OrderListParams,
                ),
            ),
            model=ReturnEnvelopeOrder,
        )

    def cancel(
        self,
        order_id: str,
        *,
        id: str,
        expand: List[Literal["returnEnvelope"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Cancels the return envelope order by `orderID` for the return envelope by `id`.
        Note that this operation cannot be undone.

        Args:
          expand: Pass `expand[]=returnEnvelope` to expand the order's `returnEnvelope` field into
              the full return envelope object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._delete(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, order_cancel_params.OrderCancelParams),
            ),
            cast_to=ReturnEnvelopeOrder,
        )

    def fill(
        self,
        order_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Fills the return envelope order by `orderID` for the return envelope by `id`.
        This is only available in test mode and can be used to simulate how a live order
        would be filled.

        Note: this will fail with a `return_envelope_order_cannot_fill_error` if the
        order's status is not `placed`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._post(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}/fills", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelopeOrder,
        )


class AsyncOrdersResource(AsyncAPIResource):
    """
    You can use the return envelopes API to create and manage return envelopes.
     These are envelopes that are sent along with your mail (if specified) and
     allow your recipients to send mail to a particular address without having to
     purchase their own envelopes/stamps.

     Note that you must order return envelopes and wait for the order to be
     filled before you can use them. You can manage these return envelope orders
     via the API as well as the dashboard.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        quantity_ordered: int,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """Creates a batch order of return envelopes.

        The minimum order quantity is 5000.

        Args:
          quantity_ordered: The quantity of return envelopes ordered. Minimum 5000.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/return_envelopes/{id}/orders", id=id),
            body=await async_maybe_transform(
                {
                    "quantity_ordered": quantity_ordered,
                    "description": description,
                    "metadata": metadata,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelopeOrder,
        )

    async def retrieve(
        self,
        order_id: str,
        *,
        id: str,
        expand: List[Literal["returnEnvelope"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Gets a specific return envelope order by return envelope ID as `id` and return
        envelope order ID as `orderID`.

        Args:
          expand: Pass `expand[]=returnEnvelope` to expand the order's `returnEnvelope` field into
              the full return envelope object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, order_retrieve_params.OrderRetrieveParams),
            ),
            cast_to=ReturnEnvelopeOrder,
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
    ) -> AsyncPaginator[ReturnEnvelopeOrder, AsyncSkipLimit[ReturnEnvelopeOrder]]:
        """
        Gets a list of orders for the return envelope by `id`.

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
            path_template("/print-mail/v1/return_envelopes/{id}/orders", id=id),
            page=AsyncSkipLimit[ReturnEnvelopeOrder],
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
                    order_list_params.OrderListParams,
                ),
            ),
            model=ReturnEnvelopeOrder,
        )

    async def cancel(
        self,
        order_id: str,
        *,
        id: str,
        expand: List[Literal["returnEnvelope"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Cancels the return envelope order by `orderID` for the return envelope by `id`.
        Note that this operation cannot be undone.

        Args:
          expand: Pass `expand[]=returnEnvelope` to expand the order's `returnEnvelope` field into
              the full return envelope object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._delete(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, order_cancel_params.OrderCancelParams),
            ),
            cast_to=ReturnEnvelopeOrder,
        )

    async def fill(
        self,
        order_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelopeOrder:
        """
        Fills the return envelope order by `orderID` for the return envelope by `id`.
        This is only available in test mode and can be used to simulate how a live order
        would be filled.

        Note: this will fail with a `return_envelope_order_cannot_fill_error` if the
        order's status is not `placed`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._post(
            path_template("/print-mail/v1/return_envelopes/{id}/orders/{order_id}/fills", id=id, order_id=order_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelopeOrder,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_raw_response_wrapper(
            orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            orders.list,
        )
        self.cancel = to_raw_response_wrapper(
            orders.cancel,
        )
        self.fill = to_raw_response_wrapper(
            orders.fill,
        )


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_raw_response_wrapper(
            orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            orders.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            orders.cancel,
        )
        self.fill = async_to_raw_response_wrapper(
            orders.fill,
        )


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_streamed_response_wrapper(
            orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            orders.list,
        )
        self.cancel = to_streamed_response_wrapper(
            orders.cancel,
        )
        self.fill = to_streamed_response_wrapper(
            orders.fill,
        )


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_streamed_response_wrapper(
            orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            orders.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            orders.cancel,
        )
        self.fill = async_to_streamed_response_wrapper(
            orders.fill,
        )
