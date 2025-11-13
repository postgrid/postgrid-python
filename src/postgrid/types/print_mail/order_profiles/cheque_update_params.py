# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr, Base64FileInput
from ...._utils import PropertyInfo
from ..cheque_size import ChequeSize
from .currency_code import CurrencyCode

__all__ = ["ChequeUpdateParams"]


class ChequeUpdateParams(TypedDict, total=False):
    bank_account: Required[Annotated[str, PropertyInfo(alias="bankAccount")]]
    """ID of the bank account to use for the cheque. Required for creation."""

    size: Required[ChequeSize]
    """Enum representing the supported cheque sizes."""

    expand: SequenceNotStr[str]
    """Optional list of related resources to expand in the response."""

    currency_code: Annotated[CurrencyCode, PropertyInfo(alias="currencyCode")]
    """Enum representing the supported currency codes."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    letter_pdf: Annotated[Union[str, Base64FileInput], PropertyInfo(alias="letterPDF", format="base64")]
    """PDF file for an optional attached letter.

    Cannot be used with `letterHTML` or `letterTemplate`. Input only.
    """

    letter_template: Annotated[str, PropertyInfo(alias="letterTemplate")]
    """ID of a template for an optional attached letter.

    Cannot be used with `letterHTML` or `letterPDF`.
    """

    logo: Optional[str]
    """A publicly accessible URL for the logo to print on the cheque.

    Set to `null` to remove during update.
    """

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
    """Mailing class.

    Generally must be first class (or equivalent for destination country) for
    cheques.
    """

    memo: Optional[str]
    """Memo line text for the cheque. Set to `null` to remove during update."""

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    message: Optional[str]
    """Message included on the cheque stub. Set to `null` to remove during update."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""
