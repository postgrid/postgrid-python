# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from .contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = ["VirtualMailboxCreateParams", "Capabilities", "CapabilitiesForwardMailTo"]


class VirtualMailboxCreateParams(TypedDict, total=False):
    country_code: Required[Annotated[Literal["US"], PropertyInfo(alias="countryCode")]]
    """All of the supported countries for virtual mailboxes."""

    capabilities: Capabilities
    """The capabilities the virtual mailbox should support."""


CapabilitiesForwardMailTo: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]


class Capabilities(TypedDict, total=False):
    """The capabilities the virtual mailbox should support."""

    envelope_scans: Required[Annotated[bool, PropertyInfo(alias="envelopeScans")]]
    """If the virtual mailbox should support envelope scans or not."""

    forward_mail_to: Annotated[CapabilitiesForwardMailTo, PropertyInfo(alias="forwardMailTo")]
    """A contact ID or contact object."""
