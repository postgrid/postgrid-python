# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, strip_not_given, async_maybe_transform
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
    campaign_list_params,
    campaign_send_params,
    campaign_create_params,
    campaign_update_params,
)
from ...types.print_mail.campaign import Campaign
from ...types.print_mail.campaign_delete_response import CampaignDeleteResponse

__all__ = ["CampaignsResource", "AsyncCampaignsResource"]


class CampaignsResource(SyncAPIResource):
    """
    The campaigns API enables you to send out large volumes of fully
     personalized mail to a mailing list.
    """

    @cached_property
    def with_raw_response(self) -> CampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return CampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return CampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        mailing_list: str,
        cheque: campaign_create_params.Cheque | Omit = omit,
        default_sender_contact: str | Omit = omit,
        description: str | Omit = omit,
        letter: campaign_create_params.Letter | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        postcard: campaign_create_params.Postcard | Omit = omit,
        self_mailer: campaign_create_params.SelfMailer | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        snap_pack: campaign_create_params.SnapPack | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Create a new campaign.

        A campaign links a mailing list with a specific mail piece configuration
        (letter, postcard, cheque, self-mailer, or snap pack) to send bulk mail. Only
        one collateral type can be set per campaign.

        Upon creation, the campaign enters the `drafting` status while assets are
        validated.

        Args:
          mailing_list: The ID of the mailing list associated with this campaign.

          cheque: Inline cheque configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          default_sender_contact: The ID of the default sender contact to use for orders if not specified per
              recipient.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          letter: Inline letter configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          metadata: See the section on Metadata.

          postcard: Inline postcard configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          self_mailer: Inline self-mailer configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          send_date: The scheduled date and time for the campaign to be sent.

          snap_pack: Inline snap pack configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "mailing_list": mailing_list,
                "cheque": cheque,
                "default_sender_contact": default_sender_contact,
                "description": description,
                "letter": letter,
                "metadata": metadata,
                "postcard": postcard,
                "self_mailer": self_mailer,
                "send_date": send_date,
                "snap_pack": snap_pack,
            },
            [
                ["letter", "pdf"],
                ["postcard", "pdf"],
                ["cheque", "letterPDF"],
                ["selfMailer", "pdf"],
                ["snapPack", "pdf"],
            ],
        )
        files = extract_files(
            cast(Mapping[str, object], body),
            paths=[
                ["letter", "pdf"],
                ["postcard", "pdf"],
                ["cheque", "letterPDF"],
                ["selfMailer", "pdf"],
                ["snapPack", "pdf"],
            ],
        )
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/print-mail/v1/campaigns",
            body=maybe_transform(body, campaign_create_params.CampaignCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
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
    ) -> Campaign:
        """
        Retrieve a specific campaign by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    def update(
        self,
        id: str,
        *,
        cheque: Optional[campaign_update_params.Cheque] | Omit = omit,
        default_sender_contact: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        letter: Optional[campaign_update_params.Letter] | Omit = omit,
        mailing_list: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        postcard: Optional[campaign_update_params.Postcard] | Omit = omit,
        self_mailer: Optional[campaign_update_params.SelfMailer] | Omit = omit,
        snap_pack: Optional[campaign_update_params.SnapPack] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Update an existing campaign.

        Campaigns can only be updated if they are in the `draft` or `changes_required`
        status. Updating a campaign will trigger reprocessing and set its status back to
        `drafting`.

        Args:
          cheque: Inline cheque configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          default_sender_contact: The ID of the default sender contact. Set to `null` to remove.

          description: An optional description for the campaign. Set to `null` to remove the existing
              description.

          letter: Inline letter configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          mailing_list: The ID of the mailing list to associate with this campaign.

          metadata: Optional key-value data associated with the campaign. Set to `null` to remove
              existing metadata.

          postcard: Inline postcard configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          self_mailer: Inline self-mailer configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          snap_pack: Inline snap pack configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            body=maybe_transform(
                {
                    "cheque": cheque,
                    "default_sender_contact": default_sender_contact,
                    "description": description,
                    "letter": letter,
                    "mailing_list": mailing_list,
                    "metadata": metadata,
                    "postcard": postcard,
                    "self_mailer": self_mailer,
                    "snap_pack": snap_pack,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
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
    ) -> SyncSkipLimit[Campaign]:
        """
        Retrieve a list of campaigns.

        Returns a paginated list of campaigns associated with the authenticated
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
            "/print-mail/v1/campaigns",
            page=SyncSkipLimit[Campaign],
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
                    campaign_list_params.CampaignListParams,
                ),
            ),
            model=Campaign,
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
    ) -> CampaignDeleteResponse:
        """
        Delete a campaign.

        Campaigns can only be deleted if they are in `draft`, `changes_required`, or
        `ready` status. This also permanently deletes associated resources. This
        operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDeleteResponse,
        )

    def send(
        self,
        id: str,
        *,
        send_date: Union[Union[str, datetime], str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Send a campaign for processing.

        This action transitions a campaign from the `draft` status to `creating_orders`.
        You can optionally specify a future `sendDate`. Once sent, the campaign cannot
        be updated.

        Args:
          send_date: The date and time the campaign should be sent. Must be in the future. If
              omitted, defaults to the earliest possible processing date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/print-mail/v1/campaigns/{id}/send", id=id),
            body=maybe_transform({"send_date": send_date}, campaign_send_params.CampaignSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )


class AsyncCampaignsResource(AsyncAPIResource):
    """
    The campaigns API enables you to send out large volumes of fully
     personalized mail to a mailing list.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        mailing_list: str,
        cheque: campaign_create_params.Cheque | Omit = omit,
        default_sender_contact: str | Omit = omit,
        description: str | Omit = omit,
        letter: campaign_create_params.Letter | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        postcard: campaign_create_params.Postcard | Omit = omit,
        self_mailer: campaign_create_params.SelfMailer | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        snap_pack: campaign_create_params.SnapPack | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Create a new campaign.

        A campaign links a mailing list with a specific mail piece configuration
        (letter, postcard, cheque, self-mailer, or snap pack) to send bulk mail. Only
        one collateral type can be set per campaign.

        Upon creation, the campaign enters the `drafting` status while assets are
        validated.

        Args:
          mailing_list: The ID of the mailing list associated with this campaign.

          cheque: Inline cheque configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          default_sender_contact: The ID of the default sender contact to use for orders if not specified per
              recipient.

          description: An optional string describing this resource. Will be visible in the API and the
              dashboard.

          letter: Inline letter configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          metadata: See the section on Metadata.

          postcard: Inline postcard configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          self_mailer: Inline self-mailer configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          send_date: The scheduled date and time for the campaign to be sent.

          snap_pack: Inline snap pack configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "mailing_list": mailing_list,
                "cheque": cheque,
                "default_sender_contact": default_sender_contact,
                "description": description,
                "letter": letter,
                "metadata": metadata,
                "postcard": postcard,
                "self_mailer": self_mailer,
                "send_date": send_date,
                "snap_pack": snap_pack,
            },
            [
                ["letter", "pdf"],
                ["postcard", "pdf"],
                ["cheque", "letterPDF"],
                ["selfMailer", "pdf"],
                ["snapPack", "pdf"],
            ],
        )
        files = extract_files(
            cast(Mapping[str, object], body),
            paths=[
                ["letter", "pdf"],
                ["postcard", "pdf"],
                ["cheque", "letterPDF"],
                ["selfMailer", "pdf"],
                ["snapPack", "pdf"],
            ],
        )
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/print-mail/v1/campaigns",
            body=await async_maybe_transform(body, campaign_create_params.CampaignCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
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
    ) -> Campaign:
        """
        Retrieve a specific campaign by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )

    async def update(
        self,
        id: str,
        *,
        cheque: Optional[campaign_update_params.Cheque] | Omit = omit,
        default_sender_contact: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        letter: Optional[campaign_update_params.Letter] | Omit = omit,
        mailing_list: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        postcard: Optional[campaign_update_params.Postcard] | Omit = omit,
        self_mailer: Optional[campaign_update_params.SelfMailer] | Omit = omit,
        snap_pack: Optional[campaign_update_params.SnapPack] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Update an existing campaign.

        Campaigns can only be updated if they are in the `draft` or `changes_required`
        status. Updating a campaign will trigger reprocessing and set its status back to
        `drafting`.

        Args:
          cheque: Inline cheque configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          default_sender_contact: The ID of the default sender contact. Set to `null` to remove.

          description: An optional description for the campaign. Set to `null` to remove the existing
              description.

          letter: Inline letter configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          mailing_list: The ID of the mailing list to associate with this campaign.

          metadata: Optional key-value data associated with the campaign. Set to `null` to remove
              existing metadata.

          postcard: Inline postcard configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          self_mailer: Inline self-mailer configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          snap_pack: Inline snap pack configuration for a campaign. All fields are optional since
              campaigns may be in a partial state during drafting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "cheque": cheque,
                    "default_sender_contact": default_sender_contact,
                    "description": description,
                    "letter": letter,
                    "mailing_list": mailing_list,
                    "metadata": metadata,
                    "postcard": postcard,
                    "self_mailer": self_mailer,
                    "snap_pack": snap_pack,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
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
    ) -> AsyncPaginator[Campaign, AsyncSkipLimit[Campaign]]:
        """
        Retrieve a list of campaigns.

        Returns a paginated list of campaigns associated with the authenticated
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
            "/print-mail/v1/campaigns",
            page=AsyncSkipLimit[Campaign],
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
                    campaign_list_params.CampaignListParams,
                ),
            ),
            model=Campaign,
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
    ) -> CampaignDeleteResponse:
        """
        Delete a campaign.

        Campaigns can only be deleted if they are in `draft`, `changes_required`, or
        `ready` status. This also permanently deletes associated resources. This
        operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/print-mail/v1/campaigns/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CampaignDeleteResponse,
        )

    async def send(
        self,
        id: str,
        *,
        send_date: Union[Union[str, datetime], str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Campaign:
        """
        Send a campaign for processing.

        This action transitions a campaign from the `draft` status to `creating_orders`.
        You can optionally specify a future `sendDate`. Once sent, the campaign cannot
        be updated.

        Args:
          send_date: The date and time the campaign should be sent. Must be in the future. If
              omitted, defaults to the earliest possible processing date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/print-mail/v1/campaigns/{id}/send", id=id),
            body=await async_maybe_transform({"send_date": send_date}, campaign_send_params.CampaignSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Campaign,
        )


class CampaignsResourceWithRawResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = to_raw_response_wrapper(
            campaigns.delete,
        )
        self.send = to_raw_response_wrapper(
            campaigns.send,
        )


class AsyncCampaignsResourceWithRawResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            campaigns.delete,
        )
        self.send = async_to_raw_response_wrapper(
            campaigns.send,
        )


class CampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.send = to_streamed_response_wrapper(
            campaigns.send,
        )


class AsyncCampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            campaigns.delete,
        )
        self.send = async_to_streamed_response_wrapper(
            campaigns.send,
        )
