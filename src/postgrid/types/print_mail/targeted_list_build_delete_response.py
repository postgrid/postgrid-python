# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TargetedListBuildDeleteResponse"]


class TargetedListBuildDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with targeted*list_build*"""

    deleted: Literal[True]
