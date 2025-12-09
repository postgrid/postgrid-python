# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["MailingListUpdate"]


class MailingListUpdate(BaseModel):
    """Parameters for updating an existing mailing list."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""
