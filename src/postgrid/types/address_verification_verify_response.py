# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .errors import Errors
from .status import Status
from .._models import BaseModel

__all__ = ["AddressVerificationVerifyResponse", "Data", "DataDetails", "DataGeocodeResult", "DataGeocodeResultLocation"]


class DataDetails(BaseModel):
    """
    If you supply `includeDetails=true` as a query parameter, we will also populate an additional `details` field that follows the [Address Details](https://avdocs.postgrid.com/#address-details) schema.
    """

    box_id: Optional[str] = FieldInfo(alias="boxID", default=None)
    """PO Box ID"""

    county: Optional[str] = None
    """County in the United States (US address only)"""

    county_num: Optional[str] = FieldInfo(alias="countyNum", default=None)
    """FIPS code for county (US address only)"""

    delivery_installation_area_name: Optional[str] = FieldInfo(alias="deliveryInstallationAreaName", default=None)
    """Delivery installation area name"""

    delivery_installation_qualifier: Optional[str] = FieldInfo(alias="deliveryInstallationQualifier", default=None)
    """Delivery installation qualifier"""

    delivery_installation_type: Optional[str] = FieldInfo(alias="deliveryInstallationType", default=None)
    """Delivery installation type"""

    extra_info: Optional[str] = FieldInfo(alias="extraInfo", default=None)
    """Any extra information relevant to the address"""

    post_direction: Optional[str] = FieldInfo(alias="postDirection", default=None)
    """The post-direction of the street (after the street name, US addresses only)"""

    pre_direction: Optional[str] = FieldInfo(alias="preDirection", default=None)
    """The pre-direction of the street (before the street name, US addresses only)"""

    residential: Optional[bool] = None
    """Indicates that the address is residential (US address only)"""

    rural_route_number: Optional[str] = FieldInfo(alias="ruralRouteNumber", default=None)
    """Rural route number"""

    rural_route_type: Optional[str] = FieldInfo(alias="ruralRouteType", default=None)
    """Rural route type"""

    street_direction: Optional[str] = FieldInfo(alias="streetDirection", default=None)
    """The direction of the street (N, S, E, W, etc)"""

    street_name: Optional[str] = FieldInfo(alias="streetName", default=None)
    """Name of the street where the address is located"""

    street_number: Optional[str] = FieldInfo(alias="streetNumber", default=None)
    """Street number (e.g. the 20 in 20 Bay St)"""

    street_type: Optional[str] = FieldInfo(alias="streetType", default=None)
    """Type of the street (DR, ST, BLVD, etc)"""

    suite_id: Optional[str] = FieldInfo(alias="suiteID", default=None)
    """The unit number/name"""

    suite_key: Optional[str] = FieldInfo(alias="suiteKey", default=None)
    """The suite key"""

    us_census_block_number: Optional[str] = FieldInfo(alias="usCensusBlockNumber", default=None)
    """US Census block number"""

    us_census_cmsa: Optional[str] = FieldInfo(alias="usCensusCMSA", default=None)
    """US Census consolidated metropolitan statistical area"""

    us_census_ma: Optional[str] = FieldInfo(alias="usCensusMA", default=None)
    """US Census metropolitan area"""

    us_census_msa: Optional[str] = FieldInfo(alias="usCensusMSA", default=None)
    """US Census metropolitan statistical area"""

    us_census_pmsa: Optional[str] = FieldInfo(alias="usCensusPMSA", default=None)
    """US Census primary metropolitan statistical area"""

    us_census_tract_number: Optional[str] = FieldInfo(alias="usCensusTractNumber", default=None)
    """US Census tract number"""

    us_congressional_district_number: Optional[str] = FieldInfo(alias="usCongressionalDistrictNumber", default=None)
    """US congressional district number"""

    us_has_daylight_savings: Optional[bool] = FieldInfo(alias="usHasDaylightSavings", default=None)
    """True if address location recognizes DST"""

    us_mailing_check_digit: Optional[str] = FieldInfo(alias="usMailingCheckDigit", default=None)
    """PostNet barcode digit"""

    us_mailings_carrier_route: Optional[str] = FieldInfo(alias="usMailingsCarrierRoute", default=None)
    """4-character code assigned to mail delivery route within a 5 digit zip code"""

    us_mailings_default_flag: Optional[bool] = FieldInfo(alias="usMailingsDefaultFlag", default=None)
    """
    True if US address matches a high-rise default or rural route default in the
    USPS data
    """

    us_mailings_delivery_point: Optional[str] = FieldInfo(alias="usMailingsDeliveryPoint", default=None)
    """Unique USPS identifier for the delivery point"""

    us_mailings_dpv_confirmation_indicator: Optional[str] = FieldInfo(
        alias="usMailingsDpvConfirmationIndicator", default=None
    )
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_mailings_dpv_crma_indicator: Optional[str] = FieldInfo(alias="usMailingsDpvCrmaIndicator", default=None)
    """Y if this is a commercial mail receiving agency, N otherwise"""

    us_mailings_dpv_footnote1: Optional[str] = FieldInfo(alias="usMailingsDpvFootnote1", default=None)
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_mailings_dpv_footnote2: Optional[str] = FieldInfo(alias="usMailingsDpvFootnote2", default=None)
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_mailings_dpv_footnote3: Optional[str] = FieldInfo(alias="usMailingsDpvFootnote3", default=None)
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_mailings_elot_asc_desc: Optional[str] = FieldInfo(alias="usMailingsElotAscDesc", default=None)
    """A for ascending, D for descending"""

    us_mailings_elot_sequence_number: Optional[str] = FieldInfo(alias="usMailingsElotSequenceNumber", default=None)
    """eLOT sequence number"""

    us_mailings_ews_flag: Optional[str] = FieldInfo(alias="usMailingsEWSFlag", default=None)
    """Y if address is in early warning system database"""

    us_mailings_lacs_flag: Optional[str] = FieldInfo(alias="usMailingsLACSFlag", default=None)
    """Y if address converted by LACS"""

    us_mailings_lacs_return_code: Optional[str] = FieldInfo(alias="usMailingsLACSReturnCode", default=None)
    """Corresponds to USPS LACSLink return code"""

    us_mailings_record_type_code: Optional[str] = FieldInfo(alias="usMailingsRecordTypeCode", default=None)
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_mailings_suite_link_return_code: Optional[str] = FieldInfo(alias="usMailingsSuiteLinkReturnCode", default=None)
    """See [USPS DPV](https://avdocs.postgrid.com/#usps-dpv)"""

    us_state_legislative_lower: Optional[str] = FieldInfo(alias="usStateLegislativeLower", default=None)
    """Lower legislative district for the US address"""

    us_state_legislative_upper: Optional[str] = FieldInfo(alias="usStateLegislativeUpper", default=None)
    """Upper legislative district for the US address"""

    us_time_zone: Optional[str] = FieldInfo(alias="usTimeZone", default=None)
    """Time zone for the US address area"""

    vacant: Optional[bool] = None
    """Indicates that the address is vacant according to the USPS (US address only)"""


