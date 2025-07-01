
# crafting.py
from inventory import Inventory

class CraftingSystem:
    def __init__(self, player_inventory):
        self.inventory = player_inventory
        self.recipes = {
            "Iron Sword": {"Iron Ore": 3, "Wood": 1},
            "Steel Armor": {"Steel Ingot": 5, "Leather": 2},
            "Elixir of Health": {"Red Herb": 2, "Water Flask": 1},
        }

    def can_craft(self, item_name):
        if item_name not in self.recipes:
            return False
        for material, qty in self.recipes[item_name].items():
            if self.inventory.count_item(material) < qty:
                return False
        return True

    def craft(self, item_name):
        if not self.can_craft(item_name):
            return False
        for material, qty in self.recipes[item_name].items():
            self.inventory.remove_item(material, qty)
        self.inventory.add_item(item_name)
        return True

    def get_craftable_items(self):
        return [item for item in self.recipes if self.can_craft(item)]
