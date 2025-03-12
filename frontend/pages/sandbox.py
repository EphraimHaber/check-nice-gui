from nicegui import app, ui
from frontend.core import header
from typing import Callable, Optional

from nicegui.element import Element


@ui.page("/foo")
def foo():
    header()
    ui.label("foo page")
