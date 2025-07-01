
import tkinter as tk
from PIL import Image, ImageTk

class WorldMapExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title("World of Firos - Map Explorer")

        self.canvas = tk.Canvas(self.master, width=1152, height=768, bg='black')
        self.canvas.pack()

        # Wczytaj mapę świata
        map_image_path = "assets/world_map/world_of_firos.png"
        try:
            self.map_image = Image.open(map_image_path)
            self.map_photo = ImageTk.PhotoImage(self.map_image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.map_photo)
        except Exception as e:
            self.canvas.create_text(500, 300, text="Mapa nie znaleziona: " + str(e), fill="white", font=("Arial", 20))
            return

        # Lokacje (można dodać więcej punktów)
        self.locations = {
            "Dalhal": (530, 460),
            "Grimwood": (500, 620),
            "Ruins of Koroth": (420, 290),
            "Yesoroth": (670, 150),
            "Ashen Lake": (730, 340),
            "River Styx": (370, 400),
            "Wastelands": (300, 100)
        }

        # Narysuj punkty
        for name, (x, y) in self.locations.items():
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
            self.canvas.create_text(x+30, y, text=name, fill="white", font=("Arial", 10), anchor="w")

        # Ruchomy pionek
        self.token = self.canvas.create_oval(530-6, 460-6, 530+6, 460+6, fill="gold", tags="player")
        self.current_position = [530, 460]

        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

    def move_up(self, event): self._move(0, -10)
    def move_down(self, event): self._move(0, 10)
    def move_left(self, event): self._move(-10, 0)
    def move_right(self, event): self._move(10, 0)

    def _move(self, dx, dy):
        self.current_position[0] += dx
        self.current_position[1] += dy
        self.canvas.move(self.token, dx, dy)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldMapExplorer(root)
    root.mainloop()
