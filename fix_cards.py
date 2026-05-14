"""
Comprehensive fix script for flashcard design rule violations.
Run from the repo root: py -3 fix_cards.py
"""

import os

SRC = os.path.join(os.path.dirname(__file__), "src")

def read(name):
    path = os.path.join(SRC, name)
    with open(path, encoding="utf-8") as f:
        return f.readlines()

def write(name, lines):
    path = os.path.join(SRC, name)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"  Wrote {name}")

def tab(*fields):
    return "\t".join(fields) + "\n"

# ─────────────────────────────────────────────
# 1. Lit P1 – Macbeth
# ─────────────────────────────────────────────
def fix_macbeth():
    name = "Lit P1 - Macbeth.txt"
    lines = read(name)
    out = []
    for line in lines:
        # Fix 1: "in Act 4 Scene 1" in question front
        line = line.replace(
            "What are the three apparitions' prophecies in Act 4 Scene 1?",
            "What are the three apparitions' prophecies in Macbeth?"
        )
        # Fix 2: "By Act 5" in ambition card back
        line = line.replace("By Act 5 his men serve him", "By the end, his men serve him")
        # Fix 3: clothing motif card – remove "(Act 1)" and "By Act 5:"
        line = line.replace(" (Act 1)", "")
        line = line.replace("By Act 5: ‘Now", "By the end: ‘Now")
        line = line.replace("By Act 5: 'Now", "By the end: 'Now")
        # Fix 4: skip the duplicate plant motif card (line 107)
        if "How does the plant motif develop through Macbeth?" in line:
            continue
        out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 2. Lit P2 – Lord of the Flies
# ─────────────────────────────────────────────
def fix_lotf():
    name = "Lit P2 - Lord of the Flies.txt"
    lines = read(name)
    out = []
    for line in lines:
        # Fix 1: remove chapter number from Simon card
        line = line.replace(
            "His death in Chapter 9 is the moral turning point",
            "His death near the middle of the novel is the moral turning point"
        )
        # Fix 2: delete the chapter-names list card
        if "What are the key events and their chapter names in Lord of the Flies?" in line:
            continue
        # Fix 3: delete the 12-item symbols list card
        if "What does each key symbol represent in LOTF according to your teacher?" in line:
            continue
        out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 3. Geography P1 – split list cards
