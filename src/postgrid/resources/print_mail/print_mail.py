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
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
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
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
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
from .return_envelopes.return_envelopes import (
    ReturnEnvelopesResource,
    AsyncReturnEnvelopesResource,
    ReturnEnvelopesResourceWithRawResponse,
    AsyncReturnEnvelopesResourceWithRawResponse,
    ReturnEnvelopesResourceWithStreamingResponse,
    AsyncReturnEnvelopesResourceWithStreamingResponse,
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return ContactsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> WebhooksResource:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return WebhooksResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return EventsResource(self._client)

    @cached_property
    def letters(self) -> LettersResource:
        """Create and manage letter orders."""
        return LettersResource(self._client)

    @cached_property
    def postcards(self) -> PostcardsResource:
        """Create and manage postcard mailings."""
        return PostcardsResource(self._client)

    @cached_property
    def bank_accounts(self) -> BankAccountsResource:
        """Manage bank accounts that will be used for mailing cheques."""
        return BankAccountsResource(self._client)

    @cached_property
    def cheques(self) -> ChequesResource:
        """Create and manage cheque orders."""
        return ChequesResource(self._client)

    @cached_property
    def self_mailers(self) -> SelfMailersResource:
        """Create and manage self mailers."""
        return SelfMailersResource(self._client)

    @cached_property
    def return_envelopes(self) -> ReturnEnvelopesResource:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return ReturnEnvelopesResource(self._client)

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
        """Create and manage box orders."""
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return AsyncContactsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> AsyncWebhooksResource:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return AsyncWebhooksResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return AsyncEventsResource(self._client)

    @cached_property
    def letters(self) -> AsyncLettersResource:
        """Create and manage letter orders."""
        return AsyncLettersResource(self._client)

    @cached_property
    def postcards(self) -> AsyncPostcardsResource:
        """Create and manage postcard mailings."""
        return AsyncPostcardsResource(self._client)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResource:
        """Manage bank accounts that will be used for mailing cheques."""
        return AsyncBankAccountsResource(self._client)

    @cached_property
    def cheques(self) -> AsyncChequesResource:
        """Create and manage cheque orders."""
        return AsyncChequesResource(self._client)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResource:
        """Create and manage self mailers."""
        return AsyncSelfMailersResource(self._client)

    @cached_property
    def return_envelopes(self) -> AsyncReturnEnvelopesResource:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncReturnEnvelopesResource(self._client)

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
        """Create and manage box orders."""
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return ContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return WebhooksResourceWithRawResponse(self._print_mail.webhooks)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return EventsResourceWithRawResponse(self._print_mail.events)

    @cached_property
    def letters(self) -> LettersResourceWithRawResponse:
        """Create and manage letter orders."""
        return LettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithRawResponse:
        """Create and manage postcard mailings."""
        return PostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithRawResponse:
        """Manage bank accounts that will be used for mailing cheques."""
        return BankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> ChequesResourceWithRawResponse:
        """Create and manage cheque orders."""
        return ChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithRawResponse:
        """Create and manage self mailers."""
        return SelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def return_envelopes(self) -> ReturnEnvelopesResourceWithRawResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return ReturnEnvelopesResourceWithRawResponse(self._print_mail.return_envelopes)

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
        """Create and manage box orders."""
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return AsyncContactsResourceWithRawResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return AsyncWebhooksResourceWithRawResponse(self._print_mail.webhooks)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return AsyncEventsResourceWithRawResponse(self._print_mail.events)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithRawResponse:
        """Create and manage letter orders."""
        return AsyncLettersResourceWithRawResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithRawResponse:
        """Create and manage postcard mailings."""
        return AsyncPostcardsResourceWithRawResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithRawResponse:
        """Manage bank accounts that will be used for mailing cheques."""
        return AsyncBankAccountsResourceWithRawResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithRawResponse:
        """Create and manage cheque orders."""
        return AsyncChequesResourceWithRawResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithRawResponse:
        """Create and manage self mailers."""
        return AsyncSelfMailersResourceWithRawResponse(self._print_mail.self_mailers)

    @cached_property
    def return_envelopes(self) -> AsyncReturnEnvelopesResourceWithRawResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncReturnEnvelopesResourceWithRawResponse(self._print_mail.return_envelopes)

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
        """Create and manage box orders."""
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return ContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return WebhooksResourceWithStreamingResponse(self._print_mail.webhooks)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return EventsResourceWithStreamingResponse(self._print_mail.events)

    @cached_property
    def letters(self) -> LettersResourceWithStreamingResponse:
        """Create and manage letter orders."""
        return LettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> PostcardsResourceWithStreamingResponse:
        """Create and manage postcard mailings."""
        return PostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> BankAccountsResourceWithStreamingResponse:
        """Manage bank accounts that will be used for mailing cheques."""
        return BankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> ChequesResourceWithStreamingResponse:
        """Create and manage cheque orders."""
        return ChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> SelfMailersResourceWithStreamingResponse:
        """Create and manage self mailers."""
        return SelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def return_envelopes(self) -> ReturnEnvelopesResourceWithStreamingResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return ReturnEnvelopesResourceWithStreamingResponse(self._print_mail.return_envelopes)

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
        """Create and manage box orders."""
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
        """Manage contacts that you can mail to.

        Test mode addresses will always have a
         `verified` status. In live mode, they may be `verified`, `corrected`, or
         `failed`. Addresses that fail to be corrected are likely undeliverable, but
         you can still send to them if you want to.

         For test mode contacts, you have the ability to assert the `addressStatus` of
         the contact by passing specific values to the `description` field. To receive
         an `addressStatus` of `failed`, the description of the contact should be a
         string with the exact value `test failed`. For an `addressStatus` value of
         `corrected`, the description of the contact should be a string with the exact
         value `test corrected`.

         Our address correction engine will often be able to fix missing postal/ZIP
         codes, city names, and also append ZIP+4. It is SERP (Canada Post) and CASS
         (USPS) certified, so you can rest assured that if an address is verified, we
         can deliver to it.
        """
        return AsyncContactsResourceWithStreamingResponse(self._print_mail.contacts)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """Create and manage reusable HTML templates.

        A template's HTML can include
         merge variables (e.g. `{{firstName}}`) and be referenced by ID when creating
         letters, postcards, cheques, and self mailers.
        """
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
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Create and manage Webhooks.

        Webhooks can be used to notify your application when events occur in PostGrid.
        For example, you may use a `letter.updated` webhook to receive a notification
        when a letter has been processed for delivery.

        Every webhook has a `secret` and this is used to sign the payload of the event.

        You can choose what format you want the payload to be delivered in. By default,
        the webhook payload will be delivered as a [JSON Web Token](https://jwt.io/).
        When you receive the event, you can verify it using a JWT library available for
        your particular language (using the HMAC SHA256 Algorithm). There are
        [many](https://jwt.io/#libraries-io) off-the-shelf solutions you can use.

        You can alternatively choose to receive a JSON payload. In this case, you'll
        also receive a `PostGrid-Signature` HTTP header along with the payload.

        You must respond with a `200` status from your webhook. Otherwise, PostGrid
        will retry the webhook up to 3 times. First, after 1 hour, then 2 hours, then
        4 hours. We will also keep track of every invocation and its response status.
        You can retrieve data about prior invocations using the webhook invocations
        list endpoint below.
        """
        return AsyncWebhooksResourceWithStreamingResponse(self._print_mail.webhooks)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """View Events related to your orders.

        An event is created whenever a webhook is triggered. For example, if a webhook
        is created that listens to `letter.updated` events and the delivery status of a
        letter is updated, an event detailing the updated fields will get created.
        """
        return AsyncEventsResourceWithStreamingResponse(self._print_mail.events)

    @cached_property
    def letters(self) -> AsyncLettersResourceWithStreamingResponse:
        """Create and manage letter orders."""
        return AsyncLettersResourceWithStreamingResponse(self._print_mail.letters)

    @cached_property
    def postcards(self) -> AsyncPostcardsResourceWithStreamingResponse:
        """Create and manage postcard mailings."""
        return AsyncPostcardsResourceWithStreamingResponse(self._print_mail.postcards)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        """Manage bank accounts that will be used for mailing cheques."""
        return AsyncBankAccountsResourceWithStreamingResponse(self._print_mail.bank_accounts)

    @cached_property
    def cheques(self) -> AsyncChequesResourceWithStreamingResponse:
        """Create and manage cheque orders."""
        return AsyncChequesResourceWithStreamingResponse(self._print_mail.cheques)

    @cached_property
    def self_mailers(self) -> AsyncSelfMailersResourceWithStreamingResponse:
        """Create and manage self mailers."""
        return AsyncSelfMailersResourceWithStreamingResponse(self._print_mail.self_mailers)

    @cached_property
    def return_envelopes(self) -> AsyncReturnEnvelopesResourceWithStreamingResponse:
        """
        You can use the return envelopes API to create and manage return envelopes.
         These are envelopes that are sent along with your mail (if specified) and
         allow your recipients to send mail to a particular address without having to
         purchase their own envelopes/stamps.

         Note that you must order return envelopes and wait for the order to be
         filled before you can use them. You can manage these return envelope orders
         via the API as well as the dashboard.
        """
        return AsyncReturnEnvelopesResourceWithStreamingResponse(self._print_mail.return_envelopes)

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
        """Create and manage box orders."""
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
