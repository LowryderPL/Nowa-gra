
import sqlite3

# Ścieżka do Twojej bazy danych
db_path = "firos_game_database.db"  # Upewnij się, że ścieżka jest poprawna

# Połączenie z bazą danych
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tworzenie tabeli na NFT, jeśli nie istnieje
cursor.execute("""
CREATE TABLE IF NOT EXISTS nft_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rarity TEXT,
    crafting TEXT,
    attributes TEXT,
    available TEXT
)
""")

# Przykładowe dane NFT
nft_cards = [
    {
        "name": "Znachorka",
        "rarity": "Epic",
        "crafting": "Eliksir Wilczego Kła, Zioła Snów, Korzeń Wieszczki",
        "attributes": "Leczenie 9, Alchemia 10, Inteligencja 8",
        "available": "TON, RFN"
    },
    {
        "name": "Berserker z Gór",
        "rarity": "Rare",
        "crafting": "Kamień Furii, Kość Trolla",
        "attributes": "Siła 10, Wściekłość 9, Obrona 6",
        "available": "RFN"
    },
    {
        "name": "Nekromanta",
        "rarity": "Legendary",
        "crafting": "Proch Umarłych, Krew Demona",
        "attributes": "Magia Ciemności 10, Mana 9",
        "available": "TON"
    }
]

# Wyczyść tabelę (opcjonalnie, jeśli robisz update)
cursor.execute("DELETE FROM nft_inventory")

# Zapisz NFT do bazy
for card in nft_cards:
    cursor.execute("""
        INSERT INTO nft_inventory (name, rarity, crafting, attributes, available)
        VALUES (?, ?, ?, ?, ?)
    """, (
        card["name"],
        card["rarity"],
        card["crafting"],
        card["attributes"],
        card["available"]
    ))

conn.commit()
conn.close()

print("Zaktualizowano NFT w bazie danych.")
