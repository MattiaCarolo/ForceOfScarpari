import flet as ft
from utils import top_bar

def deck_placeholder(page: ft.Page):
    page.title = "Deck Builder – coming soon"
    page.window_width, page.window_height = 400, 300
    page.add(
        top_bar(page, "Deck Builder"),
        ft.Column(
            [ft.Text("Deck Builder\n\nFeature coming soon!", size=24)],
            alignment="center",
            expand=True
        )
    )