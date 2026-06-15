# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookInvocation"]


class WebhookInvocation(BaseModel):
    id: str
    """A unique ID prefixed with `webhook_invocation_`."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this invocation was created."""

    event: str
    """The ID of the event that was delivered in this invocation."""

    object: Literal["webhook_invocation"]
    """Always `webhook_invocation`."""

    status_code: int = FieldInfo(alias="statusCode")
    """The HTTP status code returned by your endpoint for this invocation."""

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

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this invocation was last updated."""

    webhook: str
    """The ID of the webhook that was invoked."""

    order_id: Optional[str] = FieldInfo(alias="orderID", default=None)
    """
    The ID of the order associated with this invocation, if the event was
    order-related.
    """
