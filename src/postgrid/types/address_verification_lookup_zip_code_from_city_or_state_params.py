# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AddressVerificationLookupZipCodeFromCityOrStateParams"]


class AddressVerificationLookupZipCodeFromCityOrStateParams(TypedDict, total=False):
    city: Required[str]
    """The city name."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The country code. Currently only `US` is supported."""

    state: Required[str]
    """The state abbreviation (e.g. `NY`)."""
