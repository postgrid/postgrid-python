# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .self_mailer_size import SelfMailerSize
from ..order_mailing_class import OrderMailingClass

__all__ = ["SelfMailerProfile"]


class SelfMailerProfile(BaseModel):
    id: str
    """Unique identifier for the order profile."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the profile was created."""

    live: bool
    """Indicates if the profile is associated with the live or test environment."""

    object: Literal["self_mailer_profile"]
    """Always `self_mailer_profile`."""

    size: SelfMailerSize
    """Enum representing the supported self-mailer sizes."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the profile was last updated."""

    description: Optional[str] = None
    """An optional description for the profile. Set to `null` to remove during update."""

    inside_template: Optional[str] = FieldInfo(alias="insideTemplate", default=None)
    """ID of the template for the inside. Required unless `pdf` is provided."""

    mailing_class: Optional[OrderMailingClass] = FieldInfo(alias="mailingClass", default=None)
    """Mailing class (cannot include extra services for self-mailers)."""

    merge_variables: Optional[Dict[str, builtins.object]] = FieldInfo(alias="mergeVariables", default=None)
    """Default merge variables for orders created using this profile."""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata."""

    outside_template: Optional[str] = FieldInfo(alias="outsideTemplate", default=None)
    """ID of the template for the outside. Required unless `pdf` is provided."""

    uploaded_pdf: Optional[str] = FieldInfo(alias="uploadedPDF", default=None)
    """A temporary, signed URL to view the uploaded PDF, if any."""
