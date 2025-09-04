import flet as ft
from landing import landing_page

def top_bar(page: ft.Page, title: str):
    """Returns a Row that can be inserted at the top of any feature."""
    return ft.Row(
        [
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                tooltip="Back to menu",
                on_click=lambda e: landing_page(page)
            ),
            ft.Text(title, size=20, weight="bold")
        ],
        alignment="start"
    )