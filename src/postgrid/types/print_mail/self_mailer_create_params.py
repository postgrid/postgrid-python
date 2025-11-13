# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from .order_profiles.self_mailer_size import SelfMailerSize
from ..contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from ..contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = [
    "SelfMailerCreateParams",
    "SelfMailerCreateWithHTML",
    "SelfMailerCreateWithHTMLFrom",
    "SelfMailerCreateWithHTMLTo",
    "SelfMailerCreateWithTemplate",
    "SelfMailerCreateWithPdfurl",
    "SelfMailerCreateWithPdfurlFrom",
    "SelfMailerCreateWithPdfurlTo",
    "SelfMailerCreateWithPdfFile",
    "SelfMailerCreateWithPdfFileFrom",
    "SelfMailerCreateWithPdfFileTo",
]


class SelfMailerCreateWithHTML(TypedDict, total=False):
    from_: Required[Annotated[SelfMailerCreateWithHTMLFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    inside_html: Required[Annotated[str, PropertyInfo(alias="insideHTML")]]
    """The HTML content for the inside of the self-mailer.

    You can supply _either_ this or `insideTemplate` but not both.
    """

    outside_html: Required[Annotated[str, PropertyInfo(alias="outsideHTML")]]
    """The HTML content for the outside of the self-mailer.

    You can supply _either_ this or `outsideTemplate` but not both.
    """

    size: Required[SelfMailerSize]
    """Enum representing the supported self-mailer sizes."""

    to: Required[SelfMailerCreateWithHTMLTo]
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


SelfMailerCreateWithHTMLFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

SelfMailerCreateWithHTMLTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class SelfMailerCreateWithTemplate(TypedDict, total=False):
    inside_template: Required[Annotated[str, PropertyInfo(alias="insideTemplate")]]
    """The template ID for the inside of the self-mailer.

    You can supply _either_ this or `insideHTML` but not both.
    """

    outside_template: Required[Annotated[str, PropertyInfo(alias="outsideTemplate")]]
    """The template ID for the outside of the self-mailer.

    You can supply _either_ this or `outsideHTML` but not both.
    """


class SelfMailerCreateWithPdfurl(TypedDict, total=False):
    from_: Required[Annotated[SelfMailerCreateWithPdfurlFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    pdf: Required[str]
    """A URL pointing to a 2 page PDF file.

    The first page is the inside of the self-mailer and the second page is the
    outside (where the address will be stamped on).
    """

    size: Required[SelfMailerSize]
    """Enum representing the supported self-mailer sizes."""

    to: Required[SelfMailerCreateWithPdfurlTo]
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


SelfMailerCreateWithPdfurlFrom: TypeAlias = Union[
    ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str
]

SelfMailerCreateWithPdfurlTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class SelfMailerCreateWithPdfFile(TypedDict, total=False):
    from_: Required[Annotated[SelfMailerCreateWithPdfFileFrom, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    pdf: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """A 2 page PDF file.

    The first page is the inside of the self-mailer and the second page is the
    outside (where the address will be stamped on).
    """

    size: Required[SelfMailerSize]
    """Enum representing the supported self-mailer sizes."""

    to: Required[SelfMailerCreateWithPdfFileTo]
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


SelfMailerCreateWithPdfFileFrom: TypeAlias = Union[
    ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str
]

SelfMailerCreateWithPdfFileTo: TypeAlias = Union[
    ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str
]

SelfMailerCreateParams: TypeAlias = Union[
    SelfMailerCreateWithHTML, SelfMailerCreateWithTemplate, SelfMailerCreateWithPdfurl, SelfMailerCreateWithPdfFile
]
