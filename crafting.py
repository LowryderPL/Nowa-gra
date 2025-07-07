# crafting.py — Pełny system rzemiosła FIROS (Zastępuje wszystko)

class Recipe:
    def __init__(self, name, materials, result, rarity="zwykły", level_required=1, allowed_classes=["All"]):
        self.name = name
        self.materials = materials
        self.result = result
        self.rarity = rarity
        self.level_required = level_required
        self.allowed_classes = allowed_classes


class CraftingSystem:
    def __init__(self):
        self.recipes = self.load_recipes()

    def load_recipes(self):
        return [
            Recipe(
                name="Mikstura Życia",
                materials=["Kwiat Życia", "Czerwony Grzyb"],
                result={"name": "Mikstura Życia", "slot": "Backpack", "level": 1, "rarity": "zwykły", "allowed_classes": ["All"]},
                rarity="zwykły",
                level_required=1
            ),
            Recipe(
                name="Zwój Ognia",
                materials=["Proch", "Kryształ Ognia"],
                result={"name": "Zwój Ognia", "slot": "Rune", "level": 2, "rarity": "rzadki", "allowed_classes": ["Mag"]}
            ),
            Recipe(
                name="Miecz Żelazny",
                materials=["Żelazo", "Drewno"],
                result={"name": "Miecz Żelazny", "slot": "Main Weapon", "level": 3, "rarity": "zwykły", "allowed_classes": ["Wojownik", "Rogue"]}
            ),
            Recipe(
                name="Zbroja Cienia",
                materials=["Skóra Cienia", "Tkanka Upiora"],
                result={"name": "Zbroja Cienia", "slot": "Torso", "level": 5, "rarity": "epicki", "allowed_classes": ["Rogue", "Mag"]},
                rarity="epicki",
                level_required=5
            )
        ]

    def list_recipes(self):
        return [f"{r.name} (lvl {r.level_required}) → {', '.join(r.materials)}" for r in self.recipes]

    def craft(self, selected_name, inventory, player_level, player_class):
        for recipe in self.recipes:
            if recipe.name == selected_name:
                # Sprawdź poziom i klasę
                if player_level < recipe.level_required:
                    return f"❌ Potrzebny poziom {recipe.level_required} do stworzenia {recipe.name}."

                if player_class not in recipe.allowed_classes and "All" not in recipe.allowed_classes:
                    return f"❌ Klasa {player_class} nie może stworzyć {recipe.name}."

                # Sprawdź materiały
                if all(any(item["name"] == mat for item in inventory) for mat in recipe.materials):
                    # Usuń materiały
                    for mat in recipe.materials:
                        for item in inventory:
                            if item["name"] == mat:
                                inventory.remove(item)
                                break
                    # Dodaj efekt
                    inventory.append(recipe.result)
                    return f"🛠 Stworzono {recipe.result['name']}!"
                else:
                    return f"❌ Brakuje materiałów do {recipe.name}."
        return "❌ Przepis nie znaleziony."

# Przykład użycia — tylko testowo:
if __name__ == "__main__":
    crafting = CraftingSystem()
    player_inventory = [
        {"name": "Kwiat Życia"}, {"name": "Czerwony Grzyb"}, {"name": "Żelazo"}, {"name": "Drewno"}
    ]
    print("🧾 Dostępne przepisy:")
    for r in crafting.list_recipes():
        print(" -", r)

    result = crafting.craft("Mikstura Życia", player_inventory, player_level=2, player_class="Mag")
    print(result)
