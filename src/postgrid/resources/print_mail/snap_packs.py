# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Mapping, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import (
    extract_files,
    path_template,
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
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
from ...types.print_mail import snap_pack_list_params, snap_pack_create_params, snap_pack_retrieve_capabilities_params
from ...types.print_mail.snap_pack import SnapPack
from ...types.print_mail.snap_pack_create_response import SnapPackCreateResponse
from ...types.print_mail.snap_pack_retrieve_capabilities_response import SnapPackRetrieveCapabilitiesResponse

__all__ = ["SnapPacksResource", "AsyncSnapPacksResource"]


class SnapPacksResource(SyncAPIResource):
    """
    Snap packs are pressure-sealed mailers that resemble official documents
     and encourage higher open rates. They do not require envelopes and are
     opened by tearing along perforated edges. The sealed design keeps contents
     hidden until opened, making snap packs ideal for sensitive or important
     documents such as contracts, forms, or notices.

     You can request access to this feature by reaching out to
     support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> SnapPacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return SnapPacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnapPacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return SnapPacksResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        from_: snap_pack_create_params.SnapPackCreateWithHTMLFrom,
        inside_html: str,
        outside_html: str,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithHTMLTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          inside_html: The HTML content for the inside of the snap pack. You can supply _either_ this
              or `insideTemplate` but not both.

          outside_html: The HTML content for the outside of the snap pack. You can supply _either_ this
              or `outsideTemplate` but not both.

          size: Enum representing the supported snap pack sizes.

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
        from_: snap_pack_create_params.SnapPackCreateWithTemplateFrom,
        inside_template: str,
        outside_template: str,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithTemplateTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          inside_template: The template ID for the inside of the snap pack. You can supply _either_ this or
              `insideHTML` but not both.

          outside_template: The template ID for the outside of the snap pack. You can supply _either_ this
              or `outsideHTML` but not both.

          size: Enum representing the supported snap pack sizes.

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
        from_: snap_pack_create_params.SnapPackCreateWithPdfFrom,
        pdf: Union[str, FileTypes],
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithPdfTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          pdf: A URL or a multipart-uploaded two-page PDF (first page is the outside, second
              page is the inside) that matches the selected snap pack size.

          size: Enum representing the supported snap pack sizes.

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
        ["from_", "inside_template", "outside_template", "size", "to"],
        ["from_", "pdf", "size", "to"],
    )
    def create(
        self,
        *,
        from_: snap_pack_create_params.SnapPackCreateWithHTMLFrom
        | snap_pack_create_params.SnapPackCreateWithTemplateFrom
        | snap_pack_create_params.SnapPackCreateWithPdfFrom,
        inside_html: str | Omit = omit,
        outside_html: str | Omit = omit,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithHTMLTo
        | snap_pack_create_params.SnapPackCreateWithTemplateTo
        | snap_pack_create_params.SnapPackCreateWithPdfTo,
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
        idempotency_key: str | Omit = omit,
        inside_template: str | Omit = omit,
        outside_template: str | Omit = omit,
        pdf: Union[str, FileTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
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
            [["pdf"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["pdf"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            SnapPackCreateResponse,
            self._post(
                "/print-mail/v1/snap_packs",
                body=maybe_transform(body, snap_pack_create_params.SnapPackCreateParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, SnapPackCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SnapPack:
        """
        Retrieve a snap pack by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/snap_packs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
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
    ) -> SyncSkipLimit[SnapPack]:
        """
        Get a list of snap packs.

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
            "/print-mail/v1/snap_packs",
            page=SyncSkipLimit[SnapPack],
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
                    snap_pack_list_params.SnapPackListParams,
                ),
            ),
            model=SnapPack,
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
    ) -> SnapPack:
        """Cancel a snap pack by ID.

        Note that this operation cannot be undone and that
        only snap packs with a status of `ready` can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/print-mail/v1/snap_packs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
        )

    def progressions(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPack:
        """Progresses a snap pack's `status` to the next stage.

        This is only available in
        test mode and can be used to simulate how a live order would progress through
        the different statuses.

        Note: this will fail with an `invalid_progression_error` if the status is one of
        `completed` or `cancelled`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/snap_packs/{id}/progressions", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
        )

    def retrieve_capabilities(
        self,
        *,
        return_country_code: str,
        destination_country_code: str | Omit = omit,
        mailing_list: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackRetrieveCapabilitiesResponse:
        """
        Provides sizes and mailing classes available for the destination.

        Args:
          return_country_code: The country code where mail may be returned to.

          destination_country_code: The country code of where the snap pack will be sent to. One of `mailingList` or
              `destinationCountryCode` must be supplied but not both.

          mailing_list: Sources destination countries from the provided mailing list. One of
              `mailingList` or `destinationCountryCode` must be supplied but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/print-mail/v1/snap_packs/capabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "return_country_code": return_country_code,
                        "destination_country_code": destination_country_code,
                        "mailing_list": mailing_list,
                    },
                    snap_pack_retrieve_capabilities_params.SnapPackRetrieveCapabilitiesParams,
                ),
            ),
            cast_to=SnapPackRetrieveCapabilitiesResponse,
        )


