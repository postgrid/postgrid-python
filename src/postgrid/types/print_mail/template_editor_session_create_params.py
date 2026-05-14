# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TemplateEditorSessionCreateParams", "Styles", "StylesCanvas", "StylesPanelText", "StylesSaveButton"]


class TemplateEditorSessionCreateParams(TypedDict, total=False):
    template: Required[str]
    """ID of the underlying template that this edits."""

    back_url: Annotated[str, PropertyInfo(alias="backURL")]
    """The URL supplied when this editor session was created."""

    styles: Styles
    """Style overrides for the template editor session."""

    title: str
    """The title supplied when this editor session was created."""

    trackers: Union[Literal["all", "none"], SequenceNotStr[str]]
    """Controls which Trackers are displayed in the template editor session."""


class StylesCanvas(TypedDict, total=False):
    """Style overrides for the template editor canvas."""

    background_color: Annotated[str, PropertyInfo(alias="backgroundColor")]
    """The canvas background color."""


class StylesPanelText(TypedDict, total=False):
    """Style overrides for template editor panel text."""

    color: str
    """The panel text color."""


class StylesSaveButton(TypedDict, total=False):
    """Style overrides for the template editor save button."""

    background_color: Annotated[str, PropertyInfo(alias="backgroundColor")]
    """The save button background color."""

    text_color: Annotated[str, PropertyInfo(alias="textColor")]
    """The save button text color."""


class Styles(TypedDict, total=False):
    """Style overrides for the template editor session."""

    canvas: StylesCanvas
    """Style overrides for the template editor canvas."""

    panel_text: Annotated[StylesPanelText, PropertyInfo(alias="panelText")]
    """Style overrides for template editor panel text."""

    save_button: Annotated[StylesSaveButton, PropertyInfo(alias="saveButton")]
    """Style overrides for the template editor save button."""
