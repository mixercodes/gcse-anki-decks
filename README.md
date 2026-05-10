# GCSE Revision — Anki Decks

**1288 flashcards** across six subjects.

---

## How to install

1. Install [CrowdAnki](https://ankiweb.net/shared/info/1788670778) in Anki (Tools → Add-ons → Get Add-ons → code `1788670778`)

**Option A — GitHub (easiest, gets updates automatically):**

2. In Anki: **File → CrowdAnki: Import from GitHub**
3. Enter: `https://github.com/mixercodes/gcse-anki-decks`

**Option B — Manual download:**

2. Download the latest release from the [Releases page](../../releases) and extract the zip
3. In Anki: **File → CrowdAnki: Import from disk**
4. Select the **repo root folder** (the one containing `gcse-anki-decks.json`) — do not select the file itself
5. Click OK

## How to update (without losing progress)

Repeat the same import — CrowdAnki matches cards by GUID, so your review history is preserved. New cards are added, edited cards are updated, nothing is duplicated.

---

## Contents

### English Literature — AQA (8702)
| Topic | Cards |
|---|---|
| Macbeth | 103 |
| Jekyll and Hyde | 39 |
| Lord of the Flies | 76 |
| Power and Conflict Poetry (all 15 poems) | 156 |

### English Language — AQA (8700)
| Topic | Cards |
|---|---|
| Poetry Terms | 31 |
| Analysis Terms | 42 |
| Paper 1 — Reading and Writing | 25 |
| Paper 2 — Non-fiction and Viewpoint | 26 |

### Geography — AQA (8035)
| Topic | Cards |
|---|---|
| Paper 1 — Physical Geography | 77 |
| Paper 2 — Human Geography | 59 |
| Paper 3 — Geographical Applications | 57 |

### Science — AQA Combined Science Trilogy (8464)
24 files covering all topics across Biology, Chemistry and Physics Papers 1 and 2.

### Computer Science — OCR (J277)
| Topic | Cards |
|---|---|
| Paper 1 — Computer Systems | 94 |
| Paper 2 — Computational Thinking, Algorithms and Programming | 81 |

### History — OCR (J411, History B — Schools History Project)
| Topic | Cards |
|---|---|
| Paper 1 — People's Health (c.1250–present) | 29 |
| Paper 1 — Norman Conquest (1065–1087) | 20 |
| Paper 2 — Life in Nazi Germany | 22 |
| Paper 2 — Making of America (1789–1900) | 26 |
| Paper 3 — Historical Environment: Framlingham Castle | 17 |

---

## Repo structure

```
src/                    ← source card files (.txt, tab-separated) — edit these
gcse-anki-decks.json    ← built CrowdAnki JSON — import the repo root folder into Anki
build.py                ← converts src/ → gcse-anki-decks.json
```

Cards live in `src/` as tab-separated `.txt` files. Run `python build.py` after editing to regenerate `gcse-anki-decks.json`. GitHub Actions also runs `build.py` automatically on every push to main.

See `CLAUDE.md` for the card format spec and guidance on adding cards with Claude Code.
