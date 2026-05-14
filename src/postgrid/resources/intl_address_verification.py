# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import overload

import httpx

from ..types import (
    intl_address_verification_verify_params,
    intl_address_verification_autocomplete_params,
    intl_address_verification_batch_verification_params,
    intl_address_verification_get_autocomplete_previews_params,
    intl_address_verification_get_autocomplete_advanced_previews_params,
)
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
from ..types.intl_address_verification_autocomplete_response import IntlAddressVerificationAutocompleteResponse
from ..types.intl_address_verification_batch_verification_response import (
    IntlAddressVerificationBatchVerificationResponse,
)
from ..types.intl_address_verification_get_autocomplete_previews_response import (
    IntlAddressVerificationGetAutocompletePreviewsResponse,
)
from ..types.intl_address_verification_get_autocomplete_advanced_previews_response import (
    IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
)

__all__ = ["IntlAddressVerificationResource", "AsyncIntlAddressVerificationResource"]


class IntlAddressVerificationResource(SyncAPIResource):
    """International Address Verification API.

    Provides endpoints to verify and standardize international addresses,
    supporting both structured and freeform inputs.
    """

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

    def autocomplete(
        self,
        *,
        id: str,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        verify: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationAutocompleteResponse:
        """
        Resolves an address preview `id` (from `GET /completions`) into a full address.

        Optionally verifies the resolved address through the standard US/CA verifier
        when `verify=true` is supplied and the address is in the US or Canada.

        - Uses 1 lookup per call.
        - When `verify=true` resolves a US or CA address, the response will be a
          `VerifiedAddress` instead of an `IntlAddressCompletion`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/intl_addver/completions",
            body=maybe_transform(
                {"id": id}, intl_address_verification_autocomplete_params.IntlAddressVerificationAutocompleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_details": include_details,
                        "proper_case": proper_case,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                        "verify": verify,
                    },
                    intl_address_verification_autocomplete_params.IntlAddressVerificationAutocompleteParams,
                ),
            ),
            cast_to=IntlAddressVerificationAutocompleteResponse,
        )

    def batch_verification(
        self,
        *,
        addresses: Iterable[intl_address_verification_batch_verification_params.Address],
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationBatchVerificationResponse:
        """Verify a batch of international addresses in a single request.

        Each address can
        be freeform or structured, matching the same input formats accepted by the
        single verification endpoint.

        - Uses 1 lookup per address.
        - Requires a secret API key.
        - Returns results in the same order as the input addresses.
        - If an individual address fails, its result will contain an `error` field
          rather than a `verifiedAddress`.

        Args:
          addresses: Array of addresses to verify. Each item can be a freeform string or a structured
              address object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/intl_addver/verifications/batch",
            body=maybe_transform(
                {"addresses": addresses},
                intl_address_verification_batch_verification_params.IntlAddressVerificationBatchVerificationParams,
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
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_batch_verification_params.IntlAddressVerificationBatchVerificationParams,
                ),
            ),
            cast_to=IntlAddressVerificationBatchVerificationResponse,
        )

    def get_autocomplete_advanced_previews(
        self,
        *,
        advanced: bool | Omit = omit,
        city_filter: str | Omit = omit,
        container: str | Omit = omit,
        countries_filter: str | Omit = omit,
        disable_ip_biasing: bool | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        partial_street: str | Omit = omit,
        postal_or_zip_filter: str | Omit = omit,
        standard_fallback: bool | Omit = omit,
        street_filter: str | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse:
        """
        Returns address completion previews for a partial address string, suitable for
        populating an autocomplete dropdown.

        **Regular mode** — supply `partialStreet` to search by partial street address.
        Results may include `Address` types (resolvable directly) and `Container` types
        (buildings/complexes that require a follow-up call).

        **Advanced mode** — supply `advanced=true` and a `container` ID (from a previous
        regular call) to drill into a building or complex and retrieve individual unit
        addresses.

        Results with `type: "Address"` can be fully resolved by passing their `id` to
        `POST /completions`.

        - Does not consume a lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/intl_addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "advanced": advanced,
                        "city_filter": city_filter,
                        "container": container,
                        "countries_filter": countries_filter,
                        "disable_ip_biasing": disable_ip_biasing,
                        "language": language,
                        "limit": limit,
                        "partial_street": partial_street,
                        "postal_or_zip_filter": postal_or_zip_filter,
                        "standard_fallback": standard_fallback,
                        "street_filter": street_filter,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_get_autocomplete_advanced_previews_params.IntlAddressVerificationGetAutocompleteAdvancedPreviewsParams,
                ),
            ),
            cast_to=IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
        )

    def get_autocomplete_previews(
        self,
        *,
        advanced: bool | Omit = omit,
        city_filter: str | Omit = omit,
        container: str | Omit = omit,
        countries_filter: str | Omit = omit,
        disable_ip_biasing: bool | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        partial_street: str | Omit = omit,
        postal_or_zip_filter: str | Omit = omit,
        standard_fallback: bool | Omit = omit,
        street_filter: str | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationGetAutocompletePreviewsResponse:
        """
        Returns address completion previews for a partial address string, suitable for
        populating an autocomplete dropdown.

        **Regular mode** — supply `partialStreet` to search by partial street address.
        Results may include `Address` types (resolvable directly) and `Container` types
        (buildings/complexes that require a follow-up call).

        **Advanced mode** — supply `advanced=true` and a `container` ID (from a previous
        regular call) to drill into a building or complex and retrieve individual unit
        addresses.

        Results with `type: "Address"` can be fully resolved by passing their `id` to
        `POST /completions`.

        - Does not consume a lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/intl_addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "advanced": advanced,
                        "city_filter": city_filter,
                        "container": container,
                        "countries_filter": countries_filter,
                        "disable_ip_biasing": disable_ip_biasing,
                        "language": language,
                        "limit": limit,
                        "partial_street": partial_street,
                        "postal_or_zip_filter": postal_or_zip_filter,
                        "standard_fallback": standard_fallback,
                        "street_filter": street_filter,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_get_autocomplete_previews_params.IntlAddressVerificationGetAutocompletePreviewsParams,
                ),
            ),
            cast_to=IntlAddressVerificationGetAutocompletePreviewsResponse,
        )

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
    """International Address Verification API.

    Provides endpoints to verify and standardize international addresses,
    supporting both structured and freeform inputs.
    """

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

    async def autocomplete(
        self,
        *,
        id: str,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        verify: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationAutocompleteResponse:
        """
        Resolves an address preview `id` (from `GET /completions`) into a full address.

        Optionally verifies the resolved address through the standard US/CA verifier
        when `verify=true` is supplied and the address is in the US or Canada.

        - Uses 1 lookup per call.
        - When `verify=true` resolves a US or CA address, the response will be a
          `VerifiedAddress` instead of an `IntlAddressCompletion`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/intl_addver/completions",
            body=await async_maybe_transform(
                {"id": id}, intl_address_verification_autocomplete_params.IntlAddressVerificationAutocompleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_details": include_details,
                        "proper_case": proper_case,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                        "verify": verify,
                    },
                    intl_address_verification_autocomplete_params.IntlAddressVerificationAutocompleteParams,
                ),
            ),
            cast_to=IntlAddressVerificationAutocompleteResponse,
        )

    async def batch_verification(
        self,
        *,
        addresses: Iterable[intl_address_verification_batch_verification_params.Address],
        geo_data: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationBatchVerificationResponse:
        """Verify a batch of international addresses in a single request.

        Each address can
        be freeform or structured, matching the same input formats accepted by the
        single verification endpoint.

        - Uses 1 lookup per address.
        - Requires a secret API key.
        - Returns results in the same order as the input addresses.
        - If an individual address fails, its result will contain an `error` field
          rather than a `verifiedAddress`.

        Args:
          addresses: Array of addresses to verify. Each item can be a freeform string or a structured
              address object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/intl_addver/verifications/batch",
            body=await async_maybe_transform(
                {"addresses": addresses},
                intl_address_verification_batch_verification_params.IntlAddressVerificationBatchVerificationParams,
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
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_batch_verification_params.IntlAddressVerificationBatchVerificationParams,
                ),
            ),
            cast_to=IntlAddressVerificationBatchVerificationResponse,
        )

    async def get_autocomplete_advanced_previews(
        self,
        *,
        advanced: bool | Omit = omit,
        city_filter: str | Omit = omit,
        container: str | Omit = omit,
        countries_filter: str | Omit = omit,
        disable_ip_biasing: bool | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        partial_street: str | Omit = omit,
        postal_or_zip_filter: str | Omit = omit,
        standard_fallback: bool | Omit = omit,
        street_filter: str | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse:
        """
        Returns address completion previews for a partial address string, suitable for
        populating an autocomplete dropdown.

        **Regular mode** — supply `partialStreet` to search by partial street address.
        Results may include `Address` types (resolvable directly) and `Container` types
        (buildings/complexes that require a follow-up call).

        **Advanced mode** — supply `advanced=true` and a `container` ID (from a previous
        regular call) to drill into a building or complex and retrieve individual unit
        addresses.

        Results with `type: "Address"` can be fully resolved by passing their `id` to
        `POST /completions`.

        - Does not consume a lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/intl_addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "advanced": advanced,
                        "city_filter": city_filter,
                        "container": container,
                        "countries_filter": countries_filter,
                        "disable_ip_biasing": disable_ip_biasing,
                        "language": language,
                        "limit": limit,
                        "partial_street": partial_street,
                        "postal_or_zip_filter": postal_or_zip_filter,
                        "standard_fallback": standard_fallback,
                        "street_filter": street_filter,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_get_autocomplete_advanced_previews_params.IntlAddressVerificationGetAutocompleteAdvancedPreviewsParams,
                ),
            ),
            cast_to=IntlAddressVerificationGetAutocompleteAdvancedPreviewsResponse,
        )

    async def get_autocomplete_previews(
        self,
        *,
        advanced: bool | Omit = omit,
        city_filter: str | Omit = omit,
        container: str | Omit = omit,
        countries_filter: str | Omit = omit,
        disable_ip_biasing: bool | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        partial_street: str | Omit = omit,
        postal_or_zip_filter: str | Omit = omit,
        standard_fallback: bool | Omit = omit,
        street_filter: str | Omit = omit,
        use_enhanced_china_dataset: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntlAddressVerificationGetAutocompletePreviewsResponse:
        """
        Returns address completion previews for a partial address string, suitable for
        populating an autocomplete dropdown.

        **Regular mode** — supply `partialStreet` to search by partial street address.
        Results may include `Address` types (resolvable directly) and `Container` types
        (buildings/complexes that require a follow-up call).

        **Advanced mode** — supply `advanced=true` and a `container` ID (from a previous
        regular call) to drill into a building or complex and retrieve individual unit
        addresses.

        Results with `type: "Address"` can be fully resolved by passing their `id` to
        `POST /completions`.

        - Does not consume a lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/intl_addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "advanced": advanced,
                        "city_filter": city_filter,
                        "container": container,
                        "countries_filter": countries_filter,
                        "disable_ip_biasing": disable_ip_biasing,
                        "language": language,
                        "limit": limit,
                        "partial_street": partial_street,
                        "postal_or_zip_filter": postal_or_zip_filter,
                        "standard_fallback": standard_fallback,
                        "street_filter": street_filter,
                        "use_enhanced_china_dataset": use_enhanced_china_dataset,
                    },
                    intl_address_verification_get_autocomplete_previews_params.IntlAddressVerificationGetAutocompletePreviewsParams,
                ),
            ),
            cast_to=IntlAddressVerificationGetAutocompletePreviewsResponse,
        )

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

        self.autocomplete = to_raw_response_wrapper(
            intl_address_verification.autocomplete,
        )
        self.batch_verification = to_raw_response_wrapper(
            intl_address_verification.batch_verification,
        )
        self.get_autocomplete_advanced_previews = to_raw_response_wrapper(
            intl_address_verification.get_autocomplete_advanced_previews,
        )
        self.get_autocomplete_previews = to_raw_response_wrapper(
            intl_address_verification.get_autocomplete_previews,
        )
        self.verify = to_raw_response_wrapper(
            intl_address_verification.verify,
        )


