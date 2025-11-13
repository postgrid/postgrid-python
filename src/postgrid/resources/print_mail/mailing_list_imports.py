# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
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
    FileType,
    mailing_list_import_list_params,
    mailing_list_import_create_params,
    mailing_list_import_update_params,
)
from ...types.print_mail.file_type import FileType
from ...types.print_mail.mailing_list_import_response import MailingListImportResponse
from ...types.print_mail.mailing_list_import_delete_response import MailingListImportDeleteResponse

__all__ = ["MailingListImportsResource", "AsyncMailingListImportsResource"]


class MailingListImportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MailingListImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return MailingListImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MailingListImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return MailingListImportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: str,
        file_type: FileType,
        receiver_address_mapping: Dict[str, str],
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        receiver_merge_variable_mapping: Dict[str, str] | Omit = omit,
        sender_address_mapping: Dict[str, str] | Omit = omit,
        sender_merge_variable_mapping: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListImportResponse:
        """
        Create a new mailing list import.

        Initiates the import process for a contact list file. The import enters the
        `validating` status while contacts are processed and verified.

        Args:
          file: The CSV file for this import.

          file_type: Type of file supported for mailing list imports.

          receiver_address_mapping: Mapping of columns for receiver addresses.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          receiver_merge_variable_mapping: Optional mapping of columns for receiver merge variables.

          sender_address_mapping: Optional mapping of columns for sender addresses. If this is present, then all
              receivers should have a corresponding sender.

          sender_merge_variable_mapping: Optional mapping of columns for sender merge variables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/print-mail/v1/mailing_list_imports",
            body=maybe_transform(
                {
                    "file": file,
                    "file_type": file_type,
                    "receiver_address_mapping": receiver_address_mapping,
                    "description": description,
                    "metadata": metadata,
                    "receiver_merge_variable_mapping": receiver_merge_variable_mapping,
                    "sender_address_mapping": sender_address_mapping,
                    "sender_merge_variable_mapping": sender_merge_variable_mapping,
                },
                mailing_list_import_create_params.MailingListImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
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
    ) -> MailingListImportResponse:
        """
        Retrieve a specific mailing list import by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/mailing_list_imports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListImportResponse:
        """
        Update an existing mailing list import.

        Args:
          description: An optional description for the import. Set to `null` to remove the existing
              description.

          metadata: Optional key-value data associated with the import. Set to `null` to remove
              existing metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/mailing_list_imports/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_import_update_params.MailingListImportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
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
    ) -> SyncSkipLimit[MailingListImportResponse]:
        """
        Retrieve a list of mailing list imports.

        Returns a paginated list of imports associated with the authenticated
        organization, filterable by various parameters.

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
            "/print-mail/v1/mailing_list_imports",
            page=SyncSkipLimit[MailingListImportResponse],
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
                    mailing_list_import_list_params.MailingListImportListParams,
                ),
            ),
            model=MailingListImportResponse,
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
    ) -> MailingListImportDeleteResponse:
        """
        Delete a mailing list import.

        This permanently deletes the import and its associated resources. This operation
        cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/mailing_list_imports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportDeleteResponse,
        )


class AsyncMailingListImportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMailingListImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMailingListImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMailingListImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncMailingListImportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: str,
        file_type: FileType,
        receiver_address_mapping: Dict[str, str],
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        receiver_merge_variable_mapping: Dict[str, str] | Omit = omit,
        sender_address_mapping: Dict[str, str] | Omit = omit,
        sender_merge_variable_mapping: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListImportResponse:
        """
        Create a new mailing list import.

        Initiates the import process for a contact list file. The import enters the
        `validating` status while contacts are processed and verified.

        Args:
          file: The CSV file for this import.

          file_type: Type of file supported for mailing list imports.

          receiver_address_mapping: Mapping of columns for receiver addresses.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          receiver_merge_variable_mapping: Optional mapping of columns for receiver merge variables.

          sender_address_mapping: Optional mapping of columns for sender addresses. If this is present, then all
              receivers should have a corresponding sender.

          sender_merge_variable_mapping: Optional mapping of columns for sender merge variables.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/print-mail/v1/mailing_list_imports",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "file_type": file_type,
                    "receiver_address_mapping": receiver_address_mapping,
                    "description": description,
                    "metadata": metadata,
                    "receiver_merge_variable_mapping": receiver_merge_variable_mapping,
                    "sender_address_mapping": sender_address_mapping,
                    "sender_merge_variable_mapping": sender_merge_variable_mapping,
                },
                mailing_list_import_create_params.MailingListImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
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
    ) -> MailingListImportResponse:
        """
        Retrieve a specific mailing list import by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/mailing_list_imports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListImportResponse:
        """
        Update an existing mailing list import.

        Args:
          description: An optional description for the import. Set to `null` to remove the existing
              description.

          metadata: Optional key-value data associated with the import. Set to `null` to remove
              existing metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/mailing_list_imports/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_import_update_params.MailingListImportUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportResponse,
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
    ) -> AsyncPaginator[MailingListImportResponse, AsyncSkipLimit[MailingListImportResponse]]:
        """
        Retrieve a list of mailing list imports.

        Returns a paginated list of imports associated with the authenticated
        organization, filterable by various parameters.

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
            "/print-mail/v1/mailing_list_imports",
            page=AsyncSkipLimit[MailingListImportResponse],
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
                    mailing_list_import_list_params.MailingListImportListParams,
                ),
            ),
            model=MailingListImportResponse,
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
    ) -> MailingListImportDeleteResponse:
        """
        Delete a mailing list import.

        This permanently deletes the import and its associated resources. This operation
        cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/mailing_list_imports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListImportDeleteResponse,
        )


class MailingListImportsResourceWithRawResponse:
    def __init__(self, mailing_list_imports: MailingListImportsResource) -> None:
        self._mailing_list_imports = mailing_list_imports

        self.create = to_raw_response_wrapper(
            mailing_list_imports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mailing_list_imports.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mailing_list_imports.update,
        )
        self.list = to_raw_response_wrapper(
            mailing_list_imports.list,
        )
        self.delete = to_raw_response_wrapper(
            mailing_list_imports.delete,
        )


class AsyncMailingListImportsResourceWithRawResponse:
    def __init__(self, mailing_list_imports: AsyncMailingListImportsResource) -> None:
        self._mailing_list_imports = mailing_list_imports

        self.create = async_to_raw_response_wrapper(
            mailing_list_imports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mailing_list_imports.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mailing_list_imports.update,
        )
        self.list = async_to_raw_response_wrapper(
            mailing_list_imports.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mailing_list_imports.delete,
        )


class MailingListImportsResourceWithStreamingResponse:
    def __init__(self, mailing_list_imports: MailingListImportsResource) -> None:
        self._mailing_list_imports = mailing_list_imports

        self.create = to_streamed_response_wrapper(
            mailing_list_imports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mailing_list_imports.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mailing_list_imports.update,
        )
        self.list = to_streamed_response_wrapper(
            mailing_list_imports.list,
        )
        self.delete = to_streamed_response_wrapper(
            mailing_list_imports.delete,
        )


class AsyncMailingListImportsResourceWithStreamingResponse:
    def __init__(self, mailing_list_imports: AsyncMailingListImportsResource) -> None:
        self._mailing_list_imports = mailing_list_imports

        self.create = async_to_streamed_response_wrapper(
            mailing_list_imports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mailing_list_imports.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mailing_list_imports.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mailing_list_imports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mailing_list_imports.delete,
        )
