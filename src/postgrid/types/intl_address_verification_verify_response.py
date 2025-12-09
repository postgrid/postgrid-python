# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .errors import Errors
from .status import Status
from .._models import BaseModel

__all__ = ["IntlAddressVerificationVerifyResponse", "Data", "DataDetails", "DataGeoData", "DataSummary"]


class DataDetails(BaseModel):
    """
    Additional details about the verified address, such as premise, thoroughfare, and locality.
    """

    building: Optional[str] = None
    """The building name or number."""

    building_type: Optional[str] = FieldInfo(alias="buildingType", default=None)
    """The type of building (e.g., apartment, office)."""

    city_name: Optional[str] = FieldInfo(alias="cityName", default=None)
    """The full city name."""

    city_secondary: Optional[str] = FieldInfo(alias="citySecondary", default=None)
    """Secondary city information."""

    city_type: Optional[str] = FieldInfo(alias="cityType", default=None)
    """The type of city (e.g., city, town, village)."""

    delivery_address: Optional[str] = FieldInfo(alias="deliveryAddress", default=None)
    """The full delivery address."""

    dependent_locality: Optional[str] = FieldInfo(alias="dependentLocality", default=None)
    """The dependent locality (UK addresses)."""

    double_dependent_locality: Optional[str] = FieldInfo(alias="doubleDependentLocality", default=None)
    """The double dependent locality (UK addresses)."""

    organization: Optional[str] = None
    """The organization or company name."""

    postal_or_zip_primary: Optional[str] = FieldInfo(alias="postalOrZipPrimary", default=None)
    """The primary part of the postal or ZIP code."""

    postal_or_zip_secondary: Optional[str] = FieldInfo(alias="postalOrZipSecondary", default=None)
    """The secondary part of the postal or ZIP code."""

    post_box: Optional[str] = FieldInfo(alias="postBox", default=None)
    """The post box number."""

    premise: Optional[str] = None
    """The premise name or number."""

    premise_number: Optional[str] = FieldInfo(alias="premiseNumber", default=None)
    """The premise number."""

    premise_secondary: Optional[str] = FieldInfo(alias="premiseSecondary", default=None)
    """Secondary premise information."""

    premise_type: Optional[str] = FieldInfo(alias="premiseType", default=None)
    """The type of premise (e.g., house, flat)."""

    province_or_state_name: Optional[str] = FieldInfo(alias="provinceOrStateName", default=None)
    """The full name of the province or state."""

    province_or_state_type: Optional[str] = FieldInfo(alias="provinceOrStateType", default=None)
    """The type of province or state (e.g., province, state, region)."""

    street: Optional[str] = None
    """The street name."""

    street_post_direction: Optional[str] = FieldInfo(alias="streetPostDirection", default=None)
    """The directional suffix for the street (e.g., N, S, E, W)."""

    street_pre_direction: Optional[str] = FieldInfo(alias="streetPreDirection", default=None)
    """The directional prefix for the street (e.g., N, S, E, W)."""

    street_type: Optional[str] = FieldInfo(alias="streetType", default=None)
    """The type of street (e.g., St, Ave, Blvd)."""

    sub_administrative_area: Optional[str] = FieldInfo(alias="subAdministrativeArea", default=None)
    """The sub-administrative area."""

    sub_building: Optional[str] = FieldInfo(alias="subBuilding", default=None)
    """The sub-building name or number (e.g., unit, suite)."""

    sub_building_floor: Optional[str] = FieldInfo(alias="SubBuildingFloor", default=None)
    """The floor of the sub-building."""

    sub_building_number: Optional[str] = FieldInfo(alias="subBuildingNumber", default=None)
    """The sub-building number."""

    sub_building_type: Optional[str] = FieldInfo(alias="subBuildingType", default=None)
    """The type of sub-building (e.g., floor, wing)."""

    sub_street: Optional[str] = FieldInfo(alias="subStreet", default=None)
    """The sub-street name."""

    sub_street_post_direction: Optional[str] = FieldInfo(alias="subStreetPostDirection", default=None)
    """The directional suffix for the sub-street."""

    sub_street_pre_direction: Optional[str] = FieldInfo(alias="subStreetPreDirection", default=None)
    """The directional prefix for the sub-street."""

    sub_street_type: Optional[str] = FieldInfo(alias="subStreetType", default=None)
    """The type of sub-street."""

    super_administrative_area: Optional[str] = FieldInfo(alias="superAdministrativeArea", default=None)
    """The super-administrative area."""

    telephone: Optional[str] = None
    """The telephone number associated with the address."""


