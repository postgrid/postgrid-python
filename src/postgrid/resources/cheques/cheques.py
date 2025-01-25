# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .url import (
    URLResource,
    AsyncURLResource,
    URLResourceWithRawResponse,
    AsyncURLResourceWithRawResponse,
    URLResourceWithStreamingResponse,
    AsyncURLResourceWithStreamingResponse,
)
from ...types import cheque_list_params, cheque_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...pagination import SyncList, AsyncList
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cheque import Cheque
from .with_deposit_ready_pdf import (
    WithDepositReadyPdfResource,
    AsyncWithDepositReadyPdfResource,
    WithDepositReadyPdfResourceWithRawResponse,
    AsyncWithDepositReadyPdfResourceWithRawResponse,
    WithDepositReadyPdfResourceWithStreamingResponse,
    AsyncWithDepositReadyPdfResourceWithStreamingResponse,
)

__all__ = ["ChequesResource", "AsyncChequesResource"]


class ChequesResource(SyncAPIResource):
    @cached_property
    def url(self) -> URLResource:
        return URLResource(self._client)

    @cached_property
    def with_deposit_ready_pdf(self) -> WithDepositReadyPdfResource:
        return WithDepositReadyPdfResource(self._client)

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
        amount: int,
        bank_account: str,
        from_: cheque_create_params.From,
        to: cheque_create_params.To,
        currency_code: Literal["USD", "CAD"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_only: cheque_create_params.DigitalOnly | NotGiven = NOT_GIVEN,
        envelope: Union[Literal["standard"], str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        merge_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        number: int | NotGiven = NOT_GIVEN,
        redirect_to: cheque_create_params.RedirectTo | NotGiven = NOT_GIVEN,
        send_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        size: Literal["us_letter", "us_legal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Cheque:
        """
        Create a cheque.

        This endpoint allows you to create a new cheque with the specified details.

        If you would like to create a digitalOnly cheque, the digitalOnly object with
        the watermark will need to be passed in. Feature is available on request, e-mail
        support@postgrid.com for access.

        Example request body:

        ```json
        {
          "from": "contact_123",
          "bankAccount": "bank_123",
          "amount": 1000,
          "currencyCode": "USD",
          "number": 123456,
          "size": "us_letter",
          "digitalOnly": {
            "watermark": "VOID"
          }
        }
        ```

        Args:
          amount: The amount of the cheque in cents.

          bank_account: The bank account (ID) associated with the cheque.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          currency_code: The currency code of the cheque. This will be set to the default currency of the
              bank account (`USD` for US bank accounts and `CAD` for Canadian bank accounts)
              if not provided. You can set this value to `USD` if you want to draw USD from a
              Canadian bank account or vice versa.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          digital_only: The digitalOnly object contains data for digital-only cheques. A watermark must
              be provided.

          envelope: The envelope of the cheque. If a custom envelope ID is not specified, defaults
              to `standard`.

          logo_url: An optional logo URL for the cheque. This will be placed next to the recipient
              address at the top left corner of the cheque. This needs to be a public link to
              an image file (e.g. a PNG or JPEG file).

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          memo: The memo of the cheque.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          message: The message of the cheque.

          metadata: See the section on Metadata.

          number: The number of the cheque. If you don't provide this, it will automatically be
              set to an incrementing number starting from 1 across your entire account,
              ensuring that every cheque has a unique number.

          redirect_to: Providing this inserts a blank page at the start of the cheque with the
              recipient you provide here. This leaves the cheque that follows intact, which
              means you can use this to intercept at cheque at the redirected address and then
              mail it forward to the final recipient yourself. One use case for this is
              signing cheques at your office before mailing them out yourself.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported cheque sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/cheques",
            body=maybe_transform(
                {
                    "amount": amount,
                    "bank_account": bank_account,
                    "from_": from_,
                    "to": to,
                    "currency_code": currency_code,
                    "description": description,
                    "digital_only": digital_only,
                    "envelope": envelope,
                    "logo_url": logo_url,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                    "number": number,
                    "redirect_to": redirect_to,
                    "send_date": send_date,
                    "size": size,
                },
                cheque_create_params.ChequeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Cheque,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Cheque:
        """
        Retrieve a cheque by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Cheque,
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
    ) -> SyncList[Cheque]:
        """
        Get a list of cheques.

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
            "/cheques",
            page=SyncList[Cheque],
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
            model=Cheque,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Cheque:
        """Cancel a cheque by ID.

        Note that this operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Cheque,
        )


class AsyncChequesResource(AsyncAPIResource):
    @cached_property
    def url(self) -> AsyncURLResource:
        return AsyncURLResource(self._client)

    @cached_property
    def with_deposit_ready_pdf(self) -> AsyncWithDepositReadyPdfResource:
        return AsyncWithDepositReadyPdfResource(self._client)

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
        amount: int,
        bank_account: str,
        from_: cheque_create_params.From,
        to: cheque_create_params.To,
        currency_code: Literal["USD", "CAD"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        digital_only: cheque_create_params.DigitalOnly | NotGiven = NOT_GIVEN,
        envelope: Union[Literal["standard"], str] | NotGiven = NOT_GIVEN,
        logo_url: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        merge_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        number: int | NotGiven = NOT_GIVEN,
        redirect_to: cheque_create_params.RedirectTo | NotGiven = NOT_GIVEN,
        send_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        size: Literal["us_letter", "us_legal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Cheque:
        """
        Create a cheque.

        This endpoint allows you to create a new cheque with the specified details.

        If you would like to create a digitalOnly cheque, the digitalOnly object with
        the watermark will need to be passed in. Feature is available on request, e-mail
        support@postgrid.com for access.

        Example request body:

        ```json
        {
          "from": "contact_123",
          "bankAccount": "bank_123",
          "amount": 1000,
          "currencyCode": "USD",
          "number": 123456,
          "size": "us_letter",
          "digitalOnly": {
            "watermark": "VOID"
          }
        }
        ```

        Args:
          amount: The amount of the cheque in cents.

          bank_account: The bank account (ID) associated with the cheque.

          from_: The contact information of the sender. You can pass contact information inline
              here just like you can for the `to`.

          to: The recipient of this order. You can either supply the contact information
              inline here or provide a contact ID. PostGrid will automatically deduplicate
              contacts regardless of whether you provide the information inline here or call
              the contact creation endpoint.

          currency_code: The currency code of the cheque. This will be set to the default currency of the
              bank account (`USD` for US bank accounts and `CAD` for Canadian bank accounts)
              if not provided. You can set this value to `USD` if you want to draw USD from a
              Canadian bank account or vice versa.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          digital_only: The digitalOnly object contains data for digital-only cheques. A watermark must
              be provided.

          envelope: The envelope of the cheque. If a custom envelope ID is not specified, defaults
              to `standard`.

          logo_url: An optional logo URL for the cheque. This will be placed next to the recipient
              address at the top left corner of the cheque. This needs to be a public link to
              an image file (e.g. a PNG or JPEG file).

          mailing_class: The mailing class of this order. If not provided, automatically set to
              `first_class`.

          memo: The memo of the cheque.

          merge_variables: These will be merged with the variables in the template or HTML you create this
              order with. The keys in this object should match the variable names in the
              template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
              PDFs uploaded with the order.

          message: The message of the cheque.

          metadata: See the section on Metadata.

          number: The number of the cheque. If you don't provide this, it will automatically be
              set to an incrementing number starting from 1 across your entire account,
              ensuring that every cheque has a unique number.

          redirect_to: Providing this inserts a blank page at the start of the cheque with the
              recipient you provide here. This leaves the cheque that follows intact, which
              means you can use this to intercept at cheque at the redirected address and then
              mail it forward to the final recipient yourself. One use case for this is
              signing cheques at your office before mailing them out yourself.

          send_date: This order will transition from `ready` to `printing` on the day after this
              date. You can use this parameter to schedule orders for a future date.

          size: Enum representing the supported cheque sizes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/cheques",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "bank_account": bank_account,
                    "from_": from_,
                    "to": to,
                    "currency_code": currency_code,
                    "description": description,
                    "digital_only": digital_only,
                    "envelope": envelope,
                    "logo_url": logo_url,
                    "mailing_class": mailing_class,
                    "memo": memo,
                    "merge_variables": merge_variables,
                    "message": message,
                    "metadata": metadata,
                    "number": number,
                    "redirect_to": redirect_to,
                    "send_date": send_date,
                    "size": size,
                },
                cheque_create_params.ChequeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Cheque,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Cheque:
        """
        Retrieve a cheque by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Cheque,
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
    ) -> AsyncPaginator[Cheque, AsyncList[Cheque]]:
        """
        Get a list of cheques.

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
            "/cheques",
            page=AsyncList[Cheque],
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
            model=Cheque,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Cheque:
        """Cancel a cheque by ID.

        Note that this operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/cheques/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Cheque,
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
        self.list = to_raw_response_wrapper(
            cheques.list,
        )
        self.cancel = to_raw_response_wrapper(
            cheques.cancel,
        )

    @cached_property
    def url(self) -> URLResourceWithRawResponse:
        return URLResourceWithRawResponse(self._cheques.url)

    @cached_property
    def with_deposit_ready_pdf(self) -> WithDepositReadyPdfResourceWithRawResponse:
        return WithDepositReadyPdfResourceWithRawResponse(self._cheques.with_deposit_ready_pdf)


class AsyncChequesResourceWithRawResponse:
    def __init__(self, cheques: AsyncChequesResource) -> None:
        self._cheques = cheques

        self.create = async_to_raw_response_wrapper(
            cheques.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cheques.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            cheques.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            cheques.cancel,
        )

    @cached_property
    def url(self) -> AsyncURLResourceWithRawResponse:
        return AsyncURLResourceWithRawResponse(self._cheques.url)

    @cached_property
    def with_deposit_ready_pdf(self) -> AsyncWithDepositReadyPdfResourceWithRawResponse:
        return AsyncWithDepositReadyPdfResourceWithRawResponse(self._cheques.with_deposit_ready_pdf)


class ChequesResourceWithStreamingResponse:
    def __init__(self, cheques: ChequesResource) -> None:
        self._cheques = cheques

        self.create = to_streamed_response_wrapper(
            cheques.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cheques.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            cheques.list,
        )
        self.cancel = to_streamed_response_wrapper(
            cheques.cancel,
        )

    @cached_property
    def url(self) -> URLResourceWithStreamingResponse:
        return URLResourceWithStreamingResponse(self._cheques.url)

    @cached_property
    def with_deposit_ready_pdf(self) -> WithDepositReadyPdfResourceWithStreamingResponse:
        return WithDepositReadyPdfResourceWithStreamingResponse(self._cheques.with_deposit_ready_pdf)


class AsyncChequesResourceWithStreamingResponse:
    def __init__(self, cheques: AsyncChequesResource) -> None:
        self._cheques = cheques

        self.create = async_to_streamed_response_wrapper(
            cheques.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cheques.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            cheques.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            cheques.cancel,
        )

    @cached_property
    def url(self) -> AsyncURLResourceWithStreamingResponse:
        return AsyncURLResourceWithStreamingResponse(self._cheques.url)

    @cached_property
    def with_deposit_ready_pdf(self) -> AsyncWithDepositReadyPdfResourceWithStreamingResponse:
        return AsyncWithDepositReadyPdfResourceWithStreamingResponse(self._cheques.with_deposit_ready_pdf)
