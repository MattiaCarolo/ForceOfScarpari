import flet as ft
import json
from pathlib import Path
from time import sleep
import landing as ld
from app_layout import AppLayout

def load_landing(page: ft.Page):
    page.clean()
    ld.landing_page(page)

# class app layout -----------------------------------------------------
class ScarparApp(AppLayout):
    def __init__(self, page: ft.Page):
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Tournaments"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Judge System"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Deck Builder"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Active tournament")
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Force of Scarpari",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()

# main -----------------------------------------------------------------
def main(page: ft.Page):
    page.title = "FoW – Card Browser"
    page.window_width, page.window_height = 1100, 700
    prl = ft.Text("Wait for the completion...")

    # loading = ft.ProgressRing(width=16, height=16, stroke_width=2)
    # page.add(ft.Row(alignment="center",),
    #     ft.Column([ft.Text("Loading..."), loading], alignment="center",
    #                horizontal_alignment="center"),
    #     ft.Row([loading, prl]),
    #     )
    # for i in range(0, 50):
    #     loading.value = i * 0.2
    #     sleep(0.1)
    #     if i == 49:
    #         prl.value = "Finished!"
    #     page.update()
    # load_landing(page)
    # page.timer(1, load_landing)
    # 

    page.title = "Flet Trello clone"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_200
    app = ScarparApp(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)