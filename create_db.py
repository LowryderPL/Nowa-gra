# create_db.py – Tworzy bazę danych firos_game_database.db i wypełnia potworami

import sqlite3
import os

# Nazwa pliku bazy danych
DB_NAME = "firos_game_database.db"

# Utwórz połączenie
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Stwórz tabelę 'creatures' jeśli nie istnieje
cursor.execute("""
CREATE TABLE IF NOT EXISTS creatures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    strength INTEGER,
    weakness TEXT,
    habitat TEXT
)
""")

# Sprawdź, czy tabela już zawiera dane
cursor.execute("SELECT COUNT(*) FROM creatures")
count = cursor.fetchone()[0]

if count == 0:
    print("➕ Dodajemy przykładowe potwory do bestiariusza...")

    # Lista potworów do dodania
    creatures = [
        ("Wilk", "Drapieżnik żyjący w lasach", 20, "Ogień", "Mroczny Las"),
        ("Ghul", "Trupojad występujący na cmentarzach", 35, "Światło", "Cmentarzyska"),
        ("Bazyliszek", "Mityczne stworzenie o paraliżującym spojrzeniu", 60, "Lustro", "Ruiny"),
        ("Upiór", "Duch nienawiści z przeszłości", 45, "Srebro", "Opuszczony Dwór"),
        ("Troll", "Wielki brutalny stwór z gór", 50, "Kwasy", "Jaskinie Skaliste"),
        ("Ent", "Strażnik lasu, drzewiec", 40, "Ogień", "Stare Puszcze")
    ]

    # Wstaw dane do tabeli
    cursor.executemany("""
    INSERT INTO creatures (name, description, strength, weakness, habitat)
    VALUES (?, ?, ?, ?, ?)
    """, creatures)

    print("✅ Bestiariusz został uzupełniony.")
else:
    print("ℹ️ Baza już zawiera dane – nic nie dodano.")

# Zapisz i zamknij
conn.commit()
conn.close()
print("📦 Baza danych gotowa: firos_game_database.db")
