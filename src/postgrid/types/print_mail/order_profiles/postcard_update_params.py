# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["PostcardUpdateParams"]


class PostcardUpdateParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """Optional list of related resources to expand in the response."""

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """ID of the template for the back side. Required unless `pdf` is provided."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """ID of the template for the front side. Required unless `pdf` is provided."""

    mailing_class: Annotated[
        Literal[
            "first_class",
            "standard_class",
            "express",
            "certified",
            "certified_return_receipt",
            "registered",
            "usps_first_class",
            "usps_standard_class",
            "usps_eddm",
            "usps_express_2_day",
            "usps_express_3_day",
            "usps_first_class_certified",
            "usps_first_class_certified_return_receipt",
            "usps_first_class_registered",
            "usps_express_3_day_signature_confirmation",
            "usps_express_3_day_certified",
            "usps_express_3_day_certified_return_receipt",
            "ca_post_lettermail",
            "ca_post_personalized",
            "ca_post_neighbourhood_mail",
            "ups_express_overnight",
            "ups_express_2_day",
            "ups_express_3_day",
            "royal_mail_first_class",
            "royal_mail_second_class",
            "au_post_second_class",
        ],
        PropertyInfo(alias="mailingClass"),
    ]
    """
    Mailing class (cannot include extra services like `certified` or `registered`
    for postcards, though).
    """

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""

    pdf: str
    """A 2-page PDF file containing the postcard content (front and back).

    Cannot be used with `frontTemplate`/`backTemplate`.
    """
