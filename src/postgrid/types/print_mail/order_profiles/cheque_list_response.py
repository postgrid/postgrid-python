# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..cheque_size import ChequeSize

__all__ = ["ChequeListResponse"]


class ChequeListResponse(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    bank_account: str = FieldInfo(alias="bankAccount")
    """ID of the bank account to use for the cheque. Required for creation."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the profile was created."""

    live: bool
    """Indicates if the profile is associated with the live or test environment."""

    object: Literal["cheque_profile"]
    """Always `cheque_profile`."""

    size: ChequeSize
    """Enum representing the supported cheque sizes."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the profile was last updated."""

    description: Optional[str] = None
    """An optional description for the profile. Set to `null` to remove during update."""

    letter_template: Optional[str] = FieldInfo(alias="letterTemplate", default=None)
    """ID of a template for an optional attached letter.

    Cannot be used with `letterHTML` or `letterPDF`.
    """

    letter_uploaded_pdf: Optional[str] = FieldInfo(alias="letterUploadedPDF", default=None)
    """A temporary, signed URL to view the attached letter PDF, if any. Output only."""

    logo: Optional[str] = None
    """A publicly accessible URL for the logo to print on the cheque.

    Set to `null` to remove during update.
    """

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
    """Mailing class.

    Generally must be first class (or equivalent for destination country) for
    cheques.
    """

    memo: Optional[str] = None
    """Memo line text for the cheque. Set to `null` to remove during update."""

    merge_variables: Optional[Dict[str, builtins.object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for orders created using this profile."""

    message: Optional[str] = None
    """Message included on the cheque stub. Set to `null` to remove during update."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""
