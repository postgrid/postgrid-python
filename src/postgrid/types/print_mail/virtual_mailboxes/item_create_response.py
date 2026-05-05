# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ItemCreateResponse"]


class ItemCreateResponse(BaseModel):
    """The virtual mailbox item object."""

    id: str
    """A unique ID prefixed with virtual*mailbox_item*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["virtual_mailbox_item"]
    """Always "virtual_mailbox_item"."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    virtual_mailbox: str = FieldInfo(alias="virtualMailbox")
    """The ID of the virtual mailbox associated with this item."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    file_url: Optional[str] = FieldInfo(alias="fileURL", default=None)
    """A URL of the envelope scan PDF."""

    matched_letter: Optional[str] = FieldInfo(alias="matchedLetter", default=None)
    """The ID of the letter this item was matched to."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""
