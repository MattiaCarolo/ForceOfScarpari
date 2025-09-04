import flet as ft
from CardBrowser.Browser import card_browser
from DeckBuilder.Deck import deck_placeholder

# -------------------------------------------------
# 1) Landing page
# -------------------------------------------------
def landing_page(page: ft.Page):
    page.clean()

    page.title = "Force of Will – Main Menu"
    page.window_width, page.page_height = 400, 300

    def go_browser(e):
        page.clean()
        card_browser(page)

    def go_deck(e):
        page.clean()
        deck_placeholder(page)

    page.add(
        ft.Column(
            [
                ft.Text("Force of Will Tools", size=28, weight="bold"),
                ft.ElevatedButton("Card Browser", on_click=go_browser, width=200),
                ft.ElevatedButton("Deck Builder", on_click=go_deck,  width=200),
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
            spacing=20,
        )
    )