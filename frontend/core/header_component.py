from nicegui import ui, context


def is_active(path: str) -> bool:
    return context.client.page.path == path


def go_home():
    ui.navigate.to("/")


def go_table():
    ui.navigate.to("/table")


def header():
    with ui.header().classes(replace="row items-center p-2") as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props("flat color=white")
        ui.button("Home", on_click=go_home).classes("font-bold underline" if is_active("/") else "")
        ui.button("Table", on_click=go_table).classes("font-bold underline" if is_active("/table") else "")
    with ui.left_drawer().classes("bg-blue-100") as left_drawer:
        ui.label("Side menu")
