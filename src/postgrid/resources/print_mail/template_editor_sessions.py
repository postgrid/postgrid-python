# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.print_mail import template_editor_session_list_params, template_editor_session_create_params
from ...types.print_mail.template_editor_session_list_response import TemplateEditorSessionListResponse
from ...types.print_mail.template_editor_session_create_response import TemplateEditorSessionCreateResponse
from ...types.print_mail.template_editor_session_delete_response import TemplateEditorSessionDeleteResponse

__all__ = ["TemplateEditorSessionsResource", "AsyncTemplateEditorSessionsResource"]


class TemplateEditorSessionsResource(SyncAPIResource):
    """
    You can use template editor sessions to bring the capabilities of our
     template editor to your website. When you create a session, you provide the
     `template` which you want to edit, and we return a session with a `url` that
     you can `iframe` or redirect your customers to.

     When users save their changes in the editor session, it will update the
     underlying template. Note that sessions are only valid for 24 hours, after
     which point they are automatically deleted for security reasons.

     You can have multiple sessions active for the same template at the same time.
     In general, we recommend creating a new session every time you present our
     editor to your users.

     Note: you can use the template editor to modify templates created using HTML,
     but saving a session from the editor will override the original HTML content.
    """

    @cached_property
    def with_raw_response(self) -> TemplateEditorSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return TemplateEditorSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplateEditorSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return TemplateEditorSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        template: str,
        back_url: str | Omit = omit,
        styles: template_editor_session_create_params.Styles | Omit = omit,
        title: str | Omit = omit,
        trackers: Union[Literal["all", "none"], SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateEditorSessionCreateResponse:
        """
        Create a Template Editor Session.

        Note that if no `backURL` is supplied, PostGrid removes the Back button from the
        editor page. This is ideal for when you `iframe` the editor.

        Args:
          template: ID of the underlying template that this edits.

          back_url: The URL supplied when this editor session was created.

          styles: Style overrides for the template editor session.

          title: The title supplied when this editor session was created.

          trackers: Controls which Trackers are displayed in the template editor session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/print-mail/v1/template_editor_sessions",
            body=maybe_transform(
                {
                    "template": template,
                    "back_url": back_url,
                    "styles": styles,
                    "title": title,
                    "trackers": trackers,
                },
                template_editor_session_create_params.TemplateEditorSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateEditorSessionCreateResponse,
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
    ) -> SyncSkipLimit[TemplateEditorSessionListResponse]:
        """
        Retrieve a paginated list of Template Editor Sessions.

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
            "/print-mail/v1/template_editor_sessions",
            page=SyncSkipLimit[TemplateEditorSessionListResponse],
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
                    template_editor_session_list_params.TemplateEditorSessionListParams,
                ),
            ),
            model=TemplateEditorSessionListResponse,
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
    ) -> TemplateEditorSessionDeleteResponse:
        """
        Delete a Template Editor Session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/print-mail/v1/template_editor_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateEditorSessionDeleteResponse,
        )


class AsyncTemplateEditorSessionsResource(AsyncAPIResource):
    """
    You can use template editor sessions to bring the capabilities of our
     template editor to your website. When you create a session, you provide the
     `template` which you want to edit, and we return a session with a `url` that
     you can `iframe` or redirect your customers to.

     When users save their changes in the editor session, it will update the
     underlying template. Note that sessions are only valid for 24 hours, after
     which point they are automatically deleted for security reasons.

     You can have multiple sessions active for the same template at the same time.
     In general, we recommend creating a new session every time you present our
     editor to your users.

     Note: you can use the template editor to modify templates created using HTML,
     but saving a session from the editor will override the original HTML content.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTemplateEditorSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplateEditorSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplateEditorSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncTemplateEditorSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        template: str,
        back_url: str | Omit = omit,
        styles: template_editor_session_create_params.Styles | Omit = omit,
        title: str | Omit = omit,
        trackers: Union[Literal["all", "none"], SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateEditorSessionCreateResponse:
        """
        Create a Template Editor Session.

        Note that if no `backURL` is supplied, PostGrid removes the Back button from the
        editor page. This is ideal for when you `iframe` the editor.

        Args:
          template: ID of the underlying template that this edits.

          back_url: The URL supplied when this editor session was created.

          styles: Style overrides for the template editor session.

          title: The title supplied when this editor session was created.

          trackers: Controls which Trackers are displayed in the template editor session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/print-mail/v1/template_editor_sessions",
            body=await async_maybe_transform(
                {
                    "template": template,
                    "back_url": back_url,
                    "styles": styles,
                    "title": title,
                    "trackers": trackers,
                },
                template_editor_session_create_params.TemplateEditorSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateEditorSessionCreateResponse,
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
    ) -> AsyncPaginator[TemplateEditorSessionListResponse, AsyncSkipLimit[TemplateEditorSessionListResponse]]:
        """
        Retrieve a paginated list of Template Editor Sessions.

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
            "/print-mail/v1/template_editor_sessions",
            page=AsyncSkipLimit[TemplateEditorSessionListResponse],
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
                    template_editor_session_list_params.TemplateEditorSessionListParams,
                ),
            ),
            model=TemplateEditorSessionListResponse,
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
    ) -> TemplateEditorSessionDeleteResponse:
        """
        Delete a Template Editor Session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/print-mail/v1/template_editor_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateEditorSessionDeleteResponse,
        )


class TemplateEditorSessionsResourceWithRawResponse:
    def __init__(self, template_editor_sessions: TemplateEditorSessionsResource) -> None:
        self._template_editor_sessions = template_editor_sessions

        self.create = to_raw_response_wrapper(
            template_editor_sessions.create,
        )
        self.list = to_raw_response_wrapper(
            template_editor_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            template_editor_sessions.delete,
        )


class AsyncTemplateEditorSessionsResourceWithRawResponse:
    def __init__(self, template_editor_sessions: AsyncTemplateEditorSessionsResource) -> None:
        self._template_editor_sessions = template_editor_sessions

        self.create = async_to_raw_response_wrapper(
            template_editor_sessions.create,
        )
        self.list = async_to_raw_response_wrapper(
            template_editor_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            template_editor_sessions.delete,
        )


class TemplateEditorSessionsResourceWithStreamingResponse:
    def __init__(self, template_editor_sessions: TemplateEditorSessionsResource) -> None:
        self._template_editor_sessions = template_editor_sessions

        self.create = to_streamed_response_wrapper(
            template_editor_sessions.create,
        )
        self.list = to_streamed_response_wrapper(
            template_editor_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            template_editor_sessions.delete,
        )


class AsyncTemplateEditorSessionsResourceWithStreamingResponse:
    def __init__(self, template_editor_sessions: AsyncTemplateEditorSessionsResource) -> None:
        self._template_editor_sessions = template_editor_sessions

        self.create = async_to_streamed_response_wrapper(
            template_editor_sessions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            template_editor_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            template_editor_sessions.delete,
        )
