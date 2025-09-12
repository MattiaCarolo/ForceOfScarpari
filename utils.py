import flet as ft
from navigator import go_landing

def top_bar(page: ft.Page, title: str):
    """Returns a Row that can be inserted at the top of any feature."""
    return ft.Row(
        [
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                tooltip="Back to menu",
                on_click=lambda e: go_landing(page)
            ),
            ft.Text(title, size=20, weight="bold")
        ],
        alignment="start"
    )