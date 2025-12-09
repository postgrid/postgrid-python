# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Campaign", "Error"]


class Error(BaseModel):
    """Details of a specific error encountered during campaign processing."""

    message: str
    """A human-readable message describing the error."""

    type: Literal["processing_error", "internal_error"]
    """Type of error encountered during campaign processing."""


class Campaign(BaseModel):
    """Represents a bulk mail campaign."""

    id: str
    """A unique ID prefixed with campaign\\__"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    created_count: int = FieldInfo(alias="createdCount")
    """The number of orders successfully created for this campaign."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    mailing_list: str = FieldInfo(alias="mailingList")
    """The ID of the mailing list associated with this campaign."""

    status: Literal[
        "drafting", "changes_required", "creating_orders", "draft", "ready", "printing", "processed_for_delivery"
    ]
    """Status of the campaign lifecycle."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    cheque_profile: Optional[str] = FieldInfo(alias="chequeProfile", default=None)
    """The ID of the cheque profile used for this campaign, if applicable."""

    default_sender_contact: Optional[str] = FieldInfo(alias="defaultSenderContact", default=None)
    """
    The ID of the default sender contact to use for orders if not specified per
    recipient.
    """

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    errors: Optional[List[Error]] = None
    """A list of processing errors encountered, if any.

    Present when status is 'changes_required'.
    """

    letter_profile: Optional[str] = FieldInfo(alias="letterProfile", default=None)
    """The ID of the letter profile used for this campaign, if applicable."""

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""

    order_preview_url: Optional[str] = FieldInfo(alias="orderPreviewURL", default=None)
    """
    A temporary URL to preview the first rendered order, available once the campaign
    status is 'draft' or later.
    """

    postcard_profile: Optional[str] = FieldInfo(alias="postcardProfile", default=None)
    """The ID of the postcard profile used for this campaign, if applicable."""

    report_url: Optional[str] = FieldInfo(alias="reportURL", default=None)
    """
    A temporary URL to download the processing report, available once the campaign
    is in the `ready` status.
    """

    self_mailer_profile: Optional[str] = FieldInfo(alias="selfMailerProfile", default=None)
    """The ID of the self-mailer profile used for this campaign, if applicable."""

    send_date: Optional[datetime] = FieldInfo(alias="sendDate", default=None)
    """The scheduled date and time for the campaign to be sent."""
