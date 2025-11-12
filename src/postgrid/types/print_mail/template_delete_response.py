# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateDeleteResponse"]


class TemplateDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with template\\__"""

    deleted: Literal[True]

    object: Literal["template"]
    """Always `template`."""
