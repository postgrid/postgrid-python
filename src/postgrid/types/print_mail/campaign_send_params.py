# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CampaignSendParams"]


class CampaignSendParams(TypedDict, total=False):
    send_date: Annotated[Union[Union[str, datetime], str], PropertyInfo(alias="sendDate", format="iso8601")]
    """The date and time the campaign should be sent.

    Must be in the future. If omitted, defaults to the earliest possible processing
    date.
    """
