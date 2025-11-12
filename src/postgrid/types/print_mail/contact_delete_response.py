# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContactDeleteResponse"]


class ContactDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with contact\\__"""

    deleted: Literal[True]

    object: Literal["contact"]
    """Always `contact`."""
