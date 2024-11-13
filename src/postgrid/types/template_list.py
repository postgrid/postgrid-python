# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template import Template

__all__ = ["TemplateList"]


class TemplateList(BaseModel):
    data: List[Template]

    limit: int

    object: Literal["list"]

    skip: int

    total_count: int = FieldInfo(alias="totalCount")
