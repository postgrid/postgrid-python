# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cheques import (
    ChequesResource,
    AsyncChequesResource,
    ChequesResourceWithRawResponse,
    AsyncChequesResourceWithRawResponse,
    ChequesResourceWithStreamingResponse,
    AsyncChequesResourceWithStreamingResponse,
)
from .letters import (
    LettersResource,
    AsyncLettersResource,
    LettersResourceWithRawResponse,
    AsyncLettersResourceWithRawResponse,
    LettersResourceWithStreamingResponse,
    AsyncLettersResourceWithStreamingResponse,
)
from .postcards import (
    PostcardsResource,
    AsyncPostcardsResource,
    PostcardsResourceWithRawResponse,
    AsyncPostcardsResourceWithRawResponse,
    PostcardsResourceWithStreamingResponse,
    AsyncPostcardsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .self_mailers import (
    SelfMailersResource,
    AsyncSelfMailersResource,
    SelfMailersResourceWithRawResponse,
    AsyncSelfMailersResourceWithRawResponse,
    SelfMailersResourceWithStreamingResponse,
    AsyncSelfMailersResourceWithStreamingResponse,
)

__all__ = ["OrderProfilesResource", "AsyncOrderProfilesResource"]


class OrderProfilesResource(SyncAPIResource):
    @cached_property
    def cheques(self) -> ChequesResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return ChequesResource(self._client)

    @cached_property
    def letters(self) -> LettersResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return LettersResource(self._client)

    @cached_property
    def postcards(self) -> PostcardsResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return PostcardsResource(self._client)

    @cached_property
    def self_mailers(self) -> SelfMailersResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return SelfMailersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrderProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return OrderProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return OrderProfilesResourceWithStreamingResponse(self)


class AsyncOrderProfilesResource(AsyncAPIResource):
    @cached_property
    def cheques(self) -> AsyncChequesResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncChequesResource(self._client)

    @cached_property
    def letters(self) -> AsyncLettersResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncLettersResource(self._client)

    @cached_property
    def postcards(self) -> AsyncPostcardsResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncPostcardsResource(self._client)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResource:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncSelfMailersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrderProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncOrderProfilesResourceWithStreamingResponse(self)


class OrderProfilesResourceWithRawResponse:
    def __init__(self, order_profiles: OrderProfilesResource) -> None:
        self._order_profiles = order_profiles

    @cached_property
    def cheques(self) -> ChequesResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return ChequesResourceWithRawResponse(self._order_profiles.cheques)

    @cached_property
    def letters(self) -> LettersResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return LettersResourceWithRawResponse(self._order_profiles.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return PostcardsResourceWithRawResponse(self._order_profiles.postcards)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return SelfMailersResourceWithRawResponse(self._order_profiles.self_mailers)


class AsyncOrderProfilesResourceWithRawResponse:
    def __init__(self, order_profiles: AsyncOrderProfilesResource) -> None:
        self._order_profiles = order_profiles

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncChequesResourceWithRawResponse(self._order_profiles.cheques)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncLettersResourceWithRawResponse(self._order_profiles.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncPostcardsResourceWithRawResponse(self._order_profiles.postcards)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithRawResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncSelfMailersResourceWithRawResponse(self._order_profiles.self_mailers)


class OrderProfilesResourceWithStreamingResponse:
    def __init__(self, order_profiles: OrderProfilesResource) -> None:
        self._order_profiles = order_profiles

    @cached_property
    def cheques(self) -> ChequesResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return ChequesResourceWithStreamingResponse(self._order_profiles.cheques)

    @cached_property
    def letters(self) -> LettersResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return LettersResourceWithStreamingResponse(self._order_profiles.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return PostcardsResourceWithStreamingResponse(self._order_profiles.postcards)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return SelfMailersResourceWithStreamingResponse(self._order_profiles.self_mailers)


class AsyncOrderProfilesResourceWithStreamingResponse:
    def __init__(self, order_profiles: AsyncOrderProfilesResource) -> None:
        self._order_profiles = order_profiles

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncChequesResourceWithStreamingResponse(self._order_profiles.cheques)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncLettersResourceWithStreamingResponse(self._order_profiles.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncPostcardsResourceWithStreamingResponse(self._order_profiles.postcards)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithStreamingResponse:
        """
        Order Profiles are reusable blueprints for creating print and mail orders (Letters, Postcards, Cheques, Self-Mailers).
         They define common properties like size, content (via templates or uploaded PDFs), mailing class, and metadata.
         Using profiles simplifies order creation, especially for recurring mailings or campaigns, by pre-filling many parameters.

         Profiles are environment-specific (live vs. test).
        """
        return AsyncSelfMailersResourceWithStreamingResponse(self._order_profiles.self_mailers)
