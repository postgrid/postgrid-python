# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DeletedResponse"]


class DeletedResponse(BaseModel):
    id: str
    """The ID of the deleted resource."""

    deleted: Literal[True]
    """Indicates the resource was successfully deleted."""