class DataGeocodeResultLocation(BaseModel):
    """Object that contains `lat`, `lng` properties with number values"""

    lat: float

    lng: float


class DataGeocodeResult(BaseModel):
    """
    If the `geocode=true` query parameter is supplied, the response will include a geocodeResult
    which follows the [Geocoding](https://avdocs.postgrid.com/#geocoding) schema.  You can request
    this feature be enabled by emailing `support@postgrid.com`. This includes our verification, batch
    verification, suggestions, and POST /completions endpoint. Note that you must supply country when
    geocoding to get the result successfully.
    """

    accuracy: float
    """
    A real number from 0.00 to 1.00 which represents an
    [accuracy score](https://avdocs.postgrid.com/#accuracy-score)
    """

    accuracy_type: Literal[
        "rooftop",
        "point",
        "range_interpolation",
        "nearest_rooftop_match",
        "intersection",
        "street_center",
        "place",
        "state",
    ] = FieldInfo(alias="accuracyType")
    """
    A string representing the
    [accuracy type](https://avdocs.postgrid.com/#accuracy-type)
    """

    location: DataGeocodeResultLocation
    """Object that contains `lat`, `lng` properties with number values"""


class Data(BaseModel):
    city: str
    """The city name of the address."""

    country: str
    """The country code of the address."""

    line1: str
    """The first line of the address."""

    postal_or_zip: str = FieldInfo(alias="postalOrZip")
    """The postal code or ZIP code of the address."""

    province_or_state: str = FieldInfo(alias="provinceOrState")
    """The province or state of the address."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)
    """The country name of the address."""

    details: Optional[DataDetails] = None
    """
    If you supply `includeDetails=true` as a query parameter, we will also populate
    an additional `details` field that follows the
    [Address Details](https://avdocs.postgrid.com/#address-details) schema.
    """

    errors: Optional[Errors] = None
    """Errors encountered during address verification."""

    firm_name: Optional[str] = FieldInfo(alias="firmName", default=None)
    """The firm name of the address."""

    geocode_result: Optional[DataGeocodeResult] = FieldInfo(alias="geocodeResult", default=None)
    """
    If the `geocode=true` query parameter is supplied, the response will include a
    geocodeResult which follows the
    [Geocoding](https://avdocs.postgrid.com/#geocoding) schema. You can request this
    feature be enabled by emailing `support@postgrid.com`. This includes our
    verification, batch verification, suggestions, and POST /completions endpoint.
    Note that you must supply country when geocoding to get the result successfully.
    """

    line2: Optional[str] = None
    """The second line of the address."""

    status: Optional[Status] = None
    """The verification status of an address."""

    zip_plus4: Optional[str] = FieldInfo(alias="zipPlus4", default=None)
    """The zip plus 4 code of the address."""


class AddressVerificationVerifyResponse(BaseModel):
    data: Data

    message: str

    status: Literal["success", "error"]
