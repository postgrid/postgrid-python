# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ..types import address_verification_verify_params
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
from ..types.address_verification_verify_response import AddressVerificationVerifyResponse

__all__ = ["AddressVerificationResource", "AsyncAddressVerificationResource"]


class AddressVerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AddressVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AddressVerificationResourceWithStreamingResponse(self)

    @overload
    def verify(
        self,
        *,
        address: str,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        """1.

        **Structured Address** — Verify and standardize a structured address (e.g.,
           with `line1`, `city`, etc.).
        2. **Freeform Address** — Verify and standardize a freeform address written on
           one line. For best results, append the ISO 2-letter country code (e.g., `US`,
           `CA`) to the end of the line.

        - Specifying `includeDetails=true` will provide additional output as documented
          in the `Details` schema.
        - Uses 1 lookup for verification, and 1 more if geocoding (unless your contract
          says otherwise).

        Args:
          address: The address you want to verify, written on a single line.

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
        address: address_verification_verify_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        """1.

        **Structured Address** — Verify and standardize a structured address (e.g.,
           with `line1`, `city`, etc.).
        2. **Freeform Address** — Verify and standardize a freeform address written on
           one line. For best results, append the ISO 2-letter country code (e.g., `US`,
           `CA`) to the end of the line.

        - Specifying `includeDetails=true` will provide additional output as documented
          in the `Details` schema.
        - Uses 1 lookup for verification, and 1 more if geocoding (unless your contract
          says otherwise).

        Args:
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
        address: str | address_verification_verify_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        return self._post(
            "/v1/addver/verifications",
            body=maybe_transform(
                {"address": address}, address_verification_verify_params.AddressVerificationVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "geocode": geocode,
                        "include_details": include_details,
                        "proper_case": proper_case,
                    },
                    address_verification_verify_params.AddressVerificationVerifyParams,
                ),
            ),
            cast_to=AddressVerificationVerifyResponse,
        )


class AsyncAddressVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncAddressVerificationResourceWithStreamingResponse(self)

    @overload
    async def verify(
        self,
        *,
        address: str,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        """1.

        **Structured Address** — Verify and standardize a structured address (e.g.,
           with `line1`, `city`, etc.).
        2. **Freeform Address** — Verify and standardize a freeform address written on
           one line. For best results, append the ISO 2-letter country code (e.g., `US`,
           `CA`) to the end of the line.

        - Specifying `includeDetails=true` will provide additional output as documented
          in the `Details` schema.
        - Uses 1 lookup for verification, and 1 more if geocoding (unless your contract
          says otherwise).

        Args:
          address: The address you want to verify, written on a single line.

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
        address: address_verification_verify_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        """1.

        **Structured Address** — Verify and standardize a structured address (e.g.,
           with `line1`, `city`, etc.).
        2. **Freeform Address** — Verify and standardize a freeform address written on
           one line. For best results, append the ISO 2-letter country code (e.g., `US`,
           `CA`) to the end of the line.

        - Specifying `includeDetails=true` will provide additional output as documented
          in the `Details` schema.
        - Uses 1 lookup for verification, and 1 more if geocoding (unless your contract
          says otherwise).

        Args:
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
        address: str | address_verification_verify_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationVerifyResponse:
        return await self._post(
            "/v1/addver/verifications",
            body=await async_maybe_transform(
                {"address": address}, address_verification_verify_params.AddressVerificationVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "geocode": geocode,
                        "include_details": include_details,
                        "proper_case": proper_case,
                    },
                    address_verification_verify_params.AddressVerificationVerifyParams,
                ),
            ),
            cast_to=AddressVerificationVerifyResponse,
        )


class AddressVerificationResourceWithRawResponse:
    def __init__(self, address_verification: AddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.verify = to_raw_response_wrapper(
            address_verification.verify,
        )


class AsyncAddressVerificationResourceWithRawResponse:
    def __init__(self, address_verification: AsyncAddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.verify = async_to_raw_response_wrapper(
            address_verification.verify,
        )


class AddressVerificationResourceWithStreamingResponse:
    def __init__(self, address_verification: AddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.verify = to_streamed_response_wrapper(
            address_verification.verify,
        )


class AsyncAddressVerificationResourceWithStreamingResponse:
    def __init__(self, address_verification: AsyncAddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.verify = async_to_streamed_response_wrapper(
            address_verification.verify,
        )