# ─────────────────────────────────────────────
def fix_geo_p1():
    name = "Geography_P1.txt"
    lines = read(name)
    out = []

    erosion_cards = [
        tab("Basic", "What is hydraulic action (coastal erosion) and how does it erode cliffs?",
            "The force of waves compresses air into cracks in the cliff face. The pressure expands the crack until rock breaks off.",
            "Geography::Paper 1::Coasts"),
        tab("Basic", "What is abrasion (coastal erosion) and how does it erode cliffs?",
            "Rocks and sediment picked up by waves are hurled against the cliff face, wearing it away. Also called corrasion.",
            "Geography::Paper 1::Coasts"),
        tab("Basic", "What is attrition (coastal erosion) and what does it produce?",
            "Rocks and pebbles in the water collide with each other, breaking into smaller, rounder, smoother pieces. Produces sand and shingle.",
            "Geography::Paper 1::Coasts"),
        tab("Basic", "What is solution (coastal erosion) and which rock types does it affect?",
            "Acidic seawater chemically dissolves soluble rock such as chalk and limestone. Also called corrosion.",
            "Geography::Paper 1::Coasts"),
    ]

    glacial_landform_cards = [
        tab("Basic", "What is a U-shaped valley (glacial landform) and how does it form?",
            "A glacier erodes a V-shaped river valley downward and outward — widening and deepening it into a U-shape. Leaves steep sides and a flat floor after ice melts.",
            "Geography::Paper 1::Glaciation"),
        tab("Basic", "What is a corrie (cirque) and how does it form?",
            "A circular hollow in a mountainside. Snow collects and compresses into ice, eroding the hollow by plucking and abrasion. A rock lip forms at the front; a tarn may form when the ice melts.",
            "Geography::Paper 1::Glaciation"),
        tab("Basic", "What is an arête and how does it form?",
            "A knife-edge ridge formed when two corries erode back-to-back on either side of a mountain, leaving a narrow wall of rock between them.",
            "Geography::Paper 1::Glaciation"),
        tab("Basic", "What is a pyramidal peak and how does it form?",
            "A sharp mountain summit formed when three or more corries erode into the same mountain from different directions. Example: the Matterhorn.",
            "Geography::Paper 1::Glaciation"),
        tab("Basic", "What is a hanging valley and what does it create?",
            "A tributary valley left high above the main glacier valley floor after the main glacier erodes much deeper. Often has a waterfall at its junction with the main valley.",
            "Geography::Paper 1::Glaciation"),
        tab("Basic", "What is a ribbon lake and how does it form?",
            "A long narrow lake in a U-shaped valley, formed in an overdeepened rock basin eroded by a glacier where rock was softer. Often dammed by glacial deposits at the valley end.",
            "Geography::Paper 1::Glaciation"),
    ]

    trf_layer_cards = [
        tab("Basic", "What is the emergent layer of a tropical rainforest?",
            "The tallest trees (40–60m) with isolated, umbrella-shaped crowns. Receive the most sunlight but face the most wind and temperature variation.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "What is the canopy layer of a tropical rainforest?",
            "A dense continuous layer of overlapping tree crowns (25–40m). Blocks up to 80% of sunlight reaching lower layers. Contains the greatest biodiversity of animal life.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "What is the understorey layer of a tropical rainforest?",
            "Shrubs and small trees (10–25m) adapted to shade. Plants have large, dark leaves to capture limited light. Includes young trees waiting for a gap in the canopy above.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "What is the forest floor layer of a tropical rainforest?",
            "Very dark — little light penetrates here. Sparse vegetation. Dead matter decomposes rapidly in the heat and humidity, returning nutrients to the soil almost immediately.",
            "Geography::Paper 1::Living World - Rainforests"),
    ]

    plant_adapt_cards = [
        tab("Basic", "What are buttress roots and why do tropical rainforest trees have them?",
            "Large triangular root extensions that spread from the base of tall trees. They provide structural support in shallow, nutrient-poor soils where deep roots cannot anchor the tree.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "Why do tropical rainforest plant leaves have drip tips?",
            "Drip tips (pointed leaf ends) allow excess rainfall to run off quickly, preventing algae and moss from growing on the leaf surface and blocking sunlight.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "What is an epiphyte and why do they exist in the tropical rainforest?",
            "A plant that grows on another plant (e.g. a tree) to reach the light in the canopy, without rooting in the soil. Examples: orchids, bromeliads. They are not parasitic.",
            "Geography::Paper 1::Living World - Rainforests"),
        tab("Basic", "Why do tropical rainforest trees have shallow, wide root systems?",
            "Nutrients exist only in the top few centimetres of soil. Shallow roots spread widely to capture nutrients before heavy rainfall leaches them out of reach.",
            "Geography::Paper 1::Living World - Rainforests"),
    ]

    for line in lines:
        if "What are the four processes of coastal erosion?" in line:
            out.extend(erosion_cards)
        elif "What glacial landforms result from erosion?" in line:
            out.extend(glacial_landform_cards)
        elif "What are the four layers of a tropical rainforest?" in line:
            out.extend(trf_layer_cards)
        elif "How do plants adapt to the tropical rainforest?" in line:
            out.extend(plant_adapt_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 4. History – People's Health
# ─────────────────────────────────────────────
def fix_peoples_health():
    name = "History - Paper 1 - People's Health.txt"
    lines = read(name)

    aids_cloze = tab(
        "Cloze",
        "Five phases of UK response to AIDS: 1. Growing {{c1::awareness}} (1970s–1983): first deaths reported, Terrence Higgins Trust set up. "
        "2. Growing {{c2::alarm}} (1984–85): widespread fear and stigma. "
        "3. Growing {{c3::understanding}} (1986–87): clean needle programmes, Princess Diana shook hands with AIDS patients. "
        "4. Growing {{c4::acceptance}} (1988–95): Freddie Mercury concert raised £20 million for research. "
        "5. Growing {{c5::complacency}} (1996+): anti-retroviral drugs led many to believe AIDS was curable.",
        "",
        "History::Paper 1::People's Health"
    )

    out = []
    for line in lines:
        # Delete the industrial period improvements list (already covered by individual cloze cards)
        if "What key improvements to public health were made in the industrial period" in line:
            continue
        # Replace the five-phases list card with a Cloze
        elif "What were the five phases of society" in line:
            out.append(aids_cloze)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 5. Biology – Cell Biology
# ─────────────────────────────────────────────
def fix_cell_biology():
    name = "Science - Biology - Paper 1 - Cell Biology.txt"
    lines = read(name)

    specialised_cards = [
        tab("Basic", "What are the adaptations of the red blood cell and how do they relate to its function?",
            "<b>Function:</b> carry oxygen around the body.<br>"
            "<b>Adaptations:</b> biconcave disc shape → large surface area for O₂ absorption. No nucleus → more space for haemoglobin. Flexible membrane → can squeeze through narrow capillaries.",
            "Science::Biology::Paper 1::Cell Biology"),
        tab("Basic", "What are the adaptations of the sperm cell and how do they relate to its function?",
            "<b>Function:</b> reach and fertilise an egg cell.<br>"
            "<b>Adaptations:</b> long flagellum (tail) for motility. Many mitochondria → supply ATP for swimming. Acrosome at the head contains enzymes to digest through the egg membrane.",
            "Science::Biology::Paper 1::Cell Biology"),
        tab("Basic", "What are the adaptations of the nerve cell (neurone) and how do they relate to its function?",
            "<b>Function:</b> transmit electrical impulses rapidly over long distances.<br>"
            "<b>Adaptations:</b> very long → signals travel far without a relay. Myelin sheath insulates the axon and speeds up transmission. Many synaptic terminals connect to other neurones.",
            "Science::Biology::Paper 1::Cell Biology"),
        tab("Basic", "What are the adaptations of the root hair cell and how do they relate to its function?",
            "<b>Function:</b> absorb water and mineral ions from the soil.<br>"
            "<b>Adaptations:</b> long hair-like projection → greatly increased surface area for absorption. Large permanent vacuole → maintains osmotic gradient to draw in water.",
            "Science::Biology::Paper 1::Cell Biology"),
        tab("Basic", "What are the adaptations of the muscle cell and how do they relate to its function?",
            "<b>Function:</b> contract to generate movement.<br>"
            "<b>Adaptations:</b> many mitochondria → supply ATP for contraction. Contains the proteins actin and myosin, which slide past each other to shorten the cell.",
            "Science::Biology::Paper 1::Cell Biology"),
    ]

    out = []
    for line in lines:
        if "Describe the adaptations of specialised cells: red blood cell" in line:
            out.extend(specialised_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 6. Biology – Homeostasis
# ─────────────────────────────────────────────
def fix_homeostasis():
    name = "Science - Biology - Paper 2 - Homeostasis and Response.txt"
    lines = read(name)

    contraception_cards = [
        tab("Basic", "How do hormonal contraceptives prevent pregnancy and what are the examples?",
            "All hormonal methods work by inhibiting FSH and LH production — preventing egg maturation (ovulation).<br>"
            "<b>Examples:</b> combined pill (oestrogen + progesterone, daily); progesterone-only pill (mini pill — also thickens cervical mucus); "
            "injection/implant/patch/hormonal IUD (Mirena) — all slow-release progesterone, long-acting.",
            "Science::Biology::Paper 2::Homeostasis and Response"),
        tab("Basic", "How do barrier contraceptives work and what are the examples?",
            "Barrier methods physically prevent sperm from reaching the egg.<br>"
            "<b>Male condom:</b> rolled over the penis. <b>Female condom:</b> inserted into the vagina. <b>Diaphragm:</b> dome-shaped cap covering the cervix, used with spermicide.<br>"
            "<b>Key advantage of condoms:</b> the only contraceptive that also protects against STIs.",
            "Science::Biology::Paper 2::Homeostasis and Response"),
        tab("Basic", "How does the copper IUD work as a non-hormonal contraceptive?",
            "The copper IUD is inserted into the uterus by a clinician. Copper is toxic to sperm — reduces their motility and ability to fertilise an egg. "
            "It may also prevent implantation of a fertilised egg. Non-hormonal, long-lasting (up to 10 years), and immediately reversible.",
            "Science::Biology::Paper 2::Homeostasis and Response"),
    ]

    out = []
    for line in lines:
        if "What are the methods of contraception and how do they work?" in line:
            out.extend(contraception_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 7. Biology – Ecology
# ─────────────────────────────────────────────
def fix_ecology():
    name = "Science - Biology - Paper 2 - Ecology.txt"
    lines = read(name)

    human_impact_cards = [
        tab("Basic", "How does deforestation affect ecosystems?",
            "Trees are the main store of carbon on land. Cutting them down releases stored CO₂ (contributing to climate change) and removes the CO₂ sink. "
            "It also destroys habitats, reduces biodiversity, and disrupts the water cycle — less water is transpired, changing local rainfall patterns.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "How does water pollution from fertilisers cause eutrophication?",
            "Fertiliser runoff adds excess nitrates and phosphates to water. This causes algal bloom — algae block light → plants below die → decomposers break down dead plants → decomposers use up oxygen → aquatic life (fish etc.) suffocates and dies.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "How does peat bog destruction contribute to climate change?",
            "Peat bogs store huge amounts of carbon as partially decomposed organic matter. Draining or burning peat for fuel or compost releases this stored CO₂ into the atmosphere, accelerating climate change.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "How do overfishing and intensive farming reduce biodiversity?",
            "<b>Overfishing:</b> removes fish faster than populations can recover — can collapse entire food chains. "
            "<b>Intensive farming:</b> monocultures remove habitat variety. Pesticides kill non-target insects (including pollinators). Hedgerow removal destroys corridors between habitats.",
            "Science::Biology::Paper 2::Ecology"),
    ]

    biodiversity_cards = [
        tab("Basic", "What are breeding programmes and how do they protect biodiversity?",
            "Captive breeding programmes in zoos breed endangered species in controlled conditions, maintaining genetic diversity. Animals may be reintroduced to the wild once habitats are restored or threats are reduced. Example: giant panda, Arabian oryx.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "What is a seed bank and why is it important for biodiversity?",
            "A facility that stores seeds of plant species at very low temperatures to preserve genetic diversity. If a species becomes extinct in the wild, its seeds can be used to reintroduce it. The Svalbard Global Seed Vault is a key example.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "How do nature reserves and marine protected areas conserve biodiversity?",
            "They protect habitats from development, pollution and human disturbance. Species can live and breed without disruption. Buffer zones reduce edge effects. Marine protected areas ban or limit fishing in critical habitats such as coral reefs and spawning grounds.",
            "Science::Biology::Paper 2::Ecology"),
        tab("Basic", "How do international agreements protect biodiversity?",
            "CITES (Convention on International Trade in Endangered Species) bans or controls trade in threatened species and their products. The Rio Convention and other agreements commit countries to protecting habitats and reducing pollution. Effectiveness depends on national enforcement.",
            "Science::Biology::Paper 2::Ecology"),
    ]

    out = []
    for line in lines:
        if "What are the effects of human activities on ecosystems?" in line:
            out.extend(human_impact_cards)
        elif "What methods are used to protect biodiversity?" in line:
            out.extend(biodiversity_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 8. Biology – Infection and Response
# ─────────────────────────────────────────────
def fix_infection():
    name = "Science - Biology - Paper 1 - Infection and Response.txt"
    lines = read(name)

    pathogen_cloze = tab(
        "Cloze",
        "The four types of pathogen: {{c1::bacteria}} (e.g. Salmonella, gonorrhoea — produce toxins), "
        "{{c2::viruses}} (e.g. measles, HIV, TMV — replicate inside cells), "
        "{{c3::fungi}} (e.g. rose black spot), "
        "{{c4::protists}} (e.g. malaria — spread by mosquito vector).",
        "",
        "Science::Biology::Paper 1::Infection and Response"
    )

    nonspecific_cards = [
        tab("Basic", "How does the skin act as a non-specific defence against infection?",
            "The skin forms a continuous physical barrier that prevents pathogens from entering the body. It also produces antimicrobial secretions (including sebum from sebaceous glands) that kill microorganisms on the surface.",
            "Science::Biology::Paper 1::Infection and Response"),
        tab("Basic", "How does the respiratory tract defend against pathogens?",
            "The nose contains hairs and mucus that trap pathogens in inhaled air. The trachea and bronchi are lined with ciliated epithelial cells — cilia sweep mucus (and trapped pathogens) upward to the throat, where it is swallowed and destroyed by stomach acid.",
            "Science::Biology::Paper 1::Infection and Response"),
        tab("Basic", "How does the stomach defend against pathogens?",
            "The stomach produces hydrochloric acid (pH 2), which kills most pathogens that are swallowed in food, drink, or mucus swept from the respiratory tract.",
            "Science::Biology::Paper 1::Infection and Response"),
    ]

    out = []
    for line in lines:
        if "What are the four types of pathogen?" in line:
            out.append(pathogen_cloze)
        elif "What are the non-specific defences of the human body?" in line:
            out.extend(nonspecific_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 9. Physics – Energy
# ─────────────────────────────────────────────
def fix_energy():
    name = "Science - Physics - Paper 1 - Energy.txt"
    lines = read(name)

    stores_cloze = tab(
        "Cloze",
        "The eight energy stores: {{c1::kinetic}}, {{c2::gravitational potential}}, {{c3::elastic potential}}, "
        "{{c4::chemical}}, {{c5::thermal}}, {{c6::magnetic}}, {{c7::electrostatic}}, {{c8::nuclear}}. "
        "Energy is conserved — it is {{c9::transferred}} between stores, never created or destroyed.",
        "",
        "Science::Physics::Paper 1::Energy"
    )

    transfers_cloze = tab(
        "Cloze",
        "Energy is transferred by four pathways: {{c1::mechanically}} (by forces doing work), "
        "{{c2::electrically}} (by electric current), "
        "{{c3::by heating}} (from hot to cold), "
        "{{c4::by radiation}} (e.g. light, infrared, sound waves).",
        "",
        "Science::Physics::Paper 1::Energy"
    )

    energy_resource_cards = [
        tab("Basic", "What are the advantages and disadvantages of fossil fuels as an energy resource?",
            "<b>Advantages:</b> reliable baseload power, high energy density, existing infrastructure worldwide.<br>"
            "<b>Disadvantages:</b> finite (non-renewable), burning releases CO₂ (climate change) and SO₂ (acid rain), "
            "coal mining damages landscapes.",
            "Science::Physics::Paper 1::Energy"),
        tab("Basic", "What are the advantages and disadvantages of nuclear power?",
            "<b>Advantages:</b> very reliable, no CO₂ during generation, very high energy density (small fuel needed).<br>"
            "<b>Disadvantages:</b> radioactive waste (difficult to dispose of safely), very expensive to build and decommission, risk of accidents (Chernobyl, Fukushima).",
            "Science::Physics::Paper 1::Energy"),
        tab("Basic", "What are the advantages and disadvantages of wind energy?",
            "<b>Advantages:</b> renewable, no CO₂ during operation, cheap to run once built.<br>"
            "<b>Disadvantages:</b> intermittent (only works when wind blows), visual and noise impact, potential harm to birds. Offshore is more reliable but more expensive.",
            "Science::Physics::Paper 1::Energy"),
        tab("Basic", "What are the advantages and disadvantages of solar energy?",
            "<b>Advantages:</b> renewable, no CO₂ or pollution during operation, no moving parts (low maintenance).<br>"
            "<b>Disadvantages:</b> intermittent (only works in daylight/clear weather), large land area required for solar farms, manufacturing panels has environmental cost.",
            "Science::Physics::Paper 1::Energy"),
        tab("Basic", "What are the advantages and disadvantages of hydroelectric power?",
            "<b>Advantages:</b> reliable and renewable, no CO₂ during operation, can store energy (pump water up at off-peak times).<br>"
            "<b>Disadvantages:</b> requires flooding valleys — destroys habitats and displaces communities. Limited to suitable geography.",
            "Science::Physics::Paper 1::Energy"),
        tab("Basic", "What are the advantages and disadvantages of biofuels?",
            "<b>Advantages:</b> renewable, theoretically carbon-neutral (CO₂ released equals CO₂ absorbed while growing).<br>"
            "<b>Disadvantages:</b> land used for fuel crops competes with food production. Growing and processing biofuels still has significant carbon footprint in practice.",
            "Science::Physics::Paper 1::Energy"),
    ]

    out = []
    for line in lines:
        if "What are the main energy stores and transfers?" in line:
            out.append(stores_cloze)
            out.append(transfers_cloze)
        elif "How do you compare different energy resources? What are the advantages of each?" in line:
            out.extend(energy_resource_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# 10. Chemistry – Rate of Reaction
# ─────────────────────────────────────────────
def fix_rate_of_reaction():
    name = "Science - Chemistry - Paper 2 - Rate of Reaction.txt"
    lines = read(name)

    factor_cards = [
        tab("Basic", "How does concentration affect the rate of a chemical reaction?",
            "Higher concentration means more particles per unit volume — more frequent collisions between reactant particles — "
            "more successful collisions per second — faster rate of reaction.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
        tab("Basic", "How does temperature affect the rate of a chemical reaction?",
            "Higher temperature gives particles more kinetic energy — they move faster — more frequent AND more energetic collisions. "
            "A greater proportion of collisions have energy equal to or greater than the activation energy — rate increases significantly. "
            "A 10°C rise roughly doubles the rate.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
        tab("Basic", "How does surface area affect the rate of a chemical reaction?",
            "Increasing surface area exposes more particles of the solid reactant — more collisions per second with the other reactant — "
            "faster rate. Example: powdered marble reacts faster with HCl than marble chips of the same mass.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
        tab("Basic", "How does a catalyst affect the rate of a chemical reaction?",
            "A catalyst provides an alternative reaction pathway with a lower activation energy — a greater proportion of collisions now have enough energy to react — "
            "faster rate. The catalyst is not used up and does not change the products or the overall energy change.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
    ]

    method_cards = [
        tab("Basic", "How do you measure rate of reaction using the loss of mass method?",
            "Place the flask on a balance. As a gas product escapes, record mass at regular intervals. Plot mass vs time — "
            "gradient = rate. The curve levels off when one reactant is used up. Works when the reaction produces a gas "
            "(e.g. CaCO₃ + HCl → CO₂ escapes).",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
        tab("Basic", "How do you measure rate of reaction using the gas volume method?",
            "Connect the flask to a gas syringe or inverted measuring cylinder over water. Record the volume of gas produced at regular intervals. "
            "Plot volume vs time — gradient = rate. Example: H₂O₂ decomposition → O₂ collected. More precise than loss of mass for small volumes.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
        tab("Basic", "How do you measure rate of reaction using the colour change / turbidity method?",
            "Draw a cross on paper and place the flask over it. Add reactants and time how long until the cross disappears "
            "(obscured by a precipitate forming in the flask). Rate ∝ 1/time. "
            "Used for Na₂S₂O₃ + HCl → yellow sulphur precipitate.",
            "Science::Chemistry::Paper 2::Rate of Reaction"),
    ]

    out = []
    for line in lines:
        if "What four factors affect the rate of reaction and why?" in line:
            out.extend(factor_cards)
        elif "What are the three methods of measuring the rate of a reaction?" in line:
            out.extend(method_cards)
        else:
            out.append(line)
    write(name, out)

# ─────────────────────────────────────────────
# Run all fixes
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Running all card fixes...")
    fix_macbeth()
    fix_lotf()
    fix_geo_p1()
    fix_peoples_health()
    fix_cell_biology()
    fix_homeostasis()
    fix_ecology()
    fix_infection()
    fix_energy()
    fix_rate_of_reaction()
    print("Done.")
