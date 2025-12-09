# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PlasticCard", "DoubleSided", "SingleSided"]


class DoubleSided(BaseModel):
    """Model representing a double-sided plastic card."""

    back_html: Optional[str] = FieldInfo(alias="backHTML", default=None)
    """The HTML content for the back side of the double-sided plastic card."""

    back_template: Optional[str] = FieldInfo(alias="backTemplate", default=None)
    """The template ID for the back side of the double-sided plastic card."""

    front_html: Optional[str] = FieldInfo(alias="frontHTML", default=None)
    """The HTML content for the front side of the double-sided plastic card."""

    front_template: Optional[str] = FieldInfo(alias="frontTemplate", default=None)
    """The template ID for the front side of the double-sided plastic card."""

    pdf: Optional[str] = None
    """
    A URL pointing to a PDF file for the double-sided plastic card or the file
    itself.
    """


class SingleSided(BaseModel):
    """Model representing a single-sided plastic card."""

    html: Optional[str] = None
    """The HTML content for the single-sided plastic card.

    Can specify one of this, `template`, or `pdf`.
    """

    pdf: Optional[str] = None
    """
    A URL pointing to a PDF file for the single-sided plastic card or the PDF file
    itself.
    """

    template: Optional[str] = None
    """The template ID for the single-sided plastic card."""


class PlasticCard(BaseModel):
    """Model representing a plastic card."""

    size: Literal["standard"]
    """Enum representing the size of the plastic card."""

    double_sided: Optional[DoubleSided] = FieldInfo(alias="doubleSided", default=None)
    """Model representing a double-sided plastic card."""

    single_sided: Optional[SingleSided] = FieldInfo(alias="singleSided", default=None)
    """Model representing a single-sided plastic card."""
