# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReportUpdateParams"]


class ReportUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """An optional user-friendly description for the report. Set to null to remove."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata associated with the report. Set to null to remove."""

    sql_query: Annotated[str, PropertyInfo(alias="sqlQuery")]
    """The SQL query defining the report."""
