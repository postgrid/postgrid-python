# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    enabled: bool
    """Whether this webhook is enabled. Disabled webhooks are not triggered."""

    enabled_events: Annotated[
        List[
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
        ],
        PropertyInfo(alias="enabledEvents"),
    ]
    """The list of event types this webhook listens for."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    payload_format: Annotated[Literal["jwt", "json"], PropertyInfo(alias="payloadFormat")]
    """The format in which a Webhook's event payload is delivered."""

    secret: str
    """A webhook signing secret with at least 20 non-whitespace characters."""

    url: str
    """An HTTPS URL that PostGrid can invoke for webhook deliveries."""
