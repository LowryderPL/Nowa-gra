# alchemy_gui.py – GUI do systemu alchemii
# Zintegrowane z alchemy.py

import tkinter as tk
from tkinter import messagebox
from alchemy import Alchemy

class AlchemyGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Warsztat Alchemiczny")
        self.master.geometry("700x600")
        self.master.configure(bg="#2d2d2d")

        self.alchemy = Alchemy()
        self.selected_ingredients = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.master, text="🧪 Alchemia: Tworzenie Mikstur", font=("Georgia", 18, "bold"), fg="#00ffcc", bg="#2d2d2d")
        title.pack(pady=10)

        # Lista receptur
        self.recipe_listbox = tk.Listbox(self.master, width=60, height=12, bg="#1e1e1e", fg="#ffffff", font=("Courier", 11))
        self.recipe_listbox.pack(pady=10)

        for recipe in self.alchemy.recipes:
            self.recipe_listbox.insert(tk.END, f"{recipe.name} ({recipe.category}) – {', '.join(recipe.ingredients)}")

        # Składniki (ręczne wybieranie)
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

        # Przyciski
        btn_frame = tk.Frame(self.master, bg="#2d2d2d")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Stwórz 🧪", command=self.create_potion, bg="#00cc99", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="📦 Plecak", command=self.show_backpack, bg="#444444", fg="white", font=("Arial", 11)).grid(row=0, column=1, padx=10)

    def create_potion(self):
        ing1 = self.ing1_entry.get().strip().lower()
        ing2 = self.ing2_entry.get().strip().lower()
        ing3 = self.ing3_entry.get().strip().lower()

        ingredients = [i for i in [ing1, ing2, ing3] if i]
        if not ingredients:
            messagebox.showwarning("Błąd", "Wprowadź przynajmniej 2 składniki.")
            return

        result = self.alchemy.craft(ingredients)
        messagebox.showinfo("Wynik alchemii", result)

    def show_backpack(self):
        messagebox.showinfo("📦 Plecak", self.alchemy.show_backpack())

# Uruchomienie GUI (do testów lokalnych)
if __name__ == "__main__":
    root = tk.Tk()
    app = AlchemyGUI(root)
    root.mainloop()
