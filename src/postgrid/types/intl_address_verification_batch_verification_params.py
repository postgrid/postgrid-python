# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IntlAddressVerificationBatchVerificationParams",
    "Address",
    "AddressStructuredAddressInput",
    "AddressStructuredAddressInputAddress",
    "AddressFreeformAddressInput",
]


class IntlAddressVerificationBatchVerificationParams(TypedDict, total=False):
    addresses: Required[Iterable[Address]]
    """Array of addresses to verify.

    Each item can be a freeform string or a structured address object.
    """

    geo_data: Annotated[bool, PropertyInfo(alias="geoData")]

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]

    use_enhanced_china_dataset: Annotated[bool, PropertyInfo(alias="useEnhancedChinaDataset")]


class AddressStructuredAddressInputAddress(TypedDict, total=False):
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


class AddressStructuredAddressInput(TypedDict, total=False):
    """Input model for structured international address verification."""

    address: Required[AddressStructuredAddressInputAddress]


class AddressFreeformAddressInput(TypedDict, total=False):
    """Input model for freeform international address verification."""

    address: Required[str]
    """The full address as a single string."""


Address: TypeAlias = Union[AddressStructuredAddressInput, AddressFreeformAddressInput]
