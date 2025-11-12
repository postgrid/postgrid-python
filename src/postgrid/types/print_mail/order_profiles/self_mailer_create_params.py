# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .self_mailer_size import SelfMailerSize
from ..order_mailing_class import OrderMailingClass

__all__ = ["SelfMailerCreateParams"]


class SelfMailerCreateParams(TypedDict, total=False):
    size: Required[SelfMailerSize]
    """Enum representing the supported self-mailer sizes."""

    expand: List[str]
    """Optional list of related resources to expand in the response."""

    description: Optional[str]
    """An optional description for the profile. Set to `null` to remove during update."""

    inside_template: Annotated[str, PropertyInfo(alias="insideTemplate")]
    """ID of the template for the inside. Required unless `pdf` is provided."""

    mailing_class: Annotated[OrderMailingClass, PropertyInfo(alias="mailingClass")]
    """Mailing class (cannot include extra services for self-mailers)."""

    merge_variables: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="mergeVariables")]
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]]
    """Optional key-value metadata."""

    outside_template: Annotated[str, PropertyInfo(alias="outsideTemplate")]
    """ID of the template for the outside. Required unless `pdf` is provided."""

    pdf: str
    """A 2-page PDF file containing the self-mailer content (inside and outside).

    Cannot be used with `insideTemplate`/`outsideTemplate`.
    """
