# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
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
from ...types.print_mail import event_list_params
from ...types.print_mail.event import Event

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """View Events related to your orders.

    An event is created whenever a webhook is triggered. For example, if a webhook
    is created that listens to `letter.updated` events and the delivery status of a
    letter is updated, an event detailing the updated fields will get created.
    """

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        type: List[
            Literal[
                "letter.created",
                "letter.updated",
                "postcard.created",
                "postcard.updated",
                "self_mailer.created",
                "self_mailer.updated",
                "cheque.created",
                "cheque.updated",
                "box.created",
                "box.updated",
                "snap_pack.created",
                "snap_pack.updated",
                "return_envelope_order.created",
                "return_envelope_order.updated",
                "tracker.visited",
                "campaign.created",
                "campaign.updated",
                "virtual_mailbox_item.created",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimit[Event]:
        """
        Retrieve a paginated list of Events.

        Args:
          type: An optional list of event types to filter the results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/print-mail/v1/events",
            page=SyncSkipLimit[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "type": type,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )


class AsyncEventsResource(AsyncAPIResource):
    """View Events related to your orders.

    An event is created whenever a webhook is triggered. For example, if a webhook
    is created that listens to `letter.updated` events and the delivery status of a
    letter is updated, an event detailing the updated fields will get created.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        type: List[
            Literal[
                "letter.created",
                "letter.updated",
                "postcard.created",
                "postcard.updated",
                "self_mailer.created",
                "self_mailer.updated",
                "cheque.created",
                "cheque.updated",
                "box.created",
                "box.updated",
                "snap_pack.created",
                "snap_pack.updated",
                "return_envelope_order.created",
                "return_envelope_order.updated",
                "tracker.visited",
                "campaign.created",
                "campaign.updated",
                "virtual_mailbox_item.created",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Event, AsyncSkipLimit[Event]]:
        """
        Retrieve a paginated list of Events.

        Args:
          type: An optional list of event types to filter the results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/print-mail/v1/events",
            page=AsyncSkipLimit[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                        "type": type,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
