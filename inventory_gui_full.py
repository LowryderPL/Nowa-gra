import tkinter as tk
from tkinter import messagebox

class InventoryGUI:
    def __init__(self, master, player):
        self.master = master
        self.master.title("Ekwipunek FIROS")
        self.player = player
        self.inventory = player["inventory"]
        self.character_class = player["class"]
        self.level = player.get("level", 1)
        self.xp = player.get("xp", 0)
        self.ton = player.get("ton", 0)

        self.weight_limit = 100
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
        self.update_display()

    def create_widgets(self):
        tk.Label(self.master, text="🎒 Plecak:").grid(row=0, column=0, sticky='w')
        self.inventory_listbox = tk.Listbox(self.master, width=50)
        self.inventory_listbox.grid(row=1, column=0, rowspan=12)
        self.inventory_listbox.bind("<Double-1>", self.equip_item)

        tk.Label(self.master, text="🛡 Wyposażenie:").grid(row=0, column=1, sticky='w')
        self.equipped_labels = {}
        for i, slot in enumerate(self.equipped_slots.keys()):
            tk.Label(self.master, text=f"{slot}:").grid(row=i+1, column=1, sticky='e')
            label = tk.Label(self.master, text="(puste)", width=30, anchor='w')
            label.grid(row=i+1, column=2, sticky='w')
            self.equipped_labels[slot] = label

        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=13, column=0, sticky='w')

        self.xp_label = tk.Label(self.master, text="")
        self.xp_label.grid(row=13, column=1, sticky='w')

        tk.Button(self.master, text="🔥 Spal za XP", command=self.burn_item).grid(row=14, column=0)
        tk.Button(self.master, text="📦 Zobacz plecak", command=self.show_inventory).grid(row=14, column=1)

    def update_display(self):
        self.inventory_listbox.delete(0, tk.END)
        for item in self.inventory:
            rarity = item.get("rarity", "zwykły")
            self.inventory_listbox.insert(tk.END, f"{item['name']} (Rzadkość: {rarity})")

        total_weight = sum(item.get("weight", 0) for item in self.inventory)
        self.status_label.config(text=f"⚖ Waga: {total_weight} / {self.weight_limit}")
        self.xp_label.config(text=f"🎖 Poziom: {self.level} | XP: {self.xp} | TON: {self.ton}")

    def equip_item(self, event):
        idx = self.inventory_listbox.curselection()
        if not idx:
            return
        item = self.inventory[idx[0]]
        slot = item.get("slot")
        level_req = item.get("level", 1)
        allowed = item.get("allowed_classes", ["All"])

        if self.character_class not in allowed and "All" not in allowed:
            messagebox.showwarning("❌ Klasa", "Nie możesz założyć tego przedmiotu.")
            return
        if self.level < level_req:
            messagebox.showwarning("❌ Poziom", f"Potrzebny poziom {level_req}.")
            return

        self.equipped_slots[slot] = item
        self.equipped_labels[slot].config(text=f"{item['name']}")
        self.inventory.pop(idx[0])
        self.update_display()

    def burn_item(self):
        idx = self.inventory_listbox.curselection()
        if not idx:
            messagebox.showwarning("Brak wyboru", "Wybierz przedmiot.")
            return
        item = self.inventory.pop(idx[0])
        gained_xp = item.get("level", 1) * 10
        self.xp += gained_xp
        messagebox.showinfo("🔥 Spalone", f"{item['name']} zniszczony.\nZyskano {gained_xp} XP.")
        self.check_level_up()
        self.update_display()

    def check_level_up(self):
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            messagebox.showinfo("🎉 Awans!", f"Nowy poziom: {self.level}!")

    def show_inventory(self):
        if not self.inventory:
            messagebox.showinfo("📦 Plecak", "Plecak jest pusty.")
        else:
            contents = "\n".join([f"{item['name']} (Lvl {item['level']})" for item in self.inventory])
            messagebox.showinfo("📦 Plecak", contents)

# --- PRZYKŁAD UŻYCIA ---
if __name__ == "__main__":
    player = {
        "health": 70,
        "max_health": 100,
        "mana": 40,
        "max_mana": 100,
        "class": "Mag",
        "level": 1,
        "xp": 0,
        "ton": 1.0,
        "inventory": [
            {"name": "Mikstura Życia", "slot": "Backpack", "level": 1, "rarity": "zwykły", "allowed_classes": ["All"]},
            {"name": "Runa Cienia", "slot": "Rune", "level": 2, "rarity": "rzadki", "allowed_classes": ["Mag"]},
            {"name": "Hełm Wilka", "slot": "Head", "level": 3, "rarity": "epicki", "allowed_classes": ["Wojownik", "Rogue"]},
        ]
    }

    root = tk.Tk()
    app = InventoryGUI(root, player)
    root.mainloop()
