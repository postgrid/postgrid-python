# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MailingListDeleteResponse"]


class MailingListDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with mailing*list*"""

    deleted: Literal[True]
