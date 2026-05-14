# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AddressVerificationGetAutocompletePreviewsResponse", "Data", "DataPreview"]


class DataPreview(BaseModel):
    """
    A partial view of the address, suitable for display in an autocomplete dropdown.
    """

    address: str
    """The street address line."""

    city: Optional[str] = None
    """The city."""

    pc: Optional[str] = None
    """For US addresses, the full postal code.

    For non-US addresses, only the first 3 digits are returned to avoid consuming a
    lookup.
    """

    prov: Optional[str] = None
    """The province or state abbreviation.

    Returned instead of `pc` when `provInsteadOfPC=true`.
    """


class Data(BaseModel):
    preview: DataPreview
    """
    A partial view of the address, suitable for display in an autocomplete dropdown.
    """


class AddressVerificationGetAutocompletePreviewsResponse(BaseModel):
    data: List[Data]

    message: str

    status: Literal["success", "error"]
