# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubOrganization"]


class SubOrganization(BaseModel):
    """The Sub-Organization object."""

    id: str
    """A unique ID prefixed with `sub_org_`."""

    country_code: str = FieldInfo(alias="countryCode")
    """The country code of the sub-organization."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    limit: int
    """
    The limit of mailings the sub-organization can send before being charged
    overages for the month.
    """

    name: str
    """The name of the sub-organization."""

    object: Literal["sub_org"]
    """Always `sub_org`."""

    spend: int
    """The current rolling charge for the sub-organization for the month, in cents."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last update."""

    usage: int
    """The amount of mail the sub-organization has sent out this month."""