class AsyncSnapPacksResource(AsyncAPIResource):
    """
    Snap packs are pressure-sealed mailers that resemble official documents
     and encourage higher open rates. They do not require envelopes and are
     opened by tearing along perforated edges. The sealed design keeps contents
     hidden until opened, making snap packs ideal for sensitive or important
     documents such as contracts, forms, or notices.

     You can request access to this feature by reaching out to
     support@postgrid.com
    """

    @cached_property
    def with_raw_response(self) -> AsyncSnapPacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSnapPacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnapPacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncSnapPacksResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        from_: snap_pack_create_params.SnapPackCreateWithHTMLFrom,
        inside_html: str,
        outside_html: str,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithHTMLTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          inside_html: The HTML content for the inside of the snap pack. You can supply _either_ this
              or `insideTemplate` but not both.

          outside_html: The HTML content for the outside of the snap pack. You can supply _either_ this
              or `outsideTemplate` but not both.

          size: Enum representing the supported snap pack sizes.

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
        from_: snap_pack_create_params.SnapPackCreateWithTemplateFrom,
        inside_template: str,
        outside_template: str,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithTemplateTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          inside_template: The template ID for the inside of the snap pack. You can supply _either_ this or
              `insideHTML` but not both.

          outside_template: The template ID for the outside of the snap pack. You can supply _either_ this
              or `outsideHTML` but not both.

          size: Enum representing the supported snap pack sizes.

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
        from_: snap_pack_create_params.SnapPackCreateWithPdfFrom,
        pdf: Union[str, FileTypes],
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithPdfTo,
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
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        """Create a snap pack.

        You can supply one of the following:

        - HTML content for the inside and outside of the snap pack
        - Template IDs for the inside and outside of the snap pack
        - A URL for a two-page PDF that matches the snap pack layout Create a snap pack
          via a multipart/form-data request. Accepts the same fields as the JSON create
          body (nested objects are bracket-encoded form fields, e.g. `to[firstName]`);
          use this content type to upload the PDF file directly.

        Args:
          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to` contact.

          pdf: A URL or a multipart-uploaded two-page PDF (first page is the outside, second
              page is the inside) that matches the selected snap pack size.

          size: Enum representing the supported snap pack sizes.

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
        ["from_", "inside_template", "outside_template", "size", "to"],
        ["from_", "pdf", "size", "to"],
    )
    async def create(
        self,
        *,
        from_: snap_pack_create_params.SnapPackCreateWithHTMLFrom
        | snap_pack_create_params.SnapPackCreateWithTemplateFrom
        | snap_pack_create_params.SnapPackCreateWithPdfFrom,
        inside_html: str | Omit = omit,
        outside_html: str | Omit = omit,
        size: Literal["8.5x11_bifold_v"],
        to: snap_pack_create_params.SnapPackCreateWithHTMLTo
        | snap_pack_create_params.SnapPackCreateWithTemplateTo
        | snap_pack_create_params.SnapPackCreateWithPdfTo,
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
        idempotency_key: str | Omit = omit,
        inside_template: str | Omit = omit,
        outside_template: str | Omit = omit,
        pdf: Union[str, FileTypes] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackCreateResponse:
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
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
            [["pdf"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["pdf"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            SnapPackCreateResponse,
            await self._post(
                "/print-mail/v1/snap_packs",
                body=await async_maybe_transform(body, snap_pack_create_params.SnapPackCreateParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, SnapPackCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SnapPack:
        """
        Retrieve a snap pack by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/snap_packs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
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
    ) -> AsyncPaginator[SnapPack, AsyncSkipLimit[SnapPack]]:
        """
        Get a list of snap packs.

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
            "/print-mail/v1/snap_packs",
            page=AsyncSkipLimit[SnapPack],
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
                    snap_pack_list_params.SnapPackListParams,
                ),
            ),
            model=SnapPack,
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
    ) -> SnapPack:
        """Cancel a snap pack by ID.

        Note that this operation cannot be undone and that
        only snap packs with a status of `ready` can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/print-mail/v1/snap_packs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
        )

    async def progressions(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPack:
        """Progresses a snap pack's `status` to the next stage.

        This is only available in
        test mode and can be used to simulate how a live order would progress through
        the different statuses.

        Note: this will fail with an `invalid_progression_error` if the status is one of
        `completed` or `cancelled`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/snap_packs/{id}/progressions", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SnapPack,
        )

    async def retrieve_capabilities(
        self,
        *,
        return_country_code: str,
        destination_country_code: str | Omit = omit,
        mailing_list: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SnapPackRetrieveCapabilitiesResponse:
        """
        Provides sizes and mailing classes available for the destination.

        Args:
          return_country_code: The country code where mail may be returned to.

          destination_country_code: The country code of where the snap pack will be sent to. One of `mailingList` or
              `destinationCountryCode` must be supplied but not both.

          mailing_list: Sources destination countries from the provided mailing list. One of
              `mailingList` or `destinationCountryCode` must be supplied but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/print-mail/v1/snap_packs/capabilities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "return_country_code": return_country_code,
                        "destination_country_code": destination_country_code,
                        "mailing_list": mailing_list,
                    },
                    snap_pack_retrieve_capabilities_params.SnapPackRetrieveCapabilitiesParams,
                ),
            ),
            cast_to=SnapPackRetrieveCapabilitiesResponse,
        )


