
class Item:
    def __init__(self, name, weight, item_type, required_class=None):
        self.name = name
        self.weight = weight
        self.item_type = item_type
        self.required_class = required_class

class Inventory:
    def __init__(self, character_class):
        self.character_class = character_class
        self.slots = {
            "głowa": None,
            "klatka": None,
            "nogi": None,
            "buty": None,
            "broń": None,
            "tarcza": None,
            "plecak": [],
            "pas": [],
            "zwój": [],
            "artefakt": [],
            "zwierzę": None,
            "skrzydła": None,
            "interfejs_runiczny": [],
            "skrzynki": [],
            "craftingowe_sloty": []
        }
        self.max_weight = 100
        self.current_weight = 0

    def can_equip(self, item):
        if item.required_class and item.required_class != self.character_class:
            return False
        return True

    def add_item(self, slot, item):
        if not self.can_equip(item):
            return f"Nie można założyć przedmiotu: wymagana klasa {item.required_class}"
        if self.current_weight + item.weight > self.max_weight:
            return "Przekroczono limit wagi!"
        if isinstance(self.slots[slot], list):
            self.slots[slot].append(item)
        else:
            self.slots[slot] = item
        self.current_weight += item.weight
        return f"Dodano {item.name} do {slot}"

    def remove_item(self, slot, item_name=None):
        if isinstance(self.slots[slot], list):
            for i, item in enumerate(self.slots[slot]):
                if item.name == item_name:
                    self.current_weight -= item.weight
                    del self.slots[slot][i]
                    return f"Usunięto {item.name} z {slot}"
        elif self.slots[slot]:
            self.current_weight -= self.slots[slot].weight
            removed = self.slots[slot]
            self.slots[slot] = None
            return f"Usunięto {removed.name} z {slot}"
        return "Nie znaleziono przedmiotu"

    def show_inventory(self):
        output = f"Klasa postaci: {self.character_class}
Aktualna waga: {self.current_weight}/{self.max_weight}
"
        for slot, item in self.slots.items():
            if isinstance(item, list):
                output += f"{slot.title()}: {[i.name for i in item]}
"
            elif item:
                output += f"{slot.title()}: {item.name}
"
            else:
                output += f"{slot.title()}: Pusto
"
        return output
