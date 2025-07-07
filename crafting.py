# crafting.py – logika rzemiosła dla Świata Firos: Magic & Magic
# Obsługuje przepisy, tworzenie przedmiotów, rarity, trudność i tooltips

from rarity import get_rarity_for_result
from tooltips import generate_tooltip
import random


class Recipe:
    def __init__(self, name, materials, result, difficulty="normal"):
        self.name = name
        self.materials = materials  # Lista nazw materiałów (str)
        self.result = result  # Nazwa przedmiotu wynikowego
        self.difficulty = difficulty  # np. "easy", "normal", "hard"


class CraftingSystem:
    def __init__(self, all_recipes):
        self.recipes = all_recipes

    def match_recipe(self, materials_input):
        """
        Porównuje podane materiały z receptami i zwraca pasującą.
        """
        input_set = set([m.lower().strip() for m in materials_input])
        for recipe in self.recipes:
            if set(recipe.materials) == input_set:
                return recipe
        return None

    def craft(self, materials_input):
        """
        Tworzy przedmiot na podstawie podanych materiałów.
        """
        recipe = self.match_recipe(materials_input)
        if not recipe:
            return "❌ Nie znaleziono pasującej receptury."

        # Losowy wynik na podstawie trudności
        success_chance = {
            "easy": 0.95,
            "normal": 0.80,
            "hard": 0.60,
            "legendary": 0.40
        }.get(recipe.difficulty, 0.75)

        if random.random() > success_chance:
            return "💥 Tworzenie nie powiodło się..."

        # Ustal rarity
        rarity = get_rarity_for_result(recipe.result)

        # Generuj tooltip
        tooltip = generate_tooltip(recipe.result, rarity)

        return f"✅ Stworzono: **{recipe.result}**\n🎖️ Rzadkość: {rarity}\n📜 {tooltip}"


# 🔧 Przykładowe recepty (możesz je trzymać też w JSON albo bazie danych)
default_recipes = [
    Recipe("Mikstura Leczenia", ["zioło", "woda"], "Mikstura Leczenia", "easy"),
    Recipe("Eliksir Siły", ["krew trolla", "czarna perła"], "Eliksir Siły", "hard"),
    Recipe("Miecz Cieni", ["stal", "cień"], "Miecz Cieni", "legendary"),
    Recipe("Zbroja Łowcy", ["skóra", "srebro", "kość"], "Zbroja Łowcy", "normal"),
]

# Jeśli chcesz przetestować lokalnie
if __name__ == "__main__":
    crafting = CraftingSystem(default_recipes)
    test_input = ["krew trolla", "czarna perła"]
    print(crafting.craft(test_input))
