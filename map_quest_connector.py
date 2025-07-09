
from npc_database import npc_list

class MapQuestConnector:
    def __init__(self):
        self.location_map = {}
        self.build_location_index()

    def build_location_index(self):
        for npc in npc_list:
            loc = npc['location']
            if loc not in self.location_map:
                self.location_map[loc] = []
            self.location_map[loc].append({
                "npc": npc['name'],
                "faction": npc['faction'],
                "quests": [q['title'] for q in npc['quests']]
            })

    def get_quests_for_location(self, location):
        return self.location_map.get(location, [])

    def list_all_locations(self):
        return list(self.location_map.keys())

    def show_location_data(self, location):
        quests = self.get_quests_for_location(location)
        if not quests:
            print(f"📍 {location}: No available quests.")
            return
        print(f"📍 {location} – Available Quests:")
        for entry in quests:
            print(f"🧙 {entry['npc']} ({entry['faction']})")
            for q in entry['quests']:
                print(f"  📘 {q}")
