# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressVerificationParseAnAddressResponse", "Data"]


class Data(BaseModel):
    category: Optional[str] = None
    """The category of the location (e.g. restaurant)."""

    city: Optional[str] = None
    """The city name."""

    city_district: Optional[str] = FieldInfo(alias="cityDistrict", default=None)
    """The borough within a city."""

    country: Optional[str] = None
    """The country."""

    house: Optional[str] = None
    """The name of the location."""

    house_number: Optional[str] = FieldInfo(alias="houseNumber", default=None)
    """The house or street number."""

    island: Optional[str] = None
    """The name of the island."""

    level: Optional[str] = None
    """The floor."""

    near: Optional[str] = None
    """Populated if the input query contains a near/in qualifier."""

    po_box: Optional[str] = FieldInfo(alias="poBox", default=None)
    """The postal office box."""

    postcode: Optional[str] = None
    """The postal or ZIP code."""

    road: Optional[str] = None
    """The street name."""

    state: Optional[str] = None
    """The state or province."""

    state_district: Optional[str] = FieldInfo(alias="stateDistrict", default=None)
    """The county."""

    suburb: Optional[str] = None
    """The unofficial neighborhood name."""

    unit: Optional[str] = None
    """The apartment, unit, office, lot, or other secondary unit designator."""


class AddressVerificationParseAnAddressResponse(BaseModel):
    data: Data

    message: str

    status: Literal["success", "error"]
