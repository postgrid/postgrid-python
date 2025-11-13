# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
    mailing_list_jobs_params,
    mailing_list_list_params,
    mailing_list_create_params,
    mailing_list_update_params,
)
from ...types.print_mail.mailing_list import MailingList
from ...types.print_mail.mailing_list_update import MailingListUpdate
from ...types.print_mail.mailing_list_delete_response import MailingListDeleteResponse

__all__ = ["MailingListsResource", "AsyncMailingListsResource"]


class MailingListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MailingListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return MailingListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MailingListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return MailingListsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingList:
        """
        Create a new mailing list.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/print-mail/v1/mailing_lists",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_create_params.MailingListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
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
    ) -> MailingList:
        """
        Retrieve a specific mailing list by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/mailing_lists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListUpdate:
        """
        Update an existing mailing list.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/mailing_lists/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_update_params.MailingListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListUpdate,
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
    ) -> SyncSkipLimit[MailingList]:
        """
        Retrieve a list of mailing lists.

        Returns a paginated list of mailing lists associated with the authenticated
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
            "/print-mail/v1/mailing_lists",
            page=SyncSkipLimit[MailingList],
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
                    mailing_list_list_params.MailingListListParams,
                ),
            ),
            model=MailingList,
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
    ) -> MailingListDeleteResponse:
        """
        Delete a mailing list.

        This permanently deletes the mailing list and its associations. This operation
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
            f"/print-mail/v1/mailing_lists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListDeleteResponse,
        )

    def jobs(
        self,
        id: str,
        *,
        add_contacts: SequenceNotStr[str] | Omit = omit,
        add_mailing_list_imports: SequenceNotStr[str] | Omit = omit,
        remove_contacts: SequenceNotStr[str] | Omit = omit,
        remove_mailing_list_imports: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingList:
        """Runs a mailing list job.

        Mailing list jobs allow you to add or remove contacts
        to your mailing list from mailing list imports or directly with contact IDs.
        Only one job can be ran at a time and jobs are only able to be ran while the
        mailing list has a `status` of "completed".

        Once a job as successfully been kicked off, the mailing list will have a
        `status` of either `creating_contacts` or `removing_contacts` depending on which
        job was ran. After the job has finished, the mailing list will go back into the
        `completed` state where more jobs can be ran. If there are any errors while
        running a job, the `errors` field on the mailing list will contain a list of
        error objects which describe the errors.

        Args:
          add_contacts: List of contact IDs to add to the mailing list. Cannot be used with other
              operations.

          add_mailing_list_imports: List of mailing list import IDs to add to the mailing list. Cannot be used with
              other operations.

          remove_contacts: List of contact IDs to remove from the mailing list. Cannot be used with other
              operations.

          remove_mailing_list_imports: List of mailing list import IDs to remove from the mailing list. Cannot be used
              with other operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/print-mail/v1/mailing_lists/{id}/jobs",
            body=maybe_transform(
                {
                    "add_contacts": add_contacts,
                    "add_mailing_list_imports": add_mailing_list_imports,
                    "remove_contacts": remove_contacts,
                    "remove_mailing_list_imports": remove_mailing_list_imports,
                },
                mailing_list_jobs_params.MailingListJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
        )


class AsyncMailingListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMailingListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMailingListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMailingListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncMailingListsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingList:
        """
        Create a new mailing list.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/print-mail/v1/mailing_lists",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_create_params.MailingListCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
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
    ) -> MailingList:
        """
        Retrieve a specific mailing list by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/mailing_lists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingListUpdate:
        """
        Update an existing mailing list.

        Args:
          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          metadata: See the section on Metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/mailing_lists/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                },
                mailing_list_update_params.MailingListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListUpdate,
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
    ) -> AsyncPaginator[MailingList, AsyncSkipLimit[MailingList]]:
        """
        Retrieve a list of mailing lists.

        Returns a paginated list of mailing lists associated with the authenticated
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
            "/print-mail/v1/mailing_lists",
            page=AsyncSkipLimit[MailingList],
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
                    mailing_list_list_params.MailingListListParams,
                ),
            ),
            model=MailingList,
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
    ) -> MailingListDeleteResponse:
        """
        Delete a mailing list.

        This permanently deletes the mailing list and its associations. This operation
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
            f"/print-mail/v1/mailing_lists/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingListDeleteResponse,
        )

    async def jobs(
        self,
        id: str,
        *,
        add_contacts: SequenceNotStr[str] | Omit = omit,
        add_mailing_list_imports: SequenceNotStr[str] | Omit = omit,
        remove_contacts: SequenceNotStr[str] | Omit = omit,
        remove_mailing_list_imports: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MailingList:
        """Runs a mailing list job.

        Mailing list jobs allow you to add or remove contacts
        to your mailing list from mailing list imports or directly with contact IDs.
        Only one job can be ran at a time and jobs are only able to be ran while the
        mailing list has a `status` of "completed".

        Once a job as successfully been kicked off, the mailing list will have a
        `status` of either `creating_contacts` or `removing_contacts` depending on which
        job was ran. After the job has finished, the mailing list will go back into the
        `completed` state where more jobs can be ran. If there are any errors while
        running a job, the `errors` field on the mailing list will contain a list of
        error objects which describe the errors.

        Args:
          add_contacts: List of contact IDs to add to the mailing list. Cannot be used with other
              operations.

          add_mailing_list_imports: List of mailing list import IDs to add to the mailing list. Cannot be used with
              other operations.

          remove_contacts: List of contact IDs to remove from the mailing list. Cannot be used with other
              operations.

          remove_mailing_list_imports: List of mailing list import IDs to remove from the mailing list. Cannot be used
              with other operations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/print-mail/v1/mailing_lists/{id}/jobs",
            body=await async_maybe_transform(
                {
                    "add_contacts": add_contacts,
                    "add_mailing_list_imports": add_mailing_list_imports,
                    "remove_contacts": remove_contacts,
                    "remove_mailing_list_imports": remove_mailing_list_imports,
                },
                mailing_list_jobs_params.MailingListJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailingList,
        )


class MailingListsResourceWithRawResponse:
    def __init__(self, mailing_lists: MailingListsResource) -> None:
        self._mailing_lists = mailing_lists

        self.create = to_raw_response_wrapper(
            mailing_lists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mailing_lists.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mailing_lists.update,
        )
        self.list = to_raw_response_wrapper(
            mailing_lists.list,
        )
        self.delete = to_raw_response_wrapper(
            mailing_lists.delete,
        )
        self.jobs = to_raw_response_wrapper(
            mailing_lists.jobs,
        )


class AsyncMailingListsResourceWithRawResponse:
    def __init__(self, mailing_lists: AsyncMailingListsResource) -> None:
        self._mailing_lists = mailing_lists

        self.create = async_to_raw_response_wrapper(
            mailing_lists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mailing_lists.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mailing_lists.update,
        )
        self.list = async_to_raw_response_wrapper(
            mailing_lists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mailing_lists.delete,
        )
        self.jobs = async_to_raw_response_wrapper(
            mailing_lists.jobs,
        )


class MailingListsResourceWithStreamingResponse:
    def __init__(self, mailing_lists: MailingListsResource) -> None:
        self._mailing_lists = mailing_lists

        self.create = to_streamed_response_wrapper(
            mailing_lists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mailing_lists.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mailing_lists.update,
        )
        self.list = to_streamed_response_wrapper(
            mailing_lists.list,
        )
        self.delete = to_streamed_response_wrapper(
            mailing_lists.delete,
        )
        self.jobs = to_streamed_response_wrapper(
            mailing_lists.jobs,
        )


class AsyncMailingListsResourceWithStreamingResponse:
    def __init__(self, mailing_lists: AsyncMailingListsResource) -> None:
        self._mailing_lists = mailing_lists

        self.create = async_to_streamed_response_wrapper(
            mailing_lists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mailing_lists.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mailing_lists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mailing_lists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mailing_lists.delete,
        )
        self.jobs = async_to_streamed_response_wrapper(
            mailing_lists.jobs,
        )
