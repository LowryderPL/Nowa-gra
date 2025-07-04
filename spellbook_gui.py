
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import time
from runes_data import RUNES
from xp_system import get_player_xp
from spells_data import SPELLS

class SpellbookGUI:
    def __init__(self, master, player_data):
        self.master = master
        self.master.title("Księga Czarów")
        self.master.geometry("800x600")
        self.player_data = player_data
        self.xp = get_player_xp(player_data)
        self.runes = player_data.get("runes", [])

        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        try:
            self.bg_image = Image.open("spellbook_background.png")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((800, 600)))
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except:
            self.canvas.create_text(400, 300, text="Brak grafiki spellbooka", font=("Times", 24), fill="red")

        self.xp_label = tk.Label(self.master, text=f"XP: {self.xp}", font=("Times", 14), bg="black", fg="white")
        self.xp_label.place(x=30, y=20)

        self.spell_listbox = tk.Listbox(self.master, width=40, height=10, font=("Courier", 12))
        self.spell_listbox.place(x=50, y=80)

        for spell in SPELLS:
            self.spell_listbox.insert(tk.END, f"{spell['name']} (lvl {spell['level_required']})")

        self.cast_button = tk.Button(self.master, text="Rzuć zaklęcie", command=self.cast_spell, font=("Times", 12, "bold"))
        self.cast_button.place(x=300, y=400)

        self.log_label = tk.Label(self.master, text="", font=("Times", 12), bg="black", fg="yellow")
        self.log_label.place(x=50, y=500)

    def cast_spell(self):
        index = self.spell_listbox.curselection()
        if not index:
            return
        spell = SPELLS[index[0]]
        if self.xp < spell["level_required"]:
            messagebox.showwarning("Za mały poziom", "Nie masz wystarczającego poziomu, by rzucić ten czar.")
            return
        bonus = self.check_rune_bonus(spell)
        self.animate_cast(spell["name"], bonus)

    def check_rune_bonus(self, spell):
        for rune in RUNES:
            if rune["name"].lower() in spell["name"].lower() and rune["name"] in self.runes:
                return f"Bonus z runy: {rune['effect']}"
        return "Brak aktywnej runy."

    def animate_cast(self, spell_name, bonus):
        self.log_label.config(text=f"Rzucasz {spell_name}...", fg="orange")
        threading.Thread(target=self._animate_text, args=(spell_name, bonus)).start()

    def _animate_text(self, spell_name, bonus):
        time.sleep(1.5)
        self.log_label.config(text=f"Zaklęcie {spell_name} zadziałało!
{bonus}", fg="lightgreen")

if __name__ == "__main__":
    root = tk.Tk()
    player = {
        "xp": 10,
        "runes": ["Runa Ognia", "Runa Krwi"]
    }
    app = SpellbookGUI(root, player)
    root.mainloop()
