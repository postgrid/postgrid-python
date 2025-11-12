# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactCreateWithCompanyNameParam"]


class ContactCreateWithCompanyNameParam(TypedDict, total=False):
    address_line1: Required[Annotated[str, PropertyInfo(alias="addressLine1")]]
    """The first line of the contact's address."""

    company_name: Required[Annotated[str, PropertyInfo(alias="companyName")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The ISO 3611-1 country code of the contact's address."""

    address_line2: Annotated[str, PropertyInfo(alias="addressLine2")]
    """Second line of the contact's address, if applicable."""

    city: str
    """The city of the contact's address."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    email: str
    """Email of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    force_verified_status: Annotated[bool, PropertyInfo(alias="forceVerifiedStatus")]
    """
    If `true`, PostGrid will force this contact to have an `addressStatus` of
    `verified` even if our address verification system says otherwise.
    """

    job_title: Annotated[str, PropertyInfo(alias="jobTitle")]
    """Job title of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number of the contact."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The postal or ZIP code of the contact's address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """Province or state of the contact's address."""

    skip_verification: Annotated[bool, PropertyInfo(alias="skipVerification")]
    """
    If `true`, PostGrid will skip running this contact's address through our address
    verification system.
    """
