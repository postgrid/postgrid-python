# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config
from .cheque_size import ChequeSize
from .letter_size import LetterSize
from .address_placement import AddressPlacement
from .attached_pdf_param import AttachedPdfParam

__all__ = ["CampaignCreateParams", "Cheque", "ChequeLetterSettings", "Letter", "Postcard", "SelfMailer", "SnapPack"]


class CampaignCreateParams(TypedDict, total=False):
    mailing_list: Required[Annotated[str, PropertyInfo(alias="mailingList")]]
    """The ID of the mailing list associated with this campaign."""

    cheque: Cheque
    """Inline cheque configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    default_sender_contact: Annotated[str, PropertyInfo(alias="defaultSenderContact")]
    """
    The ID of the default sender contact to use for orders if not specified per
    recipient.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    letter: Letter
    """Inline letter configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    postcard: Postcard
    """Inline postcard configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    self_mailer: Annotated[SelfMailer, PropertyInfo(alias="selfMailer")]
    """Inline self-mailer configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """The scheduled date and time for the campaign to be sent."""

    snap_pack: Annotated[SnapPack, PropertyInfo(alias="snapPack")]
    """Inline snap pack configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


class ChequeLetterSettings(TypedDict, total=False):
    """Settings for the attached letter (e.g., color printing)."""

    color: bool
    """Whether to print the attached letter in color."""


class Cheque(TypedDict, total=False):
    """Inline cheque configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    bank_account: Annotated[str, PropertyInfo(alias="bankAccount")]
    """ID of the bank account to use for the cheque."""

    currency_code: Annotated[Literal["CAD", "USD"], PropertyInfo(alias="currencyCode")]
    """Enum representing the supported currency codes."""

    description: str
    """An optional description."""

    envelope: str
    """The custom envelope ID or `"standard"`."""

    letter_pdf: Annotated[Union[str, Base64FileInput], PropertyInfo(alias="letterPDF", format="base64")]
    """PDF file for an optional attached letter. Cannot be used with `letterTemplate`."""

    letter_settings: Annotated[ChequeLetterSettings, PropertyInfo(alias="letterSettings")]
    """Settings for the attached letter (e.g., color printing)."""

    letter_template: Annotated[str, PropertyInfo(alias="letterTemplate")]
    """ID of a template for an optional attached letter.

    Cannot be used with `letterPDF`.
    """

    logo: str
    """A publicly accessible URL for the logo to print on the cheque."""

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
    """Mailing class for the cheque."""

    memo: str
    """Memo line text for the cheque."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for the cheque."""

    message: str
    """Message included on the cheque stub."""

    metadata: Dict[str, str]
    """Optional key-value metadata."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """ID of a return envelope to include."""

    size: ChequeSize
    """Enum representing the supported cheque sizes."""


set_pydantic_config(Cheque, {"arbitrary_types_allowed": True})


class Letter(TypedDict, total=False):
    """Inline letter configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    address_placement: Annotated[AddressPlacement, PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[AttachedPdfParam, PropertyInfo(alias="attachedPDF")]
    """Model representing an attached PDF."""

    color: bool
    """Whether to print in color."""

    description: str
    """An optional description."""

    double_sided: Annotated[bool, PropertyInfo(alias="doubleSided")]
    """Whether to print on both sides of the paper."""

    envelope: str
    """The custom envelope ID or `"standard"`."""

    envelope_type: Annotated[Literal["standard_double_window", "flat"], PropertyInfo(alias="envelopeType")]
    """The type of envelope used for the letter."""

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
    """Mailing class for the letter."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for the letter."""

    metadata: Dict[str, str]
    """Optional key-value metadata."""

    pdf: str
    """A PDF file or URL for the letter content. Cannot be used with `template`."""

    perforated_page: Annotated[Literal[1], PropertyInfo(alias="perforatedPage")]
    """Which page number should be perforated (if any)."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """ID of a return envelope to include."""

    size: LetterSize
    """Enum representing the supported letter sizes."""

    template: str
    """ID of a template for the letter content. Cannot be used with `pdf`."""


class Postcard(TypedDict, total=False):
    """Inline postcard configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """ID of the template for the back side. Cannot be used with `pdf`."""

    description: str
    """An optional description."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """ID of the template for the front side. Cannot be used with `pdf`."""

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
    """Mailing class for the postcard."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for the postcard."""

    metadata: Dict[str, str]
    """Optional key-value metadata."""

    paper: str
    """Premium paper identifier.

    Use "standard" for regular stock or a premium*paper*\\** ID.
    """

    pdf: str
    """A 2-page PDF file for the postcard content (front and back).

    Cannot be used with `frontTemplate`/`backTemplate`.
    """

    size: Literal["6x4", "9x6", "11x6"]
    """Enum representing the supported postcard sizes."""


class SelfMailer(TypedDict, total=False):
    """Inline self-mailer configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    description: str
    """An optional description."""

    inside_template: Annotated[str, PropertyInfo(alias="insideTemplate")]
    """ID of the template for the inside. Cannot be used with `pdf`."""

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
    """Mailing class for the self-mailer."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for the self-mailer."""

    metadata: Dict[str, str]
    """Optional key-value metadata."""

    outside_template: Annotated[str, PropertyInfo(alias="outsideTemplate")]
    """ID of the template for the outside. Cannot be used with `pdf`."""

    pdf: str
    """A 2-page PDF file for the self-mailer content.

    Cannot be used with `insideTemplate`/`outsideTemplate`.
    """

    size: Literal["8.5x11_bifold", "8.5x11_trifold", "9.5x16_trifold"]
    """Enum representing the supported self-mailer sizes."""


class SnapPack(TypedDict, total=False):
    """Inline snap pack configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    description: str
    """An optional description."""

    inside_template: Annotated[str, PropertyInfo(alias="insideTemplate")]
    """ID of the template for the inside. Cannot be used with `pdf`."""

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
    """Mailing class for the snap pack."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for the snap pack."""

    metadata: Dict[str, str]
    """Optional key-value metadata."""

    outside_template: Annotated[str, PropertyInfo(alias="outsideTemplate")]
    """ID of the template for the outside. Cannot be used with `pdf`."""

    pdf: str
    """A 2-page PDF file for the snap pack content.

    Cannot be used with `insideTemplate`/`outsideTemplate`.
    """

    size: Literal["8.5x11_bifold_v"]
    """Enum representing the supported snap pack sizes."""
