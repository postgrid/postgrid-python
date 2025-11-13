# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SelfMailerRetrieveURLResponse"]


class SelfMailerRetrieveURLResponse(BaseModel):
    id: str
    """A unique ID prefixed with self*mailer*"""

    object: str

    url: str
    """A signed URL linking to the order preview PDF.

    The link remains valid for 15 minutes from the time of the API call.
    """
