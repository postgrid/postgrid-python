# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    html: str
    """The HTML content of this template."""

    metadata: Dict[str, object]
    """See the section on Metadata."""
