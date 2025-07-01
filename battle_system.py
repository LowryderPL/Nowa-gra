import random
from spellbook import cast_spell
from inventory_data import inventory_data

# Style walki (aktywny, defensywny, taktyczny)
combat_styles = {
    "agresywny": 1.2,
    "defensywny": 0.8,
    "taktyczny": 1.0
}

# Klasy postaci z dodatkowymi bonusami (rozszerzenie)
class_bonuses = {
    "Wiedźmograd": {"bonus": "unik", "value": 0.15},
    "Zjomistrz": {"bonus": "mana_regen", "value": 5},
    "Krwistostrzelec": {"bonus": "crit", "value": 0.2},
    "Duszołowca": {"bonus": "drain_mana", "value": 3},
    "Runokultan": {"bonus": "rune_amp", "value": 0.1},
    "Cierniojad": {"bonus": "reflect", "value": 0.1},
    "Żarogniew": {"bonus": "burn", "value": 0.05},
    "Mgłomistrz": {"bonus": "vanish_chance", "value": 0.1}
}

# Przykładowy efekt działania broni lub artefaktu
def apply_bonus(player_class, base_damage):
    bonus = class_bonuses.get(player_class, {})
    if bonus.get("bonus") == "crit" and random.random() < bonus["value"]:
        print("[KRITICAL HIT!]")
        return int(base_damage * 1.5)
    elif bonus.get("bonus") == "burn" and random.random() < bonus["value"]:
        print("[WRÓG PŁONIE!]")
        return base_damage + 5
    return base_damage

# System walki
def execute_battle(player, enemy, style="taktyczny"):
    print(f"\n🛡️ {player['name']} vs {enemy['name']} ⚔️")
    print(f"Styl walki: {style.capitalize()}")

    turn = 0
    while player["hp"] > 0 and enemy["hp"] > 0:
        turn += 1
        print(f"\n--- Tura {turn} ---")

        # Gracz atakuje
        weapon = inventory_data[player["class"]]["broń"]
        damage = int(weapon["power"] * combat_styles[style])
        damage = apply_bonus(player["class"], damage)
        enemy["hp"] -= damage
        print(f"{player['name']} uderza za {damage} dmg ({weapon['name']})")

        if enemy["hp"] <= 0:
            print(f"\n✅ {enemy['name']} pokonany!")
            return "win"

        # Wróg atakuje
        enemy_damage = int(enemy["power"] * 0.9)
        player["hp"] -= enemy_damage
        print(f"{enemy['name']} kontruje za {enemy_damage} dmg")

        if player["hp"] <= 0:
            print(f"\n❌ {player['name']} poległ...")
            return "lose"

# Test walki
if __name__ == "__main__":
    player = {
        "name": "Tirion",
        "class": "Żarogniew",
        "hp": 100,
        "mana": 30
    }

    enemy = {
        "name": "Wilk Cieni",
        "power": 8,
        "hp": 70
    }

    result = execute_battle(player, enemy, style="agresywny")
    print("\nWynik bitwy:", result)
