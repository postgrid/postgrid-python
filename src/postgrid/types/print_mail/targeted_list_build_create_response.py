# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TargetedListBuildCreateResponse",
    "Error",
    "PreviewRecord",
    "Quote",
    "UsCompanies",
    "UsConsumers",
    "UsConsumersZipCodesAround",
]


class Error(BaseModel):
    """Details of an error encountered while processing a targeted list build."""

    message: str
    """A human-readable message describing the error."""

    type: Literal["not_enough_info_to_quote", "insufficient_credits", "internal_service_error"]
    """Type of error encountered while generating a quote or building the list."""


class PreviewRecord(BaseModel):
    """
    A single masked preview record returned with a quote so you can sanity
    check the kind of contacts that will end up in the mailing list before
    confirming the build.
    """

    formatted_address: str = FieldInfo(alias="formattedAddress")
    """The masked, comma-joined formatted address of the contact."""

    name: str
    """The masked name of the contact or business."""


class Quote(BaseModel):
    """Details of the quote generated for a targeted list build."""

    count: int
    """The number of contacts that will be included in the built mailing list.

    This accounts for any `limit` that was provided.
    """

    generated_at: datetime = FieldInfo(alias="generatedAt")
    """The UTC time at which the quote was generated."""

    price_per_contact_cents: float = FieldInfo(alias="pricePerContactCents")
    """The price per contact, in cents.

    Multiply by `count` to get the total cost of building the list.
    """


class UsCompanies(BaseModel):
    """Filters used to target US companies (B2B) when building a list."""

    postal_codes: List[str] = FieldInfo(alias="postalCodes")
    """Required list of five-digit US ZIP codes to target."""

    company_types: Optional[
        List[Literal["public", "private", "educational", "government", "nonprofit", "public_subsidiary"]]
    ] = FieldInfo(alias="companyTypes", default=None)
    """Filter by ownership structure of the company."""

    employee_count: Optional[List[int]] = FieldInfo(alias="employeeCount", default=None)
    """Inclusive `[min, max]` range for the number of employees at the company.

    Values must be between 1 and 1,000,000.
    """

    founded_year: Optional[List[int]] = FieldInfo(alias="foundedYear", default=None)
    """
    Inclusive `[min, max]` range for the year the company was founded. Values must
    be between 1600 and 2100.
    """

    industries: Optional[List[str]] = None
    """Filter by free-form industry names (see the autocomplete endpoint)."""

    naics_codes: Optional[List[str]] = FieldInfo(alias="naicsCodes", default=None)
    """Filter by six-digit [NAICS](https://www.census.gov/naics/) industry codes."""

    tags: Optional[List[str]] = None
    """Filter by free-form company tags (e.g., `"saas"`, `"b2b"`)."""


class UsConsumersZipCodesAround(BaseModel):
    """
    A geographic filter that selects all ZIP codes within a given radius of a
    center ZIP code.
    """

    radius_in_miles: float = FieldInfo(alias="radiusInMiles")
    """The radius in miles around `zipCode` to include. Between 0.1 and 100."""

    zip_code: str = FieldInfo(alias="zipCode")
    """The five-digit ZIP code at the center of the search circle."""


