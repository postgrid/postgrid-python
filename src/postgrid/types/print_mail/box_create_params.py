# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .order_mailing_class import OrderMailingClass
from .box_cheque_base_param import BoxChequeBaseParam
from ..contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from ..contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

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

    mailing_class: Annotated[OrderMailingClass, PropertyInfo(alias="mailingClass")]
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


class Cheque(BoxChequeBaseParam):
    to: Required[ChequeTo]


From: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]

To: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]
