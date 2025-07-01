
import random
import tkinter as tk
from tkinter import messagebox

class GwentMode:
    def __init__(self, master):
        self.master = master
        self.master.title("Tryb Gwint – Pojedynek Kartowy")

        self.deck_player = self.generate_deck("player")
        self.deck_enemy = self.generate_deck("enemy")

        self.label = tk.Label(self.master, text="Rozpoczynasz pojedynek w stylu Gwint!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.battle_button = tk.Button(self.master, text="Rozegraj Rundę", command=self.play_round)
        self.battle_button.pack(pady=5)

        self.result_text = tk.Text(self.master, height=10, width=50)
        self.result_text.pack()

    def generate_deck(self, owner):
        # Tymczasowe karty testowe – do rozbudowy z bazy
        if owner == "player":
            return [("Rycerz", 5), ("Mag", 6), ("Elf", 4), ("Zwiadowca", 3), ("Olbrzym", 8)]
        else:
            return [("Ghul", 4), ("Striga", 7), ("Wraith", 5), ("Ice Troll", 6), ("Cyclops", 9)]

    def play_round(self):
        if not self.deck_player or not self.deck_enemy:
            self.result_text.insert(tk.END, "Gra zakończona. Przetasuj talie.
")
            return

        card_player = self.deck_player.pop(0)
        card_enemy = self.deck_enemy.pop(0)

        self.result_text.insert(tk.END, f"Gracz: {card_player[0]} ({card_player[1]})  VS  "
                                        f"Wróg: {card_enemy[0]} ({card_enemy[1]})
")

        if card_player[1] > card_enemy[1]:
            self.result_text.insert(tk.END, "→ Gracz wygrywa rundę!

")
        elif card_player[1] < card_enemy[1]:
            self.result_text.insert(tk.END, "→ Wróg wygrywa rundę!

")
        else:
            self.result_text.insert(tk.END, "→ Remis!

")

if __name__ == "__main__":
    root = tk.Tk()
    app = GwentMode(root)
    root.mainloop()
