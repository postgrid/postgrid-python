# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

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
from ...types.print_mail import OrderMailingClass, box_list_params, box_create_params
from ...types.print_mail.box import Box
from ...types.print_mail.order_mailing_class import OrderMailingClass

__all__ = ["BoxesResource", "AsyncBoxesResource"]


class BoxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BoxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return BoxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BoxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return BoxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cheques: Iterable[box_create_params.Cheque],
        from_: box_create_params.From,
        to: box_create_params.To,
        description: str | Omit = omit,
        mailing_class: OrderMailingClass | Omit = omit,
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Box:
        """This endpoint allows you to create a box containing up to 100 cheques.

        A Box is
        mailed to a single destination.

        To create a box. You must specify:

        - `to`: The recipient (contact or contact ID)
        - `from`: The sender (contact or contact ID)
        - `cheques`: An array of cheques to go in the box

        For each cheque You must specify:

        - `to`: The recipient (contact or contact ID)
        - `from`: The sender (contact or contact ID)
        - `bankAccount`: The bank account ID
        - `amount`: The amount to be sent
        - `number`: The cheque number

        Args:
          cheques: The cheques to be mailed in the box. Only 100 cheques can be included in a box
              at a time.

          from_: The 'from' (sender) of the entire box. Accepts inline ContactCreate or a
              contactID.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/boxes",
            body=maybe_transform(
                {
                    "cheques": cheques,
                    "from_": from_,
                    "to": to,
                    "description": description,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                },
                box_create_params.BoxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
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
    ) -> Box:
        """
        Retrieve a box by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/boxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
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
    ) -> SyncSkipLimit[Box]:
        """
        List all boxes.

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
            "/print-mail/v1/boxes",
            page=SyncSkipLimit[Box],
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
                    box_list_params.BoxListParams,
                ),
            ),
            model=Box,
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
    ) -> Box:
        """
        Cancel a box by ID (cannot be undone).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/boxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
        )


class AsyncBoxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBoxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBoxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBoxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncBoxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cheques: Iterable[box_create_params.Cheque],
        from_: box_create_params.From,
        to: box_create_params.To,
        description: str | Omit = omit,
        mailing_class: OrderMailingClass | Omit = omit,
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Box:
        """This endpoint allows you to create a box containing up to 100 cheques.

        A Box is
        mailed to a single destination.

        To create a box. You must specify:

        - `to`: The recipient (contact or contact ID)
        - `from`: The sender (contact or contact ID)
        - `cheques`: An array of cheques to go in the box

        For each cheque You must specify:

        - `to`: The recipient (contact or contact ID)
        - `from`: The sender (contact or contact ID)
        - `bankAccount`: The bank account ID
        - `amount`: The amount to be sent
        - `number`: The cheque number

        Args:
          cheques: The cheques to be mailed in the box. Only 100 cheques can be included in a box
              at a time.

          from_: The 'from' (sender) of the entire box. Accepts inline ContactCreate or a
              contactID.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/boxes",
            body=await async_maybe_transform(
                {
                    "cheques": cheques,
                    "from_": from_,
                    "to": to,
                    "description": description,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                },
                box_create_params.BoxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
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
    ) -> Box:
        """
        Retrieve a box by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/boxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
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
    ) -> AsyncPaginator[Box, AsyncSkipLimit[Box]]:
        """
        List all boxes.

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
            "/print-mail/v1/boxes",
            page=AsyncSkipLimit[Box],
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
                    box_list_params.BoxListParams,
                ),
            ),
            model=Box,
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
    ) -> Box:
        """
        Cancel a box by ID (cannot be undone).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/boxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Box,
        )


class BoxesResourceWithRawResponse:
    def __init__(self, boxes: BoxesResource) -> None:
        self._boxes = boxes

        self.create = to_raw_response_wrapper(
            boxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            boxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            boxes.list,
        )
        self.delete = to_raw_response_wrapper(
            boxes.delete,
        )


class AsyncBoxesResourceWithRawResponse:
    def __init__(self, boxes: AsyncBoxesResource) -> None:
        self._boxes = boxes

        self.create = async_to_raw_response_wrapper(
            boxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            boxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            boxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            boxes.delete,
        )


class BoxesResourceWithStreamingResponse:
    def __init__(self, boxes: BoxesResource) -> None:
        self._boxes = boxes

        self.create = to_streamed_response_wrapper(
            boxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            boxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            boxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            boxes.delete,
        )


class AsyncBoxesResourceWithStreamingResponse:
    def __init__(self, boxes: AsyncBoxesResource) -> None:
        self._boxes = boxes

        self.create = async_to_streamed_response_wrapper(
            boxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            boxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            boxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            boxes.delete,
        )
