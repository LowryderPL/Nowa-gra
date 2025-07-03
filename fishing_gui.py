
"""
🎣 GUI – Łowienie Ryb (FIROS)
System GUI do łowienia ryb: wybór lokalizacji, pokaz wyniku, punkty akcji (PA), obrazki ryb
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from extended.fishing_system import FishingSystem, FISH_TYPES, LOCATIONS, PLAYER_PA

class FishingGUI:
    def __init__(self, master, player_name="Gracz1"):
        self.master = master
        self.player = player_name
        self.fishing = FishingSystem()

        master.title("Łowienie Ryb – Firos")

        tk.Label(master, text="Wybierz lokalizację:").pack()
        self.location_var = tk.StringVar()
        self.location_menu = ttk.Combobox(master, textvariable=self.location_var)
        self.location_menu["values"] = list(LOCATIONS.keys())
        self.location_menu.current(0)
        self.location_menu.pack()

        self.pa_label = tk.Label(master, text=f"Punkty Akcji: {PLAYER_PA['current']}/{PLAYER_PA['max']}")
        self.pa_label.pack(pady=4)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=5)

        tk.Button(master, text="Złów rybę", command=self.catch_fish).pack(pady=10)

    def catch_fish(self):
        location = self.location_var.get()
        entry, result = self.fishing.fish(self.player, location)
        self.result_label.config(text=result)
        self.pa_label.config(text=f"Punkty Akcji: {PLAYER_PA['current']}/{PLAYER_PA['max']}")

        if entry:
            image_path = FISH_TYPES[entry["fish"]].get("image")
            if image_path and os.path.exists(image_path):
                img = Image.open(image_path).resize((100, 100))
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo
            else:
                self.image_label.config(image="", text="(brak grafiki)")

if __name__ == "__main__":
    root = tk.Tk()
    app = FishingGUI(root)
    root.mainloop()
