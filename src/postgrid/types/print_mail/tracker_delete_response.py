# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TrackerDeleteResponse"]


class TrackerDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with tracker\\__"""

    deleted: Literal[True]

    object: Literal["tracker"]
    """Always `tracker`."""
