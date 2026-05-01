# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntlAddressVerificationGetAutocompletePreviewsResponse", "Data"]


class Data(BaseModel):
    """
    A single address suggestion returned by `GET /completions`.
    Use the `id` field to retrieve the full address via `POST /completions`.
    """

    id: Optional[str] = None
    """The unique identifier for this result.

    Pass this to `POST /completions` to retrieve the full address. If the `type` is
    `Container`, pass it as the `container` parameter to `GET /completions` to drill
    down further.
    """

    description: Optional[str] = None
    """A secondary description of the result (e.g. city and country)."""

    error: Optional[str] = None
    """An error message if the lookup failed for this result."""

    highlight: Optional[str] = None
    """Character ranges within `text` that match the search input, for bolding in UI."""

    text: Optional[str] = None
    """The human-readable address suggestion text."""

    type: Optional[str] = None
    """The type of result.

    `Address` means this can be resolved directly via `POST /completions`.
    `Container` means the result represents a building or complex — perform another
    `GET /completions` with this `id` as `container` to get individual unit
    addresses.
    """


class IntlAddressVerificationGetAutocompletePreviewsResponse(BaseModel):
    data: List[Data]

    message: str

    status: Literal["success", "error"]
