
class GrubobrzuchItem:
    def __init__(self, name, description, effect, rarity):
        self.name = name
        self.description = description
        self.effect = effect
        self.rarity = rarity

    def use(self, player):
        print(f"🎒 Używasz: {self.name}")
        print(self.effect)

# Lista przedmiotów Grubobrzucha
grubobrzuch_items = [
    GrubobrzuchItem(
        name="Rotten Apple of Grubobrzuch",
        description="Zgniłe jabłko, które śmierdzi jak jego kufel. +10 trucizna, -10 morale.",
        effect="🧪 Czujesz się dziwnie... i bardzo źle. HP -10, ale otrzymujesz odporność na truciznę przez 1h.",
        rarity="Common"
    ),
    GrubobrzuchItem(
        name="Gold Tankard of the Drunkard",
        description="Złoty kufel. Po każdym piwie daje RFN. Uwaga: uzależnia.",
        effect="🍺 RFN +20 za każde wypite piwo. Szansa na bełt 10%.",
        rarity="Uncommon"
    ),
    GrubobrzuchItem(
        name="Brothel Whip",
        description="Stylizowany bat burdelmamy. Tylko do użytku w tawernie.",
        effect="💥 Przestrasza NPC, zwiększa skuteczność perswazji u prostytutek.",
        rarity="Rare"
    ),
    GrubobrzuchItem(
        name="Grubobrzuch's Stained Saddle",
        description="Siodło poplamione przez Grubobrzucha. Ponoć szczęśliwe.",
        effect="🐎 Mount Speed +5% / Mount Instability +15%",
        rarity="Rare"
    ),
    GrubobrzuchItem(
        name="Mystic Flask",
        description="Flaszka z nieznanym płynem. Rzut kością decyduje o losie.",
        effect="🎲 Efekt losowy: +HP / -HP / Teleport / Trucizna / Regeneracja",
        rarity="Epic"
    ),
    GrubobrzuchItem(
        name="Hooker's Heels",
        description="Obcasy damy z tawerny. Dodają stylu, ale spowalniają.",
        effect="✨ +10 Charisma, -10 Speed",
        rarity="Uncommon"
    ),
    GrubobrzuchItem(
        name="Bloody Coin",
        description="Zakrwawiona moneta. Otwiera sekrety w lochach.",
        effect="🗝️ Pozwala wejść do zamkniętych korytarzy lub grobów",
        rarity="Legendary"
    ),
    GrubobrzuchItem(
        name="Stajenny Gag",
        description="Gag zrobiony z końskiego pasa. Cisza gwarantowana.",
        effect="🧼 Uniemożliwia NPC mówienie przez 5 tur",
        rarity="Rare"
    ),
    GrubobrzuchItem(
        name="Witch's Note",
        description="Notatka z zaklęciem. Rozpoczyna linię fabularną wiedźmy.",
        effect="📜 Otwiera nowe zadania fabularne i lokację: Witch’s Marsh",
        rarity="Epic"
    ),
    GrubobrzuchItem(
        name="Invisible Rope",
        description="Niewidzialna lina do krępowania mountów i złodziei.",
        effect="🕸️ Bonus do stealth i kontrolowania zwierząt",
        rarity="Rare"
    )
]
