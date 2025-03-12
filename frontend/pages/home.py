from nicegui import app, ui
from frontend.core import header


@ui.page("/")
def home_page():
    header()
    # NOTE dark mode will be persistent for each user across tabs and server restarts
    ui.dark_mode().bind_value(app.storage.user, "dark_mode")
    ui.checkbox("dark mode").bind_value(app.storage.user, "dark_mode")
