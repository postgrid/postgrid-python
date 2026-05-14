# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse", "Data"]


class Data(BaseModel):
    city: str
    """The city name."""

    country: str
    """The ISO 2-letter country code."""

    province_or_state: str = FieldInfo(alias="provinceOrState")
    """The province or state abbreviation."""

    county: Optional[str] = None
    """The county name (US addresses only)."""

    county_fips: Optional[str] = FieldInfo(alias="countyFIPS", default=None)
    """The FIPS code for the county (US addresses only)."""

    mailable: Optional[bool] = None
    """Whether the location is mailable."""

    preferred_city: Optional[str] = FieldInfo(alias="preferredCity", default=None)
    """The USPS preferred city name for this postal code."""

    zip_class: Optional[str] = FieldInfo(alias="zipClass", default=None)
    """The USPS ZIP code class (e.g. `S` for standard, `P` for PO Box only)."""


class AddressVerificationLookupCityOrStateFromPostalOrZipCodeResponse(BaseModel):
    data: List[Data]

    message: str

    status: Literal["success", "error"]
