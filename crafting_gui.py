# crafting_gui.py – GUI do systemu rzemiosła w FIROS
# Zintegrowane z crafting.py

import tkinter as tk
from tkinter import messagebox
from crafting import Crafting

class CraftingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Warsztat Rzemieślniczy")
        self.master.geometry("700x600")
        self.master.configure(bg="#2d2d2d")

        self.crafting = Crafting()
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.master, text="🛠️ Rzemiosło: Tworzenie Przedmiotów", font=("Georgia", 18, "bold"), fg="#ffcc00", bg="#2d2d2d")
        title.pack(pady=10)

        self.recipe_listbox = tk.Listbox(self.master, width=60, height=12, bg="#1e1e1e", fg="#ffffff", font=("Courier", 11))
        self.recipe_listbox.pack(pady=10)

        for recipe in self.crafting.recipes:
            self.recipe_listbox.insert(tk.END, f"{recipe.name} ({recipe.category}) – {', '.join(recipe.ingredients)}")

        ing_frame = tk.Frame(self.master, bg="#2d2d2d")
        ing_frame.pack()

        tk.Label(ing_frame, text="Składnik 1:", fg="#cccccc", bg="#2d2d2d").grid(row=0, column=0)
        self.ing1_entry = tk.Entry(ing_frame)
        self.ing1_entry.grid(row=0, column=1, padx=5)

        tk.Label(ing_frame, text="Składnik 2:", fg="#cccccc", bg="#2d2d2d").grid(row=1, column=0)
        self.ing2_entry = tk.Entry(ing_frame)
        self.ing2_entry.grid(row=1, column=1, padx=5)

        tk.Label(ing_frame, text="Składnik 3 (opc.):", fg="#cccccc", bg="#2d2d2d").grid(row=2, column=0)
        self.ing3_entry = tk.Entry(ing_frame)
        self.ing3_entry.grid(row=2, column=1, padx=5)

        btn_frame = tk.Frame(self.master, bg="#2d2d2d")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🛠️ Stwórz", command=self.create_item, bg="#ff9900", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="📦 Plecak", command=self.show_backpack, bg="#444444", fg="white", font=("Arial", 11)).grid(row=0, column=1, padx=10)

    def create_item(self):
        ing1 = self.ing1_entry.get().strip().lower()
        ing2 = self.ing2_entry.get().strip().lower()
        ing3 = self.ing3_entry.get().strip().lower()

        ingredients = [i for i in [ing1, ing2, ing3] if i]
        if len(ingredients) < 2:
            messagebox.showwarning("Błąd", "Wprowadź przynajmniej 2 składniki.")
            return

        result = self.crafting.craft(ingredients)
        messagebox.showinfo("Wynik rzemiosła", result)

    def show_backpack(self):
        messagebox.showinfo("📦 Plecak", self.crafting.show_backpack())


# Test GUI lokalny
if __name__ == "__main__":
    root = tk.Tk()
    app = CraftingGUI(root)
    root.mainloop()
