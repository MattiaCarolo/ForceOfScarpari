import flet as ft
import json
from pathlib import Path

def card_browser(page: ft.Page):
    CARDS = json.loads(Path("data/cards.json").read_text())

    def search(term: str):
        term = term.lower()
        return [c for c in CARDS if term in c["name"].lower()]

    # widgets ------------------------------------------------------------
    page.title = "Card Browser"
    page.window_width, page.window_height = 1100, 700

    # detail panel -------------------------------------------------------
    search_box = ft.TextField(label="Search cards…", expand=True)
    card_list  = ft.ListView(expand=True, spacing=6)

    img      = ft.Image(src="", width=300, height=430, fit="cover")
    name_lbl = ft.Text("", size=20, weight="bold")
    desc_box = ft.Markdown("", selectable=True, extension_set="gitHubWeb")
    detail   = ft.Column([name_lbl, img, desc_box], expand=True, scroll="auto")

    # business logic ----------------------------------------------------
    def show_detail(card):
        name_lbl.value = card["name"]
        img.src        = f"https://fowtcg.com/storage/images/{card['id']}.png"
        desc_box.value = (
            f"**Type:** {', '.join(card['type'])}  \n"
            f"**Cost:** {card.get('cost','—')}  \n"
            f"**Rarity:** {card.get('rarity','—')}  \n"
            f"**ATK / DEF:** {card.get('ATK', '—')} / {card.get('DEF', '—')}  \n\n"
            f"{card.get('abilities', [''])[0]}"
        )
        page.update()

    def refresh():
        term = search_box.value.lower()
        hits = search(term)
        card_list.controls = [
            ft.ListTile(
                title=ft.Text(c["name"], weight="bold"),
                subtitle=ft.Text(f"{c['type']} | {c.get('cost','—')} | {c['rarity']}"),
                leading=ft.Text(c["id"], width=80),
                dense=True,
                on_click=lambda e, card=c: show_detail(card)
            )
            for c in hits
        ]
        page.update()

    search_box.on_change = lambda e: refresh()

    page.add(
        ft.Row([search_box]),
        ft.Row([card_list, ft.VerticalDivider(width=1), detail], expand=True)
    )
    refresh()