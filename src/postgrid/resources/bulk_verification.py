# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import bulk_verification_list_params, bulk_verification_upload_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.bulk_verification_list_response import BulkVerificationListResponse
from ..types.bulk_verification_upload_response import BulkVerificationUploadResponse
from ..types.bulk_verification_retrieve_response import BulkVerificationRetrieveResponse

__all__ = ["BulkVerificationResource", "AsyncBulkVerificationResource"]


class BulkVerificationResource(SyncAPIResource):
    """
    **Note: For verifying batches of addresses in real-time via JSON, please use
     the "Batch Verify Addresses" endpoint.**

     The bulk verification API allows you to submit CSV files to be processed
     through our address verification engine. Each file can contain up to 250,000
     addresses, and the output lines up with what is returned from our batch
     verification API.

     Note that you will be invoiced for every list that processes successfully.
     You can pre-purchase bulk verification credits from our
     [dashboard](https://app.postgrid.com/dashboard/upgrade) to prevent this.
     However, these cannot be used for geocoded lists, and you must individually
     pay for every list that you process with those flags.

     **Also note that in order to access bulk geocoding you must contact**
     [support@postgrid.com](mailto:support@postgrid.com) **to enable the feature.**
    """

    @cached_property
    def with_raw_response(self) -> BulkVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return BulkVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return BulkVerificationResourceWithStreamingResponse(self)

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
    ) -> BulkVerificationRetrieveResponse:
        """
        Retrieve a single bulk verification list by ID, including its processing status
        and — once processed — a link to the output CSV.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/addver_lists/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkVerificationRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkVerificationListResponse:
        """
        Retrieve a list of your bulk verification lists.

        Args:
          limit: The maximum number of lists to return.

          skip: The number of lists to skip past, for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/addver_lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    bulk_verification_list_params.BulkVerificationListParams,
                ),
            ),
            cast_to=BulkVerificationListResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        mappings: bulk_verification_upload_params.Mappings,
        name: str,
        default_country: str | Omit = omit,
        run_ccoa: bool | Omit = omit,
        run_ncoa: bool | Omit = omit,
        use_geocode: bool | Omit = omit,
        use_intl_verification: bool | Omit = omit,
        use_proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkVerificationUploadResponse:
        """Upload a CSV file of addresses to be verified in bulk.

        Supply a `mappings`
        object describing which CSV columns correspond to which address fields.

        Args:
          mappings: The mapping of your CSV column names to PostGrid address fields. Each value is
              the name of a column in your uploaded file.

          name: A name for the uploaded list. This only affects what is displayed in the
              dashboard.

          default_country: An ISO 2-letter country code used as the fallback when a row is missing a value
              in the `country` column.

          run_ccoa: Whether to run CCOA (Canada Post change of address) on the list. Note that a
              list cannot run both NCOA and CCOA — split mixed US/Canadian files into separate
              lists.

          run_ncoa: Whether to run NCOA (US National Change of Address) on the list.

          use_geocode: Whether to append geographical location information (latitude, longitude) to
              your output. Bulk geocoding must be enabled by contacting support.

          use_intl_verification: Whether to perform international (outside US & Canada) verification.

          use_proper_case: Whether to return addresses in Proper Case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "mappings": mappings,
                "name": name,
                "default_country": default_country,
                "run_ccoa": run_ccoa,
                "run_ncoa": run_ncoa,
                "use_geocode": use_geocode,
                "use_intl_verification": use_intl_verification,
                "use_proper_case": use_proper_case,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/addver_lists",
            body=maybe_transform(body, bulk_verification_upload_params.BulkVerificationUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkVerificationUploadResponse,
        )


class AsyncBulkVerificationResource(AsyncAPIResource):
    """
    **Note: For verifying batches of addresses in real-time via JSON, please use
     the "Batch Verify Addresses" endpoint.**

     The bulk verification API allows you to submit CSV files to be processed
     through our address verification engine. Each file can contain up to 250,000
     addresses, and the output lines up with what is returned from our batch
     verification API.

     Note that you will be invoiced for every list that processes successfully.
     You can pre-purchase bulk verification credits from our
     [dashboard](https://app.postgrid.com/dashboard/upgrade) to prevent this.
     However, these cannot be used for geocoded lists, and you must individually
     pay for every list that you process with those flags.

     **Also note that in order to access bulk geocoding you must contact**
     [support@postgrid.com](mailto:support@postgrid.com) **to enable the feature.**
    """

    @cached_property
    def with_raw_response(self) -> AsyncBulkVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncBulkVerificationResourceWithStreamingResponse(self)

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
    ) -> BulkVerificationRetrieveResponse:
        """
        Retrieve a single bulk verification list by ID, including its processing status
        and — once processed — a link to the output CSV.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/addver_lists/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkVerificationRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkVerificationListResponse:
        """
        Retrieve a list of your bulk verification lists.

        Args:
          limit: The maximum number of lists to return.

          skip: The number of lists to skip past, for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/addver_lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    bulk_verification_list_params.BulkVerificationListParams,
                ),
            ),
            cast_to=BulkVerificationListResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        mappings: bulk_verification_upload_params.Mappings,
        name: str,
        default_country: str | Omit = omit,
        run_ccoa: bool | Omit = omit,
        run_ncoa: bool | Omit = omit,
        use_geocode: bool | Omit = omit,
        use_intl_verification: bool | Omit = omit,
        use_proper_case: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkVerificationUploadResponse:
        """Upload a CSV file of addresses to be verified in bulk.

        Supply a `mappings`
        object describing which CSV columns correspond to which address fields.

        Args:
          mappings: The mapping of your CSV column names to PostGrid address fields. Each value is
              the name of a column in your uploaded file.

          name: A name for the uploaded list. This only affects what is displayed in the
              dashboard.

          default_country: An ISO 2-letter country code used as the fallback when a row is missing a value
              in the `country` column.

          run_ccoa: Whether to run CCOA (Canada Post change of address) on the list. Note that a
              list cannot run both NCOA and CCOA — split mixed US/Canadian files into separate
              lists.

          run_ncoa: Whether to run NCOA (US National Change of Address) on the list.

          use_geocode: Whether to append geographical location information (latitude, longitude) to
              your output. Bulk geocoding must be enabled by contacting support.

          use_intl_verification: Whether to perform international (outside US & Canada) verification.

          use_proper_case: Whether to return addresses in Proper Case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "mappings": mappings,
                "name": name,
                "default_country": default_country,
                "run_ccoa": run_ccoa,
                "run_ncoa": run_ncoa,
                "use_geocode": use_geocode,
                "use_intl_verification": use_intl_verification,
                "use_proper_case": use_proper_case,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/addver_lists",
            body=await async_maybe_transform(body, bulk_verification_upload_params.BulkVerificationUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkVerificationUploadResponse,
        )


class BulkVerificationResourceWithRawResponse:
    def __init__(self, bulk_verification: BulkVerificationResource) -> None:
        self._bulk_verification = bulk_verification

        self.retrieve = to_raw_response_wrapper(
            bulk_verification.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bulk_verification.list,
        )
        self.upload = to_raw_response_wrapper(
            bulk_verification.upload,
        )


class AsyncBulkVerificationResourceWithRawResponse:
    def __init__(self, bulk_verification: AsyncBulkVerificationResource) -> None:
        self._bulk_verification = bulk_verification

        self.retrieve = async_to_raw_response_wrapper(
            bulk_verification.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bulk_verification.list,
        )
        self.upload = async_to_raw_response_wrapper(
            bulk_verification.upload,
        )


class BulkVerificationResourceWithStreamingResponse:
    def __init__(self, bulk_verification: BulkVerificationResource) -> None:
        self._bulk_verification = bulk_verification

        self.retrieve = to_streamed_response_wrapper(
            bulk_verification.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bulk_verification.list,
        )
        self.upload = to_streamed_response_wrapper(
            bulk_verification.upload,
        )


class AsyncBulkVerificationResourceWithStreamingResponse:
    def __init__(self, bulk_verification: AsyncBulkVerificationResource) -> None:
        self._bulk_verification = bulk_verification

        self.retrieve = async_to_streamed_response_wrapper(
            bulk_verification.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bulk_verification.list,
        )
        self.upload = async_to_streamed_response_wrapper(
            bulk_verification.upload,
        )
