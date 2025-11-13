# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ReportSampleParams"]


class ReportSampleParams(TypedDict, total=False):
    sql_query: Required[Annotated[str, PropertyInfo(alias="sqlQuery")]]
    """The SQL query to execute for the sample."""

    limit: int
    """Maximum number of rows to return in the sample."""

    params: SequenceNotStr[str]
    """
    Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
    $1).
    """
