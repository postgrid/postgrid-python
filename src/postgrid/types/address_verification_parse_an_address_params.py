# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressVerificationParseAnAddressParams"]


class AddressVerificationParseAnAddressParams(TypedDict, total=False):
    address: Required[str]
    """The address you want to verify, written on a single line."""
