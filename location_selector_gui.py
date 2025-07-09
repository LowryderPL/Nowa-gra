
from location_manager_full import LocationManager

class LocationSelectorGUI:
    def __init__(self):
        self.location_manager = LocationManager()

    def show_menu(self):
        locations = self.location_manager.get_all()
        print("=== Wybierz Lokację ===")
        for i, loc in enumerate(locations[:30], 1):  # pokazuje pierwsze 30
            boss = " (BOSS)" if loc.get("boss") else ""
            print(f"{i}. {loc['name']} - {loc['type']} [{loc.get('faction')}] {boss}")
        print("=======================")
