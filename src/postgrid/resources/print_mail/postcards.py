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
from ...types.print_mail import postcard_list_params, postcard_create_params
from ...types.print_mail.postcard import Postcard
from ...types.print_mail.order_profiles import PostcardSize
from ...types.print_mail.order_profiles.postcard_size import PostcardSize
from ...types.print_mail.postcard_retrieve_url_response import PostcardRetrieveURLResponse

__all__ = ["PostcardsResource", "AsyncPostcardsResource"]


class PostcardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PostcardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return PostcardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostcardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return PostcardsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        back_html: str,
        front_html: str,
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithHTMLTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithHTMLFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          back_html: The HTML content for the back of the postcard. You can supply _either_ this or
              `backTemplate` but not both.

          front_html: The HTML content for the front of the postcard. You can supply _either_ this or
              `frontTemplate` but not both.

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        back_template: str,
        front_template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          back_template: The template ID for the back of the postcard. You can supply _either_ this or
              `backHTML` but not both.

          front_template: The template ID for the front of the postcard. You can supply _either_ this or
              `frontHTML` but not both.

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
        pdf: str,
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithPdfurlTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithPdfurlFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          pdf: A URL pointing to a 2 page PDF file. The first page is the front of the postcard
              and the second page is the back (where the address will be stamped on).

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        pdf: Union[str, Base64FileInput],
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithPdfFileTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithPdfFileFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          pdf: A 2 page PDF file. The first page is the front of the postcard and the second
              page is the back (where the address will be stamped on).

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        ["back_html", "front_html", "size", "to"], ["back_template", "front_template"], ["pdf", "size", "to"]
    )
    def create(
        self,
        *,
        back_html: str | Omit = omit,
        front_html: str | Omit = omit,
        size: PostcardSize | Omit = omit,
        to: postcard_create_params.PostcardCreateWithHTMLTo
        | postcard_create_params.PostcardCreateWithPdfurlTo
        | postcard_create_params.PostcardCreateWithPdfFileTo
        | Omit = omit,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithHTMLFrom
        | postcard_create_params.PostcardCreateWithPdfurlFrom
        | postcard_create_params.PostcardCreateWithPdfFileFrom
        | Omit = omit,
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
        back_template: str | Omit = omit,
        front_template: str | Omit = omit,
        pdf: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Postcard:
        return self._post(
            "/print-mail/v1/postcards",
            body=maybe_transform(
                {
                    "back_html": back_html,
                    "front_html": front_html,
                    "size": size,
                    "to": to,
                    "description": description,
                    "from_": from_,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                    "back_template": back_template,
                    "front_template": front_template,
                    "pdf": pdf,
                },
                postcard_create_params.PostcardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> Postcard:
        """
        Retrieve a postcard by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> SyncSkipLimit[Postcard]:
        """
        Get a list of postcards.

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
            "/print-mail/v1/postcards",
            page=SyncSkipLimit[Postcard],
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
                    postcard_list_params.PostcardListParams,
                ),
            ),
            model=Postcard,
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
    ) -> Postcard:
        """Cancel a postcard by ID.

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
            f"/print-mail/v1/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> PostcardRetrieveURLResponse:
        """
        Retrieve a postcard preview URL.

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
            f"/print-mail/v1/postcards/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostcardRetrieveURLResponse,
        )


class AsyncPostcardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPostcardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostcardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostcardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncPostcardsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        back_html: str,
        front_html: str,
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithHTMLTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithHTMLFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          back_html: The HTML content for the back of the postcard. You can supply _either_ this or
              `backTemplate` but not both.

          front_html: The HTML content for the front of the postcard. You can supply _either_ this or
              `frontTemplate` but not both.

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        back_template: str,
        front_template: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          back_template: The template ID for the back of the postcard. You can supply _either_ this or
              `backHTML` but not both.

          front_template: The template ID for the front of the postcard. You can supply _either_ this or
              `frontHTML` but not both.

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
        pdf: str,
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithPdfurlTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithPdfurlFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          pdf: A URL pointing to a 2 page PDF file. The first page is the front of the postcard
              and the second page is the back (where the address will be stamped on).

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        pdf: Union[str, Base64FileInput],
        size: PostcardSize,
        to: postcard_create_params.PostcardCreateWithPdfFileTo,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithPdfFileFrom | Omit = omit,
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
    ) -> Postcard:
        """Create a postcard.

        Note that you can supply one of the following:

        - HTML content for the front and back of the postcard
        - A template ID for the front and back of the postcard
        - A URL or file for a 2 page PDF where the first page is the front of the
          postcard and the second page is the back
        - Upload the aforementioned PDF file via a multipart form upload request

        Args:
          pdf: A 2 page PDF file. The first page is the front of the postcard and the second
              page is the back (where the address will be stamped on).

          size: Enum representing the supported postcard sizes.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`. Unlike other order types, the sender
              address is optional for postcards.

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
        ["back_html", "front_html", "size", "to"], ["back_template", "front_template"], ["pdf", "size", "to"]
    )
    async def create(
        self,
        *,
        back_html: str | Omit = omit,
        front_html: str | Omit = omit,
        size: PostcardSize | Omit = omit,
        to: postcard_create_params.PostcardCreateWithHTMLTo
        | postcard_create_params.PostcardCreateWithPdfurlTo
        | postcard_create_params.PostcardCreateWithPdfFileTo
        | Omit = omit,
        description: str | Omit = omit,
        from_: postcard_create_params.PostcardCreateWithHTMLFrom
        | postcard_create_params.PostcardCreateWithPdfurlFrom
        | postcard_create_params.PostcardCreateWithPdfFileFrom
        | Omit = omit,
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
        back_template: str | Omit = omit,
        front_template: str | Omit = omit,
        pdf: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Postcard:
        return await self._post(
            "/print-mail/v1/postcards",
            body=await async_maybe_transform(
                {
                    "back_html": back_html,
                    "front_html": front_html,
                    "size": size,
                    "to": to,
                    "description": description,
                    "from_": from_,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "send_date": send_date,
                    "back_template": back_template,
                    "front_template": front_template,
                    "pdf": pdf,
                },
                postcard_create_params.PostcardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> Postcard:
        """
        Retrieve a postcard by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> AsyncPaginator[Postcard, AsyncSkipLimit[Postcard]]:
        """
        Get a list of postcards.

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
            "/print-mail/v1/postcards",
            page=AsyncSkipLimit[Postcard],
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
                    postcard_list_params.PostcardListParams,
                ),
            ),
            model=Postcard,
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
    ) -> Postcard:
        """Cancel a postcard by ID.

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
            f"/print-mail/v1/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Postcard,
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
    ) -> PostcardRetrieveURLResponse:
        """
        Retrieve a postcard preview URL.

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
            f"/print-mail/v1/postcards/{id}/url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostcardRetrieveURLResponse,
        )


class PostcardsResourceWithRawResponse:
    def __init__(self, postcards: PostcardsResource) -> None:
        self._postcards = postcards

        self.create = to_raw_response_wrapper(
            postcards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            postcards.retrieve,
        )
        self.list = to_raw_response_wrapper(
            postcards.list,
        )
        self.delete = to_raw_response_wrapper(
            postcards.delete,
        )
        self.retrieve_url = to_raw_response_wrapper(
            postcards.retrieve_url,
        )


class AsyncPostcardsResourceWithRawResponse:
    def __init__(self, postcards: AsyncPostcardsResource) -> None:
        self._postcards = postcards

        self.create = async_to_raw_response_wrapper(
            postcards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            postcards.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            postcards.list,
        )
        self.delete = async_to_raw_response_wrapper(
            postcards.delete,
        )
        self.retrieve_url = async_to_raw_response_wrapper(
            postcards.retrieve_url,
        )


class PostcardsResourceWithStreamingResponse:
    def __init__(self, postcards: PostcardsResource) -> None:
        self._postcards = postcards

        self.create = to_streamed_response_wrapper(
            postcards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            postcards.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            postcards.list,
        )
        self.delete = to_streamed_response_wrapper(
            postcards.delete,
        )
        self.retrieve_url = to_streamed_response_wrapper(
            postcards.retrieve_url,
        )


class AsyncPostcardsResourceWithStreamingResponse:
    def __init__(self, postcards: AsyncPostcardsResource) -> None:
        self._postcards = postcards

        self.create = async_to_streamed_response_wrapper(
            postcards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            postcards.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            postcards.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            postcards.delete,
        )
        self.retrieve_url = async_to_streamed_response_wrapper(
            postcards.retrieve_url,
        )
