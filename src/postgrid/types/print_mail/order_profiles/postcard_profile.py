# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .postcard_size import PostcardSize

__all__ = ["PostcardProfile"]


class PostcardProfile(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the profile was created."""

    live: bool
    """Indicates if the profile is associated with the live or test environment."""

    object: Literal["postcard_profile"]
    """Always `postcard_profile`."""

    size: PostcardSize
    """Enum representing the supported postcard sizes."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the profile was last updated."""

    back_template: Optional[str] = FieldInfo(alias="backTemplate", default=None)
    """ID of the template for the back side. Required unless `pdf` is provided."""

    description: Optional[str] = None
    """An optional description for the profile. Set to `null` to remove during update."""

    front_template: Optional[str] = FieldInfo(alias="frontTemplate", default=None)
    """ID of the template for the front side. Required unless `pdf` is provided."""

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
    """
    Mailing class (cannot include extra services like `certified` or `registered`
    for postcards, though).
    """

    merge_variables: Optional[Dict[str, builtins.object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A temporary, signed URL to view the uploaded PDF content, if any."""
