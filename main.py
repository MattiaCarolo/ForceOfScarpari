import flet as ft
import json
from pathlib import Path
import landing as ld

# main -----------------------------------------------------------------
def main(page: ft.Page):
    page.title = "FoW – Card Browser"
    page.window_width, page.window_height = 1100, 700

    ld.landing_page
    (page)

if __name__ == "__main__":
    ft.app(target=main)