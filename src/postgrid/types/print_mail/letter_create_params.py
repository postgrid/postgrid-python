# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .letter_size import LetterSize
from .address_placement import AddressPlacement
from .attached_pdf_param import AttachedPdfParam
from .plastic_card_param import PlasticCardParam
from ..contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from ..contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = [
    "LetterCreateParams",
    "LetterCreateWithHTML",
    "LetterCreateWithHTMLFrom",
    "LetterCreateWithHTMLTo",
    "LetterCreateWithTemplate",
    "LetterCreateWithPdf",
    "LetterCreateWithPdfFrom",
    "LetterCreateWithPdfTo",
]


class LetterCreateWithHTML(TypedDict, total=False):
    from_: Required[Annotated[LetterCreateWithHTMLFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    html: Required[str]
    """The HTML content for the letter.

    You can supply _either_ this or `template` but not both.
    """

    to: Required[LetterCreateWithHTMLTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    address_placement: Annotated[AddressPlacement, PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[AttachedPdfParam, PropertyInfo(alias="attachedPDF")]
    """Model representing an attached PDF."""

    color: bool
    """Indicates if the letter is in color."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    double_sided: Annotated[bool, PropertyInfo(alias="doubleSided")]
    """Indicates if the letter is double-sided."""

    envelope: str
    """The envelope (ID) for the letter.

    You can either specify a custom envelope ID or use the default `standard`
    envelope.
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
    """The mailing class of this order.

    If not provided, automatically set to `first_class`.
    """

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """
    These will be merged with the variables in the template or HTML you create this
    order with. The keys in this object should match the variable names in the
    template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
    PDFs uploaded with the order.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    perforated_page: Annotated[Literal[1], PropertyInfo(alias="perforatedPage")]
    """If specified, indicates which letter page is perforated.

    Currently, only the first page can be perforated.
    """

    plastic_card: Annotated[PlasticCardParam, PropertyInfo(alias="plasticCard")]
    """Model representing a plastic card."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """The return envelope (ID) sent out with the letter, if any."""

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    size: LetterSize
    """Enum representing the supported letter sizes."""


LetterCreateWithHTMLFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

LetterCreateWithHTMLTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class LetterCreateWithTemplate(TypedDict, total=False):
    template: Required[str]
    """The template ID for the letter.

    You can supply _either_ this or `html` but not both.
    """


class LetterCreateWithPdf(TypedDict, total=False):
    from_: Required[Annotated[LetterCreateWithPdfFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    pdf: Required[str]
    """A URL pointing to a PDF file for the letter or the PDF file itself."""

    to: Required[LetterCreateWithPdfTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    address_placement: Annotated[AddressPlacement, PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[AttachedPdfParam, PropertyInfo(alias="attachedPDF")]
    """Model representing an attached PDF."""

    color: bool
    """Indicates if the letter is in color."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    double_sided: Annotated[bool, PropertyInfo(alias="doubleSided")]
    """Indicates if the letter is double-sided."""

    envelope: str
    """The envelope (ID) for the letter.

    You can either specify a custom envelope ID or use the default `standard`
    envelope.
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
    """The mailing class of this order.

    If not provided, automatically set to `first_class`.
    """

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """
    These will be merged with the variables in the template or HTML you create this
    order with. The keys in this object should match the variable names in the
    template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
    PDFs uploaded with the order.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    perforated_page: Annotated[Literal[1], PropertyInfo(alias="perforatedPage")]
    """If specified, indicates which letter page is perforated.

    Currently, only the first page can be perforated.
    """

    plastic_card: Annotated[PlasticCardParam, PropertyInfo(alias="plasticCard")]
    """Model representing a plastic card."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """The return envelope (ID) sent out with the letter, if any."""

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    size: LetterSize
    """Enum representing the supported letter sizes."""


LetterCreateWithPdfFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

LetterCreateWithPdfTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

LetterCreateParams: TypeAlias = Union[LetterCreateWithHTML, LetterCreateWithTemplate, LetterCreateWithPdf]
