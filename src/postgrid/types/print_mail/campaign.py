# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .cheque_size import ChequeSize
from .letter_size import LetterSize
from .attached_pdf import AttachedPdf
from .address_placement import AddressPlacement

__all__ = ["Campaign", "Cheque", "ChequeLetterSettings", "Error", "Letter", "Postcard", "SelfMailer", "SnapPack"]


class ChequeLetterSettings(BaseModel):
    """Settings for the attached letter (e.g., color printing)."""

    color: Optional[bool] = None
    """Whether to print the attached letter in color."""


class Cheque(BaseModel):
    """Inline cheque configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    bank_account: Optional[str] = FieldInfo(alias="bankAccount", default=None)
    """ID of the bank account to use for the cheque."""

    currency_code: Optional[Literal["CAD", "USD"]] = FieldInfo(alias="currencyCode", default=None)
    """Enum representing the supported currency codes."""

    description: Optional[str] = None
    """An optional description."""

    envelope: Optional[str] = None
    """The custom envelope ID or `"standard"`."""

    letter_settings: Optional[ChequeLetterSettings] = FieldInfo(alias="letterSettings", default=None)
    """Settings for the attached letter (e.g., color printing)."""

    letter_template: Optional[str] = FieldInfo(alias="letterTemplate", default=None)
    """ID of a template for an optional attached letter.

    Cannot be used with `letterPDF`.
    """

    letter_uploaded_pdf: Optional[str] = FieldInfo(alias="letterUploadedPDF", default=None)
    """A signed URL to the attached letter PDF, if any."""

    logo: Optional[str] = None
    """A publicly accessible URL for the logo to print on the cheque."""

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
    """Mailing class for the cheque."""

    memo: Optional[str] = None
    """Memo line text for the cheque."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for the cheque."""

    message: Optional[str] = None
    """Message included on the cheque stub."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    return_envelope: Optional[str] = FieldInfo(alias="returnEnvelope", default=None)
    """ID of a return envelope to include."""

    size: Optional[ChequeSize] = None
    """Enum representing the supported cheque sizes."""


class Error(BaseModel):
    """Details of a specific error encountered during campaign processing."""

    message: str
    """A human-readable message describing the error."""

    type: Literal["processing_error", "internal_error"]
    """Type of error encountered during campaign processing."""


class Letter(BaseModel):
    """Inline letter configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    address_placement: Optional[AddressPlacement] = FieldInfo(alias="addressPlacement", default=None)
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Optional[AttachedPdf] = FieldInfo(alias="attachedPDF", default=None)
    """Model representing an attached PDF."""

    color: Optional[bool] = None
    """Whether to print in color."""

    description: Optional[str] = None
    """An optional description."""

    double_sided: Optional[bool] = FieldInfo(alias="doubleSided", default=None)
    """Whether to print on both sides of the paper."""

    envelope: Optional[str] = None
    """The custom envelope ID or `"standard"`."""

    envelope_type: Optional[Literal["standard_double_window", "flat"]] = FieldInfo(alias="envelopeType", default=None)
    """The type of envelope used for the letter."""

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
    """Mailing class for the letter."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for the letter."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    perforated_page: Optional[Literal[1]] = FieldInfo(alias="perforatedPage", default=None)
    """Which page number should be perforated (if any)."""

    return_envelope: Optional[str] = FieldInfo(alias="returnEnvelope", default=None)
    """ID of a return envelope to include."""

    size: Optional[LetterSize] = None
    """Enum representing the supported letter sizes."""

    template: Optional[str] = None
    """ID of a template for the letter content. Cannot be used with `pdf`."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A signed URL to the uploaded PDF, if any."""


