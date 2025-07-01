
# npc_simulation.py

import random
import time

class NPC:
    def __init__(self, name, faction, role):
        self.name = name
        self.faction = faction
        self.role = role
        self.gold = random.randint(10, 200)
        self.inventory = []

    def perform_daily_action(self):
        action = random.choice(["trade", "fight", "rest", "explore"])
        if action == "trade":
            self.gold += random.randint(1, 10)
        elif action == "fight":
            self.gold -= random.randint(0, 10)
        elif action == "rest":
            pass
        elif action == "explore":
            found = random.choice(["herb", "scroll", "nothing"])
            if found != "nothing":
                self.inventory.append(found)

    def __repr__(self):
        return f"{self.name} [{self.role} of {self.faction}] - Gold: {self.gold} | Inventory: {self.inventory}"

class WorldSimulator:
    def __init__(self):
        self.npcs = []

    def generate_npcs(self, num=10):
        names = ["Alrik", "Mira", "Joren", "Elya", "Thrag", "Lys", "Vorin", "Kael", "Serah", "Brom"]
        factions = ["Crimson Order", "Emerald Circle", "Obsidian Pact"]
        roles = ["Trader", "Warrior", "Mage", "Hunter"]
        for _ in range(num):
            name = random.choice(names)
            faction = random.choice(factions)
            role = random.choice(roles)
            self.npcs.append(NPC(name, faction, role))

    def simulate_day(self):
        for npc in self.npcs:
            npc.perform_daily_action()

    def display_world_state(self):
        for npc in self.npcs:
            print(npc)

if __name__ == "__main__":
    world = WorldSimulator()
    world.generate_npcs()
    for day in range(3):
        print(f"--- Day {day + 1} ---")
        world.simulate_day()
        world.display_world_state()
        time.sleep(1)
