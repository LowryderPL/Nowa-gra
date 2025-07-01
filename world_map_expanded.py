
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class WorldMapExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title("World of Firos - Map Explorer")

        self.canvas = tk.Canvas(self.master, width=1152, height=768, bg='black')
        self.canvas.pack()

        # Wczytaj mapę
        try:
            self.map_image = Image.open("assets/world_map/world_of_firos.png")
            self.map_photo = ImageTk.PhotoImage(self.map_image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.map_photo)
        except:
            self.canvas.create_text(500, 300, text="Mapa nie znaleziona", fill="white", font=("Arial", 20))
            return

        # Lokacje
        self.locations = {
            "Dalhal": (530, 460),
            "Grimwood": (500, 620),
            "Ruins of Koroth": (420, 290),
            "Yesoroth": (670, 150),
            "Ashen Lake": (730, 340),
            "River Styx": (370, 400),
            "Wastelands": (300, 100)
        }

        # Bossowie (nazwa, pozycja, nagroda, typ lochu)
        self.bosses = {
            "Striga": {"pos": (450, 380), "reward": "Karta Legendarna", "mode": "Gwent"},
            "Ice Troll": {"pos": (600, 600), "reward": "Artefakt Mrozu", "mode": "Heroes"},
            "Cyclops": {"pos": (750, 480), "reward": "Runiczna Pieczęć", "mode": "Szachy"},
            "Wraith": {"pos": (350, 200), "reward": "Złoto i EXP", "mode": "Szachy Magiczne"},
        }

        # Rysuj lokacje
        for name, (x, y) in self.locations.items():
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
            self.canvas.create_text(x+30, y, text=name, fill="white", font=("Arial", 10), anchor="w")

        # Rysuj bossów
        for name, data in self.bosses.items():
            x, y = data["pos"]
            self.canvas.create_oval(x-6, y-6, x+6, y+6, fill="purple")
            self.canvas.create_text(x+35, y, text=name, fill="violet", font=("Arial", 10), anchor="w")

        # Pionek gracza
        self.token = self.canvas.create_oval(530-6, 460-6, 530+6, 460+6, fill="gold", tags="player")
        self.current_position = [530, 460]

        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

        self.canvas.bind("<Button-1>", self.check_click)

    def move_up(self, event): self._move(0, -10)
    def move_down(self, event): self._move(0, 10)
    def move_left(self, event): self._move(-10, 0)
    def move_right(self, event): self._move(10, 0)

    def _move(self, dx, dy):
        self.current_position[0] += dx
        self.current_position[1] += dy
        self.canvas.move(self.token, dx, dy)

    def check_click(self, event):
        for name, data in self.bosses.items():
            bx, by = data["pos"]
            if abs(event.x - bx) < 20 and abs(event.y - by) < 20:
                self.start_boss_battle(name, data)

    def start_boss_battle(self, name, data):
        msg = f"Boss: {name}\nNagroda: {data['reward']}\nTryb walki: {data['mode']}\n\nCzy chcesz rozpocząć bitwę?"
        if messagebox.askyesno("Bitwa z Bossem", msg):
            self.launch_mode(data["mode"])

    def launch_mode(self, mode):
        if mode == "Gwent":
            messagebox.showinfo("Tryb Gwent", "Rozpoczynasz pojedynek kartowy Gwint!")
        elif mode == "Heroes":
            messagebox.showinfo("Tryb Heroes", "Wchodzisz do taktycznej bitwy na mapie jak w Heroes!")
        elif mode == "Szachy":
            messagebox.showinfo("Tryb Szachy", "Pojedynek strategiczny w systemie szachowym!")
        elif mode == "Szachy Magiczne":
            messagebox.showinfo("Tryb Szachy Magiczne", "Zaczynasz magiczne szachy z zaklęciami i potworami!")
        else:
            messagebox.showinfo("Nieznany tryb", f"Tryb {mode} nie jest jeszcze gotowy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldMapExplorer(root)
    root.mainloop()
