# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
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
from ....types.print_mail import return_envelope_list_params, return_envelope_create_params
from ....types.print_mail.return_envelope import ReturnEnvelope

__all__ = ["ReturnEnvelopesResource", "AsyncReturnEnvelopesResource"]


class ReturnEnvelopesResource(SyncAPIResource):
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
    def orders(self) -> OrdersResource:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReturnEnvelopesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ReturnEnvelopesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReturnEnvelopesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return ReturnEnvelopesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        to: return_envelope_create_params.To,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelope:
        """Creates a new return envelope.

        Note that if there is already a return envelope
        for the destination contact, this will fail with a
        `return_envelope_already_exists_error`.

        Args:
          to: A contact ID or a contact object containing the address that will be printed
              onto the return envelope.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/print-mail/v1/return_envelopes",
            body=maybe_transform(
                {
                    "to": to,
                    "description": description,
                    "metadata": metadata,
                },
                return_envelope_create_params.ReturnEnvelopeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelope,
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
    ) -> ReturnEnvelope:
        """Gets the information for a return envelope by `id`.

        This should be a unique
        identifying string starting with `return_envelope_`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/return_envelopes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelope,
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
    ) -> SyncSkipLimit[ReturnEnvelope]:
        """
        Gets a list of return envelopes for the user.

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
            "/print-mail/v1/return_envelopes",
            page=SyncSkipLimit[ReturnEnvelope],
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
                    return_envelope_list_params.ReturnEnvelopeListParams,
                ),
            ),
            model=ReturnEnvelope,
        )


class AsyncReturnEnvelopesResource(AsyncAPIResource):
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
    def orders(self) -> AsyncOrdersResource:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReturnEnvelopesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReturnEnvelopesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReturnEnvelopesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncReturnEnvelopesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        to: return_envelope_create_params.To,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReturnEnvelope:
        """Creates a new return envelope.

        Note that if there is already a return envelope
        for the destination contact, this will fail with a
        `return_envelope_already_exists_error`.

        Args:
          to: A contact ID or a contact object containing the address that will be printed
              onto the return envelope.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/print-mail/v1/return_envelopes",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "description": description,
                    "metadata": metadata,
                },
                return_envelope_create_params.ReturnEnvelopeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelope,
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
    ) -> ReturnEnvelope:
        """Gets the information for a return envelope by `id`.

        This should be a unique
        identifying string starting with `return_envelope_`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/return_envelopes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReturnEnvelope,
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
    ) -> AsyncPaginator[ReturnEnvelope, AsyncSkipLimit[ReturnEnvelope]]:
        """
        Gets a list of return envelopes for the user.

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
            "/print-mail/v1/return_envelopes",
            page=AsyncSkipLimit[ReturnEnvelope],
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
                    return_envelope_list_params.ReturnEnvelopeListParams,
                ),
            ),
            model=ReturnEnvelope,
        )


class ReturnEnvelopesResourceWithRawResponse:
    def __init__(self, return_envelopes: ReturnEnvelopesResource) -> None:
        self._return_envelopes = return_envelopes

        self.create = to_raw_response_wrapper(
            return_envelopes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            return_envelopes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            return_envelopes.list,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return OrdersResourceWithRawResponse(self._return_envelopes.orders)


class AsyncReturnEnvelopesResourceWithRawResponse:
    def __init__(self, return_envelopes: AsyncReturnEnvelopesResource) -> None:
        self._return_envelopes = return_envelopes

        self.create = async_to_raw_response_wrapper(
            return_envelopes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            return_envelopes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            return_envelopes.list,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncOrdersResourceWithRawResponse(self._return_envelopes.orders)


class ReturnEnvelopesResourceWithStreamingResponse:
    def __init__(self, return_envelopes: ReturnEnvelopesResource) -> None:
        self._return_envelopes = return_envelopes

        self.create = to_streamed_response_wrapper(
            return_envelopes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            return_envelopes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            return_envelopes.list,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return OrdersResourceWithStreamingResponse(self._return_envelopes.orders)


class AsyncReturnEnvelopesResourceWithStreamingResponse:
    def __init__(self, return_envelopes: AsyncReturnEnvelopesResource) -> None:
        self._return_envelopes = return_envelopes

        self.create = async_to_streamed_response_wrapper(
            return_envelopes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            return_envelopes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            return_envelopes.list,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncOrdersResourceWithStreamingResponse(self._return_envelopes.orders)
