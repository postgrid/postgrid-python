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
    PostcardSize,
    postcard_list_params,
    postcard_create_params,
    postcard_update_params,
    postcard_retrieve_params,
)
from ....types.print_mail.order_profiles.postcard_size import PostcardSize
from ....types.print_mail.order_profiles.postcard_profile import PostcardProfile
from ....types.print_mail.order_profiles.postcard_delete_response import PostcardDeleteResponse

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

    def create(
        self,
        *,
        size: PostcardSize,
        expand: SequenceNotStr[str] | Omit = omit,
        back_template: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        front_template: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostcardProfile:
        """Creates a new Postcard Profile.

        Provide either `frontTemplate` and
        `backTemplate` IDs, or upload a 2-page `pdf`. If providing a `pdf`, the request
        `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported postcard sizes.

          expand: Optional list of related resources to expand in the response.

          back_template: ID of the template for the back side. Required unless `pdf` is provided.

          description: An optional description for the profile. Set to `null` to remove during update.

          front_template: ID of the template for the front side. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services like `certified` or `registered`
              for postcards, though).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A 2-page PDF file containing the postcard content (front and back). Cannot be
              used with `frontTemplate`/`backTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/order_profiles/postcards",
            body=maybe_transform(
                {
                    "size": size,
                    "back_template": back_template,
                    "description": description,
                    "front_template": front_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                },
                postcard_create_params.PostcardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, postcard_create_params.PostcardCreateParams),
            ),
            cast_to=PostcardProfile,
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
    ) -> PostcardProfile:
        """
        Retrieves the details of a specific Postcard Profile.

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
            f"/print-mail/v1/order_profiles/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, postcard_retrieve_params.PostcardRetrieveParams),
            ),
            cast_to=PostcardProfile,
        )

    def update(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        back_template: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        front_template: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostcardProfile:
        """Updates specific fields of an existing Postcard Profile.

        If providing a `pdf`,
        the request `Content-Type` must be `multipart/form-data`.

        Args:
          expand: Optional list of related resources to expand in the response.

          back_template: ID of the template for the back side. Required unless `pdf` is provided.

          description: An optional description for the profile. Set to `null` to remove during update.

          front_template: ID of the template for the front side. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services like `certified` or `registered`
              for postcards, though).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A 2-page PDF file containing the postcard content (front and back). Cannot be
              used with `frontTemplate`/`backTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/order_profiles/postcards/{id}",
            body=maybe_transform(
                {
                    "back_template": back_template,
                    "description": description,
                    "front_template": front_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                },
                postcard_update_params.PostcardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, postcard_update_params.PostcardUpdateParams),
            ),
            cast_to=PostcardProfile,
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
    ) -> SyncSkipLimit[PostcardProfile]:
        """
        Retrieves a list of Postcard Profiles.

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
            "/print-mail/v1/order_profiles/postcards",
            page=SyncSkipLimit[PostcardProfile],
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
            model=PostcardProfile,
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
    ) -> PostcardDeleteResponse:
        """
        Deletes a Postcard Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/order_profiles/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostcardDeleteResponse,
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

    async def create(
        self,
        *,
        size: PostcardSize,
        expand: SequenceNotStr[str] | Omit = omit,
        back_template: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        front_template: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostcardProfile:
        """Creates a new Postcard Profile.

        Provide either `frontTemplate` and
        `backTemplate` IDs, or upload a 2-page `pdf`. If providing a `pdf`, the request
        `Content-Type` must be `multipart/form-data`.

        Args:
          size: Enum representing the supported postcard sizes.

          expand: Optional list of related resources to expand in the response.

          back_template: ID of the template for the back side. Required unless `pdf` is provided.

          description: An optional description for the profile. Set to `null` to remove during update.

          front_template: ID of the template for the front side. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services like `certified` or `registered`
              for postcards, though).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A 2-page PDF file containing the postcard content (front and back). Cannot be
              used with `frontTemplate`/`backTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/order_profiles/postcards",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "back_template": back_template,
                    "description": description,
                    "front_template": front_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                },
                postcard_create_params.PostcardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, postcard_create_params.PostcardCreateParams),
            ),
            cast_to=PostcardProfile,
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
    ) -> PostcardProfile:
        """
        Retrieves the details of a specific Postcard Profile.

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
            f"/print-mail/v1/order_profiles/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, postcard_retrieve_params.PostcardRetrieveParams),
            ),
            cast_to=PostcardProfile,
        )

    async def update(
        self,
        id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        back_template: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        front_template: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostcardProfile:
        """Updates specific fields of an existing Postcard Profile.

        If providing a `pdf`,
        the request `Content-Type` must be `multipart/form-data`.

        Args:
          expand: Optional list of related resources to expand in the response.

          back_template: ID of the template for the back side. Required unless `pdf` is provided.

          description: An optional description for the profile. Set to `null` to remove during update.

          front_template: ID of the template for the front side. Required unless `pdf` is provided.

          mailing_class: Mailing class (cannot include extra services like `certified` or `registered`
              for postcards, though).

          merge_variables: Default merge variables for orders created using this profile.

          metadata: Optional key-value metadata.

          pdf: A 2-page PDF file containing the postcard content (front and back). Cannot be
              used with `frontTemplate`/`backTemplate`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/order_profiles/postcards/{id}",
            body=await async_maybe_transform(
                {
                    "back_template": back_template,
                    "description": description,
                    "front_template": front_template,
                    "mailing_class": mailing_class,
                    "merge_variables": merge_variables,
                    "metadata": metadata,
                    "pdf": pdf,
                },
                postcard_update_params.PostcardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, postcard_update_params.PostcardUpdateParams),
            ),
            cast_to=PostcardProfile,
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
    ) -> AsyncPaginator[PostcardProfile, AsyncSkipLimit[PostcardProfile]]:
        """
        Retrieves a list of Postcard Profiles.

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
            "/print-mail/v1/order_profiles/postcards",
            page=AsyncSkipLimit[PostcardProfile],
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
            model=PostcardProfile,
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
    ) -> PostcardDeleteResponse:
        """
        Deletes a Postcard Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/order_profiles/postcards/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostcardDeleteResponse,
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
        self.update = to_raw_response_wrapper(
            postcards.update,
        )
        self.list = to_raw_response_wrapper(
            postcards.list,
        )
        self.delete = to_raw_response_wrapper(
            postcards.delete,
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
        self.update = async_to_raw_response_wrapper(
            postcards.update,
        )
        self.list = async_to_raw_response_wrapper(
            postcards.list,
        )
        self.delete = async_to_raw_response_wrapper(
            postcards.delete,
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
        self.update = to_streamed_response_wrapper(
            postcards.update,
        )
        self.list = to_streamed_response_wrapper(
            postcards.list,
        )
        self.delete = to_streamed_response_wrapper(
            postcards.delete,
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
        self.update = async_to_streamed_response_wrapper(
            postcards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            postcards.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            postcards.delete,
        )
