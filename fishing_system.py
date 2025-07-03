
import random
import json
import os
from datetime import datetime

FISH_LOG_FILE = "fish_log.json"

FISH_TYPES = {
    "Common Carp": {"rarity": "common", "value": 5, "chance": 0.45},
    "Silver Perch": {"rarity": "common", "value": 6, "chance": 0.25},
    "Golden Trout": {"rarity": "rare", "value": 20, "chance": 0.15},
    "Ghost Eel": {"rarity": "epic", "value": 50, "chance": 0.08},
    "Abyssal Pike": {"rarity": "legendary", "value": 100, "chance": 0.04},
    "Kraken Tentacle": {"rarity": "mythic", "value": 500, "chance": 0.03}
}

LOCATIONS = {
    "Village Lake": {"bonus": 0.0},
    "Mystic River": {"bonus": 0.05},
    "Haunted Swamp": {"bonus": 0.1},
    "Frozen Fjord": {"bonus": 0.2},
    "Depths of Firos": {"bonus": 0.3}
}

class FishingSystem:
    def __init__(self):
        self.log = []
        self.load_log()

    def load_log(self):
        if os.path.exists(FISH_LOG_FILE):
            with open(FISH_LOG_FILE, 'r') as f:
                self.log = json.load(f)

    def save_log(self):
        with open(FISH_LOG_FILE, 'w') as f:
            json.dump(self.log, f, indent=4)

    def fish(self, player_name, location_name):
        if location_name not in LOCATIONS:
            return None, "Invalid location"
        location_bonus = LOCATIONS[location_name]["bonus"]

        roll = random.random()
        cumulative = 0.0
        for fish, data in FISH_TYPES.items():
            chance = data["chance"] + location_bonus
            cumulative += chance
            if roll < cumulative:
                entry = {
                    "player": player_name,
                    "fish": fish,
                    "rarity": data["rarity"],
                    "value": data["value"],
                    "location": location_name,
                    "timestamp": datetime.utcnow().isoformat()
                }
                self.log.append(entry)
                self.save_log()
                return entry, f"{player_name} caught a {fish} at {location_name}!"

        return None, f"{player_name} caught nothing..."

    def get_log(self, player_name=None):
        if player_name:
            return [entry for entry in self.log if entry["player"] == player_name]
        return self.log
