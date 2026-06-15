# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .addver_list import AddverList

__all__ = ["BulkVerificationUploadResponse"]


class BulkVerificationUploadResponse(BaseModel):
    data: AddverList
    """
    A bulk address verification list — an uploaded CSV file of addresses and its
    processing state.
    """

    message: str

    status: Literal["success", "error"]
