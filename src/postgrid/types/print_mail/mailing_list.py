# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailingList", "Error"]


class Error(BaseModel):
    """Details of a specific error encountered during processing."""

    message: str
    """A human-readable message describing the error."""

    type: Literal[
        "mailing_list_imports_not_found_error", "download_file_error", "operational_error", "internal_service_error"
    ]
    """Type of error encountered during mailing list processing."""


class MailingList(BaseModel):
    """Represents a mailing list."""

    id: str
    """A unique ID prefixed with mailing*list*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    status: Literal["creating_contacts", "removing_contacts", "counting_recipient_country_codes", "completed"]
    """Status of the mailing list processing."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    errors: Optional[List[Error]] = None
    """A list of processing errors encountered, if any."""

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""
