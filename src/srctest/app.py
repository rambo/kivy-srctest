"""Kivy App"""
from typing import Any
import logging

from kivy.app import App  # type: ignore
from kivy.uix.button import Button  # type: ignore

LOGGER = logging.getLogger(__name__)


class SrcTestApp(App):  # type: ignore
    """Talk to GNSS receivers"""

    def build(self) -> Any:
        """Build the UI"""
        return Button(text="hello world")
