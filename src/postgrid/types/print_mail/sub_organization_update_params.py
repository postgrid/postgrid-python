# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubOrganizationUpdateParams"]


class SubOrganizationUpdateParams(TypedDict, total=False):
    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]
    """The country code of the sub-organization."""

    email: Required[str]
    """The email of the user to be created alongside the sub-organization."""

    name: Required[str]
    """The name of the user to be created alongside the sub-organization."""

    organization_name: Required[Annotated[str, PropertyInfo(alias="organizationName")]]
    """The name of the sub-organization."""

    password: Required[str]
    """The password of the user to be created alongside the sub-organization."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """The phone number of the user to be created alongside the sub-organization."""