class AsyncIntlAddressVerificationResourceWithRawResponse:
    def __init__(self, intl_address_verification: AsyncIntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.autocomplete = async_to_raw_response_wrapper(
            intl_address_verification.autocomplete,
        )
        self.batch_verification = async_to_raw_response_wrapper(
            intl_address_verification.batch_verification,
        )
        self.get_autocomplete_advanced_previews = async_to_raw_response_wrapper(
            intl_address_verification.get_autocomplete_advanced_previews,
        )
        self.get_autocomplete_previews = async_to_raw_response_wrapper(
            intl_address_verification.get_autocomplete_previews,
        )
        self.verify = async_to_raw_response_wrapper(
            intl_address_verification.verify,
        )


class IntlAddressVerificationResourceWithStreamingResponse:
    def __init__(self, intl_address_verification: IntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.autocomplete = to_streamed_response_wrapper(
            intl_address_verification.autocomplete,
        )
        self.batch_verification = to_streamed_response_wrapper(
            intl_address_verification.batch_verification,
        )
        self.get_autocomplete_advanced_previews = to_streamed_response_wrapper(
            intl_address_verification.get_autocomplete_advanced_previews,
        )
        self.get_autocomplete_previews = to_streamed_response_wrapper(
            intl_address_verification.get_autocomplete_previews,
        )
        self.verify = to_streamed_response_wrapper(
            intl_address_verification.verify,
        )


class AsyncIntlAddressVerificationResourceWithStreamingResponse:
    def __init__(self, intl_address_verification: AsyncIntlAddressVerificationResource) -> None:
        self._intl_address_verification = intl_address_verification

        self.autocomplete = async_to_streamed_response_wrapper(
            intl_address_verification.autocomplete,
        )
        self.batch_verification = async_to_streamed_response_wrapper(
            intl_address_verification.batch_verification,
        )
        self.get_autocomplete_advanced_previews = async_to_streamed_response_wrapper(
            intl_address_verification.get_autocomplete_advanced_previews,
        )
        self.get_autocomplete_previews = async_to_streamed_response_wrapper(
            intl_address_verification.get_autocomplete_previews,
        )
        self.verify = async_to_streamed_response_wrapper(
            intl_address_verification.verify,
        )