class DataGeoData(BaseModel):
    """Geocoding result for the verified address."""

    geo_accuracy: Optional[str] = FieldInfo(alias="geoAccuracy", default=None)
    """The geocode accuracy."""

    latitude: Optional[str] = None
    """The latitude of the address."""

    longitude: Optional[str] = None
    """The longitude of the address."""


class DataSummary(BaseModel):
    """A summary of the verification process and match levels."""

    context_identification_match_level: Optional[str] = FieldInfo(alias="contextIdentificationMatchLevel", default=None)
    """Context identification match level."""

    lexicon_identification_match_level: Optional[str] = FieldInfo(alias="lexiconIdentificationMatchLevel", default=None)
    """Lexicon identification match level."""

    match_score: Optional[float] = FieldInfo(alias="matchScore", default=None)
    """The match score (0-100)."""

    message: Optional[str] = None
    """Additional message about the verification."""

    parsing_status: Optional[str] = FieldInfo(alias="parsingStatus", default=None)
    """The parsing status of the address."""

    post_code_status: Optional[str] = FieldInfo(alias="postCodeStatus", default=None)
    """The status of the postal code."""

    post_processed_verification_match_level: Optional[str] = FieldInfo(
        alias="postProcessedVerificationMatchLevel", default=None
    )
    """The match level after post-processing."""

    pre_processed_verification_match_level: Optional[str] = FieldInfo(
        alias="preProcessedVerificationMatchLevel", default=None
    )
    """The match level before post-processing."""

    verification_status: Optional[str] = FieldInfo(alias="verificationStatus", default=None)
    """The overall verification status."""


class Data(BaseModel):
    """The result of a verified international address."""

    city: str
    """The city or locality."""

    country: str
    """The country code (ISO 3166-1 alpha-2)."""

    line1: str
    """The first address line."""

    postal_or_zip: str = FieldInfo(alias="postalOrZip")
    """The postal or ZIP code."""

    province_or_state: str = FieldInfo(alias="provinceOrState")
    """The province or state."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)
    """The full country name."""

    details: Optional[DataDetails] = None
    """
    Additional details about the verified address, such as premise, thoroughfare,
    and locality.
    """

    errors: Optional[Errors] = None
    """Errors encountered during address verification."""

    firm_name: Optional[str] = FieldInfo(alias="firmName", default=None)
    """The firm or company name, if available."""

    formatted_address: Optional[str] = FieldInfo(alias="formattedAddress", default=None)
    """The formatted address string."""

    geo_data: Optional[DataGeoData] = FieldInfo(alias="geoData", default=None)
    """Geocoding result for the verified address."""

    line2: Optional[str] = None
    """The second address line."""

    line3: Optional[str] = None
    """The third address line, if available."""

    status: Optional[Status] = None
    """The verification status of an address."""

    summary: Optional[DataSummary] = None
    """A summary of the verification process and match levels."""

    zip_plus4: Optional[str] = FieldInfo(alias="zipPlus4", default=None)
    """The ZIP+4 code (for US addresses)."""


class IntlAddressVerificationVerifyResponse(BaseModel):
    data: Data
    """The result of a verified international address."""

    message: str

    status: Literal["success", "error"]
