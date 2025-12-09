# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PlasticCardParam", "DoubleSided", "SingleSided"]


class DoubleSided(TypedDict, total=False):
    """Model representing a double-sided plastic card."""

    back_html: Annotated[str, PropertyInfo(alias="backHTML")]
    """The HTML content for the back side of the double-sided plastic card."""

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """The template ID for the back side of the double-sided plastic card."""

    front_html: Annotated[str, PropertyInfo(alias="frontHTML")]
    """The HTML content for the front side of the double-sided plastic card."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """The template ID for the front side of the double-sided plastic card."""

    pdf: str
    """
    A URL pointing to a PDF file for the double-sided plastic card or the file
    itself.
    """


class SingleSided(TypedDict, total=False):
    """Model representing a single-sided plastic card."""

    html: str
    """The HTML content for the single-sided plastic card.

    Can specify one of this, `template`, or `pdf`.
    """

    pdf: str
    """
    A URL pointing to a PDF file for the single-sided plastic card or the PDF file
    itself.
    """

    template: str
    """The template ID for the single-sided plastic card."""


class PlasticCardParam(TypedDict, total=False):
    """Model representing a plastic card."""

    size: Required[Literal["standard"]]
    """Enum representing the size of the plastic card."""

    double_sided: Annotated[DoubleSided, PropertyInfo(alias="doubleSided")]
    """Model representing a double-sided plastic card."""

    single_sided: Annotated[SingleSided, PropertyInfo(alias="singleSided")]
    """Model representing a single-sided plastic card."""
