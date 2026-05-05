# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TargetedListBuildUpdateParams", "UsCompanies", "UsConsumers", "UsConsumersZipCodesAround"]


class TargetedListBuildUpdateParams(TypedDict, total=False):
    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    limit: int
    """Maximum number of contacts to include in the built mailing list.

    If omitted, all matching contacts are included.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    us_companies: Annotated[UsCompanies, PropertyInfo(alias="usCompanies")]
    """Filters used to target US companies (B2B) when building a list."""

    us_consumers: Annotated[UsConsumers, PropertyInfo(alias="usConsumers")]
    """Filters used to target US consumers (B2C) when building a list.

    The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are mutually
    exclusive — you may supply at most one of them.
    """


class UsCompanies(TypedDict, total=False):
    """Filters used to target US companies (B2B) when building a list."""

    postal_codes: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="postalCodes")]]
    """Required list of five-digit US ZIP codes to target."""

    company_types: Annotated[
        List[Literal["public", "private", "educational", "government", "nonprofit", "public_subsidiary"]],
        PropertyInfo(alias="companyTypes"),
    ]
    """Filter by ownership structure of the company."""

    employee_count: Annotated[Iterable[int], PropertyInfo(alias="employeeCount")]
    """Inclusive `[min, max]` range for the number of employees at the company.

    Values must be between 1 and 1,000,000.
    """

    founded_year: Annotated[Iterable[int], PropertyInfo(alias="foundedYear")]
    """
    Inclusive `[min, max]` range for the year the company was founded. Values must
    be between 1600 and 2100.
    """

    industries: SequenceNotStr[str]
    """Filter by free-form industry names (see the autocomplete endpoint)."""

    naics_codes: Annotated[SequenceNotStr[str], PropertyInfo(alias="naicsCodes")]
    """Filter by six-digit [NAICS](https://www.census.gov/naics/) industry codes."""

    tags: SequenceNotStr[str]
    """Filter by free-form company tags (e.g., `"saas"`, `"b2b"`)."""


class UsConsumersZipCodesAround(TypedDict, total=False):
    """
    A geographic filter that selects all ZIP codes within a given radius of a
    center ZIP code.
    """

    radius_in_miles: Required[Annotated[float, PropertyInfo(alias="radiusInMiles")]]
    """The radius in miles around `zipCode` to include. Between 0.1 and 100."""

    zip_code: Required[Annotated[str, PropertyInfo(alias="zipCode")]]
    """The five-digit ZIP code at the center of the search circle."""


class UsConsumers(TypedDict, total=False):
    """Filters used to target US consumers (B2C) when building a list.

    The geographic filters (`zipCodesAround`, `cityStates`, `zipCodes`) are
    mutually exclusive — you may supply at most one of them.
    """

    age_range: Annotated[Iterable[int], PropertyInfo(alias="ageRange")]
    """Inclusive `[min, max]` age range. Values must be between 18 and 80."""

    city_states: Annotated[SequenceNotStr[str], PropertyInfo(alias="cityStates")]
    """A list of `"City, ST"` strings (e.g. `"New York, NY"`) to target."""

    education_levels: Annotated[
        List[Literal["high_school", "college", "grad_school", "vocational_training"]],
        PropertyInfo(alias="educationLevels"),
    ]
    """Filter by highest level of education completed."""

    gender: Literal["male", "female"]
    """Gender filter for US consumer list builds."""

    home_value_range: Annotated[Iterable[int], PropertyInfo(alias="homeValueRange")]
    """Inclusive `[min, max]` home value range, in US dollars.

    Values must be between 0 and 1,000,000.
    """

    income_range: Annotated[Iterable[int], PropertyInfo(alias="incomeRange")]
    """
    Inclusive `[min, max]` annual household income range, in US dollars. Values must
    be between 0 and 200,000.
    """

    num_children_range: Annotated[Iterable[int], PropertyInfo(alias="numChildrenRange")]
    """Inclusive `[min, max]` number of children in the household.

    Values must be between 0 and 8.
    """

    occupations: List[
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
    """Filter by occupation classification."""

    zip_codes: Annotated[SequenceNotStr[str], PropertyInfo(alias="zipCodes")]
    """A list of five-digit US ZIP codes to target."""

    zip_codes_around: Annotated[UsConsumersZipCodesAround, PropertyInfo(alias="zipCodesAround")]
    """
    A geographic filter that selects all ZIP codes within a given radius of a center
    ZIP code.
    """
