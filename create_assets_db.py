# create_assets_db.py – Tworzy bazę danych z grafikami do gry Firos: Magic & Magic

import sqlite3

# Nazwa bazy danych
DB_NAME = "assets_database.db"

# Połączenie z bazą
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Tworzymy tabelę na grafiki
cursor.execute("""
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    filename TEXT NOT NULL,
    description TEXT
)
""")

# Sprawdź, czy już są dane
cursor.execute("SELECT COUNT(*) FROM assets")
count = cursor.fetchone()[0]

# Jeśli pusto – wstawiamy przykładowe wpisy
if count == 0:
    print("➕ Dodajemy przykładowe grafiki do bazy...")

    assets = [
        ("characters", "elf_mage.png", "Elficki mag – domyślny bohater."),
        ("monsters", "ghoul.png", "Ghul – potwór nocy z cmentarzyska."),
        ("items", "ancient_sword.png", "Starożytny miecz – legendarny drop."),
        ("spell_icons", "fireball_icon.png", "Ikona zaklęcia Ognista Kula."),
        ("backgrounds", "dark_forest.jpg", "Tło lokacji: Mroczny Las."),
        ("maps", "ruins_map.png", "Mapa ruin starożytnego miasta."),
        ("ui", "inventory_frame.png", "Ramka interfejsu ekwipunku.")
    ]

    cursor.executemany("""
    INSERT INTO assets (category, filename, description)
    VALUES (?, ?, ?)
    """, assets)

    print("✅ Baza została uzupełniona.")
else:
    print("ℹ️ Baza danych już zawiera wpisy.")

# Zapisz i zamknij
conn.commit()
conn.close()
print(f"📦 Gotowa baza danych: {DB_NAME}")
