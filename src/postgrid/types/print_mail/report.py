# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Report"]


class Report(BaseModel):
    """Represents a saved Report definition."""

    id: str
    """Unique identifier for the report."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the report was created."""

    live: bool
    """Indicates if the report is associated with the live or test environment."""

    object: Literal["report"]
    """Always `report`."""

    sql_query: str = FieldInfo(alias="sqlQuery")
    """The SQL query defining the report."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the report was last updated."""

    description: Optional[str] = None
    """An optional user-friendly description for the report."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata associated with the report."""
