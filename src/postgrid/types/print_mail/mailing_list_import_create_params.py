# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .file_type import FileType

__all__ = ["MailingListImportCreateParams"]


class MailingListImportCreateParams(TypedDict, total=False):
    file: Required[str]
    """The CSV file for this import."""

    file_type: Required[Annotated[FileType, PropertyInfo(alias="fileType")]]
    """Type of file supported for mailing list imports."""

    receiver_address_mapping: Required[Annotated[Dict[str, str], PropertyInfo(alias="receiverAddressMapping")]]
    """Mapping of columns for receiver addresses."""

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    receiver_merge_variable_mapping: Annotated[Dict[str, str], PropertyInfo(alias="receiverMergeVariableMapping")]
    """Optional mapping of columns for receiver merge variables."""

    sender_address_mapping: Annotated[Dict[str, str], PropertyInfo(alias="senderAddressMapping")]
    """
    Optional mapping of columns for sender addresses. If this is present, then all
    receivers should have a corresponding sender.
    """

    sender_merge_variable_mapping: Annotated[Dict[str, str], PropertyInfo(alias="senderMergeVariableMapping")]
    """Optional mapping of columns for sender merge variables."""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]
