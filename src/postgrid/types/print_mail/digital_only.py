# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DigitalOnly"]


class DigitalOnly(BaseModel):
    watermark: str
    """Text to be displayed as a watermark on the digital cheque."""
