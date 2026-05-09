# GCSE Anki Decks — Claude Code Instructions

This repo stores GCSE revision flashcards for AQA English, Geography and Combined Science.

## Repo structure

```
src/                    ← card source files (.txt, tab-separated) — edit these
gcse-anki-decks.json    ← built CrowdAnki JSON — never edit manually
build.py                ← converts src/ → gcse-anki-decks.json
.github/                ← GitHub Actions: auto-builds on every push to main
```

## Workflow for adding/editing cards

1. Edit the relevant file in `src/`
2. Run `python build.py` to regenerate `gcse-anki-decks.json`
3. `git add . && git commit -m "description" && git push`

GitHub Actions runs `build.py` automatically on push and commits the updated JSON.

## Card file format

Every file in `src/` uses this exact header (do not change):
```
#separator:tab
#html:true
#notetype column:1
#deck column:4
```

Each card row: `Notetype[TAB]Field1[TAB]Field2[TAB]DeckPath`

- `Basic` → Field1 = Front question, Field2 = Back answer
- `Cloze` → Field1 = text with `{{c1::answer}}` gaps, Field2 = extra info (usually empty)
- Use actual tab characters between columns, not spaces
- No blank lines between cards

## Deck path conventions

```
English Lit::Paper 1::Macbeth
English Lit::Paper 1::Jekyll and Hyde
English Lit::Paper 2::Lord of the Flies
English Lit::Paper 2::Power and Conflict Poetry
English Lang::Poetry Terms
English Lang::Analysis Terms
English Lang::Paper 1
English Lang::Paper 2
Geography::Paper 1
Geography::Paper 2
Geography::Paper 3
Science::Biology::Paper 1::Cell Biology
Science::Biology::Paper 1::Organisation
Science::Biology::Paper 1::Infection and Response
Science::Biology::Paper 1::Bioenergetics
Science::Biology::Paper 2::Homeostasis and Response
Science::Biology::Paper 2::Inheritance, Variation and Evolution
Science::Biology::Paper 2::Ecology
Science::Chemistry::Paper 1::Atomic Structure and the Periodic Table
Science::Chemistry::Paper 1::Bonding, Structure and Properties
Science::Chemistry::Paper 1::Quantitative Chemistry
Science::Chemistry::Paper 1::Chemical Changes
Science::Chemistry::Paper 1::Energy Changes
Science::Chemistry::Paper 2::Rate of Reaction
Science::Chemistry::Paper 2::Organic Chemistry
Science::Chemistry::Paper 2::Chemical Analysis
Science::Chemistry::Paper 2::The Earth's Atmosphere
Science::Chemistry::Paper 2::Using Resources
Science::Physics::Paper 1::Energy
Science::Physics::Paper 1::Electricity
Science::Physics::Paper 1::Particle Model of Matter
Science::Physics::Paper 1::Atomic Structure
Science::Physics::Paper 2::Forces
Science::Physics::Paper 2::Waves
Science::Physics::Paper 2::Magnetism and Electromagnetism
Computer Science::Paper 1::Systems Architecture
Computer Science::Paper 1::Memory and Storage
Computer Science::Paper 1::Computer Networks
Computer Science::Paper 1::Network Security
Computer Science::Paper 1::Systems Software
Computer Science::Paper 1::Ethical Legal Cultural Environmental
Computer Science::Paper 2::Algorithms
Computer Science::Paper 2::Programming Fundamentals
Computer Science::Paper 2::Producing Robust Programs
Computer Science::Paper 2::Boolean Logic
Computer Science::Paper 2::Languages and IDEs
```

---

## How build.py works (CrowdAnki format)

`build.py` outputs `gcse-anki-decks.json` in CrowdAnki format. Key things to know if you ever need to modify it:

**Stable UUIDs** — the constants `ROOT_UUID`, `CONFIG_UUID`, `BASIC_MODEL_UUID`, `CLOZE_MODEL_UUID` at the top of `build.py` must never change. They are how Anki identifies the deck and note types across imports. Changing them makes Anki treat everything as new.

**Card GUIDs** — each note's GUID is derived from `field1 + deck_path` via MD5. This means:
- The same card always gets the same GUID (review history is preserved on re-import)
- Changing a card's front text or moving it to a different deck changes its GUID (Anki sees it as a new card)
- Duplicate front text within the same deck path will collide — avoid this

**Required CrowdAnki fields** — if you ever extend the schema, these fields are required by CrowdAnki and must be present:
- Deck: `__type__`, `crowdanki_uuid`, `deck_config_uuid`, `deck_configurations`, `note_models`, `media_files`, `children`, `notes`, `dyn`, `extendNew`, `extendRev`
- Note: `__type__`, `crowdanki_uuid`, `guid`, `note_model_uuid`, `fields`, `flags`, `tags`, `data`
- NoteModel: `__type__`, `crowdanki_uuid`, `name`, `type`, `flds` (each with `media: []`), `tmpls`, `css`, `req`
- DeckConfig: `__type__`, `crowdanki_uuid`, `name`, `new`, `rev`, `lapse` (as sub-objects, not flat keys)

**Importing into Anki** — select the repo root folder (not `gcse-anki-decks.json` directly). CrowdAnki reads `gcse-anki-decks.json` automatically from whichever folder you select.

---

## English Literature rules

### NEVER include:
- Specific act numbers (Act 1, Act 3) — say 'at the start', 'in the middle', 'at the end'
- Chapter numbers for LOTF or J&H — same rule
- Specific line numbers for poetry — use 'the opening line', 'the closing image', 'the volta'
- Specific years in cloze gaps — test the ERA not the year

### Always include:
- The word class when analysing (verb, noun, adjective)
- Connotations and effect, not just technique identification
- AO3 linked to the text's argument, not just as a bare fact

### Overview cards must always include:

**Macbeth:** Jacobean tragic play · King James I patron · Divine Right of Kings · Great Chain of Being · hamartia = ambition · tragic form always ends with restoration of order · Malcolm has final words

**Jekyll & Hyde:** Late Victorian · Victorian respectability · Darwin's evolution · epistolary form legitimises horror · Gothic form · 'man is not truly one, but truly two'

**Lord of the Flies:** Post-WWII · Golding as fabulist · 'diseased and fallen being' · 'man produces evil as a bee produces honey' · 'perfectibility of man unachievable' · Coral Island 'rotted to compost'

**Poetry overview:** Both poets + both poems named immediately · era not year · shared purpose · contrast · NO quotes in overview

---

## Git commit messages

Be specific:
- `Add 6 new Macbeth quotes — Duncan and Witches`
- `Add Kamikaze AO3 cards`
- `Fix typo in Remains card`

Not:
- `Update files`
- `Changes`

Always run `python build.py` before committing if any `src/` files were changed. This regenerates `gcse-anki-decks.json` which must be committed alongside the source changes.
