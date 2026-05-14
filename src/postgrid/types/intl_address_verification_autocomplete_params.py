# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntlAddressVerificationAutocompleteParams"]


class IntlAddressVerificationAutocompleteParams(TypedDict, total=False):
    id: Required[str]

    include_details: Annotated[bool, PropertyInfo(alias="includeDetails")]

    proper_case: Annotated[bool, PropertyInfo(alias="properCase")]

    use_enhanced_china_dataset: Annotated[bool, PropertyInfo(alias="useEnhancedChinaDataset")]

    verify: bool
