# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DigitalOnly", "Payee"]


class Payee(BaseModel):
    """The payee of the digital cheque.

    Supplying `payee.name` lets you create a
    digital-only cheque without a `to` contact — when it is provided, the
    top-level `to` field may be omitted.
    """

    name: str
    """The name of the payee."""


class DigitalOnly(BaseModel):
    watermark: str
    """Text to be displayed as a watermark on the digital cheque."""

    payee: Optional[Payee] = None
    """The payee of the digital cheque.

    Supplying `payee.name` lets you create a digital-only cheque without a `to`
    contact — when it is provided, the top-level `to` field may be omitted.
    """
