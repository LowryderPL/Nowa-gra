
import tkinter as tk
from tkinter import messagebox

class Faction:
    def __init__(self, name, description, bonuses, image=None):
        self.name = name
        self.description = description
        self.bonuses = bonuses
        self.image = image

# Przykładowe frakcje
factions = [
    Faction(
        name="Redania",
        description="Imperium militarne, wierzące w siłę i dominację. Frakcja obdarzona zwiększonymi punktami ataku.",
        bonuses="+5% obrażeń fizycznych, +10% obrona w zamkach",
    ),
    Faction(
        name="Kaedwen",
        description="Kraina łowców i najemników, specjalizująca się w atakach z ukrycia.",
        bonuses="+15% do ataków z zaskoczenia, +10% do kradzieży",
    ),
    Faction(
        name="Nilfgaard",
        description="Cesarstwo znane z magii, szpiegostwa i dominacji ekonomicznej.",
        bonuses="+10% do czarów, +5% szansa na unikanie ciosów",
    ),
    Faction(
        name="Skellige",
        description="Wyspiarscy wojownicy żyjący według surowych zasad. Silni w PvP.",
        bonuses="+20% do walk PvP, +15% odporność",
    ),
]

def choose_faction(faction):
    with open("chosen_faction.txt", "w") as f:
        f.write(faction.name)
    messagebox.showinfo("Frakcja wybrana", f"Wybrałeś frakcję: {faction.name}")

def create_faction_gui():
    root = tk.Tk()
    root.title("Wybór Frakcji - Świat Firos")

    canvas = tk.Canvas(root, width=700, height=500)
    canvas.pack()

    y = 20
    for faction in factions:
        frame = tk.Frame(root, borderwidth=2, relief="ridge", bg="#2c2c2c")
        frame.place(x=20, y=y, width=660, height=100)

        label = tk.Label(frame, text=f"{faction.name}", font=("Georgia", 14, "bold"), fg="white", bg="#2c2c2c")
        label.place(x=10, y=5)

        desc = tk.Label(frame, text=faction.description, wraplength=500, justify="left", fg="#dddddd", bg="#2c2c2c")
        desc.place(x=10, y=30)

        bonus = tk.Label(frame, text=f"Bonusy: {faction.bonuses}", fg="#99cc00", bg="#2c2c2c")
        bonus.place(x=10, y=70)

        btn = tk.Button(frame, text="Wybierz", command=lambda f=faction: choose_faction(f))
        btn.place(x=580, y=35)

        y += 110

    root.mainloop()

if __name__ == "__main__":
    create_faction_gui()
