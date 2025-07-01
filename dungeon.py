# dungeon.py – System lochów i bossów w grze Firos: Magic & Magic

import random
from backpack import Backpack
from inventory import Item
from xp_system import PlayerStats

# === INSTANCJE ===
player_backpack = Backpack()
player_stats = PlayerStats("Gracz")

# === Potwory i bossowie ===
monsters = [
    {"name": "Szkielet Wojownik", "exp": 50, "loot": ["kość", "miecz rdzy"]},
    {"name": "Ghul Bagienny", "exp": 60, "loot": ["jadowity mech", "cień"]},
    {"name": "Zmiennokształtny", "exp": 70, "loot": ["śluz", "krew", "pergamin"]},
]

boss = {
    "name": "Król Czaszek",
    "exp": 200,
    "loot": ["amulet cienia", "staromagiczna księga", "runiczny_papier", "artefakt bossowy"]
}

# === Eventy środka lochu ===
events = [
    "Wdepnąłeś w zatrutą pułapkę – ale nic ci się nie stało.",
    "Znalazłeś dziwny symbol na ścianie – zapisujesz go.",
    "Usłyszałeś krzyk z oddali, ale nikogo nie widzisz.",
    "Znalazłeś zwłoki dawnego bohatera – bierzesz jego mapę."
]

# === Funkcje lochu ===
def enter_dungeon():
    print("\n🏰 Wchodzisz do LOCHU ZAPOMNIANYCH")
    print("3 etapy: walka – zdarzenie – boss. Przygotuj się.")

    input("Naciśnij Enter, aby rozpocząć FAZĘ 1: walka z potworami...")

    monster = random.choice(monsters)
    print(f"\n👹 Atakuje cię: {monster['name']}")
    print("⚔️ Walka trwa...")
    print("✅ Zwyciężyłeś!")
    for item in monster["loot"]:
        player_backpack.add_ingredient(item)
    player_stats.gain_exp(monster["exp"])

    input("\nNaciśnij Enter, aby przejść do FAZY 2: zdarzenie...")

    print(f"\n📜 {random.choice(events)}")

    input("\nNaciśnij Enter, aby przejść do FAZY 3: boss...")

    print(f"\n💀 BOSSSSS: {boss['name']} wychodzi z cienia!")
    print("⚔️ Epicka walka... Trwa... (symulowana)")

    print("🏆 UDAŁO SIĘ! Pokonałeś Króla Czaszek!")
    for item in boss["loot"]:
        player_backpack.add_ingredient(item)
    player_stats.gain_exp(boss["exp"])

    # BONUS drop
    special = Item("Pierścień Zwycięzcy", "epic", 5, "ring", description="Nagroda za pokonanie bossa")
    player_backpack.add_artifact(special)

    print("\n🎁 Zdobycze: składniki + artefakt bossa + EXP")
    player_stats.show_stats()
    print("\n🗝️ Opuszczasz loch.")

# Test lokalny
if __name__ == "__main__":
    enter_dungeon()
