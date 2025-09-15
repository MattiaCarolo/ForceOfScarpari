
import flet as ft
from sidebar import Sidebar
from data_store import SimpleDataStore


class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.Colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.Icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
        )
        # Create a simple data store for the sidebar
        store = SimpleDataStore()
        self.sidebar = Sidebar(self, store)
        self._active_view: ft.Control = ft.Column(
            controls=[ft.Text("Active View")],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,  # Allow active view to expand and fill remaining space
        )
        # Set expand=True for the entire row to fill the page
        self.expand = True
        self.controls = [self.sidebar, self.toggle_nav_rail_button, self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        # Ensure the new view expands to fill available space
        if hasattr(view, 'expand'):
            view.expand = True
        self._active_view = view
        # Update the controls list to reflect the new active view
        self.controls = [self.sidebar, self.toggle_nav_rail_button, self._active_view]
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()
