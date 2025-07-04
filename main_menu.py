
import tkinter as tk
import subprocess

class FirosMainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Firos: Magic & Magic – Menu Główne")
        self.master.geometry("400x500")
        self.master.configure(bg="#1e1e1e")

        title = tk.Label(master, text="FIROS: MAGIC & MAGIC", font=("Georgia", 18, "bold"), fg="gold", bg="#1e1e1e")
        title.pack(pady=20)

        menu_buttons = [
            ("📖 Księga Zaklęć", "spellbook_gui.py"),
            ("🛡️ Ekwipunek", "inventory_gui.py"),
            ("🧪 Alchemia", "alchemy_gui.py"),
            ("🎒 Crafting", "crafting_gui.py"),
            ("⚔️ Arena PvP", "arena_gui.py"),
            ("📍 Mapa", "world_map.py"),
            ("📚 Misje", "quests.py")
        ]

        for label, script in menu_buttons:
            btn = tk.Button(master, text=label, width=30, height=2, font=("Georgia", 12),
                            command=lambda s=script: self.run_script(s))
            btn.pack(pady=5)

        tk.Button(master, text="❌ Wyjdź", command=self.master.quit, fg="white", bg="darkred", font=("Georgia", 12)).pack(pady=10)

    def run_script(self, script_name):
        try:
            subprocess.Popen(["python", script_name])
        except Exception as e:
            tk.messagebox.showerror("Błąd", f"Nie można uruchomić: {script_name}\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FirosMainMenu(root)
    root.mainloop()
