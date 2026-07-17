# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from .contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = ["ReturnEnvelopeCreateParams", "To"]


class ReturnEnvelopeCreateParams(TypedDict, total=False):
    to: Required[To]
    """A contact provided in one of two ways:

    - an **inline contact body** with the same fields you would use to create a
      contact (there is no need to create the contact first), or
    - the **ID of an existing contact** (e.g. `contact_123`).

    You never send the full stored contact object (with `id`, `object`,
    `addressStatus`, `createdAt`, etc.) here — that shape is only ever returned in
    responses.
    """

    description: str
    """An optional string describing this resource.

    Will be visible in the API and the dashboard.
    """

    metadata: Dict[str, object]
    """See the section on Metadata."""

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


To: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam, str]
