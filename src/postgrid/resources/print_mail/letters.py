# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
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
    LetterSize,
    AddressPlacement,
    letter_list_params,
    letter_create_params,
)
from ...types.print_mail.letter import Letter
from ...types.print_mail.letter_size import LetterSize
from ...types.print_mail.address_placement import AddressPlacement
from ...types.print_mail.attached_pdf_param import AttachedPdfParam
from ...types.print_mail.plastic_card_param import PlasticCardParam
from ...types.print_mail.letter_retrieve_url_response import LetterRetrieveURLResponse

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

    @overload
    def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithHTMLFrom,
        html: str,
        to: letter_create_params.LetterCreateWithHTMLTo,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          html: The HTML content for the letter. You can supply _either_ this or `template` but
              not both.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Indicates if the letter is in color.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          double_sided: Indicates if the letter is double-sided.

          envelope: The envelope (ID) for the letter. You can either specify a custom envelope ID or
              use the default `standard` envelope.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          perforated_page: If specified, indicates which letter page is perforated. Currently, only the
              first page can be perforated.

          plastic_card: Model representing a plastic card.

          return_envelope: The return envelope (ID) sent out with the letter, if any.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported letter sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          template: The template ID for the letter. You can supply _either_ this or `html` but not
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithPdfFrom,
        pdf: str,
        to: letter_create_params.LetterCreateWithPdfTo,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A URL pointing to a PDF file for the letter or the PDF file itself.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Indicates if the letter is in color.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          double_sided: Indicates if the letter is double-sided.

          envelope: The envelope (ID) for the letter. You can either specify a custom envelope ID or
              use the default `standard` envelope.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          perforated_page: If specified, indicates which letter page is perforated. Currently, only the
              first page can be perforated.

          plastic_card: Model representing a plastic card.

          return_envelope: The return envelope (ID) sent out with the letter, if any.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported letter sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["from_", "html", "to"], ["template"], ["from_", "pdf", "to"])
    def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithHTMLFrom
        | letter_create_params.LetterCreateWithPdfFrom
        | Omit = omit,
        html: str | Omit = omit,
        to: letter_create_params.LetterCreateWithHTMLTo | letter_create_params.LetterCreateWithPdfTo | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        return self._post(
            "/print-mail/v1/letters",
            body=maybe_transform(
                {
                    "from_": from_,
                    "html": html,
                    "to": to,
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "perforated_page": perforated_page,
                    "plastic_card": plastic_card,
                    "return_envelope": return_envelope,
                    "send_date": send_date,
                    "size": size,
                    "template": template,
                    "pdf": pdf,
                },
                letter_create_params.LetterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
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
    ) -> Letter:
        """
        Retrieve a letter by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
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
    ) -> SyncSkipLimit[Letter]:
        """
        Get a list of letters.

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
            "/print-mail/v1/letters",
            page=SyncSkipLimit[Letter],
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
            model=Letter,
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
    ) -> Letter:
        """Cancel a letter by ID.

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
            f"/print-mail/v1/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
        )

    def retrieve_url(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterRetrieveURLResponse:
        """
        Retrieve a letter preview URL.

        This is only available for customers with our document management addon, which
        offers document generation and hosting capabilities. This endpoint has a much
        higher rate limit than the regular order retrieval endpoint, so it is suitable
        for customer-facing use-cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/letters/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LetterRetrieveURLResponse,
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

    @overload
    async def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithHTMLFrom,
        html: str,
        to: letter_create_params.LetterCreateWithHTMLTo,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          html: The HTML content for the letter. You can supply _either_ this or `template` but
              not both.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Indicates if the letter is in color.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          double_sided: Indicates if the letter is double-sided.

          envelope: The envelope (ID) for the letter. You can either specify a custom envelope ID or
              use the default `standard` envelope.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          perforated_page: If specified, indicates which letter page is perforated. Currently, only the
              first page can be perforated.

          plastic_card: Model representing a plastic card.

          return_envelope: The return envelope (ID) sent out with the letter, if any.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported letter sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          template: The template ID for the letter. You can supply _either_ this or `html` but not
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithPdfFrom,
        pdf: str,
        to: letter_create_params.LetterCreateWithPdfTo,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        """Create a letter.

        Note that you can supply one of the following:

        - HTML content for the letter
        - A template ID for the letter
        - A URL or file for a PDF for the letter
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A URL pointing to a PDF file for the letter or the PDF file itself.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          address_placement: Enum representing the placement of the address on the letter.

          attached_pdf: Model representing an attached PDF.

          color: Indicates if the letter is in color.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          double_sided: Indicates if the letter is double-sided.

          envelope: The envelope (ID) for the letter. You can either specify a custom envelope ID or
              use the default `standard` envelope.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          perforated_page: If specified, indicates which letter page is perforated. Currently, only the
              first page can be perforated.

          plastic_card: Model representing a plastic card.

          return_envelope: The return envelope (ID) sent out with the letter, if any.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported letter sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["from_", "html", "to"], ["template"], ["from_", "pdf", "to"])
    async def create(
        self,
        *,
        from_: letter_create_params.LetterCreateWithHTMLFrom
        | letter_create_params.LetterCreateWithPdfFrom
        | Omit = omit,
        html: str | Omit = omit,
        to: letter_create_params.LetterCreateWithHTMLTo | letter_create_params.LetterCreateWithPdfTo | Omit = omit,
        address_placement: AddressPlacement | Omit = omit,
        attached_pdf: AttachedPdfParam | Omit = omit,
        color: bool | Omit = omit,
        description: str | Omit = omit,
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
        merge_variables: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        perforated_page: Literal[1] | Omit = omit,
        plastic_card: PlasticCardParam | Omit = omit,
        return_envelope: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        size: LetterSize | Omit = omit,
        template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Letter:
        return await self._post(
            "/print-mail/v1/letters",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "html": html,
                    "to": to,
                    "address_placement": address_placement,
                    "attached_pdf": attached_pdf,
                    "color": color,
                    "description": description,
                    "double_sided": double_sided,
                    "envelope": envelope,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "perforated_page": perforated_page,
                    "plastic_card": plastic_card,
                    "return_envelope": return_envelope,
                    "send_date": send_date,
                    "size": size,
                    "template": template,
                    "pdf": pdf,
                },
                letter_create_params.LetterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
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
    ) -> Letter:
        """
        Retrieve a letter by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
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
    ) -> AsyncPaginator[Letter, AsyncSkipLimit[Letter]]:
        """
        Get a list of letters.

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
            "/print-mail/v1/letters",
            page=AsyncSkipLimit[Letter],
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
            model=Letter,
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
    ) -> Letter:
        """Cancel a letter by ID.

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
            f"/print-mail/v1/letters/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Letter,
        )

    async def retrieve_url(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LetterRetrieveURLResponse:
        """
        Retrieve a letter preview URL.

        This is only available for customers with our document management addon, which
        offers document generation and hosting capabilities. This endpoint has a much
        higher rate limit than the regular order retrieval endpoint, so it is suitable
        for customer-facing use-cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/letters/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LetterRetrieveURLResponse,
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
        self.list = to_raw_response_wrapper(
            letters.list,
        )
        self.delete = to_raw_response_wrapper(
            letters.delete,
        )
        self.retrieve_url = to_raw_response_wrapper(
            letters.retrieve_url,
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
        self.list = async_to_raw_response_wrapper(
            letters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            letters.delete,
        )
        self.retrieve_url = async_to_raw_response_wrapper(
            letters.retrieve_url,
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
        self.list = to_streamed_response_wrapper(
            letters.list,
        )
        self.delete = to_streamed_response_wrapper(
            letters.delete,
        )
        self.retrieve_url = to_streamed_response_wrapper(
            letters.retrieve_url,
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
        self.list = async_to_streamed_response_wrapper(
            letters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            letters.delete,
        )
        self.retrieve_url = async_to_streamed_response_wrapper(
            letters.retrieve_url,
        )