class Postcard(BaseModel):
    """Inline postcard configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    back_template: Optional[str] = FieldInfo(alias="backTemplate", default=None)
    """ID of the template for the back side. Cannot be used with `pdf`."""

    description: Optional[str] = None
    """An optional description."""

    front_template: Optional[str] = FieldInfo(alias="frontTemplate", default=None)
    """ID of the template for the front side. Cannot be used with `pdf`."""

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
    """Mailing class for the postcard."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for the postcard."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    paper: Optional[str] = None
    """Premium paper identifier.

    Use "standard" for regular stock or a premium*paper*\\** ID.
    """

    size: Optional[Literal["6x4", "9x6", "11x6"]] = None
    """Enum representing the supported postcard sizes."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A signed URL to the uploaded PDF, if any."""


class SelfMailer(BaseModel):
    """Inline self-mailer configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    description: Optional[str] = None
    """An optional description."""

    inside_template: Optional[str] = FieldInfo(alias="insideTemplate", default=None)
    """ID of the template for the inside. Cannot be used with `pdf`."""

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
    """Mailing class for the self-mailer."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for the self-mailer."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    outside_template: Optional[str] = FieldInfo(alias="outsideTemplate", default=None)
    """ID of the template for the outside. Cannot be used with `pdf`."""

    size: Optional[Literal["8.5x11_bifold", "8.5x11_trifold", "9.5x16_trifold"]] = None
    """Enum representing the supported self-mailer sizes."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A signed URL to the uploaded PDF, if any."""


class SnapPack(BaseModel):
    """Inline snap pack configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during drafting.
    """

    description: Optional[str] = None
    """An optional description."""

    inside_template: Optional[str] = FieldInfo(alias="insideTemplate", default=None)
    """ID of the template for the inside. Cannot be used with `pdf`."""

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
    """Mailing class for the snap pack."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for the snap pack."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    outside_template: Optional[str] = FieldInfo(alias="outsideTemplate", default=None)
    """ID of the template for the outside. Cannot be used with `pdf`."""

    size: Optional[Literal["8.5x11_bifold_v"]] = None
    """Enum representing the supported snap pack sizes."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A signed URL to the uploaded PDF, if any."""


class Campaign(BaseModel):
    """Represents a bulk mail campaign."""

    id: str
    """A unique ID prefixed with campaign\\__"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    created_count: int = FieldInfo(alias="createdCount")
    """The number of orders successfully created for this campaign."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    mailing_list: str = FieldInfo(alias="mailingList")
    """The ID of the mailing list associated with this campaign."""

    status: Literal[
        "drafting", "changes_required", "creating_orders", "draft", "ready", "printing", "processed_for_delivery"
    ]
    """Status of the campaign lifecycle."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    cheque: Optional[Cheque] = None
    """Inline cheque configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    default_sender_contact: Optional[str] = FieldInfo(alias="defaultSenderContact", default=None)
    """
    The ID of the default sender contact to use for orders if not specified per
    recipient.
    """

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    errors: Optional[List[Error]] = None
    """A list of processing errors encountered, if any.

    Present when status is 'changes_required'.
    """

    letter: Optional[Letter] = None
    """Inline letter configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""

    order_preview_url: Optional[str] = FieldInfo(alias="orderPreviewURL", default=None)
    """
    A temporary URL to preview the first rendered order, available once the campaign
    status is 'draft' or later.
    """

    postcard: Optional[Postcard] = None
    """Inline postcard configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    report_url: Optional[str] = FieldInfo(alias="reportURL", default=None)
    """
    A temporary URL to download the processing report, available once the campaign
    is in the `ready` status.
    """

    self_mailer: Optional[SelfMailer] = FieldInfo(alias="selfMailer", default=None)
    """Inline self-mailer configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """

    send_date: Optional[datetime] = FieldInfo(alias="sendDate", default=None)
    """The scheduled date and time for the campaign to be sent."""

    snap_pack: Optional[SnapPack] = FieldInfo(alias="snapPack", default=None)
    """Inline snap pack configuration for a campaign.

    All fields are optional since campaigns may be in a partial state during
    drafting.
    """
