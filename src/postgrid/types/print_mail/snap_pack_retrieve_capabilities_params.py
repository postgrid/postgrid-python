# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SnapPackRetrieveCapabilitiesParams"]


class SnapPackRetrieveCapabilitiesParams(TypedDict, total=False):
    return_country_code: Required[Annotated[str, PropertyInfo(alias="returnCountryCode")]]
    """The country code where mail may be returned to."""

    destination_country_code: Annotated[str, PropertyInfo(alias="destinationCountryCode")]
    """
    The country code of where the snap pack will be sent to. One of `mailingList` or
    `destinationCountryCode` must be supplied but not both.
    """

    mailing_list: Annotated[str, PropertyInfo(alias="mailingList")]
    """
    Sources destination countries from the provided mailing list. One of
    `mailingList` or `destinationCountryCode` must be supplied but not both.
    """
