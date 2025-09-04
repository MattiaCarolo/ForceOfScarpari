import json
from pathlib import Path

DB = Path(__file__).with_suffix('').parent / "data" / "cards.json"

def load_cards() -> list[dict]:
    if not DB.exists():
        raise FileNotFoundError("Run fetch_cards.py first!")
    return json.loads(DB.read_text(encoding="utf-8"))

def search_cards(term: str) -> list[dict]:
    term = term.lower()
    return [c for c in load_cards() if term in c.get("name", "").lower()]