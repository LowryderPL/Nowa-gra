
from location_manager_full import LocationManager

class DungeonSystem:
    def __init__(self):
        self.location_manager = LocationManager()
        self.available_dungeons = self.location_manager.get_by_type("dungeon")

    def list_dungeons(self):
        return self.available_dungeons

    def get_random_dungeon(self):
        return self.location_manager.get_random("dungeon")
