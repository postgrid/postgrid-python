# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AddressVerificationVerifyParams",
    "StandardFreeformAddressInput",
    "StandardStructuredAddressInput",
    "StandardStructuredAddressInputAddress",
]


class StandardFreeformAddressInput(TypedDict, total=False):
    address: Required[str]
    """The address you want to verify, written on a single line."""

    geocode: bool

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]


class StandardStructuredAddressInput(TypedDict, total=False):
    address: Required[StandardStructuredAddressInputAddress]

    geocode: bool

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]


class StandardStructuredAddressInputAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the address."""

    country: Required[Literal["ca", "us"]]
    """The country of your address, one of `ca` or `us`."""

    line1: Required[str]
    """The first line of the address."""

    postal_or_zip: Required[Annotated[str, PropertyInfo(alias="postalOrZip")]]
    """The postal code or ZIP code of the address."""

    province_or_state: Required[Annotated[str, PropertyInfo(alias="provinceOrState")]]
    """The province or state of the address."""

    line2: str
    """The second line of the address."""

    recipient: str
    """The optional firm/recipient name."""


AddressVerificationVerifyParams: TypeAlias = Union[StandardFreeformAddressInput, StandardStructuredAddressInput]
