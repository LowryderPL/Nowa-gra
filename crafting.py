# crafting.py – FIROS: Magic & Magic (rozszerzony system rzemiosła)

import random

class Recipe:
    def __init__(self, name, ingredients, result, level_required=1, rarity="zwykły", success_rate=100):
        self.name = name
        self.ingredients = ingredients  # Lista składników
        self.result = result  # Nazwa przedmiotu wynikowego
        self.level_required = level_required
        self.rarity = rarity
        self.success_rate = success_rate  # Szansa na powodzenie w %

    def __repr__(self):
        return f"{self.name} → {self.result} ({self.rarity}, Poziom {self.level_required})"


class CraftingSystem:
    def __init__(self):
        self.recipes = self.load_recipes()
        self.crafted_items = []

    def load_recipes(self):
        return [
            Recipe("Stwórz Żelazny Miecz", ["żelazo", "drewno"], "Żelazny Miecz", 1, "zwykły", 95),
            Recipe("Stwórz Magiczną Laskę", ["kryształ many", "stare drewno"], "Magiczna Laska", 3, "rzadki", 85),
            Recipe("Stwórz Elfi Napierśnik", ["skóra elfa", "srebro"], "Elfi Napierśnik", 5, "epicki", 75),
            Recipe("Rytualny Miecz Cienia", ["czarna stal", "serce demona", "runiczny pył"], "Miecz Cienia", 10, "legendarny", 60),
        ]

    def craft(self, inventory, ingredients, player_level=1):
        for recipe in self.recipes:
            if set(recipe.ingredients) <= set(ingredients):
                if player_level < recipe.level_required:
                    return f"❌ Potrzebujesz poziomu {recipe.level_required}, by stworzyć {recipe.result}."
                if random.randint(1, 100) <= recipe.success_rate:
                    self.crafted_items.append(recipe.result)
                    for i in recipe.ingredients:
                        if i in inventory:
                            inventory.remove(i)
                    return f"🛠️ Sukces! Stworzono: {recipe.result} ({recipe.rarity})"
                else:
                    return f"💥 Tworzenie {recipe.result} nie powiodło się."
        return "❌ Nie znaleziono pasującej receptury."

    def show_recipes(self):
        return "\n".join([str(r) for r in self.recipes])

    def show_crafted_items(self):
        return "\n".join([f"- {item}" for item in self.crafted_items]) if self.crafted_items else "🔧 Brak stworzonego ekwipunku."


# Test lokalny
if __name__ == "__main__":
    crafting = CraftingSystem()
    inventory = ["żelazo", "drewno", "kryształ many", "stare drewno"]
    print(crafting.show_recipes())
    print(crafting.craft(inventory, ["żelazo", "drewno"], player_level=2))
    print(crafting.craft(inventory, ["kryształ many", "stare drewno"], player_level=2))
    print("🎒 Twój nowy ekwipunek:")
    print(crafting.show_crafted_items())
