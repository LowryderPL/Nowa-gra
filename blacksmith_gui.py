import tkinter as tk
from tkinter import messagebox
from blacksmith import Blacksmith

class BlacksmithGUI:
    def __init__(self, root, inventory, player_stats):
        self.root = root
        self.inventory = inventory
        self.player_stats = player_stats
        self.bs = Blacksmith(inventory, player_stats)

        self.root.title("Kowal Runiczny - Firos")
        self.root.geometry("500x360")
        self.root.configure(bg="#1e1e1e")

        self.selected_item = tk.StringVar()
        self.message = tk.StringVar()

        self._build_interface()

    def _build_interface(self):
        tk.Label(self.root, text="🔨 Wybierz przedmiot do ulepszenia:", fg="white", bg="#1e1e1e", font=("Helvetica", 12)).pack(pady=10)

        items = list(self.inventory.keys())
        if items:
            self.selected_item.set(items[0])
        self.dropdown = tk.OptionMenu(self.root, self.selected_item, *items)
        self.dropdown.config(bg="#444", fg="white", font=("Helvetica", 10))
        self.dropdown["menu"].config(bg="#333", fg="white")
        self.dropdown.pack(pady=5)

        self.info_label = tk.Label(self.root, text="", fg="#ccc", bg="#1e1e1e", font=("Helvetica", 10))
        self.info_label.pack(pady=5)

        tk.Button(self.root, text="Ulepsz przedmiot", command=self.upgrade_item, bg="#5a2", fg="white", font=("Helvetica", 11, "bold")).pack(pady=10)
        tk.Label(self.root, textvariable=self.message, fg="#4caf50", bg="#1e1e1e", wraplength=420, font=("Helvetica", 10)).pack(pady=10)

        tk.Button(self.root, text="Zamknij", command=self.root.quit, bg="#a22", fg="white").pack(pady=5)

        self.selected_item.trace("w", self.update_info)
        self.update_info()

    def update_info(self, *args):
        item_name = self.selected_item.get()
        if item_name:
            item = self.inventory[item_name]
            level = item.get("level", 0)
            cost = self.bs._calculate_upgrade_cost(level)
            self.info_label.config(
                text=f"Poziom: {level}  |  Koszt: RFN {cost['rfn']}, Złoto {cost['gold']}, Mat. {cost['materials']}, Zwoje {cost['scrolls']}"
            )

    def upgrade_item(self):
        item_name = self.selected_item.get()
        if item_name:
            result = self.bs.upgrade_item(item_name)
            self.message.set(result)
            self.update_info()

# Przykładowe uruchomienie testowe (odkomentuj tylko jeśli testujesz lokalnie)
# if __name__ == "__main__":
#     inventory = {
#         "Miecz Smoczy": {"level": 1, "type": "broń"},
#         "Zbroja Feniksa": {"level": 0, "type": "zbroja"}
#     }
#     stats = {"rfn": 1500, "gold": 4000, "materials": 8, "scrolls": 3, "class": "Wojownik"}

#     root = tk.Tk()
#     app = BlacksmithGUI(root, inventory, stats)
#     root.mainloop()
