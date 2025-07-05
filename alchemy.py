# alchemy.py — pełna wersja logiczna bez GUI
# FIROS: Magic & Magic – system craftingu, run, mikstur, mutacji, zwojów

class Recipe:
    def __init__(self, name, ingredients, result, description, category):
        self.name = name
        self.ingredients = ingredients
        self.result = result
        self.description = description
        self.category = category  # "mikstura", "zwój", "mutacja"

class Alchemy:
    def __init__(self):
        self.recipes = []
        self.backpack = []  # składniki i efekty trafiają tutaj
        self.mana = 0
        self._load_recipes()

    def _load_recipes(self):
        self.recipes = [
            Recipe("Mikstura Leczenia", ["ziele życia", "woda źródlana"], "potion_heal", "Leczy 50 HP.", "mikstura"),
            Recipe("Mikstura Many", ["kwiat many", "błękitna esencja"], "potion_mana", "Przywraca 30 many.", "mikstura"),
            Recipe("Zwój Ognistej Kuli", ["krew demona", "proch", "kryształ ognia"], "scroll_fireball", "Zadaje 30 obrażeń wszystkim wrogom.", "zwój"),
            Recipe("Mutacja Wilczego Słuchu", ["ucho wilka", "szara rosa"], "mutacja_hearing", "Zwiększa szansę na unik przez 2 tury.", "mutacja"),
            Recipe("Zwój Lodowego Wybuchu", ["pazur trolla", "lodowa esencja"], "scroll_ice", "Zamraża wrogów na 1 turę.", "zwój"),
        ]

    def craft(self, ingredients):
        matched = None
        for recipe in self.recipes:
            if sorted(recipe.ingredients) == sorted(ingredients):
                matched = recipe
                break

        if matched:
            self.backpack.append(matched.result)
            if matched.category == "zwój":
                self.mana += 5  # każdy zwój zwiększa manę
            return f"Stworzono: {matched.name} – {matched.description}"
        else:
            return "Błąd: nieprawidłowa kombinacja składników."

    def show_backpack(self):
        if not self.backpack:
            return "Plecak pusty."
        return f"📦 Plecak zawiera: {', '.join(self.backpack)}\n💧 Mana: {self.mana}"

    def list_recipes(self, category=None):
        lista = []
        for recipe in self.recipes:
            if category is None or recipe.category == category:
                lista.append(f"{recipe.name} ({recipe.category}) – {', '.join(recipe.ingredients)} → {recipe.result}")
        return "\n".join(lista)

# Przykład działania – wersja testowa
if __name__ == "__main__":
    alchemy = Alchemy()
    print("🧪 Dostępne receptury:")
    print(alchemy.list_recipes())

    print("\n🎯 Tworzymy Miksturę Leczenia...")
    wynik = alchemy.craft(["ziele życia", "woda źródlana"])
    print(wynik)

    print("\n🎯 Tworzymy Zwój Ognistej Kuli...")
    wynik = alchemy.craft(["krew demona", "kryształ ognia", "proch"])
    print(wynik)

    print("\n📦 Plecak:")
    print(alchemy.show_backpack())
