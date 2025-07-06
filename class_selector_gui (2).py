
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
        self.master.geometry("700x600")

        self.klasy = load_json("klasy.json")
        self.frakcje = load_json("frakcje.json")

        self.selected_klasa = tk.StringVar()
        self.selected_frakcja = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="🧙 Wybierz klasę postaci:", font=("Arial", 14)).pack(pady=5)
        self.klasy_box = ttk.Combobox(self.master, values=[k["nazwa"] for k in self.klasy], textvariable=self.selected_klasa)
        self.klasy_box.pack(pady=5)
        self.klasy_box.bind("<<ComboboxSelected>>", self.update_klasa_info)

        self.klasa_info = tk.Label(self.master, text="", wraplength=650, justify="left")
        self.klasa_info.pack(pady=10)

        tk.Label(self.master, text="🏰 Wybierz frakcję:", font=("Arial", 14)).pack(pady=5)
        self.frakcje_box = ttk.Combobox(self.master, values=[f["nazwa"] for f in self.frakcje], textvariable=self.selected_frakcja)
        self.frakcje_box.pack(pady=5)

        self.frakcja_info = tk.Label(self.master, text="", wraplength=650, justify="left")
        self.frakcja_info.pack(pady=10)
        self.frakcje_box.bind("<<ComboboxSelected>>", self.update_frakcja_info)

        tk.Button(self.master, text="✅ Zatwierdź wybór", command=self.submit).pack(pady=20)

    def update_klasa_info(self, event):
        selected = self.selected_klasa.get()
        for klasa in self.klasy:
            if klasa["nazwa"] == selected:
                opis = f"{klasa['opis']}

Rangi:
- {klasa['rangi'][0]}
- {klasa['rangi'][1]}
- {klasa['rangi'][2]}"
                self.klasa_info.config(text=opis)
                break

    def update_frakcja_info(self, event):
        selected = self.selected_frakcja.get()
        for frakcja in self.frakcje:
            if frakcja["nazwa"] == selected:
                opis = f"{frakcja['opis']}"
                self.frakcja_info.config(text=opis)
                break

    def submit(self):
        if not self.selected_klasa.get() or not self.selected_frakcja.get():
            messagebox.showwarning("Błąd", "Musisz wybrać klasę i frakcję!")
            return
        messagebox.showinfo("Wybrano", f"Wybrałeś klasę: {self.selected_klasa.get()}
Frakcję: {self.selected_frakcja.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClassSelectorGUI(root)
    root.mainloop()
