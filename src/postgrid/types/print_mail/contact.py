# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
    id: str
    """A unique ID prefixed with contact\\__"""

    address_line1: str = FieldInfo(alias="addressLine1")
    """The first line of the contact's address."""

    address_status: Literal["verified", "corrected", "failed"] = FieldInfo(alias="addressStatus")
    """One of `verified`, `corrected`, or `failed`."""

    country_code: str = FieldInfo(alias="countryCode")
    """The ISO 3611-1 country code of the contact's address."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    object: Literal["contact"]
    """Always `contact`."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    address_errors: Optional[str] = FieldInfo(alias="addressErrors", default=None)
    """
    A series of human-readable errors/warnings that were raised when running the
    provided address through our address verification.
    """

    address_line2: Optional[str] = FieldInfo(alias="addressLine2", default=None)
    """Second line of the contact's address, if applicable."""

    city: Optional[str] = None
    """The city of the contact's address."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """Company name of the contact."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: Optional[str] = None
    """Email of the contact."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """First name of the contact."""

    force_verified_status: Optional[bool] = FieldInfo(alias="forceVerifiedStatus", default=None)
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Optional[str] = FieldInfo(alias="jobTitle", default=None)
    """Job title of the contact."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Last name of the contact."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """See the section on Metadata."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Phone number of the contact."""

    postal_or_zip: Optional[str] = FieldInfo(alias="postalOrZip", default=None)
    """The postal or ZIP code of the contact's address."""

    province_or_state: Optional[str] = FieldInfo(alias="provinceOrState", default=None)
    """Province or state of the contact's address."""

    skip_verification: Optional[bool] = FieldInfo(alias="skipVerification", default=None)
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """
