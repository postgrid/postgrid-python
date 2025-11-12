# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.print_mail import contact_list_params, contact_create_params
from ...types.print_mail.contact import Contact
from ...types.print_mail.contact_delete_response import ContactDeleteResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        address_line1: str,
        country_code: str,
        first_name: str,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Creates a contact.

        This will also verify the contact's address **if you create
        it using a live API key**. To sucessfully create a contact, either a
        `firstName`, a `companyName`, or both are required. You can supply both, but you
        **cannot** supply neither.

        You have the option to supply the entire address (except for `countryCode`) via
        `addressLine1`, in which case PostGrid will parse it automatically. However,
        this is **not guaranteed to be correct**, so we recommend passing along the
        structured address fields (`city`, `provinceOrState`, etc) if you have them.

        _Note that if you create a contact that has identical information to another
        contact, this will simply update the description of the existing contact and
        return it. This avoids creating duplicate contacts._

        Args:
          address_line1: The first line of the contact's address.

          country_code: The ISO 3611-1 country code of the contact's address.

          address_line2: Second line of the contact's address, if applicable.

          city: The city of the contact's address.

          company_name: Company name of the contact.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          email: Email of the contact.

          force_verified_status: If `true`, PostGrid will force this contact to have an `addressStatus` of
              `verified` even if our address verification system says otherwise.

          job_title: Job title of the contact.

          last_name: Last name of the contact.

          metadata: See the section on Metadata.

          phone_number: Phone number of the contact.

          postal_or_zip: The postal or ZIP code of the contact's address.

          province_or_state: Province or state of the contact's address.

          skip_verification: If `true`, PostGrid will skip running this contact's address through our address
              verification system.

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
        address_line1: str,
        company_name: str,
        country_code: str,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Creates a contact.

        This will also verify the contact's address **if you create
        it using a live API key**. To sucessfully create a contact, either a
        `firstName`, a `companyName`, or both are required. You can supply both, but you
        **cannot** supply neither.

        You have the option to supply the entire address (except for `countryCode`) via
        `addressLine1`, in which case PostGrid will parse it automatically. However,
        this is **not guaranteed to be correct**, so we recommend passing along the
        structured address fields (`city`, `provinceOrState`, etc) if you have them.

        _Note that if you create a contact that has identical information to another
        contact, this will simply update the description of the existing contact and
        return it. This avoids creating duplicate contacts._

        Args:
          address_line1: The first line of the contact's address.

          country_code: The ISO 3611-1 country code of the contact's address.

          address_line2: Second line of the contact's address, if applicable.

          city: The city of the contact's address.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          email: Email of the contact.

          first_name: First name of the contact.

          force_verified_status: If `true`, PostGrid will force this contact to have an `addressStatus` of
              `verified` even if our address verification system says otherwise.

          job_title: Job title of the contact.

          last_name: Last name of the contact.

          metadata: See the section on Metadata.

          phone_number: Phone number of the contact.

          postal_or_zip: The postal or ZIP code of the contact's address.

          province_or_state: Province or state of the contact's address.

          skip_verification: If `true`, PostGrid will skip running this contact's address through our address
              verification system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address_line1", "country_code", "first_name"], ["address_line1", "company_name", "country_code"])
    def create(
        self,
        *,
        address_line1: str,
        country_code: str,
        first_name: str | Omit = omit,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        return self._post(
            "/print-mail/v1/contacts",
            body=maybe_transform(
                {
                    "address_line1": address_line1,
                    "country_code": country_code,
                    "first_name": first_name,
                    "address_line2": address_line2,
                    "city": city,
                    "company_name": company_name,
                    "description": description,
                    "email": email,
                    "force_verified_status": force_verified_status,
                    "job_title": job_title,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "postal_or_zip": postal_or_zip,
                    "province_or_state": province_or_state,
                    "skip_verification": skip_verification,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
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
    ) -> Contact:
        """
        Retrieve a contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/print-mail/v1/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
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
    ) -> SyncSkipLimit[Contact]:
        """
        Get a list of contacts.

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
            "/print-mail/v1/contacts",
            page=SyncSkipLimit[Contact],
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
                    contact_list_params.ContactListParams,
                ),
            ),
            model=Contact,
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
    ) -> ContactDeleteResponse:
        """Delete a contact.

        Note that this will not affect orders that were sent to this
        contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/print-mail/v1/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleteResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        address_line1: str,
        country_code: str,
        first_name: str,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Creates a contact.

        This will also verify the contact's address **if you create
        it using a live API key**. To sucessfully create a contact, either a
        `firstName`, a `companyName`, or both are required. You can supply both, but you
        **cannot** supply neither.

        You have the option to supply the entire address (except for `countryCode`) via
        `addressLine1`, in which case PostGrid will parse it automatically. However,
        this is **not guaranteed to be correct**, so we recommend passing along the
        structured address fields (`city`, `provinceOrState`, etc) if you have them.

        _Note that if you create a contact that has identical information to another
        contact, this will simply update the description of the existing contact and
        return it. This avoids creating duplicate contacts._

        Args:
          address_line1: The first line of the contact's address.

          country_code: The ISO 3611-1 country code of the contact's address.

          address_line2: Second line of the contact's address, if applicable.

          city: The city of the contact's address.

          company_name: Company name of the contact.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          email: Email of the contact.

          force_verified_status: If `true`, PostGrid will force this contact to have an `addressStatus` of
              `verified` even if our address verification system says otherwise.

          job_title: Job title of the contact.

          last_name: Last name of the contact.

          metadata: See the section on Metadata.

          phone_number: Phone number of the contact.

          postal_or_zip: The postal or ZIP code of the contact's address.

          province_or_state: Province or state of the contact's address.

          skip_verification: If `true`, PostGrid will skip running this contact's address through our address
              verification system.

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
        address_line1: str,
        company_name: str,
        country_code: str,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        """Creates a contact.

        This will also verify the contact's address **if you create
        it using a live API key**. To sucessfully create a contact, either a
        `firstName`, a `companyName`, or both are required. You can supply both, but you
        **cannot** supply neither.

        You have the option to supply the entire address (except for `countryCode`) via
        `addressLine1`, in which case PostGrid will parse it automatically. However,
        this is **not guaranteed to be correct**, so we recommend passing along the
        structured address fields (`city`, `provinceOrState`, etc) if you have them.

        _Note that if you create a contact that has identical information to another
        contact, this will simply update the description of the existing contact and
        return it. This avoids creating duplicate contacts._

        Args:
          address_line1: The first line of the contact's address.

          country_code: The ISO 3611-1 country code of the contact's address.

          address_line2: Second line of the contact's address, if applicable.

          city: The city of the contact's address.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          email: Email of the contact.

          first_name: First name of the contact.

          force_verified_status: If `true`, PostGrid will force this contact to have an `addressStatus` of
              `verified` even if our address verification system says otherwise.

          job_title: Job title of the contact.

          last_name: Last name of the contact.

          metadata: See the section on Metadata.

          phone_number: Phone number of the contact.

          postal_or_zip: The postal or ZIP code of the contact's address.

          province_or_state: Province or state of the contact's address.

          skip_verification: If `true`, PostGrid will skip running this contact's address through our address
              verification system.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["address_line1", "country_code", "first_name"], ["address_line1", "company_name", "country_code"])
    async def create(
        self,
        *,
        address_line1: str,
        country_code: str,
        first_name: str | Omit = omit,
        address_line2: str | Omit = omit,
        city: str | Omit = omit,
        company_name: str | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        force_verified_status: bool | Omit = omit,
        job_title: str | Omit = omit,
        last_name: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        phone_number: str | Omit = omit,
        postal_or_zip: str | Omit = omit,
        province_or_state: str | Omit = omit,
        skip_verification: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Contact:
        return await self._post(
            "/print-mail/v1/contacts",
            body=await async_maybe_transform(
                {
                    "address_line1": address_line1,
                    "country_code": country_code,
                    "first_name": first_name,
                    "address_line2": address_line2,
                    "city": city,
                    "company_name": company_name,
                    "description": description,
                    "email": email,
                    "force_verified_status": force_verified_status,
                    "job_title": job_title,
                    "last_name": last_name,
                    "metadata": metadata,
                    "phone_number": phone_number,
                    "postal_or_zip": postal_or_zip,
                    "province_or_state": province_or_state,
                    "skip_verification": skip_verification,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
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
    ) -> Contact:
        """
        Retrieve a contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/print-mail/v1/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
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
    ) -> AsyncPaginator[Contact, AsyncSkipLimit[Contact]]:
        """
        Get a list of contacts.

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
            "/print-mail/v1/contacts",
            page=AsyncSkipLimit[Contact],
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
                    contact_list_params.ContactListParams,
                ),
            ),
            model=Contact,
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
    ) -> ContactDeleteResponse:
        """Delete a contact.

        Note that this will not affect orders that were sent to this
        contact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/print-mail/v1/contacts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactDeleteResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = to_raw_response_wrapper(
            contacts.delete,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contacts.delete,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contacts.delete,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contacts.delete,
        )
