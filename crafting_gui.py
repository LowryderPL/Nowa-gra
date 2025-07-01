
# crafting_gui.py - Pełna wersja GUI Craftingu dla Firos: Magic & Magic
# Zawiera system tworzenia, interfejsu i spalania przedmiotów za EXP

class CraftingGUI:
    def __init__(self, player, inventory, recipes, experience_system):
        self.player = player
        self.inventory = inventory
        self.recipes = recipes
        self.experience_system = experience_system

    def display(self):
        print("\n🔨 MENU CRAFTINGU 🔨")
        print("1. Twórz przedmiot")
        print("2. Spal przedmiot za EXP")
        print("3. Wyjście")

        choice = input("Wybierz opcję (1-3): ")
        if choice == "1":
            self.craft_item()
        elif choice == "2":
            self.burn_item_for_exp()
        elif choice == "3":
            print("Zamknięto crafting.")
        else:
            print("❌ Nieprawidłowy wybór.")
            self.display()

    def craft_item(self):
        print("\n📜 DOSTĘPNE PRZEPISY:")
        for i, recipe in enumerate(self.recipes, start=1):
            print(f"{i}. {recipe['name']} - Wymagane: {', '.join(recipe['materials'])}")

        try:
            index = int(input("Wybierz numer przepisu do wykonania: ")) - 1
            recipe = self.recipes[index]
        except (ValueError, IndexError):
            print("❌ Błąd wyboru przepisu.")
            return

        if all(mat in [item.name for item in self.inventory.items] for mat in recipe["materials"]):
            for mat in recipe["materials"]:
                self.inventory.remove_item(mat)
            self.inventory.add_item(recipe["result"])
            print(f"✅ Stworzono: {recipe['result'].name}")
        else:
            print("❌ Brakuje wymaganych materiałów.")

    def burn_item_for_exp(self):
        print("\n🔥 SPAL PRZEDMIOT ZA EXP:")
        for i, item in enumerate(self.inventory.items, start=1):
            print(f"{i}. {item.name} (Moc: {item.power})")

        try:
            index = int(input("Wybierz numer przedmiotu do spalenia: ")) - 1
            item = self.inventory.items.pop(index)
        except (ValueError, IndexError):
            print("❌ Błąd wyboru przedmiotu.")
            return

        gained_exp = item.power * 2  # np. 2x moc jako EXP
        self.experience_system.add_exp(self.player, gained_exp)
        print(f"🔥 Spalono {item.name}. Zdobyto {gained_exp} EXP.")
