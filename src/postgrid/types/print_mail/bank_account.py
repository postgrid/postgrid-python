# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .bank_account_country_code import BankAccountCountryCode

__all__ = ["BankAccount"]


class BankAccount(BaseModel):
    id: str
    """A unique ID prefixed with bank*account*"""

    account_number: str = FieldInfo(alias="accountNumber")
    """The account number of the bank account."""

    bank_country_code: BankAccountCountryCode = FieldInfo(alias="bankCountryCode")
    """Countries typically have different bank account formats and standards.

    These are the countries which PostGrid's bank accounts API supports.
    """

    bank_name: str = FieldInfo(alias="bankName")
    """The name of the bank."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["bank_account"]
    """Always `bank_account`."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    bank_primary_line: Optional[str] = FieldInfo(alias="bankPrimaryLine", default=None)
    """The primary address line of the bank."""

    bank_secondary_line: Optional[str] = FieldInfo(alias="bankSecondaryLine", default=None)
    """The secondary address line of the bank."""

    ca_designation_number: Optional[str] = FieldInfo(alias="caDesignationNumber", default=None)
    """The designation number of the bank account (for CA)."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""

    route_number: Optional[str] = FieldInfo(alias="routeNumber", default=None)
    """The route number of the bank account (for CA)."""

    routing_number: Optional[str] = FieldInfo(alias="routingNumber", default=None)
    """The routing number of the bank account (for US)."""

    signature_image: Optional[str] = FieldInfo(alias="signatureImage", default=None)
    """A signed link to the signature image uploaded when this bank account was
    created.

    This is omitted if `signatureText` is present.
    """

    signature_text: Optional[str] = FieldInfo(alias="signatureText", default=None)
    """
    The signature text PostGrid uses to generate a signature for cheques created
    using this bank account. This is omitted if `signatureImage` is present.
    """

    transit_number: Optional[str] = FieldInfo(alias="transitNumber", default=None)
    """The transit number of the bank account (for CA)."""
