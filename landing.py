import flet as ft
from navigator import go_browser, go_deck

# -------------------------------------------------
# 1) Landing page
# -------------------------------------------------
def landing_page(page: ft.Page):
    page.clean()

    page.title = "Force of Will – Main Menu"
    page.window_width, page.page_height = 400, 300

    page.add(
        ft.Column(
            [
                ft.Text("Force of Will Tools", size=28, weight="bold"),
                ft.ElevatedButton("Card Browser", on_click=lambda e: go_browser(page), width=200),
                ft.ElevatedButton("Deck Builder", on_click=lambda e: go_deck(page),  width=200),
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
            spacing=20,
        )
    )