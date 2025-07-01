from typing import List, Dict, Optional
import json
import datetime

class Achievement:
    def __init__(self, id: int, name: str, description: str, category: str, reward_xp: int, reward_rfm: int):
        self.id = id
        self.name = name
        self.description = description
        self.category = category  # Combat, Social, Exploration itd.
        self.reward_xp = reward_xp
        self.reward_rfm = reward_rfm

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "reward_xp": self.reward_xp,
            "reward_rfm": self.reward_rfm
        }

class AchievementTracker:
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.achievements: List[int] = []
        self.timestamps: Dict[int, str] = {}

    def unlock(self, achievement_id: int):
        if achievement_id not in self.achievements:
            self.achievements.append(achievement_id)
            self.timestamps[achievement_id] = datetime.datetime.now().isoformat()

    def has_achievement(self, achievement_id: int) -> bool:
        return achievement_id in self.achievements

    def to_dict(self) -> Dict:
        return {
            "player_id": self.player_id,
            "achievements": self.achievements,
            "timestamps": self.timestamps
        }

    def save(self, filepath: str):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    def load(self, filepath: str):
        with open(filepath, "r") as f:
            data = json.load(f)
            self.achievements = data.get("achievements", [])
            self.timestamps = data.get("timestamps", {})

class AchievementSystem:
    def __init__(self):
        self.achievements: Dict[int, Achievement] = {}
        self.load_default_achievements()

    def load_default_achievements(self):
        base_achievements = [
            Achievement(1, "Pierwsza Krew", "Pokonaj pierwszego wroga.", "Combat", 100, 10),
            Achievement(2, "Mistrz Eksploracji", "Odkryj 10 unikalnych lokacji.", "Exploration", 150, 15),
            Achievement(3, "Zbieracz Legend", "Zdobądź 3 legendarne przedmioty.", "Loot", 200, 20),
            Achievement(4, "Mistrz Czatów", "Napisz 100 wiadomości na czacie.", "Social", 50, 5),
            Achievement(5, "Twórca Gildii", "Załóż własną gildię.", "Guild", 250, 30),
            Achievement(6, "Łowca Bossów", "Pokonaj 5 unikalnych bossów.", "Combat", 300, 40),
            Achievement(7, "Kupiec", "Sprzedaj 10 przedmiotów na rynku.", "Trade", 100, 10),
            Achievement(8, "Czas to Magia", "Spędź 5 godzin w grze.", "Time", 120, 12),
            Achievement(9, "Uczeń Magii", "Rzuć 50 zaklęć.", "Magic", 180, 18),
            Achievement(10, "Sezonowy Wojownik", "Zakończ sezon PvP z miejscem w top 1000.", "PvP", 500, 100),
        ]
        for ach in base_achievements:
            self.achievements[ach.id] = ach

    def get_achievement(self, achievement_id: int) -> Optional[Achievement]:
        return self.achievements.get(achievement_id)

    def list_all(self) -> List[Dict]:
        return [ach.to_dict() for ach in self.achievements.values()]
