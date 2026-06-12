# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddverList", "Mappings", "Metadata", "MetadataStatusCount"]


class Mappings(BaseModel):
    """The mapping of your CSV column names to PostGrid address fields.

    Each value is
    the name of a column in your uploaded file.
    """

    line1: str
    """The column containing the first line of each address.

    If your entire address is in a single column, specify only this mapping.
    """

    city: Optional[str] = None
    """The column containing the city of each address."""

    country: Optional[str] = None
    """
    The column containing the 2-letter ISO country code of each address (e.g. `US`,
    not `United States`).
    """

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The column containing the first name of the person at each address.

    Only used when NCOA is run.
    """

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """The column containing the full name of the person at each address.

    Can be supplied instead of `firstName` and `lastName`. Only used when NCOA or
    CCOA is run.
    """

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The column containing the last name of the person at each address.

    Only used when NCOA is run.
    """

    line2: Optional[str] = None
    """The column containing the second line of each address."""

    postal_or_zip: Optional[str] = FieldInfo(alias="postalOrZip", default=None)
    """The column containing the postal or ZIP code of each address."""

    province_or_state: Optional[str] = FieldInfo(alias="provinceOrState", default=None)
    """The column containing the province or state of each address."""


class MetadataStatusCount(BaseModel):
    """The number of addresses by resulting verification status."""

    corrected: Optional[int] = None

    failed: Optional[int] = None

    verified: Optional[int] = None


class Metadata(BaseModel):
    """Additional metadata about the list, including a count of each status."""

    status_count: Optional[MetadataStatusCount] = FieldInfo(alias="statusCount", default=None)
    """The number of addresses by resulting verification status."""


class AddverList(BaseModel):
    """
    A bulk address verification list — an uploaded CSV file of addresses and its
    processing state.
    """

    id: str
    """A unique ID prefixed with `addver_list_`."""

    cost: int
    """The cost charged for processing this list."""

    count: int
    """The number of addresses in the uploaded file."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this list was created."""

    file: str
    """A signed URL to the uploaded input CSV file."""

    mappings: Mappings
    """The mapping of your CSV column names to PostGrid address fields.

    Each value is the name of a column in your uploaded file.
    """

    name: str
    """The name supplied for the list.

    This only affects what is displayed in the dashboard.
    """

    organization: str
    """The ID of the organization that owns this list."""

    status: str
    """The processing status of the list, e.g.

    `pending`, `processing`, or `processed`.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this list was last updated."""

    use_geocode: bool = FieldInfo(alias="useGeocode")
    """Whether geocoding (latitude/longitude) output was requested."""

    use_intl_verification: bool = FieldInfo(alias="useIntlVerification")
    """Whether international (outside US & Canada) verification was requested."""

    use_proper_case: bool = FieldInfo(alias="useProperCase")
    """Whether Proper Case output was requested."""

    user: str
    """The ID of the user that created this list."""

    default_country: Optional[str] = FieldInfo(alias="defaultCountry", default=None)
    """
    The ISO 2-letter country code used as the fallback when a row is missing a
    country. Not returned for lists uploaded without one, e.g. lists which map the
    entire address into `line1`.
    """

    metadata: Optional[Metadata] = None
    """Additional metadata about the list, including a count of each status."""

    num_invalid_rows: Optional[int] = FieldInfo(alias="numInvalidRows", default=None)
    """The number of invalid or skipped rows in the uploaded file.

    May be omitted on lists created before this field was introduced.
    """

    result: Optional[str] = None
    """A signed URL to the processed output CSV file.

    Present once the list has finished processing.
    """

    run_ccoa: Optional[bool] = FieldInfo(alias="runCCOA", default=None)
    """Whether CCOA (Canada Post change of address) was requested.

    May be omitted on lists created before COA support was introduced.
    """

    run_ncoa: Optional[bool] = FieldInfo(alias="runNCOA", default=None)
    """Whether NCOA (US National Change of Address) was requested.

    May be omitted on lists created before COA support was introduced.
    """
