# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VirtualMailboxRetrieveAddressResponse"]


class VirtualMailboxRetrieveAddressResponse(BaseModel):
    """The address information for a mailbox."""

    address_line1: str = FieldInfo(alias="addressLine1")
    """The address line 1 of the mailbox."""

    country_code: Literal["US"] = FieldInfo(alias="countryCode")
    """All of the supported countries for virtual mailboxes."""

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)
    """The address line 2 of the mailbox."""

    city: Optional[str] = None
    """The city of the mailbox."""

    postal_or_zip: Optional[str] = FieldInfo(alias="postalOrZip", default=None)
    """The postal or ZIP code of the mailbox."""

    province_or_state: Optional[str] = FieldInfo(alias="provinceOrState", default=None)
    """The province or state of the mailbox."""
