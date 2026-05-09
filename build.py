#!/usr/bin/env python3
"""
build.py — converts src/*.txt card files into a CrowdAnki JSON deck.
Run:    python build.py
Output: gcse-anki-decks.json  (repo root — named after the repo for GitHub import)
Import from disk:   Anki > CrowdAnki: Import from disk > select this repo's root folder
Import from GitHub: Anki > CrowdAnki: Import from GitHub > https://github.com/mixercodes/gcse-anki-decks
"""

import json
import os
import glob
import hashlib
import sys

SRC_DIR  = "src"
OUT_FILE = "gcse-anki-decks.json"  # must match repo name for GitHub import
DECK_NAME = "GCSE Revision"

# Stable UUIDs — NEVER change these or Anki will treat everything as new cards
ROOT_UUID        = "a1b2c3d4-0001-0001-0001-000000000001"
CONFIG_UUID      = "a1b2c3d4-0001-0001-0001-000000000002"
BASIC_MODEL_UUID = "a1b2c3d4-0001-0001-0001-000000000003"
CLOZE_MODEL_UUID = "a1b2c3d4-0001-0001-0001-000000000004"


def make_guid(text: str) -> str:
    """Stable 10-char GUID from card content — same text always gets same GUID."""
    h = hashlib.md5(text.encode("utf-8")).digest()
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    n = int.from_bytes(h[:8], "big")
    while n:
        result = chars[n % 62] + result
        n //= 62
    return result.zfill(10)[:10]


def make_child_uuid(path: str) -> str:
    """Stable UUID4-shaped string for a child deck, derived from its path."""
    h = hashlib.md5(path.encode("utf-8")).hexdigest()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def parse_txt_file(path: str):
    """Parse a tab-separated Anki txt file, return list of card dicts."""
    cards = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        notetype, field1, field2, deck_path = parts[0], parts[1], parts[2], parts[3]
        cards.append({
            "notetype": notetype.strip(),
            "field1": field1.strip(),
            "field2": field2.strip(),
            "deck_path": deck_path.strip(),
        })
    return cards


def make_note_models():
    """Return CrowdAnki note model definitions for Basic and Cloze."""
    basic = {
        "__type__": "NoteModel",
        "crowdanki_uuid": BASIC_MODEL_UUID,
        "name": "Basic (GCSE)",
        "type": 0,
        "sortf": 0,
        "tags": [],
        "css": ".card { font-family: Arial; font-size: 16px; text-align: left; padding: 10px; }",
        "flds": [
            {"name": "Front", "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Back",  "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
        ],
        "tmpls": [{
            "name": "Card 1",
            "ord": 0,
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Back}}",
            "bqfmt": "",
            "bafmt": "",
            "did": None,
        }],
        "req": [[0, "any", [0]]],
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "vers": [],
    }

    cloze = {
        "__type__": "NoteModel",
        "crowdanki_uuid": CLOZE_MODEL_UUID,
        "name": "Cloze (GCSE)",
        "type": 1,
        "sortf": 0,
        "tags": [],
        "css": ".card { font-family: Arial; font-size: 16px; text-align: left; padding: 10px; } .cloze { font-weight: bold; color: #0070c0; }",
        "flds": [
            {"name": "Text",  "ord": 0, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
            {"name": "Extra", "ord": 1, "sticky": False, "rtl": False, "font": "Arial", "size": 20, "media": []},
        ],
        "tmpls": [{
            "name": "Cloze",
            "ord": 0,
            "qfmt": "{{cloze:Text}}",
            "afmt": "{{cloze:Text}}<br><br>{{Extra}}",
            "bqfmt": "",
            "bafmt": "",
            "did": None,
        }],
        "req": [[0, "any", [0]]],
        "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
        "latexPost": "\\end{document}",
        "vers": [],
    }
    return basic, cloze


def make_deck_config():
    return {
        "__type__": "DeckConfig",
        "crowdanki_uuid": CONFIG_UUID,
        "name": "Default",
        "autoplay": True,
        "dyn": False,
        "replayq": True,
        "timer": 0,
        "new": {
            "delays": [1.0, 10.0],
            "ints": [1, 4, 7],
            "initialFactor": 2500,
            "perDay": 20,
            "bury": False,
            "separate": True,
            "order": 1,
        },
        "rev": {
            "perDay": 200,
            "ease4": 1.3,
            "fuzz": 0.05,
            "ivlFct": 1.0,
            "maxIvl": 36500,
            "bury": False,
        },
        "lapse": {
            "delays": [10.0],
            "leechFails": 8,
            "minInt": 1,
            "mult": 0.5,
        },
        "maxTaken": 60000,
    }


def build_deck_tree(all_cards):
    """
    Build nested CrowdAnki deck structure from deck_path strings like
    'English Lit::Paper 1::Macbeth'. Returns root deck dict.
    """
    basic_model, cloze_model = make_note_models()

    root = {
        "__type__": "Deck",
        "crowdanki_uuid": ROOT_UUID,
        "deck_config_uuid": CONFIG_UUID,
        "deck_configurations": [make_deck_config()],
        "desc": "GCSE Revision — English, Geography, Science (AQA). Generated by build.py.",
        "dyn": 0,
        "extendNew": 10,
        "extendRev": 50,
        "name": DECK_NAME,
        "children": [],
        "notes": [],
        "note_models": [basic_model, cloze_model],
        "media_files": [],
    }

    deck_map = {"": root}

    def get_or_create_deck(path: str):
        if path in deck_map:
            return deck_map[path]
        parts = path.split("::")
        parent_path = "::".join(parts[:-1])
        parent = get_or_create_deck(parent_path)
        new_deck = {
            "__type__": "Deck",
            "crowdanki_uuid": make_child_uuid(path),
            "deck_config_uuid": CONFIG_UUID,
            "desc": "",
            "dyn": 0,
            "extendNew": 0,
            "extendRev": 0,
            "name": parts[-1],
            "children": [],
            "notes": [],
        }
        parent["children"].append(new_deck)
        deck_map[path] = new_deck
        return new_deck

    for card in all_cards:
        deck = get_or_create_deck(card["deck_path"])
        guid = make_guid(card["field1"] + card["deck_path"])
        model_uuid = BASIC_MODEL_UUID if card["notetype"] == "Basic" else CLOZE_MODEL_UUID

        note = {
            "__type__": "Note",
            "crowdanki_uuid": guid,
            "guid": guid,
            "note_model_uuid": model_uuid,
            "fields": [card["field1"], card["field2"]],
            "flags": 0,
            "tags": [],
            "data": "",
        }
        deck["notes"].append(note)

    return root


def main():
    print("Building CrowdAnki deck from src/ files...")

    txt_files = sorted(glob.glob(os.path.join(SRC_DIR, "*.txt")))
    if not txt_files:
        print(f"ERROR: No .txt files found in {SRC_DIR}/")
        sys.exit(1)

    all_cards = []
    for path in txt_files:
        cards = parse_txt_file(path)
        all_cards.extend(cards)
        print(f"  {os.path.basename(path)}: {len(cards)} cards")

    print(f"\nTotal: {len(all_cards)} cards from {len(txt_files)} files")

    deck = build_deck_tree(all_cards)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {OUT_FILE}")
    print("Import from disk:   Anki > CrowdAnki: Import from disk > select this folder")
    print("Import from GitHub: Anki > CrowdAnki: Import from GitHub > https://github.com/mixercodes/gcse-anki-decks")


if __name__ == "__main__":
    main()
