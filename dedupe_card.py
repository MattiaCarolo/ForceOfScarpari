#!/usr/bin/env python3
import json, pathlib

raw = json.loads(pathlib.Path("cards.json").read_text())

first_seen   = {}   # name → first card object
duplicates   = {}   # name → list of duplicate dicts

for cluster in raw["fow"]["clusters"]:
    for set_ in cluster["sets"]:
        for card in set_["cards"]:
            name = card["name"]
            card.setdefault("set_code", set_["code"])
            entry = {"id": card["id"],
                     "set_code": card["set_code"],
                     "rarity": card.get("rarity", "N/A")}
            if name not in first_seen:
                first_seen[name] = card
            else:
                duplicates.setdefault(name, []).append(entry)

# 1) Save the unique list
unique_list = list(first_seen.values())
pathlib.Path("cards_unique.json").write_text(
    json.dumps(unique_list, ensure_ascii=False, indent=2)
)

# 2) Save the duplicates report
pathlib.Path("duplicates_report.json").write_text(
    json.dumps(duplicates, ensure_ascii=False, indent=2)
)

print("Unique cards:", len(unique_list))
print("Names with duplicates:", len(duplicates))