# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostcardListParams"]


class PostcardListParams(TypedDict, total=False):
    limit: int

    search: str
    """You can supply any string to help narrow down the list of resources.

    For example, if you pass `"New York"` (quoted), it will return resources that
    have that string present somewhere in their response. Alternatively, you can
    supply a structured search query. See the documentation on
    `StructuredSearchQuery` for more details.
    """

    skip: int
