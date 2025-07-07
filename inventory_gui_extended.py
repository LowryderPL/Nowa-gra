
import tkinter as tk
from tkinter import messagebox

RARITY_COLORS = {
    "zwykły": "#cccccc",
    "rzadki": "#3399ff",
    "epicki": "#9933ff",
    "legendarny": "#ffcc00"
}

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

        self.base_stats = {"attack": 10, "defense": 5, "magic": 5}
        self.equipment_stats = {"attack": 0, "defense": 0, "magic": 0}

        self.weight_limit = 100
        self.equipped_slots = {
            "Head": None, "Torso": None, "Arms": None, "Legs": None,
            "Main Weapon": None, "Off-Hand": None, "Backpack": None,
            "Belt": None, "Amulet": None, "Ring Left": None,
            "Ring Right": None, "Rune": None
        }

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        tk.Label(self.master, text="🎒 Plecak:").grid(row=0, column=0, sticky='w')
        self.inventory_listbox = tk.Listbox(self.master, width=50)
        self.inventory_listbox.grid(row=1, column=0, rowspan=15)
        self.inventory_listbox.bind("<Double-1>", self.equip_item)

        tk.Label(self.master, text="🛡 Wyposażenie:").grid(row=0, column=1, sticky='w')
        self.equipped_labels = {}
        for i, slot in enumerate(self.equipped_slots.keys()):
            tk.Label(self.master, text=f"{slot}:").grid(row=i+1, column=1, sticky='e')
            label = tk.Label(self.master, text="(puste)", width=30, anchor='w')
            label.grid(row=i+1, column=2, sticky='w')
            self.equipped_labels[slot] = label

        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=15, column=0, sticky='w')

        self.xp_label = tk.Label(self.master, text="")
        self.xp_label.grid(row=15, column=1, sticky='w')

        self.stats_label = tk.Label(self.master, text="")
        self.stats_label.grid(row=16, column=0, sticky='w')

        tk.Button(self.master, text="🔥 Spal za XP", command=self.burn_item).grid(row=17, column=0)
        tk.Button(self.master, text="⬆️ Ulepsz", command=self.upgrade_item).grid(row=17, column=1)
        tk.Button(self.master, text="📦 Zobacz plecak", command=self.show_inventory).grid(row=17, column=2)

    def update_display(self):
        self.inventory_listbox.delete(0, tk.END)
        for item in self.inventory:
            rarity = item.get("rarity", "zwykły")
            display = f"{item['name']} (Lvl {item.get('level', 1)}, {rarity})"
            self.inventory_listbox.insert(tk.END, display)

        total_weight = sum(item.get("weight", 0) for item in self.inventory)
        self.status_label.config(text=f"⚖ Waga: {total_weight} / {self.weight_limit}")
        self.xp_label.config(text=f"🎖 Poziom: {self.level} | XP: {self.xp} | TON: {self.ton}")

        self.update_stats_display()

    def update_stats_display(self):
        total_attack = self.base_stats["attack"]
        total_defense = self.base_stats["defense"]
        total_magic = self.base_stats["magic"]

        for item in self.equipped_slots.values():
            if item:
                total_attack += item.get("attack", 0)
                total_defense += item.get("defense", 0)
                total_magic += item.get("magic", 0)

        self.stats_label.config(text=f"⚔ Atak: {total_attack} | 🛡 Obrona: {total_defense} | ✨ Magia: {total_magic}")

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
        messagebox.showinfo("🔥 Spalone", f"{item['name']} zniszczony.
Zyskano {gained_xp} XP.")
        self.check_level_up()
        self.update_display()

    def upgrade_item(self):
        idx = self.inventory_listbox.curselection()
        if not idx:
            messagebox.showwarning("Brak wyboru", "Wybierz przedmiot.")
            return
        item = self.inventory[idx[0]]
        cost = item.get("level", 1) * 5
        if self.xp < cost:
            messagebox.showwarning("❌ XP", f"Potrzeba {cost} XP.")
            return
        self.xp -= cost
        item["level"] += 1
        messagebox.showinfo("⬆️ Ulepszono", f"{item['name']} awansował na poziom {item['level']}!")
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
            contents = "\n".join([f"{item['name']} (Lvl {item.get('level', 1)})" for item in self.inventory])
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
            {"name": "Mikstura Życia", "slot": "Backpack", "level": 1, "rarity": "zwykły", "allowed_classes": ["All"], "attack": 0, "defense": 0},
            {"name": "Runa Cienia", "slot": "Rune", "level": 2, "rarity": "rzadki", "allowed_classes": ["Mag"], "magic": 15},
            {"name": "Hełm Wilka", "slot": "Head", "level": 3, "rarity": "epicki", "allowed_classes": ["Wojownik", "Rogue"], "defense": 8},
        ]
    }

    root = tk.Tk()
    app = InventoryGUI(root, player)
    root.mainloop()
