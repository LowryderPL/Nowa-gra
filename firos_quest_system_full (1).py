
import random

class FirosQuestSystemFull:
    def __init__(self):
        self.completed = []
        self.active_quests = []
        self.material_inventory = {"bone": 3, "scroll": 1, "beast_heart": 0, "shadow_stone": 2}
        self.faction_reputation = {"Firos Order": 0, "Bandits": 0}
        self.player_level = 5
        self.quest_log = []

        self.npcs = [
            {
                "name": "Elandor the Gravedigger",
                "location": "Crypt of Whispers",
                "faction": "Free Folk",
                "dialogue": [
                    "Widziałem cienie w katakumbach...",
                    "Zabierz to, ale nie wracaj bez spalonych kości!"
                ],
                "quest": {
                    "id": "q_bones_01",
                    "title": "Bones for the Pyre",
                    "type": "collection",
                    "objective_item": "bone",
                    "required_amount": 5,
                    "required_location": "Crypt of Whispers",
                    "required_level": 3,
                    "reward": {"exp": 100, "fame": 5, "item": "Blessed Ashes"},
                    "battle": False
                }
            },
            {
                "name": "Soraya the Huntmistress",
                "location": "Blackwood Castle",
                "faction": "Order of Flame",
                "dialogue": [
                    "Tylko głupiec zszedłby do jaskiń bez ostrza...",
                    "Zabij bestię i przynieś mi jej serce. Jeśli przeżyjesz."
                ],
                "quest": {
                    "id": "q_beast_01",
                    "title": "The Beast Below",
                    "type": "boss_battle",
                    "required_location": "Cave of Hunger",
                    "required_level": 5,
                    "reward": {"exp": 250, "fame": 10, "item": "Hunter's Charm"},
                    "battle": True,
                    "boss": {"name": "Beast of Hunger", "hp": 100, "atk": 20, "def": 5}
                }
            }
        ]

    def list_quests(self):
        print("📜 Dostępne zadania:")
        for npc in self.npcs:
            q = npc["quest"]
            print(f"- {q['title']} ({npc['name']} – {npc['location']})")

    def talk_to_npc(self, name):
        npc = next((n for n in self.npcs if n["name"].lower() == name.lower()), None)
        if not npc:
            print("❌ Nie znaleziono takiego NPC.")
            return
        print(f"🧙 {npc['name']} – {npc['faction']}")
        for line in npc["dialogue"]:
            print(f"💬 {line}")
        self.assign_quest(npc)

    def assign_quest(self, npc):
        quest = npc["quest"]
        if quest["id"] in self.completed:
            print("✅ To zadanie zostało już wykonane.")
            return
        if quest["required_level"] > self.player_level:
            print(f"🔒 Wymagany poziom: {quest['required_level']} (twój: {self.player_level})")
            return
        if quest["id"] in [q["id"] for q in self.active_quests]:
            print("📘 Masz już to zadanie aktywne.")
            return
        self.active_quests.append(quest)
        print(f"📘 Nowe zadanie: {quest['title']}")

    def complete_quest(self, quest_id):
        quest = next((q for q in self.active_quests if q["id"] == quest_id), None)
        if not quest:
            print("❌ Nie masz tego zadania aktywnego.")
            return

        # Weryfikacja warunków
        if quest["type"] == "collection":
            item = quest["objective_item"]
            if self.material_inventory.get(item, 0) < quest["required_amount"]:
                print(f"❌ Nie masz wystarczająco materiałów: {item} ({self.material_inventory.get(item,0)}/{quest['required_amount']})")
                return
            self.material_inventory[item] -= quest["required_amount"]

        elif quest["type"] == "boss_battle":
            print(f"⚔️ Rozpoczynasz walkę z bossem: {quest['boss']['name']}")
            boss = quest["boss"]
            player_hp = 100
            while player_hp > 0 and boss["hp"] > 0:
                dmg_to_boss = max(25 - boss["def"], 5)
                boss["hp"] -= dmg_to_boss
                print(f"🗡️ Zadajesz {dmg_to_boss} obrażeń bossowi ({boss['hp']} HP pozostało)")

                if boss["hp"] <= 0:
                    break
                dmg_to_player = max(boss["atk"] - 10, 5)
                player_hp -= dmg_to_player
                print(f"💥 Boss zadaje {dmg_to_player} obrażeń tobie ({player_hp} HP pozostało)")
            if player_hp <= 0:
                print("☠️ Zginąłeś. Zadanie przerwane.")
                return

        # Zakończenie i nagroda
        print(f"🏆 Zadanie zakończone: {quest['title']}")
        reward = quest["reward"]
        print(f"🎁 Nagroda: +{reward['exp']} EXP, +{reward['fame']} sławy, przedmiot: {reward['item']}")
        self.completed.append(quest["id"])
        self.active_quests = [q for q in self.active_quests if q["id"] != quest["id"]]
        self.quest_log.append(quest["title"])

if __name__ == "__main__":
    system = FirosQuestSystemFull()
    system.list_quests()
    print("\nAby porozmawiać: system.talk_to_npc('Imię')")
    print("Aby ukończyć: system.complete_quest('ID')")
