# inventory_gui.py – Pełna wersja GUI Ekwipunku z zaawansowanymi slotami

class InventoryGUI:
    def __init__(self, inventory):
        self.inventory = inventory

    def display(self):
        print("\n📦 EKWIPUNEK POSTACI:")
        for i, item in enumerate(self.inventory.items, start=1):
            print(f"{i}. {item.name} (typ: {item.type}, moc: {item.power}, waga: {item.weight})")

        print("\n🎽 WYPSAŻENIE:")
        for slot, equipment in self.inventory.slots.items():
            equipped_item = equipment.item.name if equipment.item else "-"
            print(f"{slot.capitalize()}: {equipped_item}")

        print(f"\n🎒 Waga całkowita: {self.inventory.get_total_weight()} / {self.inventory.weight_limit} kg")
        print(f"🔒 Sloty klasowe: {', '.join(self.inventory.allowed_classes)}")

        print("\n📚 INTERFEJSY DODATKOWE:")
        print(" - [S]krzynie")
        print(" - [C]rafting")
        print(" - [R]uny")
        print(" - [B]onusy klasowe")
        print(" - [P]odsumowanie")

    def show_item_details(self, item_name):
        item = next((i for i in self.inventory.items if i.name == item_name), None)
        if item:
            print(f"\n🔍 SZCZEGÓŁY PRZEDMIOTU: {item.name}")
            print(f"Typ: {item.type}")
            print(f"Moc: {item.power}")
            print(f"Waga: {item.weight}")
            print(f"Opis: {item.description if hasattr(item, 'description') else 'brak'}")
            print(f"Limit klasowy: {item.class_limit if hasattr(item, 'class_limit') else 'dowolna'}")
        else:
            print(f"❌ Nie znaleziono przedmiotu o nazwie: {item_name}")

    def interact(self):
        while True:
            self.display()
            cmd = input("\n🧭 Wpisz nazwę przedmiotu, aby zobaczyć szczegóły, lub komendę (S/C/R/B/P/Q): ").lower()
            if cmd in ['q', 'quit', 'exit']:
                break
            elif cmd == 's':
                self.open_chest_gui()
            elif cmd == 'c':
                self.open_crafting_gui()
            elif cmd == 'r':
                self.show_rune_interface()
            elif cmd == 'b':
                self.show_class_bonuses()
            elif cmd == 'p':
                self.summary()
            else:
                self.show_item_details(cmd)

    def open_chest_gui(self):
        print("\n📦 Skrzynie – przegląd przedmiotów skrzyń (funkcja w budowie)")

    def open_crafting_gui(self):
        print("\n🔧 Crafting – tworzenie przedmiotów (funkcja w budowie)")

    def show_rune_interface(self):
        print("\n💠 Runy – przegląd run i ich aktywacji (funkcja w budowie)")

    def show_class_bonuses(self):
        print("\n🧝‍♀️ Bonusy klasowe – obecna klasa: ", self.inventory.player_class)

    def summary(self):
        print("\n📋 PODSUMOWANIE EKWIPUNKU:")
        print(f"Liczba przedmiotów: {len(self.inventory.items)}")
        print(f"Sloty: {len(self.inventory.slots)}")
        print(f"Waga: {self.inventory.get_total_weight()} / {self.inventory.weight_limit}")
