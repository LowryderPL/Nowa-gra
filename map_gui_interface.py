
import json

class FirosMapExplorer:
    def __init__(self, map_path="firos_world_map_data.json", graph_path="firos_adjacency_graph.json"):
        with open(map_path, "r", encoding="utf-8") as f:
            self.locations = {loc["id"]: loc for loc in json.load(f)}
        with open(graph_path, "r", encoding="utf-8") as f:
            self.graph = {node["id"]: node["connections"] for node in json.load(f)}
        self.current_location = None

    def list_locations(self):
        print("📜 Wszystkie Lokacje w Świecie Firos:")
        for loc in self.locations.values():
            print(f"- {loc['name']} [{loc['type']} | {loc['faction']}]")

    def enter_location(self, loc_name):
        match = next((loc for loc in self.locations.values() if loc["name"].lower() == loc_name.lower()), None)
        if match:
            self.current_location = match["id"]
            self.describe_location()
        else:
            print(f"❌ Lokacja '{loc_name}' nie istnieje.")

    def describe_location(self):
        if not self.current_location:
            print("Nie jesteś w żadnej lokacji.")
            return
        loc = self.locations[self.current_location]
        print(f"📍 Jesteś w: {loc['name']}")
        print(f"Frakcja: {loc['faction']}")
        print(f"Typ: {loc['type']}, Biom: {loc['biome']}")
        print(f"Boss obecny: {'TAK' if loc['has_boss'] else 'Nie'}")
        print("Połączenia:")
        for neighbor_id in self.graph[loc["id"]]:
            n = self.locations[neighbor_id]
            print(f"→ {n['name']} ({n['type']})")

    def travel_to(self, target_name):
        if not self.current_location:
            print("Musisz najpierw wejść do jakiejś lokacji.")
            return
        target = next((loc for loc in self.locations.values() if loc["name"].lower() == target_name.lower()), None)
        if target and target["id"] in self.graph[self.current_location]:
            self.current_location = target["id"]
            self.describe_location()
        else:
            print(f"❌ Nie możesz przejść do '{target_name}' z tej lokacji.")

if __name__ == "__main__":
    explorer = FirosMapExplorer()
    explorer.list_locations()
    print("\nAby wejść do lokacji, wpisz: explorer.enter_location('Nazwa')")
    print("Aby podróżować, wpisz: explorer.travel_to('Nazwa')")
