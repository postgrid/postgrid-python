# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .file_type import FileType
from .verification_status_count import VerificationStatusCount

__all__ = ["MailingListImportResponse", "Error", "File", "Note"]


class Error(BaseModel):
    """Details of a specific error encountered during import processing."""

    message: str
    """A human-readable message describing the error."""

    type: Literal[
        "no_valid_contacts_error", "multiple_countries_error", "invalid_contact_count_error", "internal_service_error"
    ]
    """Type of error encountered during import processing."""


class File(BaseModel):
    """The file object your controller returns: all the mappings plus a signed URL."""

    file_type: FileType = FieldInfo(alias="fileType")
    """Type of file supported for mailing list imports."""

    receiver_address_mapping: Dict[str, str] = FieldInfo(alias="receiverAddressMapping")
    """
    Mapping of columns for receiver addresses. Contact fields to file columns.
    Possible Contact fields:

    - description
    - firstName
    - lastName
    - email
    - phoneNumber
    - companyName
    - addressLine1
    - addressLine2
    - jobTitle
    - city
    - postalOrZip
    - provinceOrState
    - countryCode
    """

    url: str
    """The signed URL your controller generates."""

    receiver_merge_variable_mapping: Optional[Dict[str, str]] = FieldInfo(
        alias="receiverMergeVariableMapping", default=None
    )
    """Optional mapping of columns for receiver merge variables."""

    sender_address_mapping: Optional[Dict[str, str]] = FieldInfo(alias="senderAddressMapping", default=None)
    """Optional mapping of columns for sender addresses."""

    sender_merge_variable_mapping: Optional[Dict[str, str]] = FieldInfo(
        alias="senderMergeVariableMapping", default=None
    )
    """Optional mapping of columns for sender merge variables."""


class Note(BaseModel):
    """Details about a note in the import process."""

    message: str
    """A human-readable message describing the note."""

    type: Literal["truncated_test_file", "skipped_invalid_contacts"]
    """Type of note attached to the import process."""


class MailingListImportResponse(BaseModel):
    """Read-only view of a MailingListImport"""

    id: str
    """A unique ID prefixed with mailing*list_import*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    errors: List[Error]
    """A list of processing errors encountered, if any.

    Present when status is 'changes_required'.
    """

    file: File
    """The file object your controller returns: all the mappings plus a signed URL."""

    invalid_row_count: int = FieldInfo(alias="invalidRowCount")
    """Number of invalid rows found in the file."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    notes: List[Note]
    """Additional notes about the import process."""

    organization: str
    """The organization that owns this import."""

    receiver_status_count: VerificationStatusCount = FieldInfo(alias="receiverStatusCount")
    """Count of contact verification statuses."""

    status: Literal["validating", "completed", "changes_required"]
    """Status of the mailing list import process."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    valid_row_count: int = FieldInfo(alias="validRowCount")
    """Number of valid rows processed from the file."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""

    report_url: Optional[str] = FieldInfo(alias="reportURL", default=None)
    """
    A temporary URL to download the processing report, available once the import is
    completed.
    """

    sender_status_count: Optional[VerificationStatusCount] = FieldInfo(alias="senderStatusCount", default=None)
    """Count of contact verification statuses."""
