
from faction_reputation import FactionReputation

class PlayerJournal:
    def __init__(self):
        self.completed_quests = []
        self.quest_log = []
        self.level = 1
        self.exp = 0
        self.reputation = FactionReputation()

    def log_quest(self, quest_title, reward):
        self.completed_quests.append(quest_title)
        self.quest_log.append({
            "title": quest_title,
            "reward": reward
        })
        self.exp += reward.get("exp", 0)
        self.check_level_up()

    def check_level_up(self):
        required_exp = self.level * 100
        if self.exp >= required_exp:
            self.level += 1
            self.exp -= required_exp
            print(f"⬆️ Poziom podniesiony do {self.level}!")

    def show_journal(self):
        print("📜 Dziennik gracza:")
        for entry in self.quest_log:
            print(f"✅ {entry['title']} – Nagroda: {entry['reward']}")

    def show_status(self):
        print(f"🎖️ Poziom: {self.level} | EXP: {self.exp}")
        self.reputation.list_factions()
