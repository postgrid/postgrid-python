# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
    description: str
    """An optional user-friendly description for the export."""

    metadata: Dict[str, str]
    """Optional key-value metadata associated with the export."""

    params: SequenceNotStr[str]
    """Optional parameters to bind to the SQL query of the associated report."""
