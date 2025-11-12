# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    sql_query: Required[Annotated[str, PropertyInfo(alias="sqlQuery")]]
    """The SQL query defining the report."""

    description: str
    """An optional user-friendly description for the report."""

    metadata: Dict[str, str]
    """Optional key-value metadata associated with the report."""
