
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class AlchemyGUI:
    def __init__(self, master, inventory, xp):
        self.master = master
        self.master.title("Księga Alchemii")
        self.inventory = inventory
        self.xp = xp

        self.recipes = {
            "Eliksir Życia": {"components": ["Czerwony Korzeń", "Woda"], "xp_cost": 5, "effect": "Przywraca 20 HP"},
            "Mutagen Cienia": {"components": ["Cień Mrocznego Wilka", "Krew"], "xp_cost": 10, "effect": "+10 Uniku, -5 HP"},
            "Esencja Ognia": {"components": ["Siarczysta Żywica", "Olej"], "xp_cost": 7, "effect": "Podpala broń"}
        }

        self.create_widgets()

    def create_widgets(self):
        try:
            bg_image = Image.open("alchemy_background_main.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            canvas = tk.Canvas(self.master, width=bg_image.width, height=bg_image.height)
            canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
            canvas.grid(row=0, column=0, columnspan=3)
        except:
            tk.Label(self.master, text="Księga Alchemii", font=("Papyrus", 16, "bold")).grid(row=0, column=0, columnspan=3)

        tk.Label(self.master, text=f"XP: {self.xp}").grid(row=1, column=0, sticky='w')

        tk.Label(self.master, text="Receptury").grid(row=2, column=0)
        self.recipe_listbox = tk.Listbox(self.master, width=30)
        self.recipe_listbox.grid(row=3, column=0, rowspan=4)
        for name in self.recipes:
            self.recipe_listbox.insert(tk.END, name)

        self.effect_label = tk.Label(self.master, text="Efekt: ", wraplength=200)
        self.effect_label.grid(row=7, column=0, sticky="w")

        tk.Button(self.master, text="Utwórz miksturę", command=self.craft_potion).grid(row=8, column=0, pady=5)

        tk.Label(self.master, text="Składniki").grid(row=2, column=1)
        self.inventory_text = tk.Text(self.master, width=30, height=10)
        self.inventory_text.grid(row=3, column=1, rowspan=4)

        self.update_inventory_display()

    def update_inventory_display(self):
        self.inventory_text.delete(1.0, tk.END)
        for item in self.inventory:
            self.inventory_text.insert(tk.END, f"{item['name']}\n")

    def craft_potion(self):
        selected = self.recipe_listbox.curselection()
        if not selected:
            return

        name = self.recipe_listbox.get(selected[0])
        recipe = self.recipes[name]
        components = recipe["components"]
        xp_cost = recipe["xp_cost"]
        effect = recipe["effect"]

        if self.xp < xp_cost:
            messagebox.showwarning("Brak XP", f"Potrzeba {xp_cost} XP.")
            return

        inv_names = [item["name"] for item in self.inventory]
        if all(comp in inv_names for comp in components):
            for comp in components:
                for i, item in enumerate(self.inventory):
                    if item["name"] == comp:
                        del self.inventory[i]
                        break
            self.inventory.append({"name": name, "slot": "none", "weight": 0.5})
            self.xp -= xp_cost
            self.update_inventory_display()
            self.effect_label.config(text=f"Efekt: {effect}")
            messagebox.showinfo("Utworzono", f"Stworzono: {name}\nEfekt: {effect}")
        else:
            messagebox.showwarning("Brak składników", "Nie masz wszystkich składników.")
