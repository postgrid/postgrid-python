# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = [
    "PostcardCreateParams",
    "PostcardCreateWithHTML",
    "PostcardCreateWithHTMLTo",
    "PostcardCreateWithHTMLToContactCreateWithFirstName",
    "PostcardCreateWithHTMLToContactCreateWithCompanyName",
    "PostcardCreateWithHTMLFrom",
    "PostcardCreateWithHTMLFromContactCreateWithFirstName",
    "PostcardCreateWithHTMLFromContactCreateWithCompanyName",
    "PostcardCreateWithTemplate",
    "PostcardCreateWithPdfurl",
    "PostcardCreateWithPdfurlTo",
    "PostcardCreateWithPdfurlToContactCreateWithFirstName",
    "PostcardCreateWithPdfurlToContactCreateWithCompanyName",
    "PostcardCreateWithPdfurlFrom",
    "PostcardCreateWithPdfurlFromContactCreateWithFirstName",
    "PostcardCreateWithPdfurlFromContactCreateWithCompanyName",
    "PostcardCreateWithPdfFile",
    "PostcardCreateWithPdfFileTo",
    "PostcardCreateWithPdfFileToContactCreateWithFirstName",
    "PostcardCreateWithPdfFileToContactCreateWithCompanyName",
    "PostcardCreateWithPdfFileFrom",
    "PostcardCreateWithPdfFileFromContactCreateWithFirstName",
    "PostcardCreateWithPdfFileFromContactCreateWithCompanyName",
]


class PostcardCreateWithHTML(TypedDict, total=False):
    back_html: Required[Annotated[str, PropertyInfo(alias="backHTML")]]
    """The HTML content for the back of the postcard.

    You can supply _either_ this or `backTemplate` but not both.
    """

    front_html: Required[Annotated[str, PropertyInfo(alias="frontHTML")]]
    """The HTML content for the front of the postcard.

    You can supply _either_ this or `frontTemplate` but not both.
    """

    size: Required[Literal["6x4", "9x6", "11x6"]]
    """Enum representing the supported postcard sizes."""

    to: Required[PostcardCreateWithHTMLTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    from_: Annotated[PostcardCreateWithHTMLFrom, PropertyInfo(alias="from")]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    Unlike other order types, the sender address is optional for postcards.
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


class PostcardCreateWithHTMLToContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithHTMLToContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithHTMLTo: TypeAlias = Union[
    PostcardCreateWithHTMLToContactCreateWithFirstName, PostcardCreateWithHTMLToContactCreateWithCompanyName, str
]


class PostcardCreateWithHTMLFromContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithHTMLFromContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithHTMLFrom: TypeAlias = Union[
    PostcardCreateWithHTMLFromContactCreateWithFirstName, PostcardCreateWithHTMLFromContactCreateWithCompanyName, str
]


class PostcardCreateWithTemplate(TypedDict, total=False):
    back_template: Required[Annotated[str, PropertyInfo(alias="backTemplate")]]
    """The template ID for the back of the postcard.

    You can supply _either_ this or `backHTML` but not both.
    """

    front_template: Required[Annotated[str, PropertyInfo(alias="frontTemplate")]]
    """The template ID for the front of the postcard.

    You can supply _either_ this or `frontHTML` but not both.
    """


class PostcardCreateWithPdfurl(TypedDict, total=False):
    pdf: Required[str]
    """A URL pointing to a 2 page PDF file.

    The first page is the front of the postcard and the second page is the back
    (where the address will be stamped on).
    """

    size: Required[Literal["6x4", "9x6", "11x6"]]
    """Enum representing the supported postcard sizes."""

    to: Required[PostcardCreateWithPdfurlTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    from_: Annotated[PostcardCreateWithPdfurlFrom, PropertyInfo(alias="from")]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    Unlike other order types, the sender address is optional for postcards.
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


class PostcardCreateWithPdfurlToContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithPdfurlToContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithPdfurlTo: TypeAlias = Union[
    PostcardCreateWithPdfurlToContactCreateWithFirstName, PostcardCreateWithPdfurlToContactCreateWithCompanyName, str
]


class PostcardCreateWithPdfurlFromContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithPdfurlFromContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithPdfurlFrom: TypeAlias = Union[
    PostcardCreateWithPdfurlFromContactCreateWithFirstName,
    PostcardCreateWithPdfurlFromContactCreateWithCompanyName,
    str,
]


class PostcardCreateWithPdfFile(TypedDict, total=False):
    pdf: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """A 2 page PDF file.

    The first page is the front of the postcard and the second page is the back
    (where the address will be stamped on).
    """

    size: Required[Literal["6x4", "9x6", "11x6"]]
    """Enum representing the supported postcard sizes."""

    to: Required[PostcardCreateWithPdfFileTo]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    from_: Annotated[PostcardCreateWithPdfFileFrom, PropertyInfo(alias="from")]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    Unlike other order types, the sender address is optional for postcards.
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


class PostcardCreateWithPdfFileToContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithPdfFileToContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithPdfFileTo: TypeAlias = Union[
    PostcardCreateWithPdfFileToContactCreateWithFirstName, PostcardCreateWithPdfFileToContactCreateWithCompanyName, str
]


class PostcardCreateWithPdfFileFromContactCreateWithFirstName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Company name of the contact."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


class PostcardCreateWithPdfFileFromContactCreateWithCompanyName(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """


PostcardCreateWithPdfFileFrom: TypeAlias = Union[
    PostcardCreateWithPdfFileFromContactCreateWithFirstName,
    PostcardCreateWithPdfFileFromContactCreateWithCompanyName,
    str,
]

PostcardCreateParams: TypeAlias = Union[
    PostcardCreateWithHTML, PostcardCreateWithTemplate, PostcardCreateWithPdfurl, PostcardCreateWithPdfFile
]
