import tkinter as tk
import json

class ClassSelectorGUI:
    def __init__(self, master, class_file="class.json"):
        self.master = master
        self.master.title("Wybór Klasy Postaci")
        self.master.configure(bg="#1a1a1a")
        self.class_file = class_file
        self.classes = self.load_classes()

        self.selected_class = None
        self.create_widgets()

    def load_classes(self):
        with open(self.class_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def create_widgets(self):
        title = tk.Label(self.master, text="Wybierz swoją klasę", font=("Georgia", 18, "bold"), fg="white", bg="#1a1a1a")
        title.pack(pady=10)

        self.listbox = tk.Listbox(self.master, width=40, height=10, bg="#2a2a2a", fg="white", font=("Courier", 12))
        self.listbox.pack()
        for cls in self.classes:
            self.listbox.insert(tk.END, cls["name"])

        self.info_text = tk.Text(self.master, height=12, width=60, bg="#202020", fg="#dddddd", font=("Arial", 10))
        self.info_text.pack(pady=10)

        self.listbox.bind("<<ListboxSelect>>", self.show_class_info)

        self.confirm_button = tk.Button(self.master, text="✅ Wybierz klasę", command=self.confirm_class, bg="#00cc66",
