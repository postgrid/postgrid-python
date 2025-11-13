# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.print_mail import LetterSize, AddressPlacement
from ....types.print_mail.letter_size import LetterSize
from ....types.print_mail.order_profiles import (
    letter_list_params,
    letter_create_params,
    letter_update_params,
    letter_retrieve_params,
)
from ....types.print_mail.address_placement import AddressPlacement
from ....types.print_mail.attached_pdf_param import AttachedPdfParam
from ....types.print_mail.order_profiles.letter_profile import LetterProfile
from ....types.print_mail.order_profiles.letter_delete_response import LetterDeleteResponse

__all__ = ["LettersResource", "AsyncLettersResource"]


class LettersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LettersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return LettersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LettersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return LettersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        size: LetterSize,
        expand: SequenceNotStr[str] | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        double_sided: bool | Omit = omit,
        envelope: str | Omit = omit,
        mailing_class: Literal[
            "first_class",
            "standard_class",
            "express",
            "certified",
            "certified_return_receipt",
            "registered",
            "usps_first_class",
            "usps_standard_class",
            "usps_eddm",
            "usps_express_2_day",
            "usps_express_3_day",
            "usps_first_class_certified",
            "usps_first_class_certified_return_receipt",
            "usps_first_class_registered",
            "usps_express_3_day_signature_confirmation",
            "usps_express_3_day_certified",
            "usps_express_3_day_certified_return_receipt",
            "ca_post_lettermail",
            "ca_post_personalized",
            "ca_post_neighbourhood_mail",
            "ups_express_overnight",
            "ups_express_2_day",
            "ups_express_3_day",
            "royal_mail_first_class",
            "royal_mail_second_class",
            "au_post_second_class",
        ]
        | Omit = omit,
        merge_variables: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        pdf: str | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        return_envelope: str | Omit = omit,
        template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """Creates a new Letter Profile.

        You must provide either a `template` ID or upload
        a `pdf` file for the content. If providing PDF files (`pdf` or
        `attachedPDFFile`), the request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported letter sizes.

          expand: Optional list of related resources to expand in the response.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Specifies whether to print in color (true) or black and white (false).

          description: An optional description for the profile. Set to `null` to remove during update.

          double_sided: Specifies whether to print on both sides of the paper.

          envelope: ID of a custom envelope to use.

          mailing_class: Mailing class.

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A PDF file containing the letter content. Cannot be used with `template`.

          perforated_page: Specifies which page number should be perforated (if any).

          return_envelope: ID of a return envelope to include.

          template: ID of a template to use for the letter content. Cannot be used with `pdf`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/order_profiles/letters",
            body=maybe_transform(
                {
                    "size": size,
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                    "perforated_page": perforated_page,
                    "return_envelope": return_envelope,
                    "template": template,
                },
                letter_create_params.LetterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, letter_create_params.LetterCreateParams),
            ),
            cast_to=LetterProfile,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """
        Retrieves the details of a specific Letter Profile by its ID.

        Args:
          expand: Optional list of related resources to expand in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/order_profiles/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, letter_retrieve_params.LetterRetrieveParams),
            ),
            cast_to=LetterProfile,
        )

    def update(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        double_sided: bool | Omit = omit,
        envelope: str | Omit = omit,
        mailing_class: Literal[
            "first_class",
            "standard_class",
            "express",
            "certified",
            "certified_return_receipt",
            "registered",
            "usps_first_class",
            "usps_standard_class",
            "usps_eddm",
            "usps_express_2_day",
            "usps_express_3_day",
            "usps_first_class_certified",
            "usps_first_class_certified_return_receipt",
            "usps_first_class_registered",
            "usps_express_3_day_signature_confirmation",
            "usps_express_3_day_certified",
            "usps_express_3_day_certified_return_receipt",
            "ca_post_lettermail",
            "ca_post_personalized",
            "ca_post_neighbourhood_mail",
            "ups_express_overnight",
            "ups_express_2_day",
            "ups_express_3_day",
            "royal_mail_first_class",
            "royal_mail_second_class",
            "au_post_second_class",
        ]
        | Omit = omit,
        merge_variables: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        pdf: str | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        return_envelope: str | Omit = omit,
        template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """Updates specific fields of an existing Letter Profile.

        Only the fields provided
        in the request body will be updated. If providing PDF files (`pdf` or
        `attachedPDFFile`), the request `Content-Type` must be `multipart/form-data`.

        Args:
          expand: Optional list of related resources to expand in the response.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Specifies whether to print in color (true) or black and white (false).

          description: An optional description for the profile. Set to `null` to remove during update.

          double_sided: Specifies whether to print on both sides of the paper.

          envelope: ID of a custom envelope to use.

          mailing_class: Mailing class.

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A PDF file containing the letter content. Cannot be used with `template`.

          perforated_page: Specifies which page number should be perforated (if any).

          return_envelope: ID of a return envelope to include.

          template: ID of a template to use for the letter content. Cannot be used with `pdf`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/order_profiles/letters/{id}",
            body=maybe_transform(
                {
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                    "perforated_page": perforated_page,
                    "return_envelope": return_envelope,
                    "template": template,
                },
                letter_update_params.LetterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, letter_update_params.LetterUpdateParams),
            ),
            cast_to=LetterProfile,
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
    ) -> SyncSkipLimit[LetterProfile]:
        """Retrieves a list of Letter Profiles.

        The profiles are returned sorted by
        creation date, with the most recent appearing first.

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
            "/print-mail/v1/order_profiles/letters",
            page=SyncSkipLimit[LetterProfile],
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
                    letter_list_params.LetterListParams,
                ),
            ),
            model=LetterProfile,
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
    ) -> LetterDeleteResponse:
        """Deletes a Letter Profile.

        This action cannot be undone. Orders previously
        created using this profile are not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/order_profiles/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LetterDeleteResponse,
        )


class AsyncLettersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLettersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLettersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLettersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncLettersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        size: LetterSize,
        expand: SequenceNotStr[str] | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        double_sided: bool | Omit = omit,
        envelope: str | Omit = omit,
        mailing_class: Literal[
            "first_class",
            "standard_class",
            "express",
            "certified",
            "certified_return_receipt",
            "registered",
            "usps_first_class",
            "usps_standard_class",
            "usps_eddm",
            "usps_express_2_day",
            "usps_express_3_day",
            "usps_first_class_certified",
            "usps_first_class_certified_return_receipt",
            "usps_first_class_registered",
            "usps_express_3_day_signature_confirmation",
            "usps_express_3_day_certified",
            "usps_express_3_day_certified_return_receipt",
            "ca_post_lettermail",
            "ca_post_personalized",
            "ca_post_neighbourhood_mail",
            "ups_express_overnight",
            "ups_express_2_day",
            "ups_express_3_day",
            "royal_mail_first_class",
            "royal_mail_second_class",
            "au_post_second_class",
        ]
        | Omit = omit,
        merge_variables: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        pdf: str | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        return_envelope: str | Omit = omit,
        template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """Creates a new Letter Profile.

        You must provide either a `template` ID or upload
        a `pdf` file for the content. If providing PDF files (`pdf` or
        `attachedPDFFile`), the request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported letter sizes.

          expand: Optional list of related resources to expand in the response.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Specifies whether to print in color (true) or black and white (false).

          description: An optional description for the profile. Set to `null` to remove during update.

          double_sided: Specifies whether to print on both sides of the paper.

          envelope: ID of a custom envelope to use.

          mailing_class: Mailing class.

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A PDF file containing the letter content. Cannot be used with `template`.

          perforated_page: Specifies which page number should be perforated (if any).

          return_envelope: ID of a return envelope to include.

          template: ID of a template to use for the letter content. Cannot be used with `pdf`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/order_profiles/letters",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                    "perforated_page": perforated_page,
                    "return_envelope": return_envelope,
                    "template": template,
                },
                letter_create_params.LetterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, letter_create_params.LetterCreateParams),
            ),
            cast_to=LetterProfile,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """
        Retrieves the details of a specific Letter Profile by its ID.

        Args:
          expand: Optional list of related resources to expand in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/order_profiles/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, letter_retrieve_params.LetterRetrieveParams),
            ),
            cast_to=LetterProfile,
        )

    async def update(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: Optional[str] | Omit = omit,
        double_sided: bool | Omit = omit,
        envelope: str | Omit = omit,
        mailing_class: Literal[
            "first_class",
            "standard_class",
            "express",
            "certified",
            "certified_return_receipt",
            "registered",
            "usps_first_class",
            "usps_standard_class",
            "usps_eddm",
            "usps_express_2_day",
            "usps_express_3_day",
            "usps_first_class_certified",
            "usps_first_class_certified_return_receipt",
            "usps_first_class_registered",
            "usps_express_3_day_signature_confirmation",
            "usps_express_3_day_certified",
            "usps_express_3_day_certified_return_receipt",
            "ca_post_lettermail",
            "ca_post_personalized",
            "ca_post_neighbourhood_mail",
            "ups_express_overnight",
            "ups_express_2_day",
            "ups_express_3_day",
            "royal_mail_first_class",
            "royal_mail_second_class",
            "au_post_second_class",
        ]
        | Omit = omit,
        merge_variables: Optional[Dict[str, object]] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        pdf: str | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        return_envelope: str | Omit = omit,
        template: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterProfile:
        """Updates specific fields of an existing Letter Profile.

        Only the fields provided
        in the request body will be updated. If providing PDF files (`pdf` or
        `attachedPDFFile`), the request `Content-Type` must be `multipart/form-data`.

        Args:
          expand: Optional list of related resources to expand in the response.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Specifies whether to print in color (true) or black and white (false).

          description: An optional description for the profile. Set to `null` to remove during update.

          double_sided: Specifies whether to print on both sides of the paper.

          envelope: ID of a custom envelope to use.

          mailing_class: Mailing class.

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A PDF file containing the letter content. Cannot be used with `template`.

          perforated_page: Specifies which page number should be perforated (if any).

          return_envelope: ID of a return envelope to include.

          template: ID of a template to use for the letter content. Cannot be used with `pdf`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/order_profiles/letters/{id}",
            body=await async_maybe_transform(
                {
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                    "perforated_page": perforated_page,
                    "return_envelope": return_envelope,
                    "template": template,
                },
                letter_update_params.LetterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, letter_update_params.LetterUpdateParams),
            ),
            cast_to=LetterProfile,
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
    ) -> AsyncPaginator[LetterProfile, AsyncSkipLimit[LetterProfile]]:
        """Retrieves a list of Letter Profiles.

        The profiles are returned sorted by
        creation date, with the most recent appearing first.

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
            "/print-mail/v1/order_profiles/letters",
            page=AsyncSkipLimit[LetterProfile],
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
                    letter_list_params.LetterListParams,
                ),
            ),
            model=LetterProfile,
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
    ) -> LetterDeleteResponse:
        """Deletes a Letter Profile.

        This action cannot be undone. Orders previously
        created using this profile are not affected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/order_profiles/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LetterDeleteResponse,
        )


