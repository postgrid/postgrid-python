# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_preferences import EmailPreferences

__all__ = ["SubOrganizationRetrieveUsersResponse", "SubOrganizationRetrieveUsersResponseItem"]


class SubOrganizationRetrieveUsersResponseItem(BaseModel):
    """The user object."""

    id: str
    """A unique ID prefixed with `user_`."""

    email: str
    """The email of the user."""

    name: str
    """The name of the user."""

    organization: str
    """A unique ID prefixed with `user_`."""

    pending_invite: bool = FieldInfo(alias="pendingInvite")
    """Indicates if the user has a pending invite."""

    roles: List[str]
    """The roles given to the user. Roles can be used to restrict access for users."""

    verified_email: bool = FieldInfo(alias="verifiedEmail")
    """Indicates if the user has a verified email or not."""

    email_preferences: Optional[EmailPreferences] = FieldInfo(alias="emailPreferences", default=None)
    """A set of preferences for how a user should receive emails."""

    last_login_time: Optional[datetime] = FieldInfo(alias="lastLoginTime", default=None)
    """The date and time at which the user last logged in."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The phone number of the user."""

    previous_emails: Optional[List[str]] = FieldInfo(alias="previousEmails", default=None)
    """A list of emails the user has previously had.

    If a user has changed their email before, this list will be populated with all
    of the emails they once had.
    """


SubOrganizationRetrieveUsersResponse: TypeAlias = List[SubOrganizationRetrieveUsersResponseItem]
