# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TrackerRetrieveVisitsResponse"]


class TrackerRetrieveVisitsResponse(BaseModel):
    id: str
    """A unique ID prefixed with `tracker_visit_`."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this visit was created."""

    device: str
    """The type of device associated with the visit."""

    ip_address: str = FieldInfo(alias="ipAddress")
    """The IP address associated with the visit."""

    live: bool
    """Indicates if the visit was used in a live order or not."""

    object: Literal["tracker_visit"]
    """Always `tracker_visit`."""

    order_id: str = FieldInfo(alias="orderID")
    """The ID of the order where the interaction occurred."""

    tracker: str
    """The ID of the tracker related to this visit."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this visit was last updated."""
