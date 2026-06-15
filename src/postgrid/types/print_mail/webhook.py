# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """A unique ID prefixed with webhook\\__"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    enabled: bool
    """Whether this webhook is enabled. Disabled webhooks are not triggered."""

    enabled_events: List[
        Literal[
            "letter.created",
            "letter.updated",
            "postcard.created",
            "postcard.updated",
            "self_mailer.created",
            "self_mailer.updated",
            "cheque.created",
            "cheque.updated",
            "box.created",
            "box.updated",
            "snap_pack.created",
            "snap_pack.updated",
            "return_envelope_order.created",
            "return_envelope_order.updated",
            "tracker.visited",
            "campaign.created",
            "campaign.updated",
            "virtual_mailbox_item.created",
        ]
    ] = FieldInfo(alias="enabledEvents")
    """The list of event types this webhook listens for."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["webhook"]
    """Always `webhook`."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    url: str
    """An HTTPS URL that PostGrid can invoke for webhook deliveries."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""

    payload_format: Optional[Literal["jwt", "json"]] = FieldInfo(alias="payloadFormat", default=None)
    """The format in which a Webhook's event payload is delivered."""

    secret: Optional[str] = None
    """A webhook signing secret with at least 20 non-whitespace characters."""
