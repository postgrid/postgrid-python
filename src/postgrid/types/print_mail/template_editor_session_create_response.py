# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TemplateEditorSessionCreateResponse", "Styles", "StylesCanvas", "StylesPanelText", "StylesSaveButton"]


class StylesCanvas(BaseModel):
    """Style overrides for the template editor canvas."""

    background_color: Optional[str] = FieldInfo(alias="backgroundColor", default=None)
    """The canvas background color."""


class StylesPanelText(BaseModel):
    """Style overrides for template editor panel text."""

    color: Optional[str] = None
    """The panel text color."""


class StylesSaveButton(BaseModel):
    """Style overrides for the template editor save button."""

    background_color: Optional[str] = FieldInfo(alias="backgroundColor", default=None)
    """The save button background color."""

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)
    """The save button text color."""


class Styles(BaseModel):
    """Style overrides for the template editor session."""

    canvas: Optional[StylesCanvas] = None
    """Style overrides for the template editor canvas."""

    panel_text: Optional[StylesPanelText] = FieldInfo(alias="panelText", default=None)
    """Style overrides for template editor panel text."""

    save_button: Optional[StylesSaveButton] = FieldInfo(alias="saveButton", default=None)
    """Style overrides for the template editor save button."""


class TemplateEditorSessionCreateResponse(BaseModel):
    id: str
    """A unique ID prefixed with `template_editor_session_`."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The UTC time at which this session was created."""

    live: bool
    """`true` if this is a live mode session else `false`."""

    object: Literal["template_editor_session"]
    """Always `template_editor_session`."""

    template: str
    """ID of the underlying template that this edits."""

    url: str
    """A URL that can be iframed or redirected to for editing the template."""

    back_url: Optional[str] = FieldInfo(alias="backURL", default=None)
    """The URL supplied when this editor session was created."""

    styles: Optional[Styles] = None
    """Style overrides for the template editor session."""

    title: Optional[str] = None
    """The title supplied when this editor session was created."""

    trackers: Union[Literal["all", "none"], List[str], None] = None
    """Controls which Trackers are displayed in the template editor session."""
