# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
    webhook_list_params,
    webhook_create_params,
    webhook_update_params,
    webhook_list_invocations_params,
)
from ...types.print_mail.webhook import Webhook
from ...types.print_mail.webhook_invocation import WebhookInvocation
from ...types.print_mail.webhook_delete_response import WebhookDeleteResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """Create and manage Webhooks.

    Webhooks can be used to notify your application when events occur in PostGrid.
    For example, you may use a `letter.updated` webhook to receive a notification
    when a letter has been processed for delivery.

    Every webhook has a `secret` and this is used to sign the payload of the event.

    You can choose what format you want the payload to be delivered in. By default,
    the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
    When you receive the event, you can verify it using a JWT library available for
    your particular language (using the HMAC SHA256 Algorithm). There are
    [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

    You can alternatively choose to receive a JSON payload. In this case, you'll
    also receive a `PostGrid-Signature` HTTP header along with the payload.

    You must respond with a `200` status from your webhook. Otherwise, PostGrid
    will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
    4 hours. We will also keep track of every invocation and its response status.
    You can retrieve data about prior invocations using the webhook invocations
    list endpoint below.
    """

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        enabled_events: List[
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
        ],
        url: str,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        payload_format: Literal["jwt", "json"] | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Create a Webhook.

        Args:
          enabled_events: The list of event types this webhook listens for.

          url: An HTTPS URL that PostGrid can invoke for webhook deliveries.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          payload_format: The format in which a Webhook's event payload is delivered.

          secret: A webhook signing secret with at least 20 non-whitespace characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/webhooks",
            body=maybe_transform(
                {
                    "enabled_events": enabled_events,
                    "url": url,
                    "description": description,
                    "metadata": metadata,
                    "payload_format": payload_format,
                    "secret": secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
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
    ) -> Webhook:
        """
        Retrieve a Webhook by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        enabled_events: List[
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
        metadata: Dict[str, object] | Omit = omit,
        payload_format: Literal["jwt", "json"] | Omit = omit,
        secret: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Update a Webhook by ID.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          enabled: Whether this webhook is enabled. Disabled webhooks are not triggered.

          enabled_events: The list of event types this webhook listens for.

          metadata: See the section on Metadata.

          payload_format: The format in which a Webhook's event payload is delivered.

          secret: A webhook signing secret with at least 20 non-whitespace characters.

          url: An HTTPS URL that PostGrid can invoke for webhook deliveries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "enabled_events": enabled_events,
                    "metadata": metadata,
                    "payload_format": payload_format,
                    "secret": secret,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
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
    ) -> SyncSkipLimit[Webhook]:
        """
        Retrieve a paginated list of Webhooks.

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
            "/print-mail/v1/webhooks",
            page=SyncSkipLimit[Webhook],
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
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=Webhook,
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
    ) -> WebhookDeleteResponse:
        """Delete a Webhook by ID.

        Note that this operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_invocations(
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
    ) -> SyncSkipLimit[WebhookInvocation]:
        """
        Retrieve a paginated list of invocations for a Webhook.

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
            path_template("/print-mail/v1/webhooks/{id}/invocations", id=id),
            page=SyncSkipLimit[WebhookInvocation],
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
                    webhook_list_invocations_params.WebhookListInvocationsParams,
                ),
            ),
            model=WebhookInvocation,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    """Create and manage Webhooks.

    Webhooks can be used to notify your application when events occur in PostGrid.
    For example, you may use a `letter.updated` webhook to receive a notification
    when a letter has been processed for delivery.

    Every webhook has a `secret` and this is used to sign the payload of the event.

    You can choose what format you want the payload to be delivered in. By default,
    the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
    When you receive the event, you can verify it using a JWT library available for
    your particular language (using the HMAC SHA256 Algorithm). There are
    [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

    You can alternatively choose to receive a JSON payload. In this case, you'll
    also receive a `PostGrid-Signature` HTTP header along with the payload.

    You must respond with a `200` status from your webhook. Otherwise, PostGrid
    will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
    4 hours. We will also keep track of every invocation and its response status.
    You can retrieve data about prior invocations using the webhook invocations
    list endpoint below.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        enabled_events: List[
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
        ],
        url: str,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        payload_format: Literal["jwt", "json"] | Omit = omit,
        secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Create a Webhook.

        Args:
          enabled_events: The list of event types this webhook listens for.

          url: An HTTPS URL that PostGrid can invoke for webhook deliveries.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          payload_format: The format in which a Webhook's event payload is delivered.

          secret: A webhook signing secret with at least 20 non-whitespace characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/webhooks",
            body=await async_maybe_transform(
                {
                    "enabled_events": enabled_events,
                    "url": url,
                    "description": description,
                    "metadata": metadata,
                    "payload_format": payload_format,
                    "secret": secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
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
    ) -> Webhook:
        """
        Retrieve a Webhook by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        enabled_events: List[
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
        metadata: Dict[str, object] | Omit = omit,
        payload_format: Literal["jwt", "json"] | Omit = omit,
        secret: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Webhook:
        """
        Update a Webhook by ID.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          enabled: Whether this webhook is enabled. Disabled webhooks are not triggered.

          enabled_events: The list of event types this webhook listens for.

          metadata: See the section on Metadata.

          payload_format: The format in which a Webhook's event payload is delivered.

          secret: A webhook signing secret with at least 20 non-whitespace characters.

          url: An HTTPS URL that PostGrid can invoke for webhook deliveries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "enabled_events": enabled_events,
                    "metadata": metadata,
                    "payload_format": payload_format,
                    "secret": secret,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Webhook,
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
    ) -> AsyncPaginator[Webhook, AsyncSkipLimit[Webhook]]:
        """
        Retrieve a paginated list of Webhooks.

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
            "/print-mail/v1/webhooks",
            page=AsyncSkipLimit[Webhook],
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
                    webhook_list_params.WebhookListParams,
                ),
            ),
            model=Webhook,
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
    ) -> WebhookDeleteResponse:
        """Delete a Webhook by ID.

        Note that this operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/print-mail/v1/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_invocations(
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
    ) -> AsyncPaginator[WebhookInvocation, AsyncSkipLimit[WebhookInvocation]]:
        """
        Retrieve a paginated list of invocations for a Webhook.

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
            path_template("/print-mail/v1/webhooks/{id}/invocations", id=id),
            page=AsyncSkipLimit[WebhookInvocation],
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
                    webhook_list_invocations_params.WebhookListInvocationsParams,
                ),
            ),
            model=WebhookInvocation,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_invocations = to_raw_response_wrapper(
            webhooks.list_invocations,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_invocations = async_to_raw_response_wrapper(
            webhooks.list_invocations,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_invocations = to_streamed_response_wrapper(
            webhooks.list_invocations,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_invocations = async_to_streamed_response_wrapper(
            webhooks.list_invocations,
        )
