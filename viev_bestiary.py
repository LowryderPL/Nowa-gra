import sqlite3

def show_all_creatures():
    conn = sqlite3.connect("firos_game_database.db")
    cursor = conn.execute("SELECT * FROM creatures")

    print("\n=== BESTIARIUSZ: WSZYSTKIE POTWORY ===\n")

    for row in cursor.fetchall():
        id, name, description, strength, weakness, habitat = row
        print(f"#{id}: {name}")
        print(f"Opis: {description}")
        print(f"Siła: {strength}")
        print(f"Słabość: {weakness}")
        print(f"Siedlisko: {habitat}")
        print("-" * 40)

    conn.close()

if __name__ == "__main__":
    show_all_creatures()
