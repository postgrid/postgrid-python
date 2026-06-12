# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OrderCreateParams"]


class OrderCreateParams(TypedDict, total=False):
    quantity_ordered: Required[Annotated[int, PropertyInfo(alias="quantityOrdered")]]
    """The quantity of return envelopes ordered. Minimum 5000."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""
