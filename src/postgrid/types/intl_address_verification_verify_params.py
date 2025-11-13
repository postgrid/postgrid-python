# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IntlAddressVerificationVerifyParams",
    "StructuredAddressInput",
    "StructuredAddressInputAddress",
    "FreeformAddressInput",
]


class StructuredAddressInput(TypedDict, total=False):
    address: Required[StructuredAddressInputAddress]

    geo_data: Annotated[bool, PropertyInfo(alias="geoData")]

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]


class StructuredAddressInputAddress(TypedDict, total=False):
    country: Required[str]
    """The country code (ISO 3166-1 alpha-2 or alpha-3)."""

    line1: Required[str]
    """The first line of the address (e.g., street address, building, etc.)."""

    postal_or_zip: Required[Annotated[str, PropertyInfo(alias="postalOrZip")]]
    """The postal or ZIP code."""

    province_or_state: Required[Annotated[str, PropertyInfo(alias="provinceOrState")]]
    """The administrative area (e.g., state, province, region)."""

    city: str
    """The city, town, or locality of the address."""

    line2: str
    """The second line of the address (e.g., apartment, suite, etc.)."""

    line3: str
    """The third line of the address (e.g., additional locality or delivery info)."""

    line4: str
    """The fourth line of the address (e.g., further address details)."""


class FreeformAddressInput(TypedDict, total=False):
    address: Required[str]
    """The full address as a single string."""

    geo_data: Annotated[bool, PropertyInfo(alias="geoData")]

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]


IntlAddressVerificationVerifyParams: TypeAlias = Union[StructuredAddressInput, FreeformAddressInput]
