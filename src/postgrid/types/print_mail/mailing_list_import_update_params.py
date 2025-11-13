# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["MailingListImportUpdateParams"]


class MailingListImportUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """An optional description for the import.

    Set to `null` to remove the existing description.
    """

    metadata: Optional[Dict[str, str]]
    """Optional key-value data associated with the import.

    Set to `null` to remove existing metadata.
    """
