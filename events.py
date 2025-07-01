# events.py – Rozszerzony system wydarzeń FIROS

import datetime
import random

class Event:
    def __init__(self, event_id, name, description, start_time, end_time, event_type, rewards, participants=None):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.event_type = event_type  # "PvE", "PvP", "Frakcyjny", "Sezonowy"
        self.rewards = rewards  # {"XP": 200, "RFM": 50, "artefakt": "Miecz Cienia"}
        self.participants = participants if participants else []

    def is_active(self):
        now = datetime.datetime.now()
        return self.start_time <= now <= self.end_time

    def join_event(self, player_id):
        if player_id not in self.participants:
            self.participants.append(player_id)
            return True
        return False

    def get_info(self):
        status = "Aktywny" if self.is_active() else "Nieaktywny"
        return f"{self.name} ({status}) - {self.description}"

class EventManager:
    def __init__(self):
        self.events = {}
        self.load_sample_events()

    def load_sample_events(self):
        now = datetime.datetime.now()
        self.events[1] = Event(
            1, "Najazd Smoków", "Potężne smoki atakują stolicę FIROS!", now,
            now + datetime.timedelta(days=2), "PvE",
            {"XP": 500, "RFM": 150, "artefakt": "Zębaty Topór"}
        )
        self.events[2] = Event(
            2, "Wojna Frakcji", "Twoja frakcja walczy o dominację w ruinach Varendral.", now,
            now + datetime.timedelta(days=5), "Frakcyjny",
            {"XP": 300, "RFM": 100}
        )
        self.events[3] = Event(
            3, "Turniej Areny", "Zgłoś się do pojedynku PvP i walcz o chwałę!", now,
            now + datetime.timedelta(days=3), "PvP",
            {"XP": 200, "RFM": 75, "NFT": "ArenaChampionBadge"}
        )

    def list_active_events(self):
        return [e for e in self.events.values() if e.is_active()]

    def join_event(self, event_id, player_id):
        event = self.events.get(event_id)
        if event and event.is_active():
            return event.join_event(player_id)
        return False

    def get_event_info(self, event_id):
        event = self.events.get(event_id)
        if event:
            return event.get_info()
        return "Nie znaleziono wydarzenia."

    def claim_rewards(self, event_id, player_id):
        event = self.events.get(event_id)
        if event and player_id in event.participants:
            return event.rewards
        return {}

# Przykład użycia
if __name__ == "__main__":
    em = EventManager()
    for event in em.list_active_events():
        print(event.get_info())
    print("Dołączanie do eventu:", em.join_event(1, "gracz123"))
    print("Nagrody:", em.claim_rewards(1, "gracz123"))
