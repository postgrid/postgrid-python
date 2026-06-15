# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    limit: int

    skip: int

    type: List[
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
    ]
    """An optional list of event types to filter the results by."""
