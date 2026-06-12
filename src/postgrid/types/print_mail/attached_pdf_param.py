# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["AttachedPdfParam"]


class AttachedPdfParam(TypedDict, total=False):
    """Model representing an attached PDF."""

    file: Required[Union[str, FileTypes]]
    """The file (multipart form upload) or URL pointing to a PDF for the attached PDF."""

    placement: Required[Literal["before_template", "after_template"]]
    """Enum representing the placement of the attached PDF."""
