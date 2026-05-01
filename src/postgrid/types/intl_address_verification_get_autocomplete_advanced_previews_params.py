# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntlAddressVerificationGetAutocompleteAdvancedPreviewsParams"]


class IntlAddressVerificationGetAutocompleteAdvancedPreviewsParams(TypedDict, total=False):
    advanced: bool

    city_filter: Annotated[str, PropertyInfo(alias="cityFilter")]

    container: str

    countries_filter: Annotated[str, PropertyInfo(alias="countriesFilter")]

    disable_ip_biasing: Annotated[bool, PropertyInfo(alias="disableIPBiasing")]

    language: str

    limit: int

    partial_street: Annotated[str, PropertyInfo(alias="partialStreet")]

    postal_or_zip_filter: Annotated[str, PropertyInfo(alias="postalOrZipFilter")]

    standard_fallback: Annotated[bool, PropertyInfo(alias="standardFallback")]

    street_filter: Annotated[str, PropertyInfo(alias="streetFilter")]

    use_enhanced_china_dataset: Annotated[bool, PropertyInfo(alias="useEnhancedChinaDataset")]
