
import sqlite3

# Zdefiniuj klasę Creature
class Creature:
    def __init__(self, name, description, strength, weakness, habitat):
        self.name = name
        self.description = description
        self.strength = strength
        self.weakness = weakness
        self.habitat = habitat

# Zdefiniuj klasę Bestiary
class Bestiary:
    def __init__(self, db_path="firos_game_database.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS creatures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                strength TEXT,
                weakness TEXT,
                habitat TEXT
            )"""
        )
        self.conn.commit()

    def add_creature(self, creature):
        self.conn.execute(
            """INSERT INTO creatures (name, description, strength, weakness, habitat)
               VALUES (?, ?, ?, ?, ?)""",
            (creature.name, creature.description, creature.strength, creature.weakness, creature.habitat)
        )
        self.conn.commit()

    def get_all_creatures(self):
        cursor = self.conn.execute("SELECT * FROM creatures")
        return cursor.fetchall()

# Dane 100 potworów
creatures_data = [
    ("Upiorny Wilk", "Drapieżnik lasów północnych, niewrażliwy na zimno.", "Szybkość", "Ogień", "Lasy północy"),
    ("Wodnik Bagnisty", "Topi ofiary w podmokłych bagnach.", "Ukrycie", "Srebro", "Bagna"),
    ("Cieniowilk", "Porusza się bezszelestnie, atakuje z cienia.", "Skrytość", "Światło", "Ciemne lasy"),
    ("Topielec", "Zamieszkuje stare studnie i zatopione ruiny.", "Woda", "Ogień", "Ruiny"),
    ("Zimowy Demon", "Pojawia się podczas mroźnych nocy.", "Lód", "Ogień", "Góry północne"),
    ("Wilkołak", "Przemienia się podczas pełni księżyca.", "Siła", "Srebro", "Wioski"),
    ("Szkarłatna Harpia", "Zwabia ofiary śpiewem.", "Lot", "Magia dźwięku", "Klify"),
    ("Bezimienny", "Stwór z innego wymiaru, bez twarzy.", "Groza", "Zaklęcia pieczęci", "Pustki"),
    ("Gnilec", "Ożywiony trup żerujący na cmentarzach.", "Trucizna", "Święta woda", "Cmentarze"),
    ("Płomienny Widmo", "Zjawisko płonącej duszy.", "Ogień", "Lód", "Katakumby"),
]

# Dodajemy pozostałe automatycznie
for i in range(11, 101):
    creatures_data.append((
        f"Demon Cienia {i}",
        f"Stwór o cienistym obliczu, numer {i}.",
        "Mrok",
        "Światło",
        f"Jaskinie poziom {i % 10}"
    ))

if __name__ == "__main__":
    bestiary = Bestiary()
    for name, desc, strn, weak, hab in creatures_data:
        creature = Creature(name, desc, strn, weak, hab)
        bestiary.add_creature(creature)
    print("✅ 100 potworów zostało dodanych do bazy danych.")
