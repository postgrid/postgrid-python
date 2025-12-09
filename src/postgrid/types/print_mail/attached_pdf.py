# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AttachedPdf"]


class AttachedPdf(BaseModel):
    """Model representing an attached PDF."""

    file: str
    """The file (multipart form upload) or URL pointing to a PDF for the attached PDF."""

    placement: Literal["before_template", "after_template"]
    """Enum representing the placement of the attached PDF."""
