
import tkinter as tk
import random

class ChessMode:
    def __init__(self, master):
        self.master = master
        self.master.title("Tryb Szachowy – Firos")

        self.canvas = tk.Canvas(self.master, width=480, height=480, bg="darkgreen")
        self.canvas.pack()

        self.board = []
        self.selected = None

        self.init_board()
        self.place_units()

        self.canvas.bind("<Button-1>", self.on_click)

    def init_board(self):
        self.tiles = {}
        size = 60
        for row in range(8):
            for col in range(8):
                x0 = col * size
                y0 = row * size
                x1 = x0 + size
                y1 = y0 + size
                color = "white" if (row + col) % 2 == 0 else "black"
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.tiles[(row, col)] = rect

    def place_units(self):
        # Przykładowe jednostki gracza i wroga
        self.units = {
            (7, 0): {"type": "Gracz", "name": "Rycerz"},
            (7, 1): {"type": "Gracz", "name": "Mag"},
            (0, 6): {"type": "Wróg", "name": "Striga"},
            (0, 7): {"type": "Wróg", "name": "Cyclops"}
        }

        for pos, data in self.units.items():
            x, y = pos[1]*60 + 30, pos[0]*60 + 30
            color = "blue" if data["type"] == "Gracz" else "red"
            data["token"] = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
            self.canvas.create_text(x, y, text=data["name"][0], fill="white", font=("Arial", 10))

    def on_click(self, event):
        col = event.x // 60
        row = event.y // 60
        pos = (row, col)

        if pos in self.units:
            if self.units[pos]["type"] == "Gracz":
                self.selected = pos
        elif self.selected:
            # Przesuwanie pionka
            unit = self.units.pop(self.selected)
            self.units[pos] = unit
            self.canvas.move(unit["token"], (col - self.selected[1]) * 60, (row - self.selected[0]) * 60)
            self.selected = None
            self.check_battle(pos)

    def check_battle(self, pos):
        # Jeśli po ruchu zajęto pozycję wroga
        enemy_positions = [p for p in self.units if self.units[p]["type"] == "Wróg"]
        if pos in enemy_positions:
            enemy = self.units.pop(pos)
            self.canvas.delete(enemy["token"])
            self.canvas.create_text(240, 10, text="Wróg pokonany!", fill="yellow", font=("Arial", 14))

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessMode(root)
    root.mainloop()
