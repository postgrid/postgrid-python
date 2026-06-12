# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrderCancelParams"]


class OrderCancelParams(TypedDict, total=False):
    id: Required[str]

    expand: List[Literal["returnEnvelope"]]
    """
    Pass `expand[]=returnEnvelope` to expand the order's `returnEnvelope` field into
    the full return envelope object.
    """
