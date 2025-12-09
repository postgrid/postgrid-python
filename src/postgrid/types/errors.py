# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Errors"]


class Errors(BaseModel):
    """Errors encountered during address verification."""

    city: Optional[List[str]] = None
    """Errors related to the city."""

    generic: Optional[List[str]] = None
    """Generic errors not tied to a specific field."""

    line1: Optional[List[str]] = None
    """Errors related to the first address line."""

    line2: Optional[List[str]] = None
    """Errors related to the second address line."""

    province_or_state: Optional[List[str]] = FieldInfo(alias="provinceOrState", default=None)
    """Errors related to the province or state."""
