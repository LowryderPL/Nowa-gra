# exploration.py – Rozszerzony system eksploracji świata FIROS

import random
from map_system import MapSystem, move_to_location

class Explorer:
    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.exploration_points = 0
        self.level = 1
        self.history = []
        self.active_events = []

    def set_start(self, location):
        self.current_location = location
        location.reveal()
        self.history.append(location.name)

    def explore(self, map_system):
        if not self.current_location:
            print("🧭 Nie ustawiono miejsca startowego.")
            return

        if not self.current_location.connected_paths:
            print("🔒 Brak połączeń z innymi lokacjami.")
            return

        options = self.current_location.connected_paths
        print("\n🌍 Dostępne ścieżki:")
        for i, loc in enumerate(options):
            print(f"{i+1}. {loc.name} ({loc.special_type}, zagrożenie: {loc.danger_level})")

        try:
            choice = int(input("➡️  Wybierz miejsce do eksploracji: ")) - 1
            next_location = options[choice]
        except:
            print("❌ Błąd wyboru.")
            return

        move_to_location(map_system, self.current_location.name, next_location.name)
        self.current_location = next_location
        self.history.append(next_location.name)
        self.exploration_points += 5

        # Poziomowanie
        if self.exploration_points >= self.level * 20:
            self.level += 1
            self.exploration_points = 0
            print(f"\n🌟 {self.name} osiąga poziom eksploratora {self.level}!")

        # Wydarzenia specjalne
        self.handle_exploration_event()

    def handle_exploration_event(self):
        events = [
            "🗝️ Znaleziono klucz do starożytnej bramy.",
            "📜 Odkryto fragment zaginionej kroniki.",
            "🐉 Napotkano rannego smoka — pomóc czy odejść?",
            "🧙 Tajemniczy mag oferuje teleportację do nieznanej lokacji.",
            "🪦 Natknięto się na stary cmentarz — coś się porusza w cieniu..."
        ]
        chance = random.randint(1, 100)
        if chance < 40:
            event = random.choice(events)
            print(f"\n✨ Wydarzenie specjalne: {event}")
            self.active_events.append(event)

    def get_journal(self):
        print(f"\n📖 Dziennik eksploratora: {self.name}")
        print(f"Poziom: {self.level}, Punkty eksploracji: {self.exploration_points}")
        print("Odwiedzone lokacje:")
        for loc in self.history:
            print(f" - {loc}")
        if self.active_events:
            print("\nWydarzenia napotkane:")
            for e in self.active_events:
                print(f" - {e}")
        else:
            print("Brak wydarzeń.")

# Test systemu eksploracji

if __name__ == "__main__":
    firos_map = generate_full_firos_map()
    player = Explorer("Aelendril")
    player.set_start(firos_map.get_location_by_name("Wiedźmograd"))

    while True:
        player.explore(firos_map)
        more = input("\nEksplorować dalej? (t/n): ")
        if more.lower() != 't':
            break

    player.get_journal()
