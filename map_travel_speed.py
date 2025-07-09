
class MapTravelSystem:
    def __init__(self, player):
        self.player = player
        self.base_pa_cost = 10  # base cost per move in PA

    def get_travel_cost(self):
        mount = self.player.mount
        if not mount:
            return self.base_pa_cost
        # Apply bonus based on mount bonus
        bonus = mount.get("bonus", "")
        if "+10% movement speed" in bonus:
            return int(self.base_pa_cost * 0.9)
        elif "+15% stealth" in bonus:
            return self.base_pa_cost  # no PA bonus
        elif "+5% defense" in bonus:
            return int(self.base_pa_cost * 0.95)
        elif "+20% terror radius" in bonus:
            return self.base_pa_cost  # affects NPCs, not PA
        elif "+10% forest travel speed" in bonus:
            return int(self.base_pa_cost * 0.85)
        else:
            return self.base_pa_cost

    def move_to(self, location):
        cost = self.get_travel_cost()
        if self.player.pa >= cost:
            self.player.pa -= cost
            self.player.current_location = location
            print(f"🚶 Travelled to {location}. Remaining PA: {self.player.pa}")
        else:
            print("❌ Not enough PA to travel.")

    def show_travel_info(self):
        print(f"📍 Current location: {self.player.current_location}")
        print(f"⚡ Travel cost: {self.get_travel_cost()} PA")
