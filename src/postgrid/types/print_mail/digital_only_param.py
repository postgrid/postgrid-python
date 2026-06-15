# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DigitalOnlyParam", "Payee"]


class Payee(TypedDict, total=False):
    """The payee of the digital cheque.

    Supplying `payee.name` lets you create a
    digital-only cheque without a `to` contact — when it is provided, the
    top-level `to` field may be omitted.
    """

    name: Required[str]
    """The name of the payee."""


class DigitalOnlyParam(TypedDict, total=False):
    watermark: Required[str]
    """Text to be displayed as a watermark on the digital cheque."""

    payee: Payee
    """The payee of the digital cheque.

    Supplying `payee.name` lets you create a digital-only cheque without a `to`
    contact — when it is provided, the top-level `to` field may be omitted.
    """
