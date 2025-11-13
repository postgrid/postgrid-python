# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
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
from ...types.print_mail import self_mailer_list_params, self_mailer_create_params
from ...types.print_mail.self_mailer import SelfMailer
from ...types.print_mail.order_profiles import SelfMailerSize
from ...types.print_mail.order_profiles.self_mailer_size import SelfMailerSize
from ...types.print_mail.self_mailer_retrieve_url_response import SelfMailerRetrieveURLResponse

__all__ = ["SelfMailersResource", "AsyncSelfMailersResource"]


class SelfMailersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SelfMailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return SelfMailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelfMailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return SelfMailersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        from_: self_mailer_create_params.SelfMailerCreateWithHTMLFrom,
        inside_html: str,
        outside_html: str,
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithHTMLTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          inside_html: The HTML content for the inside of the self-mailer. You can supply _either_ this
              or `insideTemplate` but not both.

          outside_html: The HTML content for the outside of the self-mailer. You can supply _either_
              this or `outsideTemplate` but not both.

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

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
        inside_template: str,
        outside_template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          inside_template: The template ID for the inside of the self-mailer. You can supply _either_ this
              or `insideHTML` but not both.

          outside_template: The template ID for the outside of the self-mailer. You can supply _either_ this
              or `outsideHTML` but not both.

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
        from_: self_mailer_create_params.SelfMailerCreateWithPdfurlFrom,
        pdf: str,
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithPdfurlTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A URL pointing to a 2 page PDF file. The first page is the inside of the
              self-mailer and the second page is the outside (where the address will be
              stamped on).

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

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
        from_: self_mailer_create_params.SelfMailerCreateWithPdfFileFrom,
        pdf: Union[str, Base64FileInput],
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithPdfFileTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A 2 page PDF file. The first page is the inside of the self-mailer and the
              second page is the outside (where the address will be stamped on).

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["from_", "inside_html", "outside_html", "size", "to"],
        ["inside_template", "outside_template"],
        ["from_", "pdf", "size", "to"],
    )
    def create(
        self,
        *,
        from_: self_mailer_create_params.SelfMailerCreateWithHTMLFrom
        | self_mailer_create_params.SelfMailerCreateWithPdfurlFrom
        | self_mailer_create_params.SelfMailerCreateWithPdfFileFrom
        | Omit = omit,
        inside_html: str | Omit = omit,
        outside_html: str | Omit = omit,
        size: SelfMailerSize | Omit = omit,
        to: self_mailer_create_params.SelfMailerCreateWithHTMLTo
        | self_mailer_create_params.SelfMailerCreateWithPdfurlTo
        | self_mailer_create_params.SelfMailerCreateWithPdfFileTo
        | Omit = omit,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        inside_template: str | Omit = omit,
        outside_template: str | Omit = omit,
        pdf: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        return self._post(
            "/print-mail/v1/self_mailers",
            body=maybe_transform(
                {
                    "from_": from_,
                    "inside_html": inside_html,
                    "outside_html": outside_html,
                    "size": size,
                    "to": to,
                    "description": description,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                    "inside_template": inside_template,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_create_params.SelfMailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> SelfMailer:
        """
        Retrieve a self-mailer by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> SyncSkipLimit[SelfMailer]:
        """
        Get a list of self-mailers.

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
            "/print-mail/v1/self_mailers",
            page=SyncSkipLimit[SelfMailer],
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
                    self_mailer_list_params.SelfMailerListParams,
                ),
            ),
            model=SelfMailer,
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
    ) -> SelfMailer:
        """Cancel a self-mailer by ID.

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
            f"/print-mail/v1/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> SelfMailerRetrieveURLResponse:
        """
        Retrieve a self-mailer preview URL.

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
            f"/print-mail/v1/self_mailers/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailerRetrieveURLResponse,
        )


class AsyncSelfMailersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSelfMailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSelfMailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelfMailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncSelfMailersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        from_: self_mailer_create_params.SelfMailerCreateWithHTMLFrom,
        inside_html: str,
        outside_html: str,
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithHTMLTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          inside_html: The HTML content for the inside of the self-mailer. You can supply _either_ this
              or `insideTemplate` but not both.

          outside_html: The HTML content for the outside of the self-mailer. You can supply _either_
              this or `outsideTemplate` but not both.

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

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
        inside_template: str,
        outside_template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          inside_template: The template ID for the inside of the self-mailer. You can supply _either_ this
              or `insideHTML` but not both.

          outside_template: The template ID for the outside of the self-mailer. You can supply _either_ this
              or `outsideHTML` but not both.

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
        from_: self_mailer_create_params.SelfMailerCreateWithPdfurlFrom,
        pdf: str,
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithPdfurlTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A URL pointing to a 2 page PDF file. The first page is the inside of the
              self-mailer and the second page is the outside (where the address will be
              stamped on).

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

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
        from_: self_mailer_create_params.SelfMailerCreateWithPdfFileFrom,
        pdf: Union[str, Base64FileInput],
        size: SelfMailerSize,
        to: self_mailer_create_params.SelfMailerCreateWithPdfFileTo,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        """Create a self-mailer.

        Note that you can supply one of the following:

        - HTML content for the inside and outside of the self-mailer
        - A template ID for the inside and outside of the self-mailer
        - A URL or file for a 2 page PDF where the first page is the outside of the
          self-mailer and the second page is the inside
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          pdf: A 2 page PDF file. The first page is the inside of the self-mailer and the
              second page is the outside (where the address will be stamped on).

          size: Enum representing the supported self-mailer sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          metadata: See the section on Metadata.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["from_", "inside_html", "outside_html", "size", "to"],
        ["inside_template", "outside_template"],
        ["from_", "pdf", "size", "to"],
    )
    async def create(
        self,
        *,
        from_: self_mailer_create_params.SelfMailerCreateWithHTMLFrom
        | self_mailer_create_params.SelfMailerCreateWithPdfurlFrom
        | self_mailer_create_params.SelfMailerCreateWithPdfFileFrom
        | Omit = omit,
        inside_html: str | Omit = omit,
        outside_html: str | Omit = omit,
        size: SelfMailerSize | Omit = omit,
        to: self_mailer_create_params.SelfMailerCreateWithHTMLTo
        | self_mailer_create_params.SelfMailerCreateWithPdfurlTo
        | self_mailer_create_params.SelfMailerCreateWithPdfFileTo
        | Omit = omit,
        description: str | Omit = omit,
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
        send_date: Union[str, datetime] | Omit = omit,
        inside_template: str | Omit = omit,
        outside_template: str | Omit = omit,
        pdf: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailer:
        return await self._post(
            "/print-mail/v1/self_mailers",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "inside_html": inside_html,
                    "outside_html": outside_html,
                    "size": size,
                    "to": to,
                    "description": description,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                    "inside_template": inside_template,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_create_params.SelfMailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> SelfMailer:
        """
        Retrieve a self-mailer by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> AsyncPaginator[SelfMailer, AsyncSkipLimit[SelfMailer]]:
        """
        Get a list of self-mailers.

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
            "/print-mail/v1/self_mailers",
            page=AsyncSkipLimit[SelfMailer],
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
                    self_mailer_list_params.SelfMailerListParams,
                ),
            ),
            model=SelfMailer,
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
    ) -> SelfMailer:
        """Cancel a self-mailer by ID.

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
            f"/print-mail/v1/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailer,
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
    ) -> SelfMailerRetrieveURLResponse:
        """
        Retrieve a self-mailer preview URL.

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
            f"/print-mail/v1/self_mailers/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailerRetrieveURLResponse,
        )


class SelfMailersResourceWithRawResponse:
    def __init__(self, self_mailers: SelfMailersResource) -> None:
        self._self_mailers = self_mailers

        self.create = to_raw_response_wrapper(
            self_mailers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            self_mailers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            self_mailers.list,
        )
        self.delete = to_raw_response_wrapper(
            self_mailers.delete,
        )
        self.retrieve_url = to_raw_response_wrapper(
            self_mailers.retrieve_url,
        )


class AsyncSelfMailersResourceWithRawResponse:
    def __init__(self, self_mailers: AsyncSelfMailersResource) -> None:
        self._self_mailers = self_mailers

        self.create = async_to_raw_response_wrapper(
            self_mailers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            self_mailers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            self_mailers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            self_mailers.delete,
        )
        self.retrieve_url = async_to_raw_response_wrapper(
            self_mailers.retrieve_url,
        )


class SelfMailersResourceWithStreamingResponse:
    def __init__(self, self_mailers: SelfMailersResource) -> None:
        self._self_mailers = self_mailers

        self.create = to_streamed_response_wrapper(
            self_mailers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            self_mailers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            self_mailers.list,
        )
        self.delete = to_streamed_response_wrapper(
            self_mailers.delete,
        )
        self.retrieve_url = to_streamed_response_wrapper(
            self_mailers.retrieve_url,
        )


class AsyncSelfMailersResourceWithStreamingResponse:
    def __init__(self, self_mailers: AsyncSelfMailersResource) -> None:
        self._self_mailers = self_mailers

        self.create = async_to_streamed_response_wrapper(
            self_mailers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            self_mailers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            self_mailers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            self_mailers.delete,
        )
        self.retrieve_url = async_to_streamed_response_wrapper(
            self_mailers.retrieve_url,
        )
