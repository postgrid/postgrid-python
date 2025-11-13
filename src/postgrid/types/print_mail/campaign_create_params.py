# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CampaignCreateParams"]


class CampaignCreateParams(TypedDict, total=False):
    mailing_list: Required[Annotated[str, PropertyInfo(alias="mailingList")]]
    """The ID of the mailing list associated with this campaign."""

    cheque_profile: Annotated[str, PropertyInfo(alias="chequeProfile")]
    """The ID of the cheque profile used for this campaign, if applicable."""

    default_sender_contact: Annotated[str, PropertyInfo(alias="defaultSenderContact")]
    """
    The ID of the default sender contact to use for orders if not specified per
    recipient.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    letter_profile: Annotated[str, PropertyInfo(alias="letterProfile")]
    """The ID of the letter profile used for this campaign, if applicable."""

    metadata: Dict[str, object]
    """See the section on Metadata."""

    postcard_profile: Annotated[str, PropertyInfo(alias="postcardProfile")]
    """The ID of the postcard profile used for this campaign, if applicable."""

    self_mailer_profile: Annotated[str, PropertyInfo(alias="selfMailerProfile")]
    """The ID of the self-mailer profile used for this campaign, if applicable."""

    send_date: Annotated[Union[str, datetime], PropertyInfo(alias="sendDate", format="iso8601")]
    """The scheduled date and time for the campaign to be sent."""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]
