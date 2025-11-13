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
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .campaigns import (
    CampaignsResource,
    AsyncCampaignsResource,
    CampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
    AsyncCampaignsResourceWithStreamingResponse,
)
from .postcards import (
    PostcardsResource,
    AsyncPostcardsResource,
    PostcardsResourceWithRawResponse,
    AsyncPostcardsResourceWithRawResponse,
    PostcardsResourceWithStreamingResponse,
    AsyncPostcardsResourceWithStreamingResponse,
)
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .self_mailers import (
    SelfMailersResource,
    AsyncSelfMailersResource,
    SelfMailersResourceWithRawResponse,
    AsyncSelfMailersResourceWithRawResponse,
    SelfMailersResourceWithStreamingResponse,
    AsyncSelfMailersResourceWithStreamingResponse,
)
from .bank_accounts import (
    BankAccountsResource,
    AsyncBankAccountsResource,
    BankAccountsResourceWithRawResponse,
    AsyncBankAccountsResourceWithRawResponse,
    BankAccountsResourceWithStreamingResponse,
    AsyncBankAccountsResourceWithStreamingResponse,
)
from .mailing_lists import (
    MailingListsResource,
    AsyncMailingListsResource,
    MailingListsResourceWithRawResponse,
    AsyncMailingListsResourceWithRawResponse,
    MailingListsResourceWithStreamingResponse,
    AsyncMailingListsResourceWithStreamingResponse,
)
from .reports.reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from .sub_organizations import (
    SubOrganizationsResource,
    AsyncSubOrganizationsResource,
    SubOrganizationsResourceWithRawResponse,
    AsyncSubOrganizationsResourceWithRawResponse,
    SubOrganizationsResourceWithStreamingResponse,
    AsyncSubOrganizationsResourceWithStreamingResponse,
)
from .mailing_list_imports import (
    MailingListImportsResource,
    AsyncMailingListImportsResource,
    MailingListImportsResourceWithRawResponse,
    AsyncMailingListImportsResourceWithRawResponse,
    MailingListImportsResourceWithStreamingResponse,
    AsyncMailingListImportsResourceWithStreamingResponse,
)
from .order_profiles.order_profiles import (
    OrderProfilesResource,
    AsyncOrderProfilesResource,
    OrderProfilesResourceWithRawResponse,
    AsyncOrderProfilesResourceWithRawResponse,
    OrderProfilesResourceWithStreamingResponse,
    AsyncOrderProfilesResourceWithStreamingResponse,
)

__all__ = ["PrintMailResource", "AsyncPrintMailResource"]


class PrintMailResource(SyncAPIResource):
    @cached_property
    def bank_accounts(self) -> BankAccountsResource:
        return BankAccountsResource(self._client)

    @cached_property
    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    @cached_property
    def cheques(self) -> ChequesResource:
        return ChequesResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def letters(self) -> LettersResource:
        return LettersResource(self._client)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResource:
        return MailingListImportsResource(self._client)

    @cached_property
    def mailing_lists(self) -> MailingListsResource:
        return MailingListsResource(self._client)

    @cached_property
    def order_profiles(self) -> OrderProfilesResource:
        return OrderProfilesResource(self._client)

    @cached_property
    def postcards(self) -> PostcardsResource:
        return PostcardsResource(self._client)

    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def self_mailers(self) -> SelfMailersResource:
        return SelfMailersResource(self._client)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResource:
        return SubOrganizationsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrintMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return PrintMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrintMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return PrintMailResourceWithStreamingResponse(self)


