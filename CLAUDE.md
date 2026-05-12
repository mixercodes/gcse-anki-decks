# GCSE Anki Decks — Claude Code Instructions

This repo stores GCSE revision flashcards for five subjects:

| Subject | Exam Board | Spec Code |
|---|---|---|
| English Literature | AQA | 8702 |
| English Language | AQA | 8700 |
| Geography | AQA | 8035 |
| Science (Biology, Chemistry, Physics) | AQA Combined Science Trilogy | 8464 |
| Computer Science | OCR | J277 |
| History | OCR | J411 (History B — Schools History Project) |

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
History::Paper 1::People's Health
History::Paper 1::Norman Conquest
History::Paper 2::Life in Nazi Germany
History::Paper 2::Making of America
History::Paper 3::Framlingham Castle
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

## Spec PDFs

Official specification PDFs are stored in `specs/`. Read these to verify content before adding or auditing cards.

| File | Subject |
|---|---|
| `specs/science-aqa-8464.pdf` | AQA Combined Science Trilogy |
| `specs/geography-aqa-8035.pdf` | AQA Geography |
| `specs/computer-science-ocr-j277.pdf` | OCR Computer Science J277 |
| `specs/history-ocr-j411.pdf` | OCR History B (Schools History Project) |

---

## Spec boundaries — what to include and exclude

When adding or auditing cards for any non-English subject, content must be scoped strictly to the specification listed. Do not include content from higher-tier qualifications (A-level, Separate Sciences) unless confirmed by the user.

### Science — AQA Combined Science Trilogy (8464)
Do not include content from AQA Separate Sciences (8461) or A-level. Known removals already made:
- Mitosis stage names (PMAT) — Combined Science only requires 3 unlabelled stages
- EPOC (excess post-exercise oxygen consumption) — not in Trilogy spec
- Autosomes — not required; sex chromosomes (XX/XY) are sufficient
- Crossing over and random assortment in meiosis — Separate Biology only
- Antiretroviral drug terminology — plain language sufficient for Trilogy
- Maxwell-Boltzmann distribution — Chemistry only, not Biology

### Geography — AQA (8035)
- Paper 1: Physical Geography (coasts, tectonic hazards, glacial landscapes, weather/climate)
- Paper 2: Human Geography (urban issues, economic world, resource management)
- Paper 3: Geographical Skills and Fieldwork (two fieldwork enquiries — one physical, one human)
- Sheringham is the coastal fieldwork case study and appears in BOTH Paper 1 (coastal processes content) and Paper 3 (fieldwork enquiry method/analysis). This is correct — do not move it.

### History — OCR J411 (History B — Schools History Project)
- Paper 1: Medicine Through Time (People's Health) + Norman Conquest
- Paper 2: Life in Nazi Germany + Making of America
- Paper 3: Historic Environment — Framlingham Castle
- Do not include content from other SHP units not listed above.

### Computer Science — OCR J277
- Paper 1: Computer Systems
- Paper 2: Computational Thinking, Algorithms and Programming
- Do not include A-level computing content (e.g. advanced data structures, compilers beyond the spec).

---

## Flashcard design principles

Based on cognitive science research (Wozniak's minimum information principle, Roediger's retrieval practice, Bjork's desirable difficulties).

### The atomic rule — one card, one thing

Every card tests exactly one retrievable fact. If the back has two independent facts, split it into two cards. If a student can score "half marks" on the back, the card is too broad.

- **Good:** "What does the pancreas produce when blood glucose is too high?" → "Insulin"
- **Bad:** "What does the pancreas produce in response to blood glucose changes?" → combines two separate facts (insulin + glucagon)

### Avoid list cards

Never create a card asking "Name all X" or "List the Y types of Z." Lists promote shallow pattern-matching, not recall.

- Instead: create one card per item in the list, each asking for that item in isolation
- Exception: short fixed sequences (e.g. colour-coded wires, order of the electromagnetic spectrum) where the list itself is the testable fact — use a Cloze with one gap per item

### Cloze vs Basic — when to use each

**Use Cloze for:**
- Equations and formulas (gap the formula itself or a variable)
- Definitions where the term-to-definition direction matters
- Sequences and processes where context helps recall
- Facts that sit naturally inside a sentence

**Use Basic for:**
- Explanations that require reasoning ("Why does…", "How does…", "What is the difference between…")
- Comparisons and multi-part structures (arteries vs veins vs capillaries)
- Worked examples and calculation walkthroughs
- Anything where a sentence answer is more meaningful than fill-in-the-blank

Avoid Cloze cards where the gaps are obvious from context — if the surrounding text makes the answer guessable without recalling it, the card isn't testing memory.

### Front must be unambiguous and standalone

The front of every card must be answerable without any context from the deck. Ask yourself: if this card appeared randomly six months from now, would the question make sense?

- Include the subject or concept in the question if needed: "In photosynthesis, what is the role of chlorophyll?" not just "What does chlorophyll do?"
- Avoid vague fronts: "What is the formula?" — formula for what?
- Avoid yes/no fronts: these don't generate active recall

### Science-specific rules

- **Equations:** create two cards — one with the formula as Cloze ("F = {{c1::BIL}}"), one as a worked example that requires substituting values. Knowing a formula and knowing how to apply it are different memories.
- **Processes and mechanisms:** use Basic cards with "Explain how…" or "Describe the sequence of…" — don't try to capture multi-step mechanisms in a single Cloze
- **Definitions:** the term → definition direction is usually more useful than definition → term. Test what students will need in the exam.
- **Higher Tier content:** always prefix with "[HT only]" on the front so it's visible before flipping

### Diagrams

SVG diagrams with numbered labels are strongly encouraged for Biology (cell structure, heart, gas exchange), Physics (circuits, forces), and Geography (landforms). A "label the diagram" card tests spatial recall that text cards cannot. Keep the question SVG and answer SVG identical except the answer adds the label text.

### When a card is too hard — rewrite it

If a card would consistently need "Hard" or "Again" ratings in Anki, the card design is wrong — not the student's memory. Signs a card needs rewriting:

- The back requires memorising more than ~15 words as a single chunk
- There are multiple unrelated facts on the back
- The front is ambiguous enough to have several valid answers
- The gap in a Cloze card is guessable from context

Rewrite by splitting, adding a qualifier to the front, or converting a Cloze to a more targeted Basic.

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
