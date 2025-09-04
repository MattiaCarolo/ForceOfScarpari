#!/usr/bin/env python3
"""
Download the official Force of Will card list and save normalized JSON.
Run:  python fetch_cards.py
"""
import json
import pathlib
import httpx
from tqdm import tqdm

# Official source used by fowsim (change URL if it ever breaks)
URL = "https://www.fowtcg.com/cardlist/carddata.json"

OUT = pathlib.Path(__file__).with_suffix('').parent / "data" / "cards.json"
OUT.parent.mkdir(exist_ok=True)

def normalize(raw: dict) -> list[dict]:
    """
    Convert fowsim-style nested dict into a flat list of cards.
    raw["fow"]["clusters"][i]["sets"][j]["cards"][k] -> list[card]
    """
    cards = []
    for cluster in raw.get("fow", {}).get("clusters", []):
        for set_ in cluster.get("sets", []):
            for card in set_.get("cards", []):
                card.setdefault("set_code", set_.get("code"))
                card.setdefault("cluster", cluster.get("name"))
                cards.append(card)
    return cards

def main():
    print("Downloading card data…")
    with httpx.stream("GET", URL, follow_redirects=True) as resp:
        resp.raise_for_status()
        total = int(resp.headers.get("content-length", 0))
        with tqdm(total=total, unit="B", unit_scale=True) as bar:
            raw = b"".join(chunk for chunk in resp.iter_bytes() if bar.update(len(chunk)))
    data = json.loads(raw.decode("utf-8"))
    cards = normalize(data)

    print(f"Saving {len(cards)} cards → {OUT}")
    OUT.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Done.")

if __name__ == "__main__":
    main()