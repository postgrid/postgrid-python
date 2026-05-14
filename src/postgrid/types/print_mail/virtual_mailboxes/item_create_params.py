# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ItemCreateParams"]


class ItemCreateParams(TypedDict, total=False):
    description: str
    """The description of the item."""

    matched_letter: Annotated[str, PropertyInfo(alias="matchedLetter")]
    """The ID of a letter to match this test item to."""

    metadata: Dict[str, object]
    """The metadata of the item."""
