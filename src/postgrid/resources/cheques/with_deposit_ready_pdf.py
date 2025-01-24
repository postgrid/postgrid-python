# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.cheque import Cheque

__all__ = ["WithDepositReadyPdfResource", "AsyncWithDepositReadyPdfResource"]


class WithDepositReadyPdfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WithDepositReadyPdfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return WithDepositReadyPdfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WithDepositReadyPdfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#with_streaming_response
        """
        return WithDepositReadyPdfResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Cheque:
        """Retrieve the deposit-ready PDF for a digital-only cheque.

        The endpoint can only
        be called by users with 'Admin' role. In test mode, the preview PDF of the
        digitalOnly cheque and the deposit-ready PDF are the same. In live mode, the
        deposit-ready will have the full account number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/cheques/{id}/with_deposit_ready_pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Cheque,
        )


class AsyncWithDepositReadyPdfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWithDepositReadyPdfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWithDepositReadyPdfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWithDepositReadyPdfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#with_streaming_response
        """
        return AsyncWithDepositReadyPdfResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Cheque:
        """Retrieve the deposit-ready PDF for a digital-only cheque.

        The endpoint can only
        be called by users with 'Admin' role. In test mode, the preview PDF of the
        digitalOnly cheque and the deposit-ready PDF are the same. In live mode, the
        deposit-ready will have the full account number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/cheques/{id}/with_deposit_ready_pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Cheque,
        )


class WithDepositReadyPdfResourceWithRawResponse:
    def __init__(self, with_deposit_ready_pdf: WithDepositReadyPdfResource) -> None:
        self._with_deposit_ready_pdf = with_deposit_ready_pdf

        self.retrieve = to_raw_response_wrapper(
            with_deposit_ready_pdf.retrieve,
        )


class AsyncWithDepositReadyPdfResourceWithRawResponse:
    def __init__(self, with_deposit_ready_pdf: AsyncWithDepositReadyPdfResource) -> None:
        self._with_deposit_ready_pdf = with_deposit_ready_pdf

        self.retrieve = async_to_raw_response_wrapper(
            with_deposit_ready_pdf.retrieve,
        )


class WithDepositReadyPdfResourceWithStreamingResponse:
    def __init__(self, with_deposit_ready_pdf: WithDepositReadyPdfResource) -> None:
        self._with_deposit_ready_pdf = with_deposit_ready_pdf

        self.retrieve = to_streamed_response_wrapper(
            with_deposit_ready_pdf.retrieve,
        )


class AsyncWithDepositReadyPdfResourceWithStreamingResponse:
    def __init__(self, with_deposit_ready_pdf: AsyncWithDepositReadyPdfResource) -> None:
        self._with_deposit_ready_pdf = with_deposit_ready_pdf

        self.retrieve = async_to_streamed_response_wrapper(
            with_deposit_ready_pdf.retrieve,
        )
