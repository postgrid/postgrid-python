# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .. import return_envelope
from ...._models import BaseModel

__all__ = ["ReturnEnvelopeOrder", "ReturnEnvelope"]

ReturnEnvelope: TypeAlias = Union[str, return_envelope.ReturnEnvelope]


class ReturnEnvelopeOrder(BaseModel):
    id: str
    """A unique ID prefixed with return*envelope_order*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["return_envelope_order"]
    """Always `return_envelope_order`."""

    quantity_ordered: int = FieldInfo(alias="quantityOrdered")
    """The quantity of return envelopes ordered. Minimum 5000."""

    return_envelope: ReturnEnvelope = FieldInfo(alias="returnEnvelope")
    """The ID of the return envelope that this order replenishes.

    Expanded into the full return envelope object on the individual order retrieval
    and cancellation endpoints when `expand[]=returnEnvelope` is supplied.
    """

    status: Literal["placed", "filled", "cancelled"]
    """The status of a return envelope order."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""

    quantity_filled: Optional[int] = FieldInfo(alias="quantityFilled", default=None)
    """The quantity of return envelopes that were filled for this order.

    Only returned once the order's status is `filled`.
    """
