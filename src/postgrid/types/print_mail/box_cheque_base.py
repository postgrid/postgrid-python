# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BoxChequeBase"]


class BoxChequeBase(BaseModel):
    amount: int
    """The amount on the cheque."""

    bank_account: str = FieldInfo(alias="bankAccount")
    """The bank account (ID or reference) from which the cheque amount is drawn."""

    number: int
    """The cheque number."""

    logo_url: Optional[str] = FieldInfo(alias="logoURL", default=None)
    """A URL to a logo for the cheque (optional)."""

    memo: Optional[str] = None
    """The memo text on the cheque (optional)."""

    merge_variables: Optional[Dict[str, object]] = FieldInfo(alias="mergeVariables", default=None)
    """
    A set of dynamic merge variables for customizing the cheque or accompanying
    documents (optional).
    """

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)
    """An optional message template to be printed on or with the cheque."""
