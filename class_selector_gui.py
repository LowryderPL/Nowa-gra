import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

class ClassSelectorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wybór Klasy i Frakcji")
        self.master.geometry("600x500")

        self.klasy = load_json("klasy.json")
        self.frakcje = load_json("frakcje.json")

        self.selected_klasa = tk.StringVar()
        self.selected_frakcja = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Wybierz klasę postaci:", font=("Arial", 14)).pack(pady=10)
        self.klasy_box = ttk.Combobox(self.master, values=[k["nazwa"] for k in self.klasy], textvariable=self.selected_klasa)
        self.klasy_box.pack(pady=5)
        self.klasy_box.bind("<<ComboboxSelected>>", self.update_klasa_info)

        self.klasa_info = tk.Label(self.master, text="", wraplength=500, justify="left")
        self.klasa_info.pack(pady=5)

        tk.Label(self.master, text="Wybierz frakcję:", font=("Arial", 14)).pack(pady=10)
        self.frakcje_box = ttk.Combobox(self.master, values=[f["nazwa"] for f in self.frakcje], textvariable=self.selected_frakcja)
        self.frakcje_box.pack(pady=5)
        self.frakcje_box.bind("<<ComboboxSelected>>", self.update_frakcja_info)

        self.frakcja_info = tk.Label(self.master, text="", wraplength=500, justify="left")
        self.frakcja_info.pack(pady=5)

        tk.Button(self.master, text="Zatwierdź wybór", command=self.confirm_selection).pack(pady=20)

    def update_klasa_info(self, event=None):
        klasa = next((k for k in self.klasy if k["nazwa"] == self.selected_klasa.get()), None)
        if klasa:
            self.klasa_info.config(text=f"{klasa['opis']}\nStyl: {klasa['styl']}")

    def update_frakcja_info(self, event=None):
        frakcja = next((f for f in self.frakcje if f["nazwa"] == self.selected_frakcja.get()), None)
        if frakcja:
            self.frakcja_info.config(text=f"{frakcja['opis']}\nStyl: {frakcja['styl']}")

    def confirm_selection(self):
        if not self.selected_klasa.get() or not self.selected_frakcja.get():
            messagebox.showwarning("Błąd", "Musisz wybrać klasę i frakcję!")
            return
        player_data = {
            "klasa": self.selected_klasa.get(),
            "frakcja": self.selected_frakcja.get(),
            "xp": 0,
            "ranga": 1,
            "inventory": [],
            "quests": []
        }
        save_path = os.path.join(DATA_DIR, "player_data.json")
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(player_data, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Gotowe", "Postać zapisana! Możesz rozpocząć grę.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClassSelectorGUI(root)
    root.mainloop()