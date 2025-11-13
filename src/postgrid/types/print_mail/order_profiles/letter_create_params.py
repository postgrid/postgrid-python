# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..letter_size import LetterSize
from ..address_placement import AddressPlacement
from ..attached_pdf_param import AttachedPdfParam

__all__ = ["LetterCreateParams"]


class LetterCreateParams(TypedDict, total=False):
    size: Required[LetterSize]
    """Enum representing the supported letter sizes."""

    expand: SequenceNotStr[str]
    """Optional list of related resources to expand in the response."""

    address_placement: Annotated[AddressPlacement, PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[AttachedPdfParam, PropertyInfo(alias="attachedPDF")]
    """Model representing an attached PDF."""

    color: bool
    """Specifies whether to print in color (true) or black and white (false)."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    double_sided: Annotated[bool, PropertyInfo(alias="doubleSided")]
    """Specifies whether to print on both sides of the paper."""

    envelope: str
    """ID of a custom envelope to use."""

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
    """Mailing class."""

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""

    pdf: str
    """A PDF file containing the letter content. Cannot be used with `template`."""

    perforated_page: Annotated[Literal[1], PropertyInfo(alias="perforatedPage")]
    """Specifies which page number should be perforated (if any)."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """ID of a return envelope to include."""

    template: str
    """ID of a template to use for the letter content. Cannot be used with `pdf`."""
