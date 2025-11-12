# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["LetterDeleteResponse"]


class LetterDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    deleted: Literal[True]

    object: Literal["letter_profile"]
    """Always `letter_profile`."""
