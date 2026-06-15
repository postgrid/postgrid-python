# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    id: str
    """A unique ID prefixed with `event_`."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this event was created."""

    live: bool
    """`true` if this is a live mode event else `false`."""

    object: Literal["event"]
    """Always `event`."""

    type: Literal[
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
    """The type of event that a Webhook can listen for and that an Event represents."""

    data: Optional[Dict[str, builtins.object]] = None
    """The data of the resource associated with this event."""

    updated_fields: Optional[Dict[str, builtins.object]] = FieldInfo(alias="updatedFields", default=None)
    """
    A record containing the updated fields of the resource associated with this
    event.
    """
