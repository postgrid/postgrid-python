# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressVerificationLookupZipCodeFromCityOrStateResponse", "Data"]


class Data(BaseModel):
    zip_codes: List[str] = FieldInfo(alias="zipCodes")


class AddressVerificationLookupZipCodeFromCityOrStateResponse(BaseModel):
    data: Data

    message: str

    status: Literal["success", "error"]
