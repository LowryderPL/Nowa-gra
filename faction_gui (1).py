
# faction_gui.py – rozszerzony wybór frakcji

class FactionGUI:
    def __init__(self, factions):
        self.factions = factions

    def show_factions(self):
        print("=== Wybierz swoją frakcję ===")
        for i, faction in enumerate(self.factions):
            print(f"{i + 1}. {faction['name']} – {faction['description']} (Bonus: {faction['bonus']})")

    def select_faction(self, choice):
        if 1 <= choice <= len(self.factions):
            faction = self.factions[choice - 1]
            print(f"Wybrano frakcję: {faction['name']} – {faction['description']}")
            return faction
        else:
            print("❌ Nieprawidłowy wybór")
            return None


# Przykład użycia
if __name__ == "__main__":
    factions = [
        {"name": "Zakon Cienia", "description": "Mistrzowie skrytobójstw i sabotażu.", "bonus": "+10% do uniku"},
        {"name": "Strażnicy Run", "description": "Obrońcy starożytnych tajemnic i zaklęć.", "bonus": "+5 many"},
        {"name": "Wędrowni Wojownicy", "description": "Zwyciężają siłą i honorem.", "bonus": "+10% do ataku"}
    ]
    gui = FactionGUI(factions)
    gui.show_factions()
    selected = gui.select_faction(int(input("Wybierz (1-3): ")))
