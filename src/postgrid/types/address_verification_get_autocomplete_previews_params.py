# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AddressVerificationGetAutocompletePreviewsParams"]


class AddressVerificationGetAutocompletePreviewsParams(TypedDict, total=False):
    partial_street: Required[Annotated[str, PropertyInfo(alias="partialStreet")]]

    city_filter: Annotated[str, PropertyInfo(alias="cityFilter")]

    country_filter: Annotated[str, PropertyInfo(alias="countryFilter")]

    filter_exact: Annotated[bool, PropertyInfo(alias="filterExact")]

    limit: int

    pc_filter: Annotated[str, PropertyInfo(alias="pcFilter")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]

    prov_instead_of_pc: Annotated[bool, PropertyInfo(alias="provInsteadOfPC")]

    state_filter: Annotated[str, PropertyInfo(alias="stateFilter")]

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
