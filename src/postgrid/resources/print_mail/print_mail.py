# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .boxes import (
    BoxesResource,
    AsyncBoxesResource,
    BoxesResourceWithRawResponse,
    AsyncBoxesResourceWithRawResponse,
    BoxesResourceWithStreamingResponse,
    AsyncBoxesResourceWithStreamingResponse,
)
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
from .trackers import (
    TrackersResource,
    AsyncTrackersResource,
    TrackersResourceWithRawResponse,
    AsyncTrackersResourceWithRawResponse,
    TrackersResourceWithStreamingResponse,
    AsyncTrackersResourceWithStreamingResponse,
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
from .snap_packs import (
    SnapPacksResource,
    AsyncSnapPacksResource,
    SnapPacksResourceWithRawResponse,
    AsyncSnapPacksResourceWithRawResponse,
    SnapPacksResourceWithStreamingResponse,
    AsyncSnapPacksResourceWithStreamingResponse,
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
from .template_editor_sessions import (
    TemplateEditorSessionsResource,
    AsyncTemplateEditorSessionsResource,
    TemplateEditorSessionsResourceWithRawResponse,
    AsyncTemplateEditorSessionsResourceWithRawResponse,
    TemplateEditorSessionsResourceWithStreamingResponse,
    AsyncTemplateEditorSessionsResourceWithStreamingResponse,
)
from .virtual_mailboxes.virtual_mailboxes import (
    VirtualMailboxesResource,
    AsyncVirtualMailboxesResource,
    VirtualMailboxesResourceWithRawResponse,
    AsyncVirtualMailboxesResourceWithRawResponse,
    VirtualMailboxesResourceWithStreamingResponse,
    AsyncVirtualMailboxesResourceWithStreamingResponse,
)
from .targeted_list_builds.targeted_list_builds import (
    TargetedListBuildsResource,
    AsyncTargetedListBuildsResource,
    TargetedListBuildsResourceWithRawResponse,
    AsyncTargetedListBuildsResourceWithRawResponse,
    TargetedListBuildsResourceWithStreamingResponse,
    AsyncTargetedListBuildsResourceWithStreamingResponse,
)

__all__ = ["PrintMailResource", "AsyncPrintMailResource"]


class PrintMailResource(SyncAPIResource):
    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def trackers(self) -> TrackersResource:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return TrackersResource(self._client)

    @cached_property
    def letters(self) -> LettersResource:
        return LettersResource(self._client)

    @cached_property
    def postcards(self) -> PostcardsResource:
        return PostcardsResource(self._client)

    @cached_property
    def bank_accounts(self) -> BankAccountsResource:
        return BankAccountsResource(self._client)

    @cached_property
    def cheques(self) -> ChequesResource:
        return ChequesResource(self._client)

    @cached_property
    def self_mailers(self) -> SelfMailersResource:
        return SelfMailersResource(self._client)

    @cached_property
    def campaigns(self) -> CampaignsResource:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return CampaignsResource(self._client)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResource:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return MailingListImportsResource(self._client)

    @cached_property
    def mailing_lists(self) -> MailingListsResource:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return MailingListsResource(self._client)

    @cached_property
    def reports(self) -> ReportsResource:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return ReportsResource(self._client)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResource:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SubOrganizationsResource(self._client)

    @cached_property
    def boxes(self) -> BoxesResource:
        return BoxesResource(self._client)

    @cached_property
    def snap_packs(self) -> SnapPacksResource:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SnapPacksResource(self._client)

    @cached_property
    def targeted_list_builds(self) -> TargetedListBuildsResource:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return TargetedListBuildsResource(self._client)

    @cached_property
    def template_editor_sessions(self) -> TemplateEditorSessionsResource:
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
        return TemplateEditorSessionsResource(self._client)

    @cached_property
    def virtual_mailboxes(self) -> VirtualMailboxesResource:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return VirtualMailboxesResource(self._client)

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
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def trackers(self) -> AsyncTrackersResource:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return AsyncTrackersResource(self._client)

    @cached_property
    def letters(self) -> AsyncLettersResource:
        return AsyncLettersResource(self._client)

    @cached_property
    def postcards(self) -> AsyncPostcardsResource:
        return AsyncPostcardsResource(self._client)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResource:
        return AsyncBankAccountsResource(self._client)

    @cached_property
    def cheques(self) -> AsyncChequesResource:
        return AsyncChequesResource(self._client)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResource:
        return AsyncSelfMailersResource(self._client)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return AsyncCampaignsResource(self._client)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResource:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return AsyncMailingListImportsResource(self._client)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResource:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return AsyncMailingListsResource(self._client)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return AsyncReportsResource(self._client)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResource:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSubOrganizationsResource(self._client)

    @cached_property
    def boxes(self) -> AsyncBoxesResource:
        return AsyncBoxesResource(self._client)

    @cached_property
    def snap_packs(self) -> AsyncSnapPacksResource:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSnapPacksResource(self._client)

    @cached_property
    def targeted_list_builds(self) -> AsyncTargetedListBuildsResource:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return AsyncTargetedListBuildsResource(self._client)

    @cached_property
    def template_editor_sessions(self) -> AsyncTemplateEditorSessionsResource:
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
        return AsyncTemplateEditorSessionsResource(self._client)

    @cached_property
    def virtual_mailboxes(self) -> AsyncVirtualMailboxesResource:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncVirtualMailboxesResource(self._client)

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
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._print_mail.templates)

    @cached_property
    def trackers(self) -> TrackersResourceWithRawResponse:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return TrackersResourceWithRawResponse(self._print_mail.trackers)

    @cached_property
    def letters(self) -> LettersResourceWithRawResponse:
        return LettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithRawResponse:
        return PostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithRawResponse:
        return BankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> ChequesResourceWithRawResponse:
        return ChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithRawResponse:
        return SelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return CampaignsResourceWithRawResponse(self._print_mail.campaigns)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResourceWithRawResponse:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return MailingListImportsResourceWithRawResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> MailingListsResourceWithRawResponse:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return MailingListsResourceWithRawResponse(self._print_mail.mailing_lists)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return ReportsResourceWithRawResponse(self._print_mail.reports)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResourceWithRawResponse:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SubOrganizationsResourceWithRawResponse(self._print_mail.sub_organizations)

    @cached_property
    def boxes(self) -> BoxesResourceWithRawResponse:
        return BoxesResourceWithRawResponse(self._print_mail.boxes)

    @cached_property
    def snap_packs(self) -> SnapPacksResourceWithRawResponse:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SnapPacksResourceWithRawResponse(self._print_mail.snap_packs)

    @cached_property
    def targeted_list_builds(self) -> TargetedListBuildsResourceWithRawResponse:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return TargetedListBuildsResourceWithRawResponse(self._print_mail.targeted_list_builds)

    @cached_property
    def template_editor_sessions(self) -> TemplateEditorSessionsResourceWithRawResponse:
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
        return TemplateEditorSessionsResourceWithRawResponse(self._print_mail.template_editor_sessions)

    @cached_property
    def virtual_mailboxes(self) -> VirtualMailboxesResourceWithRawResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return VirtualMailboxesResourceWithRawResponse(self._print_mail.virtual_mailboxes)


class AsyncPrintMailResourceWithRawResponse:
    def __init__(self, print_mail: AsyncPrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._print_mail.templates)

    @cached_property
    def trackers(self) -> AsyncTrackersResourceWithRawResponse:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return AsyncTrackersResourceWithRawResponse(self._print_mail.trackers)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithRawResponse:
        return AsyncLettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithRawResponse:
        return AsyncPostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithRawResponse:
        return AsyncBankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithRawResponse:
        return AsyncChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithRawResponse:
        return AsyncSelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return AsyncCampaignsResourceWithRawResponse(self._print_mail.campaigns)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResourceWithRawResponse:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return AsyncMailingListImportsResourceWithRawResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResourceWithRawResponse:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return AsyncMailingListsResourceWithRawResponse(self._print_mail.mailing_lists)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return AsyncReportsResourceWithRawResponse(self._print_mail.reports)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResourceWithRawResponse:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSubOrganizationsResourceWithRawResponse(self._print_mail.sub_organizations)

    @cached_property
    def boxes(self) -> AsyncBoxesResourceWithRawResponse:
        return AsyncBoxesResourceWithRawResponse(self._print_mail.boxes)

    @cached_property
    def snap_packs(self) -> AsyncSnapPacksResourceWithRawResponse:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSnapPacksResourceWithRawResponse(self._print_mail.snap_packs)

    @cached_property
    def targeted_list_builds(self) -> AsyncTargetedListBuildsResourceWithRawResponse:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return AsyncTargetedListBuildsResourceWithRawResponse(self._print_mail.targeted_list_builds)

    @cached_property
    def template_editor_sessions(self) -> AsyncTemplateEditorSessionsResourceWithRawResponse:
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
        return AsyncTemplateEditorSessionsResourceWithRawResponse(self._print_mail.template_editor_sessions)

    @cached_property
    def virtual_mailboxes(self) -> AsyncVirtualMailboxesResourceWithRawResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncVirtualMailboxesResourceWithRawResponse(self._print_mail.virtual_mailboxes)


class PrintMailResourceWithStreamingResponse:
    def __init__(self, print_mail: PrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._print_mail.templates)

    @cached_property
    def trackers(self) -> TrackersResourceWithStreamingResponse:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return TrackersResourceWithStreamingResponse(self._print_mail.trackers)

    @cached_property
    def letters(self) -> LettersResourceWithStreamingResponse:
        return LettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithStreamingResponse:
        return PostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithStreamingResponse:
        return BankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> ChequesResourceWithStreamingResponse:
        return ChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithStreamingResponse:
        return SelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return CampaignsResourceWithStreamingResponse(self._print_mail.campaigns)

    @cached_property
    def mailing_list_imports(self) -> MailingListImportsResourceWithStreamingResponse:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return MailingListImportsResourceWithStreamingResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> MailingListsResourceWithStreamingResponse:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return MailingListsResourceWithStreamingResponse(self._print_mail.mailing_lists)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return ReportsResourceWithStreamingResponse(self._print_mail.reports)

    @cached_property
    def sub_organizations(self) -> SubOrganizationsResourceWithStreamingResponse:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SubOrganizationsResourceWithStreamingResponse(self._print_mail.sub_organizations)

    @cached_property
    def boxes(self) -> BoxesResourceWithStreamingResponse:
        return BoxesResourceWithStreamingResponse(self._print_mail.boxes)

    @cached_property
    def snap_packs(self) -> SnapPacksResourceWithStreamingResponse:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return SnapPacksResourceWithStreamingResponse(self._print_mail.snap_packs)

    @cached_property
    def targeted_list_builds(self) -> TargetedListBuildsResourceWithStreamingResponse:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return TargetedListBuildsResourceWithStreamingResponse(self._print_mail.targeted_list_builds)

    @cached_property
    def template_editor_sessions(self) -> TemplateEditorSessionsResourceWithStreamingResponse:
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
        return TemplateEditorSessionsResourceWithStreamingResponse(self._print_mail.template_editor_sessions)

    @cached_property
    def virtual_mailboxes(self) -> VirtualMailboxesResourceWithStreamingResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return VirtualMailboxesResourceWithStreamingResponse(self._print_mail.virtual_mailboxes)


class AsyncPrintMailResourceWithStreamingResponse:
    def __init__(self, print_mail: AsyncPrintMailResource) -> None:
        self._print_mail = print_mail

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._print_mail.templates)

    @cached_property
    def trackers(self) -> AsyncTrackersResourceWithStreamingResponse:
        """Create and manage Trackers.

        Trackers can be used to track interactions in your orders through
        personalized URLs and QR codes.

        As a brief introduction to using Trackers in your orders, a QR code can be
        generated by using the Tracker's ID as a merge variable in your orders HTML
        and Templates. The following example HTML uses Trackers to generate
        personalized URLs (PURLs) in your orders.

        See the following guide for more details: https://postgrid.readme.io/reference/trackers-1
        """
        return AsyncTrackersResourceWithStreamingResponse(self._print_mail.trackers)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithStreamingResponse:
        return AsyncLettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithStreamingResponse:
        return AsyncPostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        return AsyncBankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithStreamingResponse:
        return AsyncChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithStreamingResponse:
        return AsyncSelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """
        The campaigns API enables you to send out large volumes of fully
         personalized mail to a mailing list.
        """
        return AsyncCampaignsResourceWithStreamingResponse(self._print_mail.campaigns)

    @cached_property
    def mailing_list_imports(self) -> AsyncMailingListImportsResourceWithStreamingResponse:
        """
        The mailing list imports API enables you to import contact lists from files
         and validate them for use in campaigns.
        """
        return AsyncMailingListImportsResourceWithStreamingResponse(self._print_mail.mailing_list_imports)

    @cached_property
    def mailing_lists(self) -> AsyncMailingListsResourceWithStreamingResponse:
        """
        The mailing lists API enables you to manage collections of contacts
         that can be used for bulk mail campaigns.
        """
        return AsyncMailingListsResourceWithStreamingResponse(self._print_mail.mailing_lists)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        The reports API lets you run SQL queries against a data lake with all of your PostGrid data. You can use this to run ad-hoc SQL queries or save them as reports. You can bulk export data from these reports to fit all of your reporting needs.
         Note that the data this API provides may be up to 2 hours behind your current PostGrid environment.
         Your test and live data lakes are fully segregated, so you'll need a live API key to run queries against your live data.

         You can request access to this to this feature by reaching out to support@postgrid.com
        """
        return AsyncReportsResourceWithStreamingResponse(self._print_mail.reports)

    @cached_property
    def sub_organizations(self) -> AsyncSubOrganizationsResourceWithStreamingResponse:
        """
        Sub-organizations enable you to create isolated PostGrid accounts
         ("sub-organizations") under your PostGrid account (the "parent organization").
         Each sub-organization has fully isolated resources
         and users, and can act independently.

         This allows you to isolate different departments or even re-sell PostGrid
         entirely.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSubOrganizationsResourceWithStreamingResponse(self._print_mail.sub_organizations)

    @cached_property
    def boxes(self) -> AsyncBoxesResourceWithStreamingResponse:
        return AsyncBoxesResourceWithStreamingResponse(self._print_mail.boxes)

    @cached_property
    def snap_packs(self) -> AsyncSnapPacksResourceWithStreamingResponse:
        """
        Snap packs are pressure-sealed mailers that resemble official documents
         and encourage higher open rates. They do not require envelopes and are
         opened by tearing along perforated edges. The sealed design keeps contents
         hidden until opened, making snap packs ideal for sensitive or important
         documents such as contracts, forms, or notices.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncSnapPacksResourceWithStreamingResponse(self._print_mail.snap_packs)

    @cached_property
    def targeted_list_builds(self) -> AsyncTargetedListBuildsResourceWithStreamingResponse:
        """
        **Beta:** the targeted list builds API is in beta and is subject to
         breaking changes. Endpoint shapes, status values, and filter fields may
         change without notice.

         The targeted list builds API lets you programmatically build mailing
         lists of US consumers (B2C) or US companies (B2B) that match a set of
         demographic, geographic, and firmographic filters.

         The lifecycle of a list build is:

         1. Create a list build by supplying either `usConsumers` or `usCompanies`
            filters. A quote is generated asynchronously — poll the resource or
            wait for its `status` to become `quote_ready`.
         2. Review the `quote` (total count and price per contact) and masked
            `previewRecords`. Adjust the filters with an update call if needed —
            this will regenerate the quote.
         3. Confirm the build. This deducts the appropriate amount of list build
            credits from your organization (in live mode) and begins constructing
            the mailing list. `buildProgressPercent` reflects progress from 0 to
            100.
         4. Once `status` is `completed`, the ID of the resulting mailing list is
            available in the `mailingList` field and can be used like any other
            mailing list in the PostGrid API.

         Targeted list builds must be enabled on your organization before they
         can be used. Contact PostGrid support to request access.
        """
        return AsyncTargetedListBuildsResourceWithStreamingResponse(self._print_mail.targeted_list_builds)

    @cached_property
    def template_editor_sessions(self) -> AsyncTemplateEditorSessionsResourceWithStreamingResponse:
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
        return AsyncTemplateEditorSessionsResourceWithStreamingResponse(self._print_mail.template_editor_sessions)

    @cached_property
    def virtual_mailboxes(self) -> AsyncVirtualMailboxesResourceWithStreamingResponse:
        """
        Virtual mailboxes let you receive, scan, and forward your physical mail
         without needing a traditional physical mailbox. Each mailbox is fully
         digital, giving you a unique ID, status, and a set of capabilities such as
         forwarding mail to another address or viewing envelope scans. This allows you
         to manage physical correspondence entirely online.

         You can request access to this feature by reaching out to
         support@postgrid.com
        """
        return AsyncVirtualMailboxesResourceWithStreamingResponse(self._print_mail.virtual_mailboxes)
