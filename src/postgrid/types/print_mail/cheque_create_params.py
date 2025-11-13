# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .cheque_size import ChequeSize
from .digital_only_param import DigitalOnlyParam
from ..contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from ..contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = ["ChequeCreateParams", "From", "To", "RedirectTo"]


class ChequeCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The amount of the cheque in cents."""

    bank_account: Required[Annotated[str, PropertyInfo(alias="bankAccount")]]
    """The bank account (ID) associated with the cheque."""

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]
    """The contact information of the sender.

    You can pass contact information inline here just like you can for the `to`.
    """

    to: Required[To]
    """The recipient of this order.

    You can either supply the contact information inline here or provide a contact
    ID. PostGrid will automatically deduplicate contacts regardless of whether you
    provide the information inline here or call the contact creation endpoint.
    """

    currency_code: Annotated[Literal["USD", "CAD"], PropertyInfo(alias="currencyCode")]
    """The currency code of the cheque.

    This will be set to the default currency of the bank account (`USD` for US bank
    accounts and `CAD` for Canadian bank accounts) if not provided. You can set this
    value to `USD` if you want to draw USD from a Canadian bank account or vice
    versa.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    digital_only: Annotated[DigitalOnlyParam, PropertyInfo(alias="digitalOnly")]
    """The digitalOnly object contains data for digital-only cheques.

    A watermark must be provided.
    """

    envelope: Union[Literal["standard"], str]
    """The envelope of the cheque.

    If a custom envelope ID is not specified, defaults to `standard`.
    """

    logo_url: Annotated[str, PropertyInfo(alias="logoURL")]
    """An optional logo URL for the cheque.

    This will be placed next to the recipient address at the top left corner of the
    cheque. This needs to be a public link to an image file (e.g. a PNG or JPEG
    file).
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

    memo: str
    """The memo of the cheque."""

    merge_variables: Annotated[Dict[str, object], PropertyInfo(alias="mergeVariables")]
    """
    These will be merged with the variables in the template or HTML you create this
    order with. The keys in this object should match the variable names in the
    template _exactly_ as they are case-sensitive. Note that these _do not_ apply to
    PDFs uploaded with the order.
    """

    message: str
    """The message of the cheque."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    number: int
    """The number of the cheque.

    If you don't provide this, it will automatically be set to an incrementing
    number starting from 1 across your entire account, ensuring that every cheque
    has a unique number.
    """

    redirect_to: Annotated[RedirectTo, PropertyInfo(alias="redirectTo")]
    """
    Providing this inserts a blank page at the start of the cheque with the
    recipient you provide here. This leaves the cheque that follows intact, which
    means you can use this to intercept at cheque at the redirected address and then
    mail it forward to the final recipient yourself. One use case for this is
    signing cheques at your office before mailing them out yourself.
    """

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """This order will transition from `ready` to `printing` on the day after this
    date.

    You can use this parameter to schedule orders for a future date.
    """

    size: ChequeSize
    """Enum representing the supported cheque sizes."""


From: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

To: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

RedirectTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]
