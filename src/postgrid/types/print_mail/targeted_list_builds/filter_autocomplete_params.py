# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FilterAutocompleteParams"]


class FilterAutocompleteParams(TypedDict, total=False):
    field: Required[Literal["industry"]]
    """A field that can be autocompleted when configuring list build filters."""

    size: int
    """Maximum number of suggestions to return.

    Between 1 and 100. Defaults to 25 if omitted.
    """

    text: str
    """Optional text prefix to narrow the autocomplete suggestions."""
