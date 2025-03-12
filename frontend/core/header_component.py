from nicegui import ui


# this function wraps the ui.page function
def header():
    with ui.header().classes(replace="row items-center") as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
            "flat color=white"
        )
        with ui.tabs() as tabs:
            ui.tab("A")
            ui.tab("B")
            ui.tab("C")
    with ui.left_drawer().classes("bg-blue-100") as left_drawer:
        ui.label("Side menu")