class LettersResourceWithRawResponse:
    def __init__(self, letters: LettersResource) -> None:
        self._letters = letters

        self.create = to_raw_response_wrapper(
            letters.create,
        )
        self.retrieve = to_raw_response_wrapper(
            letters.retrieve,
        )
        self.update = to_raw_response_wrapper(
            letters.update,
        )
        self.list = to_raw_response_wrapper(
            letters.list,
        )
        self.delete = to_raw_response_wrapper(
            letters.delete,
        )


class AsyncLettersResourceWithRawResponse:
    def __init__(self, letters: AsyncLettersResource) -> None:
        self._letters = letters

        self.create = async_to_raw_response_wrapper(
            letters.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            letters.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            letters.update,
        )
        self.list = async_to_raw_response_wrapper(
            letters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            letters.delete,
        )


class LettersResourceWithStreamingResponse:
    def __init__(self, letters: LettersResource) -> None:
        self._letters = letters

        self.create = to_streamed_response_wrapper(
            letters.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            letters.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            letters.update,
        )
        self.list = to_streamed_response_wrapper(
            letters.list,
        )
        self.delete = to_streamed_response_wrapper(
            letters.delete,
        )


class AsyncLettersResourceWithStreamingResponse:
    def __init__(self, letters: AsyncLettersResource) -> None:
        self._letters = letters

        self.create = async_to_streamed_response_wrapper(
            letters.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            letters.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            letters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            letters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            letters.delete,
        )
