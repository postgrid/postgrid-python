# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from .contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = ["BoxCreateParams", "Cheque", "ChequeFrom", "ChequeTo", "From", "To"]


class BoxCreateParams(TypedDict, total=False):
    cheques: Required[Iterable[Cheque]]
    """The cheques to be mailed in the box.

    Only 100 cheques can be included in a box at a time.
    """

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]
    """The 'from' (sender) of the entire box.

    Accepts inline ContactCreate or a contactID.
    """

    to: Required[To]
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


ChequeFrom: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

ChequeTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

_ChequeReservedKeywords = TypedDict(
    "_ChequeReservedKeywords",
    {
        "from": ChequeFrom,
    },
    total=False,
)


class Cheque(_ChequeReservedKeywords, total=False):
    amount: Required[int]
    """The amount on the cheque."""

    bank_account: Required[Annotated[str, PropertyInfo(alias="bankAccount")]]
    """The bank account (ID or reference) from which the cheque amount is drawn."""

    number: Required[int]
    """The cheque number."""

    to: Required[ChequeTo]

    logo_url: Annotated[str, PropertyInfo(alias="logoURL")]
    """A URL to a logo for the cheque (optional)."""

    memo: str
    """The memo text on the cheque (optional)."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """
    A set of dynamic merge variables for customizing the cheque or accompanying
    documents (optional).
    """

    message_template: Annotated[str, PropertyInfo(alias="messageTemplate")]
    """An optional message template to be printed on or with the cheque."""


From: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

To: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]
