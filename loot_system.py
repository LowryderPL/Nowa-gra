# loot_system.py – Firos: Magic & Magic

import random
from inventory import Item

def drop_loot(enemy, inventory):
    print(f"\n== Drop z {enemy.name} ==")

    loot_table = [
        {"name": "Zardzewiały miecz", "rarity": "common", "power": 2, "slot": "sword"},
        {"name": "Skórzana zbroja", "rarity": "common", "power": 1, "slot": "armor"},
        {"name": "Hełm żołnierza", "rarity": "rare", "power": 3, "slot": "helmet"},
        {"name": "Pierścień many", "rarity": "epic", "power": 5, "slot": "ring"},
        {"name": "Amulet ognia", "rarity": "legendary", "power": 7, "slot": "artifact"}
    ]

    weights = {
        "common": 60,
        "rare": 25,
        "epic": 10,
        "legendary": 5
    }

    # Wybierz losowy przedmiot z tabeli dropu
    weighted_items = []
    for item in loot_table:
        weighted_items += [item] * weights[item["rarity"]]

    dropped = random.choice(weighted_items)
    loot_item = Item(
        name=dropped["name"],
        rarity=dropped["rarity"],
        power=dropped["power"],
        slot=dropped["slot"]
    )

    print(f"Znaleziono przedmiot: {loot_item.name} ({loot_item.rarity})")
    inventory.add_to_backpack(loot_item)