class UsConsumers(BaseModel):
    """Filters used to target US consumers (B2C) when building a list.

    The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are
    mutually exclusive — you may supply at most one of them.
    """

    age_range: Optional[List[int]] = FieldInfo(alias="ageRange", default=None)
    """Inclusive `[min, max]` age range. Values must be between 18 and 80."""

    city_states: Optional[List[str]] = FieldInfo(alias="cityStates", default=None)
    """A list of `"City, ST"` strings (e.g. `"New York, NY"`) to target."""

    education_levels: Optional[List[Literal["high_school", "college", "grad_school", "vocational_training"]]] = (
        FieldInfo(alias="educationLevels", default=None)
    )
    """Filter by highest level of education completed."""

    gender: Optional[Literal["male", "female"]] = None
    """Gender filter for US consumer list builds."""

    home_value_range: Optional[List[int]] = FieldInfo(alias="homeValueRange", default=None)
    """Inclusive `[min, max]` home value range, in US dollars.

    Values must be between 0 and 1,000,000.
    """

    income_range: Optional[List[int]] = FieldInfo(alias="incomeRange", default=None)
    """
    Inclusive `[min, max]` annual household income range, in US dollars. Values must
    be between 0 and 200,000.
    """

    num_children_range: Optional[List[int]] = FieldInfo(alias="numChildrenRange", default=None)
    """Inclusive `[min, max]` number of children in the household.

    Values must be between 0 and 8.
    """

    occupations: Optional[
        List[
            Literal[
                "professional_technical",
                "administration_management",
                "sales_service",
                "clerical_white_collar",
                "craftsmen_blue_collar",
                "student",
                "homemaker",
                "retired",
                "farmer",
                "military",
                "religious",
                "self_employed",
                "self_employed_professional_technical",
                "self_employed_administration_management",
                "self_employed_sales_service",
                "self_employed_clerical_white_collar",
                "self_employed_craftsmen_blue_collar",
                "self_employed_student",
                "self_employed_homemaker",
                "self_employed_retired",
                "self_employed_other",
                "educator",
                "financial_professional",
                "legal_professional",
                "medical_professional",
                "other",
            ]
        ]
    ] = None
    """Filter by occupation classification."""

    zip_codes: Optional[List[str]] = FieldInfo(alias="zipCodes", default=None)
    """A list of five-digit US ZIP codes to target."""

    zip_codes_around: Optional[UsConsumersZipCodesAround] = FieldInfo(alias="zipCodesAround", default=None)
    """
    A geographic filter that selects all ZIP codes within a given radius of a center
    ZIP code.
    """


class TargetedListBuildCreateResponse(BaseModel):
    """
    A targeted list build represents a request to build a new mailing list by
    targeting US consumers or companies matching the provided filters. Once
    created, a quote is generated asynchronously. After reviewing the quote
    and preview records, you may confirm the build, which kicks off the
    creation of the underlying mailing list.
    """

    id: str
    """A unique ID prefixed with targeted*list_build*"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this resource was created."""

    live: bool
    """`true` if this is a live mode resource else `false`."""

    organization: str
    """The ID of the organization that owns this list build."""

    status: Literal["generating_quote", "quote_ready", "creating_list", "completed", "failed"]
    """Status of a targeted list build."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The UTC time at which this resource was last updated."""

    build_progress_percent: Optional[float] = FieldInfo(alias="buildProgressPercent", default=None)
    """A percentage from 0 to 100 representing how much of the build has completed.

    Only populated while `status` is `creating_list`.
    """

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """The UTC time at which the build finished successfully.

    Only present once `status` is `completed`.
    """

    confirmed_at: Optional[datetime] = FieldInfo(alias="confirmedAt", default=None)
    """The UTC time at which the build was confirmed, if any."""

    description: Optional[str] = None
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    errors: Optional[List[Error]] = None
    """Any errors encountered while generating a quote or building the list."""

    limit: Optional[int] = None
    """Maximum number of contacts to include in the built mailing list.

    If omitted, all matching contacts are included.
    """

    mailing_list: Optional[str] = FieldInfo(alias="mailingList", default=None)
    """The ID of the mailing list that was built.

    Present once `status` is `completed`.
    """

    metadata: Optional[Dict[str, object]] = None
    """See the section on Metadata."""

    preview_records: Optional[List[PreviewRecord]] = FieldInfo(alias="previewRecords", default=None)
    """
    A small number of masked sample records for the configured filters, populated
    alongside `quote`.
    """

    quote: Optional[Quote] = None
    """Details of the quote generated for a targeted list build."""

    us_companies: Optional[UsCompanies] = FieldInfo(alias="usCompanies", default=None)
    """Filters used to target US companies (B2B) when building a list."""

    us_consumers: Optional[UsConsumers] = FieldInfo(alias="usConsumers", default=None)
    """Filters used to target US consumers (B2C) when building a list.

    The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
    exclusive — you may supply at most one of them.
    """
