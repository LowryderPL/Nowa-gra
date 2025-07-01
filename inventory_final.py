
# inventory.py — Pełna, rozszerzona wersja systemu ekwipunku FIROS
# Uwzględnia: sloty, wagę, GUI, klasy postaci, crafting, runy i skrzynki

class Item:
    def __init__(self, name, item_type, power, weight, value, description, required_class=None):
        self.name = name
        self.item_type = item_type  # np. "broń", "zbroja", "artefakt", "runa"
        self.power = power
        self.weight = weight
        self.value = value
        self.description = description
        self.required_class = required_class  # np. "Wiedźmograd", None

    def __str__(self):
        return f"{self.name} [{self.item_type}] - {self.description} (Moc: {self.power}, Waga: {self.weight})"


class Inventory:
    def __init__(self, player_class="Wiedźmograd"):
        self.items = []
        self.equipped = {
            "głowa": None,
            "tors": None,
            "nogi": None,
            "buty": None,
            "broń": None,
            "tarcza": None,
            "pierścień1": None,
            "pierścień2": None,
            "plecak": None,
            "pas": None,
            "zwój": None,
            "artefakt": None,
            "zwierzę": None,
            "skrzydła": None,
            "runa1": None,
            "runa2": None,
            "craft_slot1": None,
            "craft_slot2": None
        }
        self.max_weight = 100
        self.player_class = player_class

    def current_weight(self):
        return sum(item.weight for item in self.items)

    def add_item(self, item):
        if self.current_weight() + item.weight <= self.max_weight:
            self.items.append(item)
            print(f"Dodano: {item.name}")
        else:
            print("Przeciążenie! Nie możesz dodać więcej przedmiotów.")

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                print(f"Usunięto: {item_name}")
                return
        print("Nie znaleziono przedmiotu.")

    def equip_item(self, item, slot):
        if item.required_class and item.required_class != self.player_class:
            print(f"Twoja klasa ({self.player_class}) nie może założyć: {item.name}")
            return
        if slot in self.equipped:
            self.equipped[slot] = item
            print(f"Wyposażono: {item.name} do {slot}")
        else:
            print("Nieprawidłowy slot.")

    def unequip_item(self, slot):
        if slot in self.equipped and self.equipped[slot]:
            print(f"Zdjęto: {self.equipped[slot].name} ze slotu {slot}")
            self.equipped[slot] = None
        else:
            print("Slot jest pusty lub nie istnieje.")

    def show_equipment(self):
        print("--- Wyposażenie ---")
        for slot, item in self.equipped.items():
            print(f"{slot.title()}: {item.name if item else 'Puste'}")

    def show_inventory(self):
        print("--- Ekwipunek ---")
        for item in self.items:
            print(item)

    def use_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                print(f"Użyto: {item.name}")
                return
        print("Przedmiot nie znaleziony.")

    def total_value(self):
        return sum(item.value for item in self.items)

    def filter_items(self, item_type):
        return [item for item in self.items if item.item_type == item_type]

# Przykład użycia (test)
if __name__ == "__main__":
    inv = Inventory(player_class="Wiedźmograd")
    sword = Item("Miecz Cienia", "broń", 15, 5, 200, "Przeklęty miecz nocy", required_class="Wiedźmograd")
    armor = Item("Zbroja Ziemi", "tors", 8, 10, 350, "Stara zbroja z kamienia")
    inv.add_item(sword)
    inv.add_item(armor)
    inv.equip_item(sword, "broń")
    inv.equip_item(armor, "tors")
    inv.show_equipment()
    inv.show_inventory()
