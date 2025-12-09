# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VerificationStatusCount"]


class VerificationStatusCount(BaseModel):
    """Count of contact verification statuses."""

    corrected_count: int = FieldInfo(alias="correctedCount")
    """Number of contacts that were corrected during verification."""

    failed_count: int = FieldInfo(alias="failedCount")
    """Number of contacts that failed verification."""

    verified_count: int = FieldInfo(alias="verifiedCount")
    """Number of contacts that were verified without changes."""
