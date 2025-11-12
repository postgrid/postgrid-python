# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DigitalOnlyParam"]


class DigitalOnlyParam(TypedDict, total=False):
    watermark: Required[str]
    """Text to be displayed as a watermark on the digital cheque."""
