# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BulkVerificationListParams"]


class BulkVerificationListParams(TypedDict, total=False):
    limit: int
    """The maximum number of lists to return."""

    skip: int
    """The number of lists to skip past, for pagination."""
