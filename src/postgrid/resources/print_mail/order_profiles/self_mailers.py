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
from ....types.print_mail.order_profiles import (
    SelfMailerSize,
    self_mailer_list_params,
    self_mailer_create_params,
    self_mailer_update_params,
    self_mailer_retrieve_params,
)
from ....types.print_mail.order_profiles.self_mailer_size import SelfMailerSize
from ....types.print_mail.order_profiles.self_mailer_profile import SelfMailerProfile
from ....types.print_mail.order_profiles.self_mailer_delete_response import SelfMailerDeleteResponse

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

    def create(
        self,
        *,
        size: SelfMailerSize,
        expand: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        inside_template: str | Omit = omit,
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
        outside_template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailerProfile:
        """Creates a new Self-Mailer Profile.

        Provide either `insideTemplate` and
        `outsideTemplate` IDs, or upload a 2-page `pdf`. If providing a `pdf`, the
        request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported self-mailer sizes.

          expand: Optional list of related resources to expand in the response.

          description: An optional description for the profile. Set to `null` to remove during update.

          inside_template: ID of the template for the inside. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services for self-mailers).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          outside_template: ID of the template for the outside. Required unless `pdf` is provided.

          pdf: A 2-page PDF file containing the self-mailer content (inside and outside).
              Cannot be used with `insideTemplate`/`outsideTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/order_profiles/self_mailers",
            body=maybe_transform(
                {
                    "size": size,
                    "description": description,
                    "inside_template": inside_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_create_params.SelfMailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, self_mailer_create_params.SelfMailerCreateParams),
            ),
            cast_to=SelfMailerProfile,
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
    ) -> SelfMailerProfile:
        """
        Retrieves the details of a specific Self-Mailer Profile.

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
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, self_mailer_retrieve_params.SelfMailerRetrieveParams),
            ),
            cast_to=SelfMailerProfile,
        )

    def update(
        self,
        id: str,
        *,
        size: SelfMailerSize,
        expand: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        inside_template: str | Omit = omit,
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
        outside_template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailerProfile:
        """Updates specific fields of an existing Self-Mailer Profile.

        If providing a
        `pdf`, the request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported self-mailer sizes.

          expand: Optional list of related resources to expand in the response.

          description: An optional description for the profile. Set to `null` to remove during update.

          inside_template: ID of the template for the inside. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services for self-mailers).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          outside_template: ID of the template for the outside. Required unless `pdf` is provided.

          pdf: A 2-page PDF file containing the self-mailer content (inside and outside).
              Cannot be used with `insideTemplate`/`outsideTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            body=maybe_transform(
                {
                    "size": size,
                    "description": description,
                    "inside_template": inside_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_update_params.SelfMailerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, self_mailer_update_params.SelfMailerUpdateParams),
            ),
            cast_to=SelfMailerProfile,
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
    ) -> SyncSkipLimit[SelfMailerProfile]:
        """
        Retrieves a list of Self-Mailer Profiles.

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
            "/print-mail/v1/order_profiles/self_mailers",
            page=SyncSkipLimit[SelfMailerProfile],
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
            model=SelfMailerProfile,
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
    ) -> SelfMailerDeleteResponse:
        """
        Deletes a Self-Mailer Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailerDeleteResponse,
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

    async def create(
        self,
        *,
        size: SelfMailerSize,
        expand: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        inside_template: str | Omit = omit,
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
        outside_template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailerProfile:
        """Creates a new Self-Mailer Profile.

        Provide either `insideTemplate` and
        `outsideTemplate` IDs, or upload a 2-page `pdf`. If providing a `pdf`, the
        request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported self-mailer sizes.

          expand: Optional list of related resources to expand in the response.

          description: An optional description for the profile. Set to `null` to remove during update.

          inside_template: ID of the template for the inside. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services for self-mailers).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          outside_template: ID of the template for the outside. Required unless `pdf` is provided.

          pdf: A 2-page PDF file containing the self-mailer content (inside and outside).
              Cannot be used with `insideTemplate`/`outsideTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/order_profiles/self_mailers",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "description": description,
                    "inside_template": inside_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_create_params.SelfMailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, self_mailer_create_params.SelfMailerCreateParams),
            ),
            cast_to=SelfMailerProfile,
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
    ) -> SelfMailerProfile:
        """
        Retrieves the details of a specific Self-Mailer Profile.

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
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, self_mailer_retrieve_params.SelfMailerRetrieveParams
                ),
            ),
            cast_to=SelfMailerProfile,
        )

    async def update(
        self,
        id: str,
        *,
        size: SelfMailerSize,
        expand: SequenceNotStr[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        inside_template: str | Omit = omit,
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
        outside_template: str | Omit = omit,
        pdf: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelfMailerProfile:
        """Updates specific fields of an existing Self-Mailer Profile.

        If providing a
        `pdf`, the request `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported self-mailer sizes.

          expand: Optional list of related resources to expand in the response.

          description: An optional description for the profile. Set to `null` to remove during update.

          inside_template: ID of the template for the inside. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services for self-mailers).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          outside_template: ID of the template for the outside. Required unless `pdf` is provided.

          pdf: A 2-page PDF file containing the self-mailer content (inside and outside).
              Cannot be used with `insideTemplate`/`outsideTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "description": description,
                    "inside_template": inside_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "outside_template": outside_template,
                    "pdf": pdf,
                },
                self_mailer_update_params.SelfMailerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, self_mailer_update_params.SelfMailerUpdateParams),
            ),
            cast_to=SelfMailerProfile,
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
    ) -> AsyncPaginator[SelfMailerProfile, AsyncSkipLimit[SelfMailerProfile]]:
        """
        Retrieves a list of Self-Mailer Profiles.

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
            "/print-mail/v1/order_profiles/self_mailers",
            page=AsyncSkipLimit[SelfMailerProfile],
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
            model=SelfMailerProfile,
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
    ) -> SelfMailerDeleteResponse:
        """
        Deletes a Self-Mailer Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/order_profiles/self_mailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelfMailerDeleteResponse,
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
        self.update = to_raw_response_wrapper(
            self_mailers.update,
        )
        self.list = to_raw_response_wrapper(
            self_mailers.list,
        )
        self.delete = to_raw_response_wrapper(
            self_mailers.delete,
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
        self.update = async_to_raw_response_wrapper(
            self_mailers.update,
        )
        self.list = async_to_raw_response_wrapper(
            self_mailers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            self_mailers.delete,
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
        self.update = to_streamed_response_wrapper(
            self_mailers.update,
        )
        self.list = to_streamed_response_wrapper(
            self_mailers.list,
        )
        self.delete = to_streamed_response_wrapper(
            self_mailers.delete,
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
        self.update = async_to_streamed_response_wrapper(
            self_mailers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            self_mailers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            self_mailers.delete,
        )
