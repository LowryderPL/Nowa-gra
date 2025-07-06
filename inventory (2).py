
# inventory.py — Pełna wersja systemu ekwipunku (GUI + logika + integracja z grą)

import json
import os

class Inventory:
    def __init__(self, max_size=30):
        self.items = []
        self.max_size = max_size
        self.load_inventory()

    def load_inventory(self, path="data/inventory.json"):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self.items = json.load(f)
        else:
            self.items = []

    def save_inventory(self, path="data/inventory.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

    def add_item(self, item):
        if len(self.items) >= self.max_size:
            return "❌ Brak miejsca w plecaku."
        self.items.append(item)
        self.save_inventory()
        return f"✅ Dodano: {item['name']}"

    def remove_item(self, item_name):
        for item in self.items:
            if item["name"] == item_name:
                self.items.remove(item)
                self.save_inventory()
                return f"🗑️ Usunięto: {item_name}"
        return "❌ Przedmiot nie znaleziony."

    def use_item(self, item_name, player):
        for item in self.items:
            if item["name"] == item_name:
                effect = item.get("effect", "")
                if "HP" in effect:
                    player["health"] = min(player["max_health"], player["health"] + int(effect.replace("HP", "")))
                elif "Mana" in effect:
                    player["mana"] = min(player["max_mana"], player["mana"] + int(effect.replace("Mana", "")))
                self.items.remove(item)
                self.save_inventory()
                return f"✅ Użyto {item_name} ({effect})"
        return "❌ Nie posiadasz tego przedmiotu."

    def show_inventory(self):
        if not self.items:
            return "🎒 Plecak jest pusty."
        return "\n".join([f"{item['name']} (lvl {item['level']}) — {item['rarity']}" for item in self.items])

    def has_item(self, item_name):
        return any(item["name"] == item_name for item in self.items)

# Test
if __name__ == "__main__":
    inv = Inventory()
    player = {"health": 70, "max_health": 100, "mana": 30, "max_mana": 50}
    print(inv.add_item({"name": "Mikstura Życia", "level": 1, "rarity": "zwykły", "effect": "30HP"}))
    print(inv.use_item("Mikstura Życia", player))
    print(inv.show_inventory())
    print("HP gracza:", player["health"])
