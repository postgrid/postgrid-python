# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import overload

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
from ...types.print_mail import BankAccountCountryCode, bank_account_list_params, bank_account_create_params
from ...types.print_mail.bank_account import BankAccount
from ...types.print_mail.bank_account_country_code import BankAccountCountryCode
from ...types.print_mail.bank_account_delete_response import BankAccountDeleteResponse

__all__ = ["BankAccountsResource", "AsyncBankAccountsResource"]


class BankAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BankAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return BankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return BankAccountsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_text: str,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_text: The signature text of the bank account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

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
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_image: str,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_image: Link to signature image which PostGrid will download and apply to cheques
              created with this bank account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

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
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_image: Union[str, Base64FileInput],
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_image: A PNG or JPEG file which PostGrid will apply to checks created with this bank
              account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_number", "bank_country_code", "bank_name", "signature_text"],
        ["account_number", "bank_country_code", "bank_name", "signature_image"],
    )
    def create(
        self,
        *,
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_text: str | Omit = omit,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        signature_image: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        return self._post(
            "/print-mail/v1/bank_accounts",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "bank_country_code": bank_country_code,
                    "bank_name": bank_name,
                    "signature_text": signature_text,
                    "bank_primary_line": bank_primary_line,
                    "bank_secondary_line": bank_secondary_line,
                    "ca_designation_number": ca_designation_number,
                    "description": description,
                    "metadata": metadata,
                    "route_number": route_number,
                    "routing_number": routing_number,
                    "transit_number": transit_number,
                    "signature_image": signature_image,
                },
                bank_account_create_params.BankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> BankAccount:
        """
        Retrieve a bank account by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/bank_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> SyncSkipLimit[BankAccount]:
        """
        Get a list of bank accounts.

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
            "/print-mail/v1/bank_accounts",
            page=SyncSkipLimit[BankAccount],
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
                    bank_account_list_params.BankAccountListParams,
                ),
            ),
            model=BankAccount,
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
    ) -> BankAccountDeleteResponse:
        """Delete a bank account by ID.

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
            f"/print-mail/v1/bank_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccountDeleteResponse,
        )


class AsyncBankAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBankAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncBankAccountsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_text: str,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_text: The signature text of the bank account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

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
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_image: str,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_image: Link to signature image which PostGrid will download and apply to cheques
              created with this bank account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

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
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_image: Union[str, Base64FileInput],
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        """Create a bank account.

        A US bank account is created by setting `bankCountryCode`
        to `US` and providing `accountNumber` and `routingNumber`. A canadian bank
        account can be created by specifying `bankCountryCode` as `CA` and setting
        `accountNumber`, `routeNumber`, and `transitNumber` accordingly.

        You must specify _either_ `signatureImage` or `signatureText`. The image can be
        supplied as either a URL or a multipart file upload.

        Args:
          account_number: The account number of the bank account.

          bank_country_code: Countries typically have different bank account formats and standards. These are
              the countries which PostGrid's bank accounts API supports.

          bank_name: The name of the bank.

          signature_image: A PNG or JPEG file which PostGrid will apply to checks created with this bank
              account.

          bank_primary_line: The primary address line of the bank.

          bank_secondary_line: The secondary address line of the bank.

          ca_designation_number: The designation number of the bank account (for CA).

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          route_number: The route number of the bank account (for CA).

          routing_number: The routing number of the bank account (for US).

          transit_number: The transit number of the bank account (for CA).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_number", "bank_country_code", "bank_name", "signature_text"],
        ["account_number", "bank_country_code", "bank_name", "signature_image"],
    )
    async def create(
        self,
        *,
        account_number: str,
        bank_country_code: BankAccountCountryCode,
        bank_name: str,
        signature_text: str | Omit = omit,
        bank_primary_line: str | Omit = omit,
        bank_secondary_line: str | Omit = omit,
        ca_designation_number: str | Omit = omit,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        route_number: str | Omit = omit,
        routing_number: str | Omit = omit,
        transit_number: str | Omit = omit,
        signature_image: str | Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccount:
        return await self._post(
            "/print-mail/v1/bank_accounts",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "bank_country_code": bank_country_code,
                    "bank_name": bank_name,
                    "signature_text": signature_text,
                    "bank_primary_line": bank_primary_line,
                    "bank_secondary_line": bank_secondary_line,
                    "ca_designation_number": ca_designation_number,
                    "description": description,
                    "metadata": metadata,
                    "route_number": route_number,
                    "routing_number": routing_number,
                    "transit_number": transit_number,
                    "signature_image": signature_image,
                },
                bank_account_create_params.BankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> BankAccount:
        """
        Retrieve a bank account by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/bank_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccount,
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
    ) -> AsyncPaginator[BankAccount, AsyncSkipLimit[BankAccount]]:
        """
        Get a list of bank accounts.

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
            "/print-mail/v1/bank_accounts",
            page=AsyncSkipLimit[BankAccount],
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
                    bank_account_list_params.BankAccountListParams,
                ),
            ),
            model=BankAccount,
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
    ) -> BankAccountDeleteResponse:
        """Delete a bank account by ID.

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
            f"/print-mail/v1/bank_accounts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankAccountDeleteResponse,
        )


class BankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = to_raw_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bank_accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            bank_accounts.delete,
        )


class AsyncBankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = async_to_raw_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bank_accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bank_accounts.delete,
        )


class BankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = to_streamed_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bank_accounts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            bank_accounts.delete,
        )


class AsyncBankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.create = async_to_streamed_response_wrapper(
            bank_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bank_accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bank_accounts.delete,
        )
