
# crafting_gui_expanded.py - pełna wersja GUI Craftingu z kategoriami, spalaniem i połączeniem z innymi systemami

import inventory
import xp_system
import random

class CraftingGUI:
    def __init__(self, player):
        self.player = player
        self.recipes = {
            "Broń": [
                {"name": "Miecz z kości", "materials": {"kość": 5, "drewno": 2}, "power": 10},
                {"name": "Topór cienia", "materials": {"obsydian": 3, "stal": 2}, "power": 18}
            ],
            "Zbroje": [
                {"name": "Skórzana zbroja", "materials": {"skóra": 10, "nić": 5}, "power": 8},
                {"name": "Pancerz runiczny", "materials": {"stal": 5, "runa ochrony": 1}, "power": 22}
            ],
            "Mikstury": [
                {"name": "Mikstura leczenia", "materials": {"ziele": 3, "woda": 1}, "power": 0},
                {"name": "Mikstura many", "materials": {"niebieski kryształ": 2, "woda": 1}, "power": 0}
            ],
            "Runy": [
                {"name": "Runa ognia", "materials": {"magiczny pył": 2, "kamień": 1}, "power": 5}
            ]
        }

    def show_menu(self):
        print("\n--- Crafting GUI ---")
        print("1. Tworzenie przedmiotu")
        print("2. Spal przedmiot za EXP")
        print("3. Wyjście")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            self.crafting_menu()
        elif choice == "2":
            self.burn_item()
        else:
            print("Zamknięto GUI Craftingu.")

    def crafting_menu(self):
        print("\nKategorie craftingu:")
        for i, category in enumerate(self.recipes.keys(), 1):
            print(f"{i}. {category}")
        cat_index = int(input("Wybierz kategorię: ")) - 1
        category = list(self.recipes.keys())[cat_index]

        for i, recipe in enumerate(self.recipes[category], 1):
            print(f"{i}. {recipe['name']} - wymagane: {recipe['materials']}")

        item_index = int(input("Wybierz przedmiot do stworzenia: ")) - 1
        recipe = self.recipes[category][item_index]

        if all(self.player.inventory.has_item(k, v) for k, v in recipe["materials"].items()):
            for k, v in recipe["materials"].items():
                self.player.inventory.remove_item(k, v)
            self.player.inventory.add_item(recipe["name"])
            print(f"Stworzono przedmiot: {recipe['name']}!")
        else:
            print("Brak wymaganych materiałów.")

    def burn_item(self):
        print("\n--- Spal przedmiot ---")
        self.player.inventory.list_items()
        item = input("Wpisz nazwę przedmiotu do spalenia: ")
        if self.player.inventory.has_item(item):
            power = random.randint(5, 20)
            self.player.inventory.remove_item(item)
            self.player.exp += power
            print(f"Spalono {item} za {power} EXP!")
            xp_system.update_level(self.player)
        else:
            print("Brak takiego przedmiotu.")

# Przykładowy test:
if __name__ == "__main__":
    class Player:
        def __init__(self):
            self.inventory = inventory.Inventory()
            self.exp = 0
            self.level = 1
    player = Player()
    gui = CraftingGUI(player)
    gui.show_menu()
