# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["BulkVerificationUploadParams", "Mappings"]


class BulkVerificationUploadParams(TypedDict, total=False):
    file: Required[FileTypes]

    mappings: Required[Mappings]
    """The mapping of your CSV column names to PostGrid address fields.

    Each value is the name of a column in your uploaded file.
    """

    name: Required[str]
    """A name for the uploaded list.

    This only affects what is displayed in the dashboard.
    """

    default_country: Annotated[str, PropertyInfo(alias="defaultCountry")]
    """
    An ISO 2-letter country code used as the fallback when a row is missing a value
    in the `country` column.
    """

    run_ccoa: Annotated[bool, PropertyInfo(alias="runCCOA")]
    """Whether to run CCOA (Canada Post change of address) on the list.

    Note that a list cannot run both NCOA and CCOA — split mixed US/Canadian files
    into separate lists.
    """

    run_ncoa: Annotated[bool, PropertyInfo(alias="runNCOA")]
    """Whether to run NCOA (US National Change of Address) on the list."""

    use_geocode: Annotated[bool, PropertyInfo(alias="useGeocode")]
    """
    Whether to append geographical location information (latitude, longitude) to
    your output. Bulk geocoding must be enabled by contacting support.
    """

    use_intl_verification: Annotated[bool, PropertyInfo(alias="useIntlVerification")]
    """Whether to perform international (outside US & Canada) verification."""

    use_proper_case: Annotated[bool, PropertyInfo(alias="useProperCase")]
    """Whether to return addresses in Proper Case."""


class Mappings(TypedDict, total=False):
    """The mapping of your CSV column names to PostGrid address fields.

    Each value is
    the name of a column in your uploaded file.
    """

    line1: Required[str]
    """The column containing the first line of each address.

    If your entire address is in a single column, specify only this mapping.
    """

    city: str
    """The column containing the city of each address."""

    country: str
    """
    The column containing the 2-letter ISO country code of each address (e.g. `US`,
    not `United States`).
    """

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The column containing the first name of the person at each address.

    Only used when NCOA is run.
    """

    full_name: Annotated[str, PropertyInfo(alias="fullName")]
    """The column containing the full name of the person at each address.

    Can be supplied instead of `firstName` and `lastName`. Only used when NCOA or
    CCOA is run.
    """

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The column containing the last name of the person at each address.

    Only used when NCOA is run.
    """

    line2: str
    """The column containing the second line of each address."""

    postal_or_zip: Annotated[str, PropertyInfo(alias="postalOrZip")]
    """The column containing the postal or ZIP code of each address."""

    province_or_state: Annotated[str, PropertyInfo(alias="provinceOrState")]
    """The column containing the province or state of each address."""