class SnapPacksResourceWithRawResponse:
    def __init__(self, snap_packs: SnapPacksResource) -> None:
        self._snap_packs = snap_packs

        self.create = to_raw_response_wrapper(
            snap_packs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            snap_packs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            snap_packs.list,
        )
        self.delete = to_raw_response_wrapper(
            snap_packs.delete,
        )
        self.progressions = to_raw_response_wrapper(
            snap_packs.progressions,
        )
        self.retrieve_capabilities = to_raw_response_wrapper(
            snap_packs.retrieve_capabilities,
        )


class AsyncSnapPacksResourceWithRawResponse:
    def __init__(self, snap_packs: AsyncSnapPacksResource) -> None:
        self._snap_packs = snap_packs

        self.create = async_to_raw_response_wrapper(
            snap_packs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            snap_packs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            snap_packs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            snap_packs.delete,
        )
        self.progressions = async_to_raw_response_wrapper(
            snap_packs.progressions,
        )
        self.retrieve_capabilities = async_to_raw_response_wrapper(
            snap_packs.retrieve_capabilities,
        )


class SnapPacksResourceWithStreamingResponse:
    def __init__(self, snap_packs: SnapPacksResource) -> None:
        self._snap_packs = snap_packs

        self.create = to_streamed_response_wrapper(
            snap_packs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            snap_packs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            snap_packs.list,
        )
        self.delete = to_streamed_response_wrapper(
            snap_packs.delete,
        )
        self.progressions = to_streamed_response_wrapper(
            snap_packs.progressions,
        )
        self.retrieve_capabilities = to_streamed_response_wrapper(
            snap_packs.retrieve_capabilities,
        )


class AsyncSnapPacksResourceWithStreamingResponse:
    def __init__(self, snap_packs: AsyncSnapPacksResource) -> None:
        self._snap_packs = snap_packs

        self.create = async_to_streamed_response_wrapper(
            snap_packs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            snap_packs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            snap_packs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            snap_packs.delete,
        )
        self.progressions = async_to_streamed_response_wrapper(
            snap_packs.progressions,
        )
        self.retrieve_capabilities = async_to_streamed_response_wrapper(
            snap_packs.retrieve_capabilities,
        )
