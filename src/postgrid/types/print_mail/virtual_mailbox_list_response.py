# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .contact import Contact
from ..._models import BaseModel

__all__ = ["VirtualMailboxListResponse", "Capabilities"]


class Capabilities(BaseModel):
    """All of the capabilities a virtual mailbox may have."""

    envelope_scans: bool = FieldInfo(alias="envelopeScans")
    """Indicates if the virtual mailbox can produce scans of envelopes."""

    forward_mail_to: Optional[Contact] = FieldInfo(alias="forwardMailTo", default=None)
    """A contact to forward any returned mail to."""


class VirtualMailboxListResponse(BaseModel):
    """The virtual mailbox object."""

    id: str
    """A unique ID prefixed with virtual*mailbox*"""

    capabilities: Capabilities
    """All of the capabilities a virtual mailbox may have."""

    country_code: Literal["US"] = FieldInfo(alias="countryCode")
    """All of the supported countries for virtual mailboxes."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["virtual_mailbox"]
    """Always "virtual_mailbox"."""

    status: Literal["active", "pending_assignment"]
    """The possible statuses of virtual mailboxes."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""
