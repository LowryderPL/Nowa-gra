
"""
💬 CHAT GILDII / GRY (FIROS)
Prosty lokalny chat do rozmów między graczami (symulowany)
"""

import tkinter as tk
import os
import time

CHAT_FILE = "chat_log.txt"

class ChatGUI:
    def __init__(self, master, player_name="Gracz1"):
        self.master = master
        self.player = player_name
        self.master.title("Czat Gildii – Firos")

        self.text_display = tk.Text(master, state='disabled', width=60, height=20, wrap=tk.WORD)
        self.text_display.pack(padx=10, pady=5)

        self.entry_msg = tk.Entry(master, width=40)
        self.entry_msg.pack(side=tk.LEFT, padx=(10,0), pady=10)

        tk.Button(master, text="Wyślij", command=self.send_message).pack(side=tk.LEFT, padx=5)

        self.refresh_chat()

    def send_message(self):
        msg = self.entry_msg.get().strip()
        if msg:
            with open(CHAT_FILE, "a") as f:
                f.write(f"[{self.player}] {msg}\n")
            self.entry_msg.delete(0, tk.END)
            self.refresh_chat()

    def refresh_chat(self):
        if os.path.exists(CHAT_FILE):
            with open(CHAT_FILE, "r") as f:
                lines = f.readlines()
        else:
            lines = []

        self.text_display.config(state='normal')
        self.text_display.delete(1.0, tk.END)
        for line in lines[-20:]:
            self.text_display.insert(tk.END, line)
        self.text_display.config(state='disabled')
        self.master.after(3000, self.refresh_chat)  # auto-odświeżanie

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()
