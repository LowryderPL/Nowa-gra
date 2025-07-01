# enemy.py – Rozszerzony system przeciwników FIROS

import random

class Enemy:
    def __init__(self, name, hp, attack, level, loot, faction=None, rarity="normal", abilities=None, description=""):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.level = level
        self.loot = loot  # np. {"gold": 30, "item": "Czaszka Wampira"}
        self.faction = faction  # np. "Runokultan", "Mgłomistrzowie"
        self.rarity = rarity  # normal, rare, elite, legendary, boss
        self.abilities = abilities or []
        self.description = description

    def is_boss(self):
        return self.rarity in ["boss", "legendary"]

    def __str__(self):
        return f"{self.name} (Lvl {self.level}) – {self.rarity.upper()} [{self.faction or 'Neutralny'}]"

    def display_info(self):
        print(f"\n👹 {self.name} (Poziom {self.level})")
        print(f"HP: {self.hp} | Atak: {self.attack}")
        print(f"Frakcja: {self.faction or 'Brak'} | Rzadkość: {self.rarity}")
        print(f"Opis: {self.description}")
        print("Zdolności:")
        for ab in self.abilities:
            print(f" - {ab}")
        print("Łup:")
        for item, val in self.loot.items():
            print(f"   {item}: {val}")


# Lista wrogów
ENEMY_LIST = [
    Enemy("Cień Cierni", 40, 8, 3, {"złoto": 15}, "Runokultan", "normal", ["Ukłucie cienia"], "Mroczna istota z żyjącego lasu."),
    Enemy("Płonący Wilk", 60, 12, 5, {"złoto": 35, "płomień": 1}, "Żarogniew", "rare", ["Podpalenie", "Ryk"], "Zwierzę płonące wiecznym gniewem."),
    Enemy("Zgniłomag", 80, 14, 6, {"kryształ": 2}, "Mgłomistrzowie", "elite", ["Zatruta mgła", "Zgniły dotyk"], "Zmutowany mag zaklęty przez mgłę."),
    Enemy("Duszołowca Widmo", 110, 20, 9, {"esencja duszy": 1}, "Duszołowcy", "legendary", ["Kradzież życia", "Nieśmiertelność"], "Upiór wyssany z pokonanego Wiedźmina."),
    Enemy("Król Krwi Zjomistrzów", 150, 30, 12, {"korona krwi": 1, "TON": 5}, "Zjomistrzowie", "boss", ["Krzyk Krwi", "Rytuał Życia", "Rozbłysk Cierpienia"], "Pradawny przywódca, który przetrwał zagładę epok.")
]


# API
def get_enemy_by_name(name):
    return next((e for e in ENEMY_LIST if e.name == name), None)

def generate_random_enemy(level=None):
    pool = [e for e in ENEMY_LIST if (level is None or e.level <= level)]
    return random.choice(pool) if pool else None

def get_all_enemies():
    return ENEMY_LIST

def get_bosses():
    return [e for e in ENEMY_LIST if e.is_boss()]

def get_enemies_by_faction(faction):
    return [e for e in ENEMY_LIST if e.faction == faction]

# Przykład
if __name__ == "__main__":
    enemy = generate_random_enemy(level=6)
    print("\n🎯 Wylosowany przeciwnik:")
    enemy.display_info()
