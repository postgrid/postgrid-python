# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SelfMailerDeleteResponse"]


class SelfMailerDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    deleted: Literal[True]

    object: Literal["self_mailer_profile"]
    """Always `self_mailer_profile`."""
