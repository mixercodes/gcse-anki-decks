# GCSE Revision — Anki Decks

**734 flashcards** across English Literature, English Language, Geography and Science (AQA).

---

## How to install

1. Install the [CrowdAnki add-on](https://ankiweb.net/shared/info/1788670778) in Anki
2. Download the latest release from the [Releases page](../../releases)
3. Extract the zip
4. In Anki: **File → CrowdAnki: Import from disk** → select the `deck/` folder
5. Click OK

## How to update (without losing progress)

Same process — CrowdAnki matches notes by GUID, so existing cards keep their review history. New cards are added, changed cards are updated, nothing is duplicated.

---

## Contents

### English Literature
| File | Cards |
|---|---|
| Macbeth | 93 |
| Jekyll and Hyde | 37 |
| Lord of the Flies | 74 |
| Power and Conflict Poetry (all 15 poems) | 146 |

### English Language
| File | Cards |
|---|---|
| Poetry Terms | 31 |
| Analysis Terms | 40 |
| Paper 1 — Reading and Writing | 21 |
| Paper 2 — Non-fiction and Viewpoint | 18 |

### Geography (AQA 8035)
| File | Cards |
|---|---|
| Paper 1 | 50 |
| Paper 2 | 31 |
| Paper 3 | 27 |

### Science (AQA Combined Science Trilogy 8464)
24 files covering all topics across Biology, Chemistry and Physics Papers 1 and 2.

---

## Repo structure

```
src/        ← source card files (.txt) — human-readable, easy to edit
deck/       ← built CrowdAnki JSON — import this into Anki
build.py    ← converts src/ → deck/
```

Cards live in `src/` as tab-separated `.txt` files. `build.py` converts them into the CrowdAnki JSON format. GitHub Actions runs `build.py` automatically on every push.

See `CLAUDE.md` for how to add cards using Claude Code.
