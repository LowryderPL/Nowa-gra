class Ritual:
    def __init__(self, name, cost, effect, ingredients, description):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.ingredients = ingredients
        self.description = description

    def show_details(self):
        print(f"\n🔮 {self.name}")
        print(f"Koszt many: {self.cost}")
        print(f"Efekt: {self.effect}")
        print(f"Składniki: {', '.join(self.ingredients)}")
        print(f"Opis: {self.description}")

def get_rituals():
    return [
        Ritual("Rytuał Krwi", 40, "Odbiera 20% HP przeciwnika, przywraca 10% HP rzucającemu", ["Krew Wilka", "Kamień Rytualny"], "Starożytna sztuka zakazana przez rady magów."),
        Ritual("Zaklęcie Cienia", 30, "Przeciwnik traci 2 tury", ["Popiół Zguby", "Czarna Runa"], "Pozwala na zniknięcie z pola widzenia."),
        Ritual("Ochrona Przodków", 25, "+20 do obrony na 3 tury", ["Pióro Orła", "Esencja Dębu"], "Wezwanie duchów dawnych wojowników."),
        Ritual("Płomień Feniksa", 50, "Zadaje 60 DMG wszystkim wrogom", ["Łuska Feniksa", "Zioła Ognia"], "Ostatnia nadzieja dla tych, którzy stanęli pod ścianą."),
    ]

def show_ritual_book():
    rituals = get_rituals()
    print("\n=== 📖 Księga Rytuałów ===")
    for i, r in enumerate(rituals, 1):
        print(f"{i}. {r.name} - {r.effect}")
    choice = input("Wybierz rytuał, by zobaczyć szczegóły: ")
    try:
        rituals[int(choice)-1].show_details()
    except:
        print("Niepoprawny wybór.")
