# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReportExport", "Report"]


class Report(BaseModel):
    """Details of the report this export was generated from."""

    id: str
    """The ID of the report."""

    sql_query: str = FieldInfo(alias="sqlQuery")
    """The SQL query used for this export (snapshotted at creation time)."""


class ReportExport(BaseModel):
    """Represents a report export job and its results."""

    id: str
    """Unique identifier for the report export."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the export was created."""

    live: bool
    """Indicates if the export is associated with the live or test environment."""

    object: Literal["report_export"]
    """Always `report_export`."""

    report: Report
    """Details of the report this export was generated from."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the export was last updated (e.g., finished generation)."""

    description: Optional[str] = None
    """An optional user-friendly description for the export."""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """If export generation failed, this contains the error message."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata associated with the export."""

    output_url: Optional[str] = FieldInfo(alias="outputURL", default=None)
    """A signed URL to download the exported data (CSV format).

    Available when generation is complete and successful.
    """

    params: Optional[List[str]] = None
    """Optional parameters to bind to the SQL query of the associated report."""

    row_count: Optional[int] = FieldInfo(alias="rowCount", default=None)
    """The number of rows in the exported data."""

    size_in_bytes: Optional[int] = FieldInfo(alias="sizeInBytes", default=None)
    """The size of the generated export file in bytes."""

    truncated_to_bytes: Optional[int] = FieldInfo(alias="truncatedToBytes", default=None)
    """If the output was truncated, indicates the byte limit reached."""
