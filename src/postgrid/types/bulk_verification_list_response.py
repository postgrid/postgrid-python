# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .addver_list import AddverList

__all__ = ["BulkVerificationListResponse", "Data"]


class Data(BaseModel):
    """A list of bulk verification lists."""

    count: int
    """The total number of lists."""

    data: List[AddverList]
    """The requested lists."""


class BulkVerificationListResponse(BaseModel):
    data: Data
    """A list of bulk verification lists."""

    message: str

    status: Literal["success", "error"]
