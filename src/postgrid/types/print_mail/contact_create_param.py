# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from ..contact_create_with_first_name_param import ContactCreateWithFirstNameParam
from ..contact_create_with_company_name_param import ContactCreateWithCompanyNameParam

__all__ = ["ContactCreateParam"]

ContactCreateParam: TypeAlias = Union[ContactCreateWithFirstNameParam, ContactCreateWithCompanyNameParam]
