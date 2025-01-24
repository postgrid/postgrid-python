# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LetterCreateParams",
    "LetterCreateWithHTML",
    "LetterCreateWithHTMLFrom",
    "LetterCreateWithHTMLFromContactCreateWithFirstName",
    "LetterCreateWithHTMLFromContactCreateWithCompanyName",
    "LetterCreateWithHTMLTo",
    "LetterCreateWithHTMLToContactCreateWithFirstName",
    "LetterCreateWithHTMLToContactCreateWithCompanyName",
    "LetterCreateWithHTMLAttachedPdf",
    "LetterCreateWithHTMLPlasticCard",
    "LetterCreateWithHTMLPlasticCardDoubleSided",
    "LetterCreateWithHTMLPlasticCardSingleSided",
    "LetterCreateWithTemplate",
    "LetterCreateWithPdf",
    "LetterCreateWithPdfFrom",
    "LetterCreateWithPdfFromContactCreateWithFirstName",
    "LetterCreateWithPdfFromContactCreateWithCompanyName",
    "LetterCreateWithPdfTo",
    "LetterCreateWithPdfToContactCreateWithFirstName",
    "LetterCreateWithPdfToContactCreateWithCompanyName",
    "LetterCreateWithPdfAttachedPdf",
    "LetterCreateWithPdfPlasticCard",
    "LetterCreateWithPdfPlasticCardDoubleSided",
    "LetterCreateWithPdfPlasticCardSingleSided",
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

    address_placement: Annotated[Literal["top_first_page", "insert_blank_page"], PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[LetterCreateWithHTMLAttachedPdf, PropertyInfo(alias="attachedPDF")]
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

    plastic_card: Annotated[LetterCreateWithHTMLPlasticCard, PropertyInfo(alias="plasticCard")]
    """Model representing a plastic card."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """The return envelope (ID) sent out with the letter, if any."""

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    size: Literal["us_letter", "a4"]
    """Enum representing the supported letter sizes."""


class LetterCreateWithHTMLFromContactCreateWithFirstName(TypedDict, total=False):
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


class LetterCreateWithHTMLFromContactCreateWithCompanyName(TypedDict, total=False):
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


LetterCreateWithHTMLFrom: TypeAlias = Union[
    LetterCreateWithHTMLFromContactCreateWithFirstName, LetterCreateWithHTMLFromContactCreateWithCompanyName, str
]


class LetterCreateWithHTMLToContactCreateWithFirstName(TypedDict, total=False):
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


class LetterCreateWithHTMLToContactCreateWithCompanyName(TypedDict, total=False):
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


LetterCreateWithHTMLTo: TypeAlias = Union[
    LetterCreateWithHTMLToContactCreateWithFirstName, LetterCreateWithHTMLToContactCreateWithCompanyName, str
]


class LetterCreateWithHTMLAttachedPdf(TypedDict, total=False):
    file: Required[str]
    """The file (multipart form upload) or URL pointing to a PDF for the attached PDF."""

    placement: Required[Literal["before_template", "after_template"]]
    """Enum representing the placement of the attached PDF."""


class LetterCreateWithHTMLPlasticCardDoubleSided(TypedDict, total=False):
    back_html: Annotated[str, PropertyInfo(alias="backHTML")]
    """The HTML content for the back side of the double-sided plastic card."""

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """The template ID for the back side of the double-sided plastic card."""

    front_html: Annotated[str, PropertyInfo(alias="frontHTML")]
    """The HTML content for the front side of the double-sided plastic card."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """The template ID for the front side of the double-sided plastic card."""

    pdf: str
    """
    A URL pointing to a PDF file for the double-sided plastic card or the file
    itself.
    """


class LetterCreateWithHTMLPlasticCardSingleSided(TypedDict, total=False):
    html: str
    """The HTML content for the single-sided plastic card.

    Can specify one of this, `template`, or `pdf`.
    """

    pdf: str
    """
    A URL pointing to a PDF file for the single-sided plastic card or the PDF file
    itself.
    """

    template: str
    """The template ID for the single-sided plastic card."""


class LetterCreateWithHTMLPlasticCard(TypedDict, total=False):
    size: Required[Literal["standard"]]
    """Enum representing the size of the plastic card."""

    double_sided: Annotated[LetterCreateWithHTMLPlasticCardDoubleSided, PropertyInfo(alias="doubleSided")]
    """Model representing a double-sided plastic card."""

    single_sided: Annotated[LetterCreateWithHTMLPlasticCardSingleSided, PropertyInfo(alias="singleSided")]
    """Model representing a single-sided plastic card."""


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

    address_placement: Annotated[Literal["top_first_page", "insert_blank_page"], PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[LetterCreateWithPdfAttachedPdf, PropertyInfo(alias="attachedPDF")]
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

    plastic_card: Annotated[LetterCreateWithPdfPlasticCard, PropertyInfo(alias="plasticCard")]
    """Model representing a plastic card."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """The return envelope (ID) sent out with the letter, if any."""

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    size: Literal["us_letter", "a4"]
    """Enum representing the supported letter sizes."""


class LetterCreateWithPdfFromContactCreateWithFirstName(TypedDict, total=False):
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


class LetterCreateWithPdfFromContactCreateWithCompanyName(TypedDict, total=False):
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


LetterCreateWithPdfFrom: TypeAlias = Union[
    LetterCreateWithPdfFromContactCreateWithFirstName, LetterCreateWithPdfFromContactCreateWithCompanyName, str
]


class LetterCreateWithPdfToContactCreateWithFirstName(TypedDict, total=False):
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


class LetterCreateWithPdfToContactCreateWithCompanyName(TypedDict, total=False):
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


LetterCreateWithPdfTo: TypeAlias = Union[
    LetterCreateWithPdfToContactCreateWithFirstName, LetterCreateWithPdfToContactCreateWithCompanyName, str
]


class LetterCreateWithPdfAttachedPdf(TypedDict, total=False):
    file: Required[str]
    """The file (multipart form upload) or URL pointing to a PDF for the attached PDF."""

    placement: Required[Literal["before_template", "after_template"]]
    """Enum representing the placement of the attached PDF."""


class LetterCreateWithPdfPlasticCardDoubleSided(TypedDict, total=False):
    back_html: Annotated[str, PropertyInfo(alias="backHTML")]
    """The HTML content for the back side of the double-sided plastic card."""

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """The template ID for the back side of the double-sided plastic card."""

    front_html: Annotated[str, PropertyInfo(alias="frontHTML")]
    """The HTML content for the front side of the double-sided plastic card."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """The template ID for the front side of the double-sided plastic card."""

    pdf: str
    """
    A URL pointing to a PDF file for the double-sided plastic card or the file
    itself.
    """


class LetterCreateWithPdfPlasticCardSingleSided(TypedDict, total=False):
    html: str
    """The HTML content for the single-sided plastic card.

    Can specify one of this, `template`, or `pdf`.
    """

    pdf: str
    """
    A URL pointing to a PDF file for the single-sided plastic card or the PDF file
    itself.
    """

    template: str
    """The template ID for the single-sided plastic card."""


class LetterCreateWithPdfPlasticCard(TypedDict, total=False):
    size: Required[Literal["standard"]]
    """Enum representing the size of the plastic card."""

    double_sided: Annotated[LetterCreateWithPdfPlasticCardDoubleSided, PropertyInfo(alias="doubleSided")]
    """Model representing a double-sided plastic card."""

    single_sided: Annotated[LetterCreateWithPdfPlasticCardSingleSided, PropertyInfo(alias="singleSided")]
    """Model representing a single-sided plastic card."""


LetterCreateParams: TypeAlias = Union[LetterCreateWithHTML, LetterCreateWithTemplate, LetterCreateWithPdf]
