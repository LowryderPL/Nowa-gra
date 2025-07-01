inventory.py - Rozbudowany system ekwipunku w Firos: Magic & Magic

class Item: def init(self, name, item_type, power=0, weight=1, value=0, description=""): self.name = name self.type = item_type  # np. "zbroja", "mikstura", "artefakt" self.power = power self.weight = weight self.value = value self.description = description

def __str__(self):
    return f"{self.name} ({self.type}) - Moc: {self.power}, Waga: {self.weight}, Wartość: {self.value}" + (f"\nOpis: {self.description}" if self.description else "")

class EquipmentSlot: def init(self, name): self.name = name self.item = None

def equip(self, item):
    self.item = item
    print(f"🛡️ Wyposażono: {item.name} w slocie {self.name}")

def unequip(self):
    if self.item:
        print(f"❌ Zdjęto: {self.item.name} ze slotu {self.name}")
        self.item = None
    else:
        print(f"⚠️ Slot {self.name} jest już pusty.")

def __str__(self):
    return f"{self.name}: {self.item.name if self.item else 'pusty'}"

class Inventory: def init(self, capacity=30): self.slots = { "głowa": EquipmentSlot("głowa"), "tors": EquipmentSlot("tors"), "nogi": EquipmentSlot("nogi"), "buty": EquipmentSlot("buty"), "broń": EquipmentSlot("broń"), "tarcza": EquipmentSlot("tarcza"), "pierścień1": EquipmentSlot("pierścień1"), "pierścień2": EquipmentSlot("pierścień2") ,
        "plecak": None,
        "pas": None,
        "zwój": None,
        "artefakt": None,
        "zwierzę": None,
        "skrzydła": None} self.items = [] self.capacity = capacity

def add_item(self, item):
    if len(self.items) < self.capacity:
        self.items.append(item)
        print(f"➕ Dodano do plecaka: {item.name}")
    else:
        print("❌ Plecak jest pełny!")

def remove_item(self, item_name):
    for i, item in enumerate(self.items):
        if item.name == item_name:
            del self.items[i]
            print(f"❌ Usunięto: {item_name} z plecaka")
            return
    print(f"⚠️ Nie znaleziono przedmiotu: {item_name}")

def show_inventory(self):
    if not self.items:
        print("🎒 Twój plecak jest pusty.")
        return
    print("\n📦 Zawartość plecaka:")
    for item in self.items:
        print("-", item)

def equip_item(self, slot_name, item_name):
    item = next((i for i in self.items if i.name == item_name), None)
    if item and slot_name in self.slots:
        self.slots[slot_name].equip(item)
        self.items.remove(item)
    else:
        print(f"❌ Nie można wyposażyć: {item_name} w slot {slot_name}")

def unequip_item(self, slot_name):
    if slot_name in self.slots:
        item = self.slots[slot_name].item
        self.slots[slot_name].unequip()
        if item:
            self.add_item(item)
    else:
        print(f"⚠️ Slot {slot_name} nie istnieje.")

def show_equipment(self):
    print("\n🧙 Wyposażenie postaci:")
    for slot in self.slots.values():
        print("-", slot)

def use_item(self, item_name):
    item = next((i for i in self.items if i.name == item_name), None)
    if item:
        if item.type == "mikstura":
            print(f"🧪 Użyto mikstury: {item.name} - efekt: +{item.power} HP lub MANA")
            self.items.remove(item)
        else:
            print(f"⚠️ {item.name} nie jest używalnym przedmiotem!")
    else:
        print(f"❌ Brak przedmiotu: {item_name}")

def filter_items(self, item_type):
    filtered = [item for item in self.items if item.type == item_type]
    if filtered:
        print(f"🔍 Przedmioty typu '{item_type}':")
        for item in filtered:
            print("-", item)
    else:
        print(f"❌ Brak przedmiotów typu '{item_type}'")

if name == "main": inv = Inventory() inv.add_item(Item("Hełm Cienia", "zbroja", power=5, description="Lekki hełm z czarnej stali")) inv.add_item(Item("Miecz Żywiołów", "broń", power=10, description="Ognista klinga emanująca mocą")) inv.add_item(Item("Mikstura Życia", "mikstura", power=20, description="Odnawia życie")) inv.show_inventory() inv.equip_item("głowa", "Hełm Cienia") inv.equip_item("broń", "Miecz Żywiołów") inv.show_equipment() inv.use_item("Mikstura Życia") inv.show_inventory()

