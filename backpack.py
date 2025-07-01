# backpack.py - Zarządzanie plecakiem gracza w grze Firos: Magic & Magic

class Backpack:
    def __init__(self):
        self.ingredients = []
        self.artifacts = []
        self.scrolls = []
        self.items = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"🔹 Dodano składnik: {ingredient}")

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)
        print(f"✨ Dodano artefakt: {artifact}")

    def add_scroll(self, scroll):
        self.scrolls.append(scroll)
        print(f"📜 Dodano zwój: {scroll}")

    def add_item(self, item):
        self.items.append(item)
        print(f"🎒 Dodano przedmiot: {item}")

    def has_ingredients(self, required):
        return all(req in self.ingredients for req in required)

    def remove_ingredients(self, ingredients):
        for ing in ingredients:
            if ing in self.ingredients:
                self.ingredients.remove(ing)

    def list_all(self):
        print("\n📦 Zawartość plecaka:")
        print(f"Składniki ({len(self.ingredients)}): {', '.join(self.ingredients) if self.ingredients else 'brak'}")
        print(f"Artefakty ({len(self.artifacts)}): {', '.join(self.artifacts) if self.artifacts else 'brak'}")
        print(f"Zwoje ({len(self.scrolls)}): {', '.join(self.scrolls) if self.scrolls else 'brak'}")
        print(f"Przedmioty ({len(self.items)}): {', '.join(self.items) if self.items else 'brak'}")

    def show_inventory_summary(self):
        print("\n📊 Podsumowanie wyposażenia gracza:")
        print(f"- Składniki: {len(self.ingredients)}")
        print(f"- Artefakty: {len(self.artifacts)}")
        print(f"- Zwoje: {len(self.scrolls)}")
        print(f"- Przedmioty: {len(self.items)}")

# Przykład użycia (tylko do testów lokalnych)
if __name__ == "__main__":
    bp = Backpack()
    bp.add_ingredient("ziele")
    bp.add_ingredient("popiół")
    bp.add_artifact("Pierścień Mocy")
    bp.add_scroll("Zwój Ognia")
    bp.add_item("Miecz Żołnierza")
    bp.list_all()
    bp.show_inventory_summary()
