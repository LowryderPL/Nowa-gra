
import json
import random

class FirosWorldExplorer:
    def __init__(self, map_file="firos_world_map_data.json", graph_file="firos_adjacency_graph.json"):
        with open(map_file, "r", encoding="utf-8") as f:
            self.locations = {loc["id"]: loc for loc in json.load(f)}
        with open(graph_file, "r", encoding="utf-8") as f:
            self.graph = {node["id"]: node["connections"] for node in json.load(f)}
        self.current_location = None
        self.visited = set()

    def list_locations(self):
        for loc in self.locations.values():
            print(f"- {loc['name']} ({loc['type']}, {loc['faction']})")

    def enter(self, name):
        loc = next((l for l in self.locations.values() if l["name"].lower() == name.lower()), None)
        if not loc:
            print("❌ Nie znaleziono takiej lokacji.")
            return
        self.current_location = loc["id"]
        self.describe(loc)

    def describe(self, loc):
        print(f"📍 {loc['name']} ({loc['type']}) - {loc['faction']}")
        print(f"Biom: {loc['biome']}")
        print(f"Boss: {'✅ TAK' if loc['has_boss'] else '—'}")
        print(f"Opis: {loc['description']}")
        self.trigger_event(loc)

        print("\n🔗 Możesz podróżować do:")
        for nid in self.graph[loc["id"]]:
            nloc = self.locations[nid]
            print(f"→ {nloc['name']} ({nloc['type']})")

    def travel_to(self, name):
        if not self.current_location:
            print("Musisz najpierw wejść do lokacji.")
            return
        target = next((l for l in self.locations.values() if l["name"].lower() == name.lower()), None)
        if not target:
            print("❌ Nie znaleziono lokacji.")
            return
        if target["id"] not in self.graph[self.current_location]:
            print("❌ Nie możesz tam przejść bezpośrednio.")
            return
        self.current_location = target["id"]
        self.describe(target)

    def trigger_event(self, loc):
        if loc["id"] in self.visited:
            print("🕯️ Miejsce już odwiedzone, nic się nie dzieje.")
            return
        self.visited.add(loc["id"])
        print("🎲 Rzucam kością przygody...")
        roll = random.randint(1, 10)
        if roll <= 2:
            print("💀 Zostałeś zaatakowany przez dzikie stwory!")
        elif roll <= 4:
            print("📜 Znalazłeś tajemniczy zwój z zaklęciem.")
        elif roll <= 6:
            print("💰 Otrzymujesz skrzynię z nagrodą!")
        elif roll == 7:
            print("🎯 Spotykasz NPC-a z zadaniem.")
        else:
            print("🌫️ Cisza i spokój. Miejsce puste...")

if __name__ == "__main__":
    explorer = FirosWorldExplorer()
    explorer.list_locations()
    print("\nAby wejść: explorer.enter('Nazwa')")
    print("Aby podróżować: explorer.travel_to('Nazwa')")
