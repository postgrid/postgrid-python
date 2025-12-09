# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailPreferences"]


class EmailPreferences(BaseModel):
    """A set of preferences for how a user should receive emails."""

    order_preview_send_preference: Optional[Literal["do_not_send", "send_live_only", "send_live_and_test"]] = FieldInfo(
        alias="orderPreviewSendPreference", default=None
    )
    """The list of preferences for receiving order preview emails."""
