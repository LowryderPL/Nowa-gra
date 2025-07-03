
"""
💼 GUI – SZAFKI HANDLOWE (FIROS)
GUI do wystawiania, przeglądania i usuwania przedmiotów handlowych gracza.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from extended.trading_stalls import TradingStallsSystem

class TradingGUI:
    def __init__(self, master, player_name="Gracz1"):
        self.master = master
        self.player = player_name
        self.stalls = TradingStallsSystem()

        master.title("Szafka Handlowa – Firos")

        tk.Label(master, text="Przedmiot:").pack()
        self.item_var = tk.StringVar()
        tk.Entry(master, textvariable=self.item_var).pack()

        tk.Label(master, text="Cena (RFM):").pack()
        self.price_var = tk.StringVar()
        tk.Entry(master, textvariable=self.price_var).pack()

        tk.Label(master, text="Ilość:").pack()
        self.qty_var = tk.StringVar()
        tk.Entry(master, textvariable=self.qty_var).pack()

        tk.Button(master, text="➕ Wystaw Przedmiot", command=self.add_item).pack(pady=4)
        tk.Button(master, text="📋 Pokaż Moje Oferty", command=self.show_items).pack(pady=2)
        tk.Button(master, text="❌ Usuń Ofertę", command=self.remove_item).pack(pady=2)

        self.output = tk.Text(master, height=8, width=40)
        self.output.pack(pady=5)

    def add_item(self):
        name = self.item_var.get()
        try:
            price = int(self.price_var.get())
            qty = int(self.qty_var.get())
            result = self.stalls.add_stall(self.player, name, price, qty)
            messagebox.showinfo("Sukces", result)
        except ValueError:
            messagebox.showerror("Błąd", "Cena i ilość muszą być liczbami.")

    def show_items(self):
        offers = self.stalls.get_stalls(filter_by_owner=self.player)
        self.output.delete("1.0", tk.END)
        if offers:
            for o in offers:
                self.output.insert(tk.END, f"{o['item_name']} x{o['quantity']} za {o['price']} RFM\n")
        else:
            self.output.insert(tk.END, "Brak ofert.")

    def remove_item(self):
        name = self.item_var.get()
        result = self.stalls.remove_stall(self.player, name)
        messagebox.showinfo("Usunięto", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingGUI(root)
    root.mainloop()
