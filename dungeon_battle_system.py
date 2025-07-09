
import random
from firos_loot_system import FirosLootSystem

class DungeonBattleSystem:
    def __init__(self):
        self.loot = FirosLootSystem()
        self.bosses = {
            "Troll King Hurak": {"hp": 100, "atk": 15, "def": 5},
            "Necrolord Vhax": {"hp": 120, "atk": 20, "def": 10},
            "Cryptmother Lysa": {"hp": 80, "atk": 25, "def": 8},
            "Dragon of Firos": {"hp": 200, "atk": 30, "def": 12},
        }
        self.player = {"hp": 120, "atk": 25, "def": 10, "potions": 3}

    def enter_dungeon(self, location):
        print(f"🏰 Wchodzisz do lochu: {location}")
        boss = random.choice(list(self.bosses.keys()))
        print(f"👹 Boss: {boss}")
        self.fight_boss(boss)

    def fight_boss(self, boss_name):
        boss = self.bosses[boss_name]
        player = self.player.copy()
        round_num = 1

        while player["hp"] > 0 and boss["hp"] > 0:
            print(f"\n🔁 Tura {round_num}")
            # Player attacks
            dmg = max(player["atk"] - boss["def"], 5)
            boss["hp"] -= dmg
            print(f"⚔️ Gracz atakuje: -{dmg} HP Bossowi ({boss['hp']} HP pozostało)")

            if boss["hp"] <= 0:
                print(f"✅ Boss {boss_name} pokonany!")
                loot = self.loot.roll_loot()
                print(f"🎁 Drop: [{loot['rarity'].upper()}] {loot['item']}")
                return

            # Boss attacks
            dmg_boss = max(boss["atk"] - player["def"], 5)
            player["hp"] -= dmg_boss
            print(f"💥 Boss kontratakuje: -{dmg_boss} HP Graczowi ({player['hp']} HP pozostało)")

            # Player heals if low HP
            if player["hp"] <= 30 and player["potions"] > 0:
                player["hp"] += 40
                player["potions"] -= 1
                print(f"🧪 Gracz używa mikstury! +40 HP (pozostało {player['potions']} mikstur)")

            round_num += 1

        if player["hp"] <= 0:
            print("☠️ Zostałeś pokonany przez Bossa... Próbuj ponownie.")

if __name__ == "__main__":
    dungeon = DungeonBattleSystem()
    dungeon.enter_dungeon("Kargath Mines")
