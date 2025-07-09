
import random

class FirosLootSystem:
    def __init__(self):
        self.loot_table = {
            "common": ["Potion", "Herb", "Rusty Dagger", "Wooden Shield"],
            "rare": ["Silver Sword", "Magic Scroll", "Firos Crystal", "Enchanted Ring"],
            "epic": ["Ancient Relic", "Dragon Bone Staff", "Amulet of Chaos"],
            "legendary": ["Blade of Eternity", "Crown of Kings", "Book of Forbidden Magic"]
        }

    def roll_loot(self):
        roll = random.randint(1, 100)
        if roll <= 60:
            rarity = "common"
        elif roll <= 85:
            rarity = "rare"
        elif roll <= 95:
            rarity = "epic"
        else:
            rarity = "legendary"
        item = random.choice(self.loot_table[rarity])
        return {"rarity": rarity, "item": item}

if __name__ == "__main__":
    dropper = FirosLootSystem()
    for i in range(10):
        result = dropper.roll_loot()
        print(f"[{result['rarity'].upper()}] 🎁 {result['item']}")
