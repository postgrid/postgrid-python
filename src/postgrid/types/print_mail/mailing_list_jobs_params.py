# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MailingListJobsParams"]


class MailingListJobsParams(TypedDict, total=False):
    add_contacts: Annotated[SequenceNotStr[str], PropertyInfo(alias="addContacts")]
    """List of contact IDs to add to the mailing list.

    Cannot be used with other operations.
    """

    add_mailing_list_imports: Annotated[SequenceNotStr[str], PropertyInfo(alias="addMailingListImports")]
    """List of mailing list import IDs to add to the mailing list.

    Cannot be used with other operations.
    """

    remove_contacts: Annotated[SequenceNotStr[str], PropertyInfo(alias="removeContacts")]
    """List of contact IDs to remove from the mailing list.

    Cannot be used with other operations.
    """

    remove_mailing_list_imports: Annotated[SequenceNotStr[str], PropertyInfo(alias="removeMailingListImports")]
    """List of mailing list import IDs to remove from the mailing list.

    Cannot be used with other operations.
    """
