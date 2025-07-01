
import tkinter as tk
from tkinter import messagebox

class CraftingGUI:
    def __init__(self, master, inventory, xp):
        self.master = master
        self.master.title("Crafting System")
        self.inventory = inventory
        self.xp = xp

        self.recipes = {
            "Fire Sword": {"components": ["Iron Sword", "Fire Essence"], "xp_cost": 10},
            "Healing Potion": {"components": ["Herb", "Water Flask"], "xp_cost": 5},
            "Steel Armor": {"components": ["Iron Plate", "Leather Straps"], "xp_cost": 15}
        }

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=f"XP: {self.xp}").grid(row=0, column=0, columnspan=2)
        tk.Label(self.master, text="Available Recipes").grid(row=1, column=0)
        self.recipe_listbox = tk.Listbox(self.master, height=6, width=30)
        self.recipe_listbox.grid(row=2, column=0)
        for recipe in self.recipes:
            self.recipe_listbox.insert(tk.END, recipe)

        tk.Button(self.master, text="Craft", command=self.craft_item).grid(row=3, column=0)

        tk.Label(self.master, text="Inventory").grid(row=1, column=1)
        self.inv_text = tk.Text(self.master, height=10, width=30)
        self.inv_text.grid(row=2, column=1, rowspan=2)

        tk.Button(self.master, text="Smelt Item", command=self.smelt_item).grid(row=4, column=0)

        self.update_inventory_display()

    def update_inventory_display(self):
        self.inv_text.delete(1.0, tk.END)
        for item in self.inventory:
            self.inv_text.insert(tk.END, f"{item['name']}
")

    def craft_item(self):
        selected = self.recipe_listbox.curselection()
        if not selected:
            return

        recipe_name = self.recipe_listbox.get(selected[0])
        recipe = self.recipes[recipe_name]
        components = recipe["components"]
        xp_cost = recipe["xp_cost"]

        if self.xp < xp_cost:
            messagebox.showwarning("Not enough XP", f"You need {xp_cost} XP to craft this.")
            return

        inventory_names = [item["name"] for item in self.inventory]
        if all(comp in inventory_names for comp in components):
            for comp in components:
                for i, item in enumerate(self.inventory):
                    if item["name"] == comp:
                        del self.inventory[i]
                        break
            self.inventory.append({"name": recipe_name, "slot": "none", "weight": 1})
            self.xp -= xp_cost
            self.update_inventory_display()
            messagebox.showinfo("Crafted", f"You crafted a {recipe_name}!")
        else:
            messagebox.showwarning("Missing components", "You don't have all required components.")

    def smelt_item(self):
        if not self.inventory:
            messagebox.showinfo("Inventory empty", "No items to smelt.")
            return
        item = self.inventory.pop()
        self.xp += 2
        self.update_inventory_display()
        messagebox.showinfo("Smelted", f"Smelted {item['name']} for 2 XP.")
