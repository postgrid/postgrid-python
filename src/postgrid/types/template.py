# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    id: str
    """A unique ID prefixed with template\\__"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""
