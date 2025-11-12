# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

import httpx

from ...._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
    Base64FileInput,
)
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.print_mail import ChequeSize, OrderMailingClass
from ....types.print_mail.cheque_size import ChequeSize
from ....types.print_mail.order_profiles import (
    CurrencyCode,
    cheque_list_params,
    cheque_create_params,
    cheque_update_params,
    cheque_retrieve_params,
)
from ....types.print_mail.order_mailing_class import OrderMailingClass
from ....types.print_mail.order_profiles.currency_code import CurrencyCode
from ....types.print_mail.order_profiles.cheque_profile import ChequeProfile
from ....types.print_mail.order_profiles.cheque_list_response import ChequeListResponse
from ....types.print_mail.order_profiles.cheque_delete_response import ChequeDeleteResponse

__all__ = ["ChequesResource", "AsyncChequesResource"]


class ChequesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChequesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ChequesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChequesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#with_streaming_response
        """
        return ChequesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bank_account: str,
        size: ChequeSize,
        expand: List[str] | NotGiven = NOT_GIVEN,
        currency_code: CurrencyCode | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        letter_pdf: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        letter_template: str | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        mailing_class: OrderMailingClass | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        merge_variables: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """Creates a new Cheque Profile.

        Requires a `bankAccount` ID. Can optionally
        include an attached letter via `letterHTML`, `letterTemplate`, or `letterPDF`.
        If providing `letterPDF` or `logo` (if logo needs upload, though schema suggests
        URL), use `multipart/form-data`.

        Args:
          bank_account: ID of the bank account to use for the cheque. Required for creation.

          size: Enum representing the supported cheque sizes.

          expand: Optional list of related resources to expand in the response.

          currency_code: Enum representing the supported currency codes.

          description: An optional description for the profile. Set to `null` to remove during update.

          letter_pdf: PDF file for an optional attached letter. Cannot be used with `letterHTML` or
              `letterTemplate`. Input only.

          letter_template: ID of a template for an optional attached letter. Cannot be used with
              `letterHTML` or `letterPDF`.

          logo: A publicly accessible URL for the logo to print on the cheque. Set to `null` to
              remove during update.

          mailing_class: Mailing class. Generally must be first class (or equivalent for destination
              country) for cheques.

          memo: Memo line text for the cheque. Set to `null` to remove during update.

          merge_variables: Default merge variables for orders created using this profile.

          message: Message included on the cheque stub. Set to `null` to remove during update.

          metadata: Optional key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/order_profiles/cheques",
            body=maybe_transform(
                {
                    "bank_account": bank_account,
                    "size": size,
                    "currency_code": currency_code,
                    "description": description,
                    "letter_pdf": letter_pdf,
                    "letter_template": letter_template,
                    "logo": logo,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                },
                cheque_create_params.ChequeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, cheque_create_params.ChequeCreateParams),
            ),
            cast_to=ChequeProfile,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """
        Retrieves the details of a specific Cheque Profile.

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
            f"/print-mail/v1/order_profiles/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, cheque_retrieve_params.ChequeRetrieveParams),
            ),
            cast_to=ChequeProfile,
        )

    def update(
        self,
        id: str,
        *,
        bank_account: str,
        size: ChequeSize,
        expand: List[str] | NotGiven = NOT_GIVEN,
        currency_code: CurrencyCode | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        letter_pdf: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        letter_template: str | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        mailing_class: OrderMailingClass | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        merge_variables: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """Updates specific fields of an existing Cheque Profile.

        If providing `letterPDF`
        or `logo`, use `multipart/form-data`.

        Args:
          bank_account: ID of the bank account to use for the cheque. Required for creation.

          size: Enum representing the supported cheque sizes.

          expand: Optional list of related resources to expand in the response.

          currency_code: Enum representing the supported currency codes.

          description: An optional description for the profile. Set to `null` to remove during update.

          letter_pdf: PDF file for an optional attached letter. Cannot be used with `letterHTML` or
              `letterTemplate`. Input only.

          letter_template: ID of a template for an optional attached letter. Cannot be used with
              `letterHTML` or `letterPDF`.

          logo: A publicly accessible URL for the logo to print on the cheque. Set to `null` to
              remove during update.

          mailing_class: Mailing class. Generally must be first class (or equivalent for destination
              country) for cheques.

          memo: Memo line text for the cheque. Set to `null` to remove during update.

          merge_variables: Default merge variables for orders created using this profile.

          message: Message included on the cheque stub. Set to `null` to remove during update.

          metadata: Optional key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/order_profiles/cheques/{id}",
            body=maybe_transform(
                {
                    "bank_account": bank_account,
                    "size": size,
                    "currency_code": currency_code,
                    "description": description,
                    "letter_pdf": letter_pdf,
                    "letter_template": letter_template,
                    "logo": logo,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                },
                cheque_update_params.ChequeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, cheque_update_params.ChequeUpdateParams),
            ),
            cast_to=ChequeProfile,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSkipLimit[ChequeListResponse]:
        """
        Retrieves a list of Cheque Profiles.

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
            "/print-mail/v1/order_profiles/cheques",
            page=SyncSkipLimit[ChequeListResponse],
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
                    cheque_list_params.ChequeListParams,
                ),
            ),
            model=ChequeListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeDeleteResponse:
        """
        Deletes a Cheque Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/order_profiles/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChequeDeleteResponse,
        )


class AsyncChequesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChequesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChequesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChequesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/postgrid-python#with_streaming_response
        """
        return AsyncChequesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bank_account: str,
        size: ChequeSize,
        expand: List[str] | NotGiven = NOT_GIVEN,
        currency_code: CurrencyCode | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        letter_pdf: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        letter_template: str | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        mailing_class: OrderMailingClass | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        merge_variables: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """Creates a new Cheque Profile.

        Requires a `bankAccount` ID. Can optionally
        include an attached letter via `letterHTML`, `letterTemplate`, or `letterPDF`.
        If providing `letterPDF` or `logo` (if logo needs upload, though schema suggests
        URL), use `multipart/form-data`.

        Args:
          bank_account: ID of the bank account to use for the cheque. Required for creation.

          size: Enum representing the supported cheque sizes.

          expand: Optional list of related resources to expand in the response.

          currency_code: Enum representing the supported currency codes.

          description: An optional description for the profile. Set to `null` to remove during update.

          letter_pdf: PDF file for an optional attached letter. Cannot be used with `letterHTML` or
              `letterTemplate`. Input only.

          letter_template: ID of a template for an optional attached letter. Cannot be used with
              `letterHTML` or `letterPDF`.

          logo: A publicly accessible URL for the logo to print on the cheque. Set to `null` to
              remove during update.

          mailing_class: Mailing class. Generally must be first class (or equivalent for destination
              country) for cheques.

          memo: Memo line text for the cheque. Set to `null` to remove during update.

          merge_variables: Default merge variables for orders created using this profile.

          message: Message included on the cheque stub. Set to `null` to remove during update.

          metadata: Optional key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/order_profiles/cheques",
            body=await async_maybe_transform(
                {
                    "bank_account": bank_account,
                    "size": size,
                    "currency_code": currency_code,
                    "description": description,
                    "letter_pdf": letter_pdf,
                    "letter_template": letter_template,
                    "logo": logo,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                },
                cheque_create_params.ChequeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, cheque_create_params.ChequeCreateParams),
            ),
            cast_to=ChequeProfile,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """
        Retrieves the details of a specific Cheque Profile.

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
            f"/print-mail/v1/order_profiles/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, cheque_retrieve_params.ChequeRetrieveParams),
            ),
            cast_to=ChequeProfile,
        )

    async def update(
        self,
        id: str,
        *,
        bank_account: str,
        size: ChequeSize,
        expand: List[str] | NotGiven = NOT_GIVEN,
        currency_code: CurrencyCode | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        letter_pdf: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        letter_template: str | NotGiven = NOT_GIVEN,
        logo: Optional[str] | NotGiven = NOT_GIVEN,
        mailing_class: OrderMailingClass | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        merge_variables: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeProfile:
        """Updates specific fields of an existing Cheque Profile.

        If providing `letterPDF`
        or `logo`, use `multipart/form-data`.

        Args:
          bank_account: ID of the bank account to use for the cheque. Required for creation.

          size: Enum representing the supported cheque sizes.

          expand: Optional list of related resources to expand in the response.

          currency_code: Enum representing the supported currency codes.

          description: An optional description for the profile. Set to `null` to remove during update.

          letter_pdf: PDF file for an optional attached letter. Cannot be used with `letterHTML` or
              `letterTemplate`. Input only.

          letter_template: ID of a template for an optional attached letter. Cannot be used with
              `letterHTML` or `letterPDF`.

          logo: A publicly accessible URL for the logo to print on the cheque. Set to `null` to
              remove during update.

          mailing_class: Mailing class. Generally must be first class (or equivalent for destination
              country) for cheques.

          memo: Memo line text for the cheque. Set to `null` to remove during update.

          merge_variables: Default merge variables for orders created using this profile.

          message: Message included on the cheque stub. Set to `null` to remove during update.

          metadata: Optional key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/order_profiles/cheques/{id}",
            body=await async_maybe_transform(
                {
                    "bank_account": bank_account,
                    "size": size,
                    "currency_code": currency_code,
                    "description": description,
                    "letter_pdf": letter_pdf,
                    "letter_template": letter_template,
                    "logo": logo,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                },
                cheque_update_params.ChequeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"expand": expand}, cheque_update_params.ChequeUpdateParams),
            ),
            cast_to=ChequeProfile,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ChequeListResponse, AsyncSkipLimit[ChequeListResponse]]:
        """
        Retrieves a list of Cheque Profiles.

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
            "/print-mail/v1/order_profiles/cheques",
            page=AsyncSkipLimit[ChequeListResponse],
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
                    cheque_list_params.ChequeListParams,
                ),
            ),
            model=ChequeListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChequeDeleteResponse:
        """
        Deletes a Cheque Profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/order_profiles/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChequeDeleteResponse,
        )


class ChequesResourceWithRawResponse:
    def __init__(self, cheques: ChequesResource) -> None:
        self._cheques = cheques

        self.create = to_raw_response_wrapper(
            cheques.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cheques.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cheques.update,
        )
        self.list = to_raw_response_wrapper(
            cheques.list,
        )
        self.delete = to_raw_response_wrapper(
            cheques.delete,
        )


class AsyncChequesResourceWithRawResponse:
    def __init__(self, cheques: AsyncChequesResource) -> None:
        self._cheques = cheques

        self.create = async_to_raw_response_wrapper(
            cheques.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cheques.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cheques.update,
        )
        self.list = async_to_raw_response_wrapper(
            cheques.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cheques.delete,
        )


class ChequesResourceWithStreamingResponse:
    def __init__(self, cheques: ChequesResource) -> None:
        self._cheques = cheques

        self.create = to_streamed_response_wrapper(
            cheques.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cheques.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cheques.update,
        )
        self.list = to_streamed_response_wrapper(
            cheques.list,
        )
        self.delete = to_streamed_response_wrapper(
            cheques.delete,
        )


class AsyncChequesResourceWithStreamingResponse:
    def __init__(self, cheques: AsyncChequesResource) -> None:
        self._cheques = cheques

        self.create = async_to_streamed_response_wrapper(
            cheques.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cheques.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cheques.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cheques.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cheques.delete,
        )
