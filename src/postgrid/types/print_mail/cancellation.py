# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Cancellation"]


class Cancellation(BaseModel):
    reason: Literal["user_initiated", "invalid_content", "invalid_order_mailing_class"]
    """The reason for the cancellation."""

    cancelled_by_user: Optional[str] = FieldInfo(alias="cancelledByUser", default=None)
    """The user ID who cancelled the order."""

    note: Optional[str] = None
    """An optional note provided by the user who cancelled the order."""
