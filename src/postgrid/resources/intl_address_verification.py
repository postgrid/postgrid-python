# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ..types import intl_address_verification_verify_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.intl_address_verification_verify_response import IntlAddressVerificationVerifyResponse

__all__ = ["IntlAddressVerificationResource", "AsyncIntlAddressVerificationResource"]


class IntlAddressVerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntlAddressVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return IntlAddressVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntlAddressVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return IntlAddressVerificationResourceWithStreamingResponse(self)

    @overload
    def verify(
        self,
        *,
        address: intl_address_verification_verify_params.StructuredAddressInputAddress,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        """
        Verify and standardize an international address.

        - Supports both structured and freeform address inputs.
        - Specify `includeDetails=true` to get additional details as per the
          `IntlDetails` schema.
        - Uses 1 lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def verify(
        self,
        *,
        address: str,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        """
        Verify and standardize an international address.

        - Supports both structured and freeform address inputs.
        - Specify `includeDetails=true` to get additional details as per the
          `IntlDetails` schema.
        - Uses 1 lookup.

        Args:
          address: The full address as a single string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address"])
    def verify(
        self,
        *,
        address: intl_address_verification_verify_params.StructuredAddressInputAddress | str,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        return self._post(
            "/v1/intl_addver/verifications",
            body=maybe_transform(
                {"address": address}, intl_address_verification_verify_params.IntlAddressVerificationVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "geo_data": geo_data,
                        "include_details": include_details,
                        "proper_case": proper_case,
                    },
                    intl_address_verification_verify_params.IntlAddressVerificationVerifyParams,
                ),
            ),
            cast_to=IntlAddressVerificationVerifyResponse,
        )


class AsyncIntlAddressVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntlAddressVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntlAddressVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntlAddressVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncIntlAddressVerificationResourceWithStreamingResponse(self)

    @overload
    async def verify(
        self,
        *,
        address: intl_address_verification_verify_params.StructuredAddressInputAddress,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        """
        Verify and standardize an international address.

        - Supports both structured and freeform address inputs.
        - Specify `includeDetails=true` to get additional details as per the
          `IntlDetails` schema.
        - Uses 1 lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def verify(
        self,
        *,
        address: str,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        """
        Verify and standardize an international address.

        - Supports both structured and freeform address inputs.
        - Specify `includeDetails=true` to get additional details as per the
          `IntlDetails` schema.
        - Uses 1 lookup.

        Args:
          address: The full address as a single string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address"])
    async def verify(
        self,
        *,
        address: intl_address_verification_verify_params.StructuredAddressInputAddress | str,
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationVerifyResponse:
        return await self._post(
            "/v1/intl_addver/verifications",
            body=await async_maybe_transform(
                {"address": address}, intl_address_verification_verify_params.IntlAddressVerificationVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "geo_data": geo_data,
                        "include_details": include_details,
                        "proper_case": proper_case,
                    },
                    intl_address_verification_verify_params.IntlAddressVerificationVerifyParams,
                ),
            ),
            cast_to=IntlAddressVerificationVerifyResponse,
        )


class IntlAddressVerificationResourceWithRawResponse:
    def __init__(self, intl_address_verification: IntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.verify = to_raw_response_wrapper(
            intl_address_verification.verify,
        )


class AsyncIntlAddressVerificationResourceWithRawResponse:
    def __init__(self, intl_address_verification: AsyncIntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.verify = async_to_raw_response_wrapper(
            intl_address_verification.verify,
        )


class IntlAddressVerificationResourceWithStreamingResponse:
    def __init__(self, intl_address_verification: IntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.verify = to_streamed_response_wrapper(
            intl_address_verification.verify,
        )


class AsyncIntlAddressVerificationResourceWithStreamingResponse:
    def __init__(self, intl_address_verification: AsyncIntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.verify = async_to_streamed_response_wrapper(
            intl_address_verification.verify,
        )
