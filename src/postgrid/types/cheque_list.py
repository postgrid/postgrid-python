# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .cheque import Cheque
from .._models import BaseModel

__all__ = ["ChequeList"]


class ChequeList(BaseModel):
    data: List[Cheque]

    limit: int

    object: Literal["list"]

    skip: int

    total_count: int = FieldInfo(alias="totalCount")
