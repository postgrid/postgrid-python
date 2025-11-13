# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MailingListCreateParams"]


class MailingListCreateParams(TypedDict, total=False):
    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]
