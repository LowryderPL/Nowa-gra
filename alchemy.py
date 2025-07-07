# alchemy.py – FIROS: Magic & Magic (pełna wersja rozszerzona)

class Potion:
    def __init__(self, name, ingredients, effect, rarity="zwykły", category="Mikstura", level_required=1, special=False):
        self.name = name
        self.ingredients = ingredients
        self.effect = effect
        self.rarity = rarity
        self.category = category
        self.level_required = level_required
        self.special = special  # np. frakcyjna, rytualna

    def __repr__(self):
        return f"{self.name} ({self.category}) – {self.effect}"


class Alchemy:
    def __init__(self):
        self.backpack = []
        self.recipes = self.load_recipes()

    def load_recipes(self):
        return [
            # Zwykłe mikstury
            Potion("Mikstura Życia", ["czerwony grzyb", "kwiat życia"], "+30 HP"),
            Potion("Mikstura Many", ["błękitny kryształ", "łza czarodzieja"], "+20 Mana"),

            # Rzadkie mikstury
            Potion("Wywar Mocy", ["serce trolla", "czarna krew"], "+15 Ataku", "rzadki"),
            Potion("Zatruty Wywar", ["ziele śmierci", "pajęczy jad"], "Zatrucie wroga", "rzadki"),

            # Epickie mikstury
            Potion("Eliksir Krwi", ["mlecz czarownicy", "kość demona"], "Kradnie życie", "epicki"),
            Potion("Niewidzialność", ["cień nietoperza", "mgła z bagien"], "Niewidzialność na 1 turę", "epicki"),

            # Legendarne mikstury
            Potion("Eliksir Cienia", ["krew pradawnego", "cień umarłego"], "+100 do uniku, 3 tury", "legendarny", "Rytuał", 12, True),
            Potion("Wywar Chaosu", ["oko beholdera", "jądro magmy", "pióro feniksa"], "Efekt losowy: +100 lub -50 HP", "legendarny", "Mutacja", 15, True),

            # Frakcyjne mikstury
            Potion("Miód Wilczych Watah", ["czarna mięta", "szpik kości"], "+25% szału", "rzadki", "Frakcyjna", 8, True),

            # Zwoje
            Potion("Zwój Płomienia", ["popiół ognistego wilka", "runiczny papier"], "Ogień +40 dmg", "epicki", "Zwój", 6),
            Potion("Zwój Lodu", ["lodowa rosa", "runiczny papier"], "Zamraża wroga na 1 turę", "rzadki", "Zwój", 4),
        ]

    def craft(self, ingredients, player_level=1):
        for recipe in self.recipes:
            if set(recipe.ingredients) <= set(ingredients):
                if player_level < recipe.level_required:
                    return f"❌ Potrzebny poziom {recipe.level_required}, by stworzyć: {recipe.name}"
                self.backpack.append(recipe)
                return f"🧪 Stworzono: {recipe.name} – {recipe.effect}"
        return "❌ Nie udało się stworzyć mikstury."

    def show_backpack(self):
        if not self.backpack:
            return "🎒 Brak mikstur w plecaku."
        return "\n".join([f"- {p.name} ({p.rarity}): {p.effect}" for p in self.backpack])

    def use_potion(self, potion_name, player):
        for potion in self.backpack:
            if potion.name.lower() == potion_name.lower():
                self.backpack.remove(potion)
                # Tutaj logika efektu – rozbudowana wersja mogłaby wpływać na player.hp itp.
                return f"✅ Użyto {potion.name}. Efekt: {potion.effect}"
        return "❌ Nie znaleziono mikstury."

    def list_recipes(self, category=None):
        result = []
        for recipe in self.recipes:
            if not category or recipe.category.lower() == category.lower():
                result.append(f"{recipe.name} ({recipe.rarity}) – {recipe.effect}")
        return "\n".join(result)


# Test lokalny
if __name__ == "__main__":
    alchemy = Alchemy()
    print(alchemy.craft(["czerwony grzyb", "kwiat życia"]))
    print(alchemy.craft(["oko beholdera", "jądro magmy", "pióro feniksa"], player_level=16))
    print(alchemy.show_backpack())
    print("--- Receptury: ---")
    print(alchemy.list_recipes())
