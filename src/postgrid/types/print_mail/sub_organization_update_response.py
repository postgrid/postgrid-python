# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sub_organization import SubOrganization
from .email_preferences import EmailPreferences

__all__ = ["SubOrganizationUpdateResponse", "User", "UserAPIKey"]


class UserAPIKey(BaseModel):
    """An API key."""

    value: str
    """The value of the API key."""

    active_until: Optional[datetime] = FieldInfo(alias="activeUntil", default=None)
    """An optional date which the API key is active until.

    After this date, the API key will no longer be valid.
    """


class User(BaseModel):
    """The user object."""

    id: str
    """A unique ID prefixed with `user_`."""

    api_keys: List[UserAPIKey] = FieldInfo(alias="apiKeys")
    """The user's API keys. Contains live and test mode API keys."""

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


class SubOrganizationUpdateResponse(BaseModel):
    sub_organization: SubOrganization = FieldInfo(alias="subOrganization")
    """The Sub-Organization object."""

    user: User
    """The user object."""
