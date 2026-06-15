# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo
from .contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from .contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = [
    "SnapPackCreateParams",
    "SnapPackCreateWithHTML",
    "SnapPackCreateWithHTMLFrom",
    "SnapPackCreateWithHTMLTo",
    "SnapPackCreateWithTemplate",
    "SnapPackCreateWithTemplateFrom",
    "SnapPackCreateWithTemplateTo",
    "SnapPackCreateWithPdf",
    "SnapPackCreateWithPdfFrom",
    "SnapPackCreateWithPdfTo",
]


class SnapPackCreateWithHTML(TypedDict, total=False):
    from_: Required[Annotated[SnapPackCreateWithHTMLFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`
    contact.
    """

    inside_html: Required[Annotated[str, PropertyInfo(alias="insideHTML")]]
    """The HTML content for the inside of the snap pack.

    You can supply _either_ this or `insideTemplate` but not both.
    """

    outside_html: Required[Annotated[str, PropertyInfo(alias="outsideHTML")]]
    """The HTML content for the outside of the snap pack.

    You can supply _either_ this or `outsideTemplate` but not both.
    """

    size: Required[Literal["8.5x11_bifold_v"]]
    """Enum representing the supported snap pack sizes."""

    to: Required[SnapPackCreateWithHTMLTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
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

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


SnapPackCreateWithHTMLFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

SnapPackCreateWithHTMLTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class SnapPackCreateWithTemplate(TypedDict, total=False):
    from_: Required[Annotated[SnapPackCreateWithTemplateFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`
    contact.
    """

    inside_template: Required[Annotated[str, PropertyInfo(alias="insideTemplate")]]
    """The template ID for the inside of the snap pack.

    You can supply _either_ this or `insideHTML` but not both.
    """

    outside_template: Required[Annotated[str, PropertyInfo(alias="outsideTemplate")]]
    """The template ID for the outside of the snap pack.

    You can supply _either_ this or `outsideHTML` but not both.
    """

    size: Required[Literal["8.5x11_bifold_v"]]
    """Enum representing the supported snap pack sizes."""

    to: Required[SnapPackCreateWithTemplateTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
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

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


SnapPackCreateWithTemplateFrom: TypeAlias = Union[
    ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str
]

SnapPackCreateWithTemplateTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class SnapPackCreateWithPdf(TypedDict, total=False):
    from_: Required[Annotated[SnapPackCreateWithPdfFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`
    contact.
    """

    pdf: Required[Union[str, FileTypes]]
    """
    A URL or a multipart-uploaded two-page PDF (first page is the outside, second
    page is the inside) that matches the selected snap pack size.
    """

    size: Required[Literal["8.5x11_bifold_v"]]
    """Enum representing the supported snap pack sizes."""

    to: Required[SnapPackCreateWithPdfTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
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

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


SnapPackCreateWithPdfFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

SnapPackCreateWithPdfTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

SnapPackCreateParams: TypeAlias = Union[SnapPackCreateWithHTML, SnapPackCreateWithTemplate, SnapPackCreateWithPdf]
