
import random
from grubobrzuch_items import grubobrzuch_items

class DungeonEncounter:
    def __init__(self, player_name, reputation=50, corruption=0):
        self.player = player_name
        self.reputation = reputation  # 0-100
        self.corruption = corruption  # 0-100

    def enter_dungeon(self, dungeon_name):
        print(f"🏰 {self.player} wkracza do lochu: {dungeon_name}")
        self.trigger_trap()
        self.trigger_mutation()
        return self.roll_loot()

    def trigger_trap(self):
        trap_chance = random.randint(1, 100)
        if trap_chance <= 20:
            damage = random.randint(5, 20)
            print(f"💥 Pułapka! Tracisz {damage} HP. Zardzewiały kolec wbił się w twoją łydkę.")
            self.corruption += 5
        else:
            print("🔍 Omijasz pułapkę. Ale coś czai się w ciemności...")

    def trigger_mutation(self):
        mutation_roll = random.randint(1, 100)
        if mutation_roll <= 10:
            effect = random.choice([
                "🧬 Oko bestii rośnie na twoim karku. Zyskujesz +10 do percepcji.",
                "🐍 Twoja skóra łuszczy się jak u węża. Zyskujesz odporność na ogień.",
                "🧠 Słyszysz głosy. Zyskujesz +5 do magii, ale -5 do morale."
            ])
            self.corruption += 10
            print(f"⚠️ MUTACJA! {effect}")
        else:
            print("😓 Czujesz dziwne mrowienie, ale nic się nie dzieje.")

    def roll_loot(self):
        drop_chance = random.randint(1, 100)
        if drop_chance <= 20:
            item = random.choice(grubobrzuch_items)
            print(f"🎁 Znaleziono: {item.name}")
            print(f"📜 {item.description}")
            self.reputation += 2
            return item
        else:
            print("🪦 Tylko kości i cisza.")
            self.reputation -= 1
            return None

    def get_status(self):
        print(f"📊 Reputacja: {self.reputation} / 100")
        print(f"💀 Korupcja: {self.corruption} / 100")
