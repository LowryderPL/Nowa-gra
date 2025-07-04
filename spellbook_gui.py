
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class SpellbookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Księga Czarów")
        self.master.geometry("800x600")

        # Tło - załaduj grafikę spellbooka
        try:
            bg_image = Image.open("spellbook_background.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            canvas = tk.Canvas(master, width=bg_image.width, height=bg_image.height)
            canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
            canvas.pack()
        except:
            tk.Label(master, text="Błąd ładowania tła").pack()

        # Przykładowe przyciski czarów
        self.spells = ["Ignacja II", "Błyskawica III", "Lodowa Igła II", "Znak IV"]
        for i, spell in enumerate(self.spells):
            tk.Button(master, text=spell, command=lambda s=spell: self.cast_spell(s)).place(x=50, y=100+i*40)

    def cast_spell(self, spell_name):
        tk.messagebox.showinfo("Rzucono czar", f"Rzucono: {spell_name}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SpellbookGUI(root)
    root.mainloop()
