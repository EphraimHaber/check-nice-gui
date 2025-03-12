from nicegui import app, ui
from frontend.core import header


@ui.page("/about/{word}/{count}")
# @page_wrapper("/about/{word}/{count}")
def about_page(word: str = "?", count: int = 1):
    header()
    ui.label("about page!")
    ui.label(word * count)

    # NOTE dark mode will be persistent for each user across tabs and server restarts
    # ui.dark_mode().bind_value(app.storage.user, "dark_mode")
    # ui.checkbox("dark mode").bind_value(app.storage.user, "dark_mode")
