
from location_manager_full import LocationManager

class WorldMap:
    def __init__(self):
        self.location_manager = LocationManager()
        self.map_data = []

    def generate_map_points(self, count=20, category=None):
        self.map_data = []
        used = set()
        for _ in range(count):
            loc = self.location_manager.get_random(category)
            while loc in used:
                loc = self.location_manager.get_random(category)
            used.add(loc)
            self.map_data.append(loc)
        return self.map_data

    def show_map(self):
        print("📍 MAPA ŚWIATA FIROS:")
        for idx, loc in enumerate(self.map_data, 1):
            print(f"{idx}. {loc}")
