# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CampaignDeleteResponse"]


class CampaignDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with campaign\\__"""

    deleted: Literal[True]
