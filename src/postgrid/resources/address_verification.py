# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import overload

import httpx

from ..types import (
    address_verification_verify_params,
    address_verification_autocomplete_params,
    address_verification_parse_an_address_params,
    address_verification_suggest_addresses_params,
    address_verification_batch_verification_params,
    address_verification_get_autocomplete_previews_params,
    address_verification_lookup_zip_code_from_city_or_state_params,
    address_verification_lookup_city_or_state_from_postal_or_zip_code_params,
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
from ..types.address_verification_verify_response import AddressVerificationVerifyResponse
from ..types.address_verification_autocomplete_response import AddressVerificationAutocompleteResponse
from ..types.address_verification_get_lookup_info_response import AddressVerificationGetLookupInfoResponse
from ..types.address_verification_parse_an_address_response import AddressVerificationParseAnAddressResponse
from ..types.address_verification_suggest_addresses_response import AddressVerificationSuggestAddressesResponse
from ..types.address_verification_batch_verification_response import AddressVerificationBatchVerificationResponse
from ..types.address_verification_get_autocomplete_previews_response import (
    AddressVerificationGetAutocompletePreviewsResponse,
)
from ..types.address_verification_lookup_zip_code_from_city_or_state_response import (
    AddressVerificationLookupZipCodeFromCityOrStateResponse,
)
from ..types.address_verification_lookup_city_or_state_from_postal_or_zip_code_response import (
    AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse,
)

__all__ = ["AddressVerificationResource", "AsyncAddressVerificationResource"]


class AddressVerificationResource(SyncAPIResource):
    """Standard Address Verification API.

    Provides endpoints to verify and standardize addresses across US and Canada,
    supporting both structured and freeform inputs.

    Note that this uses a different set of lookups than our international API.
    """

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

    def autocomplete(
        self,
        *,
        partial_street: str,
        filter_exact: bool | Omit = omit,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        index: int | Omit = omit,
        limit: int | Omit = omit,
        proper_case: bool | Omit = omit,
        query_verified_only: bool | Omit = omit,
        verify: bool | Omit = omit,
        city_filter: str | Omit = omit,
        country_filter: str | Omit = omit,
        pc_filter: str | Omit = omit,
        state_filter: str | Omit = omit,
        body_verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationAutocompleteResponse:
        """
        Resolves a partial street address into a list of full address candidates,
        optionally selecting a specific candidate by index and verifying it.

        **Basic usage** — omit `index`: returns an array of `CompletedAddressItem`
        results for the given `partialStreet`.

        **With `index`** — specify `index` to resolve a single candidate. Returns a
        single `CompletedAddressItem`.

        **With `index` + `verify=true`** — additionally runs the selected address
        through the USPS/Canada Post verifier and returns a `StandardVerifiedAddress`.

        - Uses 1 lookup per call (plus 1 more if geocoding a result).

        Args:
          partial_street: The partial street address to complete (e.g. `"22 Bay"`).

          city_filter: Filter results to a specific city.

          country_filter: Filter results to a specific country code.

          pc_filter: Filter results to a specific postal code prefix.

          state_filter: Filter results to a specific state or province abbreviation.

          body_verified_only: If true, only return addresses that passed USPS/Canada Post verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/addver/completions",
            body=maybe_transform(
                {
                    "partial_street": partial_street,
                    "city_filter": city_filter,
                    "country_filter": country_filter,
                    "pc_filter": pc_filter,
                    "state_filter": state_filter,
                    "body_verified_only": body_verified_only,
                },
                address_verification_autocomplete_params.AddressVerificationAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_exact": filter_exact,
                        "geocode": geocode,
                        "include_details": include_details,
                        "index": index,
                        "limit": limit,
                        "proper_case": proper_case,
                        "query_verified_only": query_verified_only,
                        "verify": verify,
                    },
                    address_verification_autocomplete_params.AddressVerificationAutocompleteParams,
                ),
            ),
            cast_to=AddressVerificationAutocompleteResponse,
        )

    def batch_verification(
        self,
        *,
        addresses: Iterable[address_verification_batch_verification_params.Address],
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationBatchVerificationResponse:
        """Verify a batch of US or Canadian addresses in a single request.

        Each address can
        be freeform or structured, matching the same input formats accepted by the
        single verification endpoint.

        - Uses 1 lookup per address (plus 1 more per address if geocoding).
        - Requires a secret API key.
        - Returns results in the same order as the input addresses.
        - If an individual address fails, its result will contain an `error` field
          rather than a `verifiedAddress`.

        Args:
          addresses: Array of addresses to verify. Each item can be a freeform string or structured
              address object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/addver/verifications/batch",
            body=maybe_transform(
                {"addresses": addresses},
                address_verification_batch_verification_params.AddressVerificationBatchVerificationParams,
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
                    address_verification_batch_verification_params.AddressVerificationBatchVerificationParams,
                ),
            ),
            cast_to=AddressVerificationBatchVerificationResponse,
        )

    def get_autocomplete_previews(
        self,
        *,
        partial_street: str,
        city_filter: str | Omit = omit,
        country_filter: str | Omit = omit,
        filter_exact: bool | Omit = omit,
        limit: int | Omit = omit,
        pc_filter: str | Omit = omit,
        proper_case: bool | Omit = omit,
        prov_instead_of_pc: bool | Omit = omit,
        state_filter: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationGetAutocompletePreviewsResponse:
        """
        Returns address completion previews for a partial street address, suitable for
        populating an autocomplete dropdown without consuming a lookup per keystroke.

        Each result contains a partial address preview (street, city, and — for non-US
        addresses — only the first 3 digits of the postal code, to avoid revealing the
        full code before a lookup is charged).

        - Does not consume a lookup.
        - Use `POST /completions` to resolve a full address once the user selects a
          result.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "partial_street": partial_street,
                        "city_filter": city_filter,
                        "country_filter": country_filter,
                        "filter_exact": filter_exact,
                        "limit": limit,
                        "pc_filter": pc_filter,
                        "proper_case": proper_case,
                        "prov_instead_of_pc": prov_instead_of_pc,
                        "state_filter": state_filter,
                        "verified_only": verified_only,
                    },
                    address_verification_get_autocomplete_previews_params.AddressVerificationGetAutocompletePreviewsParams,
                ),
            ),
            cast_to=AddressVerificationGetAutocompletePreviewsResponse,
        )

    def get_lookup_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationGetLookupInfoResponse:
        """Returns your organization's current lookup usage and plan information.

        Useful
        for checking how many lookups you have consumed and whether you are on a paid
        plan.
        """
        return self._get(
            "/v1/addver/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationGetLookupInfoResponse,
        )

    def lookup_city_or_state_from_postal_or_zip_code(
        self,
        *,
        postal_or_zip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse:
        """
        Looks up city, county, and other location metadata for a given US or Canadian
        postal code or ZIP code.

        A single postal code may map to multiple cities (e.g. a ZIP that spans several
        towns), so the response is an array.

        - Uses 1 lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/addver/city_states",
            body=maybe_transform(
                {"postal_or_zip": postal_or_zip},
                address_verification_lookup_city_or_state_from_postal_or_zip_code_params.AddressVerificationLookupCityOrStateFromPostalOrZipCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse,
        )

    def lookup_zip_code_from_city_or_state(
        self,
        *,
        city: str,
        country_code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationLookupZipCodeFromCityOrStateResponse:
        """
        Looks up all ZIP codes that correspond to a given US city and state.

        - Currently only supported for US addresses (`countryCode: "US"`).
        - Uses 1 lookup.

        Args:
          city: The city name.

          country_code: The country code. Currently only `US` is supported.

          state: The state abbreviation (e.g. `NY`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/addver/zip_codes",
            body=maybe_transform(
                {
                    "city": city,
                    "country_code": country_code,
                    "state": state,
                },
                address_verification_lookup_zip_code_from_city_or_state_params.AddressVerificationLookupZipCodeFromCityOrStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationLookupZipCodeFromCityOrStateResponse,
        )

    def parse_an_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationParseAnAddressResponse:
        """
        Parses a freeform address string into its individual components (house number,
        street name, city, state, postal code, etc.).

        Useful for extracting structured data from a single-line address without running
        a full verification.

        - Uses 1 lookup.

        Args:
          address: The address you want to verify, written on a single line.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/addver/parses",
            body=maybe_transform(
                {"address": address},
                address_verification_parse_an_address_params.AddressVerificationParseAnAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationParseAnAddressResponse,
        )

    @overload
    def suggest_addresses(
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
    ) -> AddressVerificationSuggestAddressesResponse:
        """
        Returns up to 3 verified address suggestions for a given input address.

        Useful as a fallback when `POST /verifications` returns a `failed` status —
        suggestions represent the closest matches found and may help the user identify
        the correct address.

        Accepts the same freeform or structured input formats as `POST /verifications`.

        - Uses 1 lookup per call (plus 1 more if geocoding).

        Args:
          address: The address you want to verify, written on a single line.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def suggest_addresses(
        self,
        *,
        address: address_verification_suggest_addresses_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationSuggestAddressesResponse:
        """
        Returns up to 3 verified address suggestions for a given input address.

        Useful as a fallback when `POST /verifications` returns a `failed` status —
        suggestions represent the closest matches found and may help the user identify
        the correct address.

        Accepts the same freeform or structured input formats as `POST /verifications`.

        - Uses 1 lookup per call (plus 1 more if geocoding).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address"])
    def suggest_addresses(
        self,
        *,
        address: str | address_verification_suggest_addresses_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationSuggestAddressesResponse:
        return self._post(
            "/v1/addver/suggestions",
            body=maybe_transform(
                {"address": address},
                address_verification_suggest_addresses_params.AddressVerificationSuggestAddressesParams,
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
                    address_verification_suggest_addresses_params.AddressVerificationSuggestAddressesParams,
                ),
            ),
            cast_to=AddressVerificationSuggestAddressesResponse,
        )

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
    """Standard Address Verification API.

    Provides endpoints to verify and standardize addresses across US and Canada,
    supporting both structured and freeform inputs.

    Note that this uses a different set of lookups than our international API.
    """

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

    async def autocomplete(
        self,
        *,
        partial_street: str,
        filter_exact: bool | Omit = omit,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        index: int | Omit = omit,
        limit: int | Omit = omit,
        proper_case: bool | Omit = omit,
        query_verified_only: bool | Omit = omit,
        verify: bool | Omit = omit,
        city_filter: str | Omit = omit,
        country_filter: str | Omit = omit,
        pc_filter: str | Omit = omit,
        state_filter: str | Omit = omit,
        body_verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationAutocompleteResponse:
        """
        Resolves a partial street address into a list of full address candidates,
        optionally selecting a specific candidate by index and verifying it.

        **Basic usage** — omit `index`: returns an array of `CompletedAddressItem`
        results for the given `partialStreet`.

        **With `index`** — specify `index` to resolve a single candidate. Returns a
        single `CompletedAddressItem`.

        **With `index` + `verify=true`** — additionally runs the selected address
        through the USPS/Canada Post verifier and returns a `StandardVerifiedAddress`.

        - Uses 1 lookup per call (plus 1 more if geocoding a result).

        Args:
          partial_street: The partial street address to complete (e.g. `"22 Bay"`).

          city_filter: Filter results to a specific city.

          country_filter: Filter results to a specific country code.

          pc_filter: Filter results to a specific postal code prefix.

          state_filter: Filter results to a specific state or province abbreviation.

          body_verified_only: If true, only return addresses that passed USPS/Canada Post verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/addver/completions",
            body=await async_maybe_transform(
                {
                    "partial_street": partial_street,
                    "city_filter": city_filter,
                    "country_filter": country_filter,
                    "pc_filter": pc_filter,
                    "state_filter": state_filter,
                    "body_verified_only": body_verified_only,
                },
                address_verification_autocomplete_params.AddressVerificationAutocompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_exact": filter_exact,
                        "geocode": geocode,
                        "include_details": include_details,
                        "index": index,
                        "limit": limit,
                        "proper_case": proper_case,
                        "query_verified_only": query_verified_only,
                        "verify": verify,
                    },
                    address_verification_autocomplete_params.AddressVerificationAutocompleteParams,
                ),
            ),
            cast_to=AddressVerificationAutocompleteResponse,
        )

    async def batch_verification(
        self,
        *,
        addresses: Iterable[address_verification_batch_verification_params.Address],
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationBatchVerificationResponse:
        """Verify a batch of US or Canadian addresses in a single request.

        Each address can
        be freeform or structured, matching the same input formats accepted by the
        single verification endpoint.

        - Uses 1 lookup per address (plus 1 more per address if geocoding).
        - Requires a secret API key.
        - Returns results in the same order as the input addresses.
        - If an individual address fails, its result will contain an `error` field
          rather than a `verifiedAddress`.

        Args:
          addresses: Array of addresses to verify. Each item can be a freeform string or structured
              address object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/addver/verifications/batch",
            body=await async_maybe_transform(
                {"addresses": addresses},
                address_verification_batch_verification_params.AddressVerificationBatchVerificationParams,
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
                    address_verification_batch_verification_params.AddressVerificationBatchVerificationParams,
                ),
            ),
            cast_to=AddressVerificationBatchVerificationResponse,
        )

    async def get_autocomplete_previews(
        self,
        *,
        partial_street: str,
        city_filter: str | Omit = omit,
        country_filter: str | Omit = omit,
        filter_exact: bool | Omit = omit,
        limit: int | Omit = omit,
        pc_filter: str | Omit = omit,
        proper_case: bool | Omit = omit,
        prov_instead_of_pc: bool | Omit = omit,
        state_filter: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationGetAutocompletePreviewsResponse:
        """
        Returns address completion previews for a partial street address, suitable for
        populating an autocomplete dropdown without consuming a lookup per keystroke.

        Each result contains a partial address preview (street, city, and — for non-US
        addresses — only the first 3 digits of the postal code, to avoid revealing the
        full code before a lookup is charged).

        - Does not consume a lookup.
        - Use `POST /completions` to resolve a full address once the user selects a
          result.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/addver/completions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "partial_street": partial_street,
                        "city_filter": city_filter,
                        "country_filter": country_filter,
                        "filter_exact": filter_exact,
                        "limit": limit,
                        "pc_filter": pc_filter,
                        "proper_case": proper_case,
                        "prov_instead_of_pc": prov_instead_of_pc,
                        "state_filter": state_filter,
                        "verified_only": verified_only,
                    },
                    address_verification_get_autocomplete_previews_params.AddressVerificationGetAutocompletePreviewsParams,
                ),
            ),
            cast_to=AddressVerificationGetAutocompletePreviewsResponse,
        )

    async def get_lookup_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationGetLookupInfoResponse:
        """Returns your organization's current lookup usage and plan information.

        Useful
        for checking how many lookups you have consumed and whether you are on a paid
        plan.
        """
        return await self._get(
            "/v1/addver/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationGetLookupInfoResponse,
        )

    async def lookup_city_or_state_from_postal_or_zip_code(
        self,
        *,
        postal_or_zip: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse:
        """
        Looks up city, county, and other location metadata for a given US or Canadian
        postal code or ZIP code.

        A single postal code may map to multiple cities (e.g. a ZIP that spans several
        towns), so the response is an array.

        - Uses 1 lookup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/addver/city_states",
            body=await async_maybe_transform(
                {"postal_or_zip": postal_or_zip},
                address_verification_lookup_city_or_state_from_postal_or_zip_code_params.AddressVerificationLookupCityOrStateFromPostalOrZipCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse,
        )

    async def lookup_zip_code_from_city_or_state(
        self,
        *,
        city: str,
        country_code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationLookupZipCodeFromCityOrStateResponse:
        """
        Looks up all ZIP codes that correspond to a given US city and state.

        - Currently only supported for US addresses (`countryCode: "US"`).
        - Uses 1 lookup.

        Args:
          city: The city name.

          country_code: The country code. Currently only `US` is supported.

          state: The state abbreviation (e.g. `NY`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/addver/zip_codes",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "country_code": country_code,
                    "state": state,
                },
                address_verification_lookup_zip_code_from_city_or_state_params.AddressVerificationLookupZipCodeFromCityOrStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationLookupZipCodeFromCityOrStateResponse,
        )

    async def parse_an_address(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationParseAnAddressResponse:
        """
        Parses a freeform address string into its individual components (house number,
        street name, city, state, postal code, etc.).

        Useful for extracting structured data from a single-line address without running
        a full verification.

        - Uses 1 lookup.

        Args:
          address: The address you want to verify, written on a single line.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/addver/parses",
            body=await async_maybe_transform(
                {"address": address},
                address_verification_parse_an_address_params.AddressVerificationParseAnAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressVerificationParseAnAddressResponse,
        )

    @overload
    async def suggest_addresses(
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
    ) -> AddressVerificationSuggestAddressesResponse:
        """
        Returns up to 3 verified address suggestions for a given input address.

        Useful as a fallback when `POST /verifications` returns a `failed` status —
        suggestions represent the closest matches found and may help the user identify
        the correct address.

        Accepts the same freeform or structured input formats as `POST /verifications`.

        - Uses 1 lookup per call (plus 1 more if geocoding).

        Args:
          address: The address you want to verify, written on a single line.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def suggest_addresses(
        self,
        *,
        address: address_verification_suggest_addresses_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationSuggestAddressesResponse:
        """
        Returns up to 3 verified address suggestions for a given input address.

        Useful as a fallback when `POST /verifications` returns a `failed` status —
        suggestions represent the closest matches found and may help the user identify
        the correct address.

        Accepts the same freeform or structured input formats as `POST /verifications`.

        - Uses 1 lookup per call (plus 1 more if geocoding).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address"])
    async def suggest_addresses(
        self,
        *,
        address: str | address_verification_suggest_addresses_params.StandardStructuredAddressInputAddress,
        geocode: bool | Omit = omit,
        include_details: bool | Omit = omit,
        proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressVerificationSuggestAddressesResponse:
        return await self._post(
            "/v1/addver/suggestions",
            body=await async_maybe_transform(
                {"address": address},
                address_verification_suggest_addresses_params.AddressVerificationSuggestAddressesParams,
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
                    address_verification_suggest_addresses_params.AddressVerificationSuggestAddressesParams,
                ),
            ),
            cast_to=AddressVerificationSuggestAddressesResponse,
        )

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

        self.autocomplete = to_raw_response_wrapper(
            address_verification.autocomplete,
        )
        self.batch_verification = to_raw_response_wrapper(
            address_verification.batch_verification,
        )
        self.get_autocomplete_previews = to_raw_response_wrapper(
            address_verification.get_autocomplete_previews,
        )
        self.get_lookup_info = to_raw_response_wrapper(
            address_verification.get_lookup_info,
        )
        self.lookup_city_or_state_from_postal_or_zip_code = to_raw_response_wrapper(
            address_verification.lookup_city_or_state_from_postal_or_zip_code,
        )
        self.lookup_zip_code_from_city_or_state = to_raw_response_wrapper(
            address_verification.lookup_zip_code_from_city_or_state,
        )
        self.parse_an_address = to_raw_response_wrapper(
            address_verification.parse_an_address,
        )
        self.suggest_addresses = to_raw_response_wrapper(
            address_verification.suggest_addresses,
        )
        self.verify = to_raw_response_wrapper(
            address_verification.verify,
        )


class AsyncAddressVerificationResourceWithRawResponse:
    def __init__(self, address_verification: AsyncAddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.autocomplete = async_to_raw_response_wrapper(
            address_verification.autocomplete,
        )
        self.batch_verification = async_to_raw_response_wrapper(
            address_verification.batch_verification,
        )
        self.get_autocomplete_previews = async_to_raw_response_wrapper(
            address_verification.get_autocomplete_previews,
        )
        self.get_lookup_info = async_to_raw_response_wrapper(
            address_verification.get_lookup_info,
        )
        self.lookup_city_or_state_from_postal_or_zip_code = async_to_raw_response_wrapper(
            address_verification.lookup_city_or_state_from_postal_or_zip_code,
        )
        self.lookup_zip_code_from_city_or_state = async_to_raw_response_wrapper(
            address_verification.lookup_zip_code_from_city_or_state,
        )
        self.parse_an_address = async_to_raw_response_wrapper(
            address_verification.parse_an_address,
        )
        self.suggest_addresses = async_to_raw_response_wrapper(
            address_verification.suggest_addresses,
        )
        self.verify = async_to_raw_response_wrapper(
            address_verification.verify,
        )


class AddressVerificationResourceWithStreamingResponse:
    def __init__(self, address_verification: AddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.autocomplete = to_streamed_response_wrapper(
            address_verification.autocomplete,
        )
        self.batch_verification = to_streamed_response_wrapper(
            address_verification.batch_verification,
        )
        self.get_autocomplete_previews = to_streamed_response_wrapper(
            address_verification.get_autocomplete_previews,
        )
        self.get_lookup_info = to_streamed_response_wrapper(
            address_verification.get_lookup_info,
        )
        self.lookup_city_or_state_from_postal_or_zip_code = to_streamed_response_wrapper(
            address_verification.lookup_city_or_state_from_postal_or_zip_code,
        )
        self.lookup_zip_code_from_city_or_state = to_streamed_response_wrapper(
            address_verification.lookup_zip_code_from_city_or_state,
        )
        self.parse_an_address = to_streamed_response_wrapper(
            address_verification.parse_an_address,
        )
        self.suggest_addresses = to_streamed_response_wrapper(
            address_verification.suggest_addresses,
        )
        self.verify = to_streamed_response_wrapper(
            address_verification.verify,
        )


class AsyncAddressVerificationResourceWithStreamingResponse:
    def __init__(self, address_verification: AsyncAddressVerificationResource) -> None:
        self._address_verification = address_verification

        self.autocomplete = async_to_streamed_response_wrapper(
            address_verification.autocomplete,
        )
        self.batch_verification = async_to_streamed_response_wrapper(
            address_verification.batch_verification,
        )
        self.get_autocomplete_previews = async_to_streamed_response_wrapper(
            address_verification.get_autocomplete_previews,
        )
        self.get_lookup_info = async_to_streamed_response_wrapper(
            address_verification.get_lookup_info,
        )
        self.lookup_city_or_state_from_postal_or_zip_code = async_to_streamed_response_wrapper(
            address_verification.lookup_city_or_state_from_postal_or_zip_code,
        )
        self.lookup_zip_code_from_city_or_state = async_to_streamed_response_wrapper(
            address_verification.lookup_zip_code_from_city_or_state,
        )
        self.parse_an_address = async_to_streamed_response_wrapper(
            address_verification.parse_an_address,
        )
        self.suggest_addresses = async_to_streamed_response_wrapper(
            address_verification.suggest_addresses,
        )
        self.verify = async_to_streamed_response_wrapper(
            address_verification.verify,
        )
