# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["ChequeRetrieveParams"]


class ChequeRetrieveParams(TypedDict, total=False):
    expand: List[str]
    """Optional list of related resources to expand in the response."""
