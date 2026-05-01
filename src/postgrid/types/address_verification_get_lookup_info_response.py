# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressVerificationGetLookupInfoResponse", "Data"]


class Data(BaseModel):
    free_limit: Optional[int] = FieldInfo(alias="freeLimit", default=None)
    """
    The maximum number of lookups allowed in the current billing period. `null`
    indicates an unlimited plan.
    """

    used: int
    """The number of lookups consumed in the current billing period."""


class AddressVerificationGetLookupInfoResponse(BaseModel):
    data: Data

    message: str

    status: Literal["success", "error"]
