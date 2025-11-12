# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BankAccountDeleteResponse"]


class BankAccountDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with bank*account*"""

    deleted: Literal[True]

    object: Literal["bank_account"]
    """Always `bank_account`."""
