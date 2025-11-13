# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    cheque_profile: Annotated[Optional[str], PropertyInfo(alias="chequeProfile")]
    """The ID of the cheque profile to use.

    Setting this will remove other profile types. Set to `null` to remove.
    """

    default_sender_contact: Annotated[Optional[str], PropertyInfo(alias="defaultSenderContact")]
    """The ID of the default sender contact. Set to `null` to remove."""

    description: Optional[str]
    """An optional description for the campaign.

    Set to `null` to remove the existing description.
    """

    letter_profile: Annotated[Optional[str], PropertyInfo(alias="letterProfile")]
    """The ID of the letter profile to use.

    Setting this will remove other profile types. Set to `null` to remove.
    """

    mailing_list: Annotated[str, PropertyInfo(alias="mailingList")]
    """The ID of the mailing list to associate with this campaign."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value data associated with the campaign.

    Set to `null` to remove existing metadata.
    """

    postcard_profile: Annotated[Optional[str], PropertyInfo(alias="postcardProfile")]
    """The ID of the postcard profile to use.

    Setting this will remove other profile types. Set to `null` to remove.
    """

    self_mailer_profile: Annotated[Optional[str], PropertyInfo(alias="selfMailerProfile")]
    """The ID of the self-mailer profile to use.

    Setting this will remove other profile types. Set to `null` to remove.
    """
