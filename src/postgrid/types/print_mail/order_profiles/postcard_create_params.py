# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from .postcard_size import PostcardSize
from ..order_mailing_class import OrderMailingClass

__all__ = ["PostcardCreateParams"]


class PostcardCreateParams(TypedDict, total=False):
    size: Required[PostcardSize]
    """Enum representing the supported postcard sizes."""

    expand: SequenceNotStr[str]
    """Optional list of related resources to expand in the response."""

    back_template: Annotated[str, PropertyInfo(alias="backTemplate")]
    """ID of the template for the back side. Required unless `pdf` is provided."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    front_template: Annotated[str, PropertyInfo(alias="frontTemplate")]
    """ID of the template for the front side. Required unless `pdf` is provided."""

    mailing_class: Annotated[OrderMailingClass, PropertyInfo(alias="mailingClass")]
    """
    Mailing class (cannot include extra services like `certified` or `registered`
    for postcards, though).
    """

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""

    pdf: str
    """A 2-page PDF file containing the postcard content (front and back).

    Cannot be used with `frontTemplate`/`backTemplate`.
    """
