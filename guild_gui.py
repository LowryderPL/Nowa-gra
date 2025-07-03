
"""
🏰 GUI – GILDIE (FIROS)
GUI do tworzenia, dołączania, opuszczania gildii z użyciem tkinter
"""

import tkinter as tk
from tkinter import messagebox
from extended.guild_system import GuildSystem

class GuildGUI:
    def __init__(self, master, player_name="Gracz1"):
        self.master = master
        self.player = player_name
        self.guild_system = GuildSystem()

        master.title("Gildie – Firos")

        # Etykieta
        tk.Label(master, text="Zarządzanie Gildią", font=("Arial", 16)).pack(pady=10)

        # Pole nazwy gildii
        self.guild_name_var = tk.StringVar()
        tk.Entry(master, textvariable=self.guild_name_var, width=30).pack(pady=5)

        # Przycisk tworzenia
        tk.Button(master, text="Stwórz Gildię", command=self.create_guild).pack(pady=2)
        tk.Button(master, text="Dołącz do Gildii", command=self.join_guild).pack(pady=2)
        tk.Button(master, text="Opuść Gildię", command=self.leave_guild).pack(pady=2)

        # Info
        self.info_label = tk.Label(master, text="", fg="blue")
        self.info_label.pack(pady=10)

    def create_guild(self):
        name = self.guild_name_var.get()
        success, msg = self.guild_system.create_guild(name, self.player)
        self.info_label.config(text=msg)
        if success:
            messagebox.showinfo("Sukces", msg)
        else:
            messagebox.showerror("Błąd", msg)

    def join_guild(self):
        name = self.guild_name_var.get()
        success, msg = self.guild_system.join_guild(name, self.player)
        self.info_label.config(text=msg)
        if success:
            messagebox.showinfo("Dołączono", msg)
        else:
            messagebox.showwarning("Problem", msg)

    def leave_guild(self):
        name = self.guild_name_var.get()
        success, msg = self.guild_system.leave_guild(name, self.player)
        self.info_label.config(text=msg)
        if success:
            messagebox.showinfo("Opuszczono", msg)
        else:
            messagebox.showerror("Błąd", msg)

# Uruchomienie GUI (testowo)
if __name__ == "__main__":
    root = tk.Tk()
    app = GuildGUI(root)
    root.mainloop()
