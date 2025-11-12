# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OrderStatus"]

OrderStatus: TypeAlias = Literal["ready", "printing", "processed_for_delivery", "completed", "cancelled"]
