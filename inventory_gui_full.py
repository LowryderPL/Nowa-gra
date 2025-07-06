
import tkinter as tk
from tkinter import messagebox
import json
import os

class InventoryGUI:
    def __init__(self, master, inventory, character_class):
        self.master = master
        self.master.title("Inventory GUI")
        self.inventory = inventory
        self.character_class = character_class
        self.weight_limit = 100
        self.player_xp = 0
        self.player_level = 1

        self.equipped_slots = {
            "Head": None,
            "Torso": None,
            "Arms": None,
            "Legs": None,
            "Main Weapon": None,
            "Off-Hand": None,
            "Backpack": None,
            "Belt": None,
            "Amulet": None,
            "Ring Left": None,
            "Ring Right": None,
            "Rune": None
        }

        self.create_widgets()
        self.update_inventory_display()

    def create_widgets(self):
        tk.Label(self.master, text="Inventory Items:").grid(row=0, column=0)
        self.inventory_listbox = tk.Listbox(self.master, width=40)
        self.inventory_listbox.grid(row=1, column=0, rowspan=10)
        self.inventory_listbox.bind('<Double-1>', self.equip_item)

        tk.Label(self.master, text="Equipped Items:").grid(row=0, column=1)
        self.equipped_labels = {}
        for idx, slot in enumerate(self.equipped_slots.keys()):
            tk.Label(self.master, text=f"{slot}:").grid(row=idx+1, column=1, sticky='e')
            label = tk.Label(self.master, text="None", width=30)
            label.grid(row=idx+1, column=2, sticky='w')
            self.equipped_labels[slot] = label

        self.weight_label = tk.Label(self.master, text="Total Weight: 0 / 100")
        self.weight_label.grid(row=13, column=0, sticky='w')

        self.xp_label = tk.Label(self.master, text="XP: 0 | Level: 1")
        self.xp_label.grid(row=13, column=1, sticky='w')

        self.burn_button = tk.Button(self.master, text="Burn Item for XP", command=self.burn_item)
        self.burn_button.grid(row=14, column=0, pady=5)

        self.craft_button = tk.Button(self.master, text="Open Crafting", command=self.open_crafting)
        self.craft_button.grid(row=14, column=1)

        self.alchemy_button = tk.Button(self.master, text="Open Alchemy", command=self.open_alchemy)
        self.alchemy_button.grid(row=14, column=2)

    def update_inventory_display(self):
        self.inventory_listbox.delete(0, tk.END)
        for item in self.inventory:
            name = item['name']
            rarity = item.get('rarity', 'common')
            display = f"{name} [{item['type']}] ({rarity})"
            self.inventory_listbox.insert(tk.END, display)

        total_weight = sum(item['weight'] for item in self.inventory)
        self.weight_label.config(text=f"Total Weight: {total_weight} / {self.weight_limit}")

    def equip_item(self, event):
        selection = self.inventory_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        item = self.inventory[index]

        if self.character_class not in item.get("allowed_classes", ["All"]):
            messagebox.showwarning("Class Restriction", "Your class cannot equip this item.")
            return

        slot = item["slot"]
        self.equipped_slots[slot] = item
        self.equipped_labels[slot].config(text=item["name"])
        del self.inventory[index]
        self.update_inventory_display()

    def burn_item(self):
        selection = self.inventory_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Select an item to burn.")
            return
        index = selection[0]
        item = self.inventory.pop(index)
        gained_xp = item['value'] // 2
        self.player_xp += gained_xp
        self.check_level_up()
        messagebox.showinfo("Item Burned", f"You gained {gained_xp} XP from burning {item['name']}.")
        self.update_inventory_display()

    def check_level_up(self):
        level_threshold = self.player_level * 100
        while self.player_xp >= level_threshold:
            self.player_level += 1
            self.player_xp -= level_threshold
            level_threshold = self.player_level * 100
            messagebox.showinfo("Level Up!", f"You reached level {self.player_level}!")
        self.xp_label.config(text=f"XP: {self.player_xp} | Level: {self.player_level}")

    def open_crafting(self):
        messagebox.showinfo("Crafting", "Crafting system opening...")

    def open_alchemy(self):
        messagebox.showinfo("Alchemy", "Alchemy system opening...")

# Wczytywanie inventory.json
def load_inventory_from_json(path="inventory.json"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Przykład uruchomienia
if __name__ == "__main__":
    inventory = load_inventory_from_json()
    character_class = "Warrior"
    root = tk.Tk()
    app = InventoryGUI(root, inventory, character_class)
    root.mainloop()
