
from grubobrzuch_items import grubobrzuch_items
import random

class DungeonLootSystem:
    def __init__(self, dungeon_name):
        self.dungeon_name = dungeon_name

    def roll_loot(self):
        print(f"🎲 Przeszukujesz loch: {self.dungeon_name}...")
        drop_chance = random.randint(1, 100)

        if drop_chance <= 15:
            item = random.choice(grubobrzuch_items)
            print(f"🎁 Znaleziono przedmiot: {item.name}")
            print(f"📜 Opis: {item.description}")
            print(f"⭐ Rzadkość: {item.rarity}")
            return item
        else:
            print("🪦 Znalazłeś tylko kurz, robactwo i zgniłą słomę...")
            return None

    def boss_defeated(self):
        print("💀 Boss został pokonany!")
        guaranteed_drop = random.choice(grubobrzuch_items)
        print(f"🎁 Nagroda za pokonanie bossa: {guaranteed_drop.name}")
        print(f"📜 Opis: {guaranteed_drop.description}")
        return guaranteed_drop
