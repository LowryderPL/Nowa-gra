import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
QUESTS_FILE = os.path.join(DATA_DIR, 'quests.json')
PLAYER_FILE = os.path.join(DATA_DIR, 'player_data.json')

def load_quests():
    with open(QUESTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_player():
    if not os.path.exists(PLAYER_FILE):
        return {"quests": []}
    with open(PLAYER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_player(data):
    with open(PLAYER_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class QuestsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Zadania")
        self.master.geometry("600x500")

        self.quests = load_quests()
        self.player = load_player()
        self.completed_quests = self.player.get("quests", [])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Dostępne Zadania", font=("Arial", 16)).pack(pady=10)

        self.listbox = tk.Listbox(self.master, width=50, height=15)
        self.listbox.pack()

        for quest in self.quests:
            status = "✔️" if quest["id"] in self.completed_quests else "🕘"
            self.listbox.insert(tk.END, f"{status} {quest['name']}")

        tk.Button(self.master, text="Szczegóły", command=self.show_details).pack(pady=10)

    def show_details(self):
        selected = self.listbox.curselection()
        if not selected:
            return

        index = selected[0]
        quest = self.quests[index]
        status = "WYKONANE" if quest["id"] in self.completed_quests else "DO ZROBIENIA"

        response = messagebox.askyesno("Szczegóły zadania",
            f"{quest['name']}

{quest['description']}

Status: {status}

Czy oznaczyć jako ukończone?")
        if response and quest["id"] not in self.completed_quests:
            self.completed_quests.append(quest["id"])
            self.player["quests"] = self.completed_quests
            save_player(self.player)
            self.listbox.delete(index)
            self.listbox.insert(index, f"✔️ {quest['name']}")
            messagebox.showinfo("Ukończono", f"Zadanie '{quest['name']}' zostało ukończone!")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestsGUI(root)
    root.mainloop()