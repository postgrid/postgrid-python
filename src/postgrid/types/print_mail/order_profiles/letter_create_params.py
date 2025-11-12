# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..letter_size import LetterSize
from ..address_placement import AddressPlacement
from ..attached_pdf_param import AttachedPdfParam
from ..order_mailing_class import OrderMailingClass

__all__ = ["LetterCreateParams"]


class LetterCreateParams(TypedDict, total=False):
    size: Required[LetterSize]
    """Enum representing the supported letter sizes."""

    expand: List[str]
    """Optional list of related resources to expand in the response."""

    address_placement: Annotated[AddressPlacement, PropertyInfo(alias="addressPlacement")]
    """Enum representing the placement of the address on the letter."""

    attached_pdf: Annotated[AttachedPdfParam, PropertyInfo(alias="attachedPDF")]
    """Model representing an attached PDF."""

    color: bool
    """Specifies whether to print in color (true) or black and white (false)."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    double_sided: Annotated[bool, PropertyInfo(alias="doubleSided")]
    """Specifies whether to print on both sides of the paper."""

    envelope: str
    """ID of a custom envelope to use."""

    mailing_class: Annotated[OrderMailingClass, PropertyInfo(alias="mailingClass")]
    """Mailing class."""

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""

    pdf: str
    """A PDF file containing the letter content. Cannot be used with `template`."""

    perforated_page: Annotated[Literal[1], PropertyInfo(alias="perforatedPage")]
    """Specifies which page number should be perforated (if any)."""

    return_envelope: Annotated[str, PropertyInfo(alias="returnEnvelope")]
    """ID of a return envelope to include."""

    template: str
    """ID of a template to use for the letter content. Cannot be used with `pdf`."""
