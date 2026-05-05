# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateEditorSessionDeleteResponse"]


class TemplateEditorSessionDeleteResponse(BaseModel):
    id: str
    """A unique ID prefixed with `template_editor_session_`."""

    deleted: Literal[True]

    object: Literal["template_editor_session"]
    """Always `template_editor_session`."""
