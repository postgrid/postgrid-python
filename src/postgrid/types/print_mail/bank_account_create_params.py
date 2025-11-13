# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from .bank_account_country_code import BankAccountCountryCode

__all__ = [
    "BankAccountCreateParams",
    "BankAccountCreateSignatureText",
    "BankAccountCreateSignatureImageURL",
    "BankAccountCreateSignatureImageFile",
]


class BankAccountCreateSignatureText(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]
    """The account number of the bank account."""

    bank_country_code: Required[Annotated[BankAccountCountryCode, PropertyInfo(alias="bankCountryCode")]]
    """Countries typically have different bank account formats and standards.

    These are the countries which PostGrid's bank accounts API supports.
    """

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]
    """The name of the bank."""

    signature_text: Required[Annotated[str, PropertyInfo(alias="signatureText")]]
    """The signature text of the bank account."""

    bank_primary_line: Annotated[str, PropertyInfo(alias="bankPrimaryLine")]
    """The primary address line of the bank."""

    bank_secondary_line: Annotated[str, PropertyInfo(alias="bankSecondaryLine")]
    """The secondary address line of the bank."""

    ca_designation_number: Annotated[str, PropertyInfo(alias="caDesignationNumber")]
    """The designation number of the bank account (for CA)."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    route_number: Annotated[str, PropertyInfo(alias="routeNumber")]
    """The route number of the bank account (for CA)."""

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank account (for US)."""

    transit_number: Annotated[str, PropertyInfo(alias="transitNumber")]
    """The transit number of the bank account (for CA)."""


class BankAccountCreateSignatureImageURL(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]
    """The account number of the bank account."""

    bank_country_code: Required[Annotated[BankAccountCountryCode, PropertyInfo(alias="bankCountryCode")]]
    """Countries typically have different bank account formats and standards.

    These are the countries which PostGrid's bank accounts API supports.
    """

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]
    """The name of the bank."""

    signature_image: Required[Annotated[str, PropertyInfo(alias="signatureImage")]]
    """
    Link to signature image which PostGrid will download and apply to cheques
    created with this bank account.
    """

    bank_primary_line: Annotated[str, PropertyInfo(alias="bankPrimaryLine")]
    """The primary address line of the bank."""

    bank_secondary_line: Annotated[str, PropertyInfo(alias="bankSecondaryLine")]
    """The secondary address line of the bank."""

    ca_designation_number: Annotated[str, PropertyInfo(alias="caDesignationNumber")]
    """The designation number of the bank account (for CA)."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    route_number: Annotated[str, PropertyInfo(alias="routeNumber")]
    """The route number of the bank account (for CA)."""

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank account (for US)."""

    transit_number: Annotated[str, PropertyInfo(alias="transitNumber")]
    """The transit number of the bank account (for CA)."""


class BankAccountCreateSignatureImageFile(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]
    """The account number of the bank account."""

    bank_country_code: Required[Annotated[BankAccountCountryCode, PropertyInfo(alias="bankCountryCode")]]
    """Countries typically have different bank account formats and standards.

    These are the countries which PostGrid's bank accounts API supports.
    """

    bank_name: Required[Annotated[str, PropertyInfo(alias="bankName")]]
    """The name of the bank."""

    signature_image: Required[
        Annotated[Union[str, Base64FileInput], PropertyInfo(alias="signatureImage", format="base64")]
    ]
    """
    A PNG or JPEG file which PostGrid will apply to checks created with this bank
    account.
    """

    bank_primary_line: Annotated[str, PropertyInfo(alias="bankPrimaryLine")]
    """The primary address line of the bank."""

    bank_secondary_line: Annotated[str, PropertyInfo(alias="bankSecondaryLine")]
    """The secondary address line of the bank."""

    ca_designation_number: Annotated[str, PropertyInfo(alias="caDesignationNumber")]
    """The designation number of the bank account (for CA)."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    route_number: Annotated[str, PropertyInfo(alias="routeNumber")]
    """The route number of the bank account (for CA)."""

    routing_number: Annotated[str, PropertyInfo(alias="routingNumber")]
    """The routing number of the bank account (for US)."""

    transit_number: Annotated[str, PropertyInfo(alias="transitNumber")]
    """The transit number of the bank account (for CA)."""


BankAccountCreateParams: TypeAlias = Union[
    BankAccountCreateSignatureText, BankAccountCreateSignatureImageURL, BankAccountCreateSignatureImageFile
]
