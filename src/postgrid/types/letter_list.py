# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .letter import Letter
from .._models import BaseModel

__all__ = ["LetterList"]


class LetterList(BaseModel):
    data: List[Letter]

    limit: int

    object: Literal["list"]

    skip: int

    total_count: int = FieldInfo(alias="totalCount")
