# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..letter_size import LetterSize
from ..attached_pdf import AttachedPdf
from ..address_placement import AddressPlacement

__all__ = ["LetterProfile"]


class LetterProfile(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the profile was created."""

    live: bool
    """Indicates if the profile is associated with the live or test environment."""

    object: Literal["letter_profile"]
    """Always `letter_profile`."""

    size: LetterSize
    """Enum representing the supported letter sizes."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the profile was last updated."""

    address_placement: Optional[AddressPlacement] = FieldInfo(alias="addressPlacement", default=None)
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Optional[AttachedPdf] = FieldInfo(alias="attachedPDF", default=None)
    """Model representing an attached PDF."""

    color: Optional[bool] = None
    """Specifies whether to print in color (true) or black and white (false)."""

    description: Optional[str] = None
    """An optional description for the profile. Set to `null` to remove during update."""

    double_sided: Optional[bool] = FieldInfo(alias="doubleSided", default=None)
    """Specifies whether to print on both sides of the paper."""

    envelope: Optional[str] = None
    """ID of a custom envelope to use."""

    mailing_class: Optional[
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
        ]
    ] = FieldInfo(alias="mailingClass", default=None)
    """Mailing class."""

    merge_variables: Optional[Dict[str, builtins.object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    perforated_page: Optional[Literal[1]] = FieldInfo(alias="perforatedPage", default=None)
    """Specifies which page number should be perforated (if any)."""

    template: Optional[str] = None
    """ID of a template to use for the letter content. Cannot be used with `pdf`."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A temporary, signed URL to view the uploaded PDF, if any."""
