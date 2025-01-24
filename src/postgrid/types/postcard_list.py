# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .postcard import Postcard

__all__ = ["PostcardList"]


class PostcardList(BaseModel):
    data: List[Postcard]

    limit: int

    object: Literal["list"]

    skip: int

    total_count: int = FieldInfo(alias="totalCount")
