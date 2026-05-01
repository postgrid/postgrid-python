# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AddressVerificationAutocompleteParams"]


class AddressVerificationAutocompleteParams(TypedDict, total=False):
    partial_street: Required[Annotated[str, PropertyInfo(alias="partialStreet")]]
    """The partial street address to complete (e.g. `"22 Bay"`)."""

    filter_exact: Annotated[bool, PropertyInfo(alias="filterExact")]

    geocode: bool

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    index: int

    limit: int

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]

    query_verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]

    verify: bool

    city_filter: Annotated[str, PropertyInfo(alias="cityFilter")]
    """Filter results to a specific city."""

    country_filter: Annotated[str, PropertyInfo(alias="countryFilter")]
    """Filter results to a specific country code."""

    pc_filter: Annotated[str, PropertyInfo(alias="pcFilter")]
    """Filter results to a specific postal code prefix."""

    state_filter: Annotated[str, PropertyInfo(alias="stateFilter")]
    """Filter results to a specific state or province abbreviation."""

    body_verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """If true, only return addresses that passed USPS/Canada Post verification."""
