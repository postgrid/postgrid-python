# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["SampleCreateParams"]


class SampleCreateParams(TypedDict, total=False):
    limit: int
    """Maximum number of rows to return in the sample."""

    params: SequenceNotStr[str]
    """
    Optional parameters to bind to the SQL query (e.g., for placeholders like ? or
    $1).
    """
