# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FilterAutocompleteResponse", "Data"]


class Data(BaseModel):
    """A single autocomplete suggestion."""

    type: Literal["industry"]
    """A field that can be autocompleted when configuring list build filters."""

    value: str
    """The suggested value (e.g., an industry name)."""


class FilterAutocompleteResponse(BaseModel):
    """The list of suggestions returned by an autocomplete query."""

    data: List[Data]

    object: Literal["list"]
