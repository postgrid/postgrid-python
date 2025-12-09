# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["ReportSample"]


class ReportSample(BaseModel):
    """Represents the result of a report sample query."""

    id: str
    """Unique identifier for the sample query result."""

    records: List[Dict[str, object]]
    """The actual data records returned by the sample query."""

    report: Optional[str] = None
    """
    The ID of the report this sample was generated from, or null for ad-hoc samples.
    """
