# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bank_account import BankAccount

__all__ = ["BankAccountList"]


class BankAccountList(BaseModel):
    data: List[BankAccount]

    limit: int

    object: Literal["list"]

    skip: int

    total_count: int = FieldInfo(alias="totalCount")