class AsyncPrintMailResource(AsyncAPIResource):
    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResource:
        return AsyncBankAccountsResource(self._client)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        return AsyncCampaignsResource(self._client)

    @cached_property
    def cheques(self) -> AsyncChequesResource:
        return AsyncChequesResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def letters(self) -> AsyncLettersResource:
        return AsyncLettersResource(self._client)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResource:
        return AsyncMailingListImportsResource(self._client)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResource:
        return AsyncMailingListsResource(self._client)

    @cached_property
    def order_profiles(self) -> AsyncOrderProfilesResource:
        return AsyncOrderProfilesResource(self._client)

    @cached_property
    def postcards(self) -> AsyncPostcardsResource:
        return AsyncPostcardsResource(self._client)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResource:
        return AsyncSelfMailersResource(self._client)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResource:
        return AsyncSubOrganizationsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrintMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/postgrid/postgrid-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrintMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrintMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/postgrid/postgrid-python#with_streaming_response
        """
        return AsyncPrintMailResourceWithStreamingResponse(self)


class PrintMailResourceWithRawResponse:
    def __init__(self, print_mail: PrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithRawResponse:
        return BankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        return CampaignsResourceWithRawResponse(self._print_mail.campaigns)

    @cached_property
    def cheques(self) -> ChequesResourceWithRawResponse:
        return ChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def letters(self) -> LettersResourceWithRawResponse:
        return LettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResourceWithRawResponse:
        return MailingListImportsResourceWithRawResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> MailingListsResourceWithRawResponse:
        return MailingListsResourceWithRawResponse(self._print_mail.mailing_lists)

    @cached_property
    def order_profiles(self) -> OrderProfilesResourceWithRawResponse:
        return OrderProfilesResourceWithRawResponse(self._print_mail.order_profiles)

    @cached_property
    def postcards(self) -> PostcardsResourceWithRawResponse:
        return PostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._print_mail.reports)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithRawResponse:
        return SelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResourceWithRawResponse:
        return SubOrganizationsResourceWithRawResponse(self._print_mail.sub_organizations)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._print_mail.templates)


class AsyncPrintMailResourceWithRawResponse:
    def __init__(self, print_mail: AsyncPrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithRawResponse:
        return AsyncBankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        return AsyncCampaignsResourceWithRawResponse(self._print_mail.campaigns)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithRawResponse:
        return AsyncChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithRawResponse:
        return AsyncLettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResourceWithRawResponse:
        return AsyncMailingListImportsResourceWithRawResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResourceWithRawResponse:
        return AsyncMailingListsResourceWithRawResponse(self._print_mail.mailing_lists)

    @cached_property
    def order_profiles(self) -> AsyncOrderProfilesResourceWithRawResponse:
        return AsyncOrderProfilesResourceWithRawResponse(self._print_mail.order_profiles)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithRawResponse:
        return AsyncPostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._print_mail.reports)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithRawResponse:
        return AsyncSelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResourceWithRawResponse:
        return AsyncSubOrganizationsResourceWithRawResponse(self._print_mail.sub_organizations)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._print_mail.templates)


class PrintMailResourceWithStreamingResponse:
    def __init__(self, print_mail: PrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithStreamingResponse:
        return BankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        return CampaignsResourceWithStreamingResponse(self._print_mail.campaigns)

    @cached_property
    def cheques(self) -> ChequesResourceWithStreamingResponse:
        return ChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def letters(self) -> LettersResourceWithStreamingResponse:
        return LettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResourceWithStreamingResponse:
        return MailingListImportsResourceWithStreamingResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> MailingListsResourceWithStreamingResponse:
        return MailingListsResourceWithStreamingResponse(self._print_mail.mailing_lists)

    @cached_property
    def order_profiles(self) -> OrderProfilesResourceWithStreamingResponse:
        return OrderProfilesResourceWithStreamingResponse(self._print_mail.order_profiles)

    @cached_property
    def postcards(self) -> PostcardsResourceWithStreamingResponse:
        return PostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._print_mail.reports)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithStreamingResponse:
        return SelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResourceWithStreamingResponse:
        return SubOrganizationsResourceWithStreamingResponse(self._print_mail.sub_organizations)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._print_mail.templates)


class AsyncPrintMailResourceWithStreamingResponse:
    def __init__(self, print_mail: AsyncPrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        return AsyncBankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        return AsyncCampaignsResourceWithStreamingResponse(self._print_mail.campaigns)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithStreamingResponse:
        return AsyncChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithStreamingResponse:
        return AsyncLettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResourceWithStreamingResponse:
        return AsyncMailingListImportsResourceWithStreamingResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResourceWithStreamingResponse:
        return AsyncMailingListsResourceWithStreamingResponse(self._print_mail.mailing_lists)

    @cached_property
    def order_profiles(self) -> AsyncOrderProfilesResourceWithStreamingResponse:
        return AsyncOrderProfilesResourceWithStreamingResponse(self._print_mail.order_profiles)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithStreamingResponse:
        return AsyncPostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._print_mail.reports)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithStreamingResponse:
        return AsyncSelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResourceWithStreamingResponse:
        return AsyncSubOrganizationsResourceWithStreamingResponse(self._print_mail.sub_organizations)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._print_mail.templates)
