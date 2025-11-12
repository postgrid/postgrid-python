# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BoxChequeBaseParam"]


class BoxChequeBaseParam(TypedDict, total=False):
    amount: Required[int]
    """The amount on the cheque."""

    bank_account: Required[Annotated[str, PropertyInfo(alias="bankAccount")]]
    """The bank account (ID or reference) from which the cheque amount is drawn."""

    number: Required[int]
    """The cheque number."""

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
