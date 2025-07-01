import sqlite3
import random

class Creature:
    def __init__(self, name, description, strength, weakness, habitat, level, health, damage_range, behavior_type):
        self.name = name
        self.description = description
        self.strength = strength
        self.weakness = weakness
        self.habitat = habitat
        self.level = level
        self.health = health
        self.damage_range = damage_range
        self.behavior_type = behavior_type

    def __str__(self):
        return f"{self.name} (lvl {self.level}) — {self.description} [Zachowanie: {self.behavior_type}]"

def create_table():
    conn = sqlite3.connect("firos_game_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS creatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            strength TEXT,
            weakness TEXT,
            habitat TEXT,
            level INTEGER,
            health INTEGER,
            damage_range TEXT,
            behavior_type TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_creature(creature):
    conn = sqlite3.connect("firos_game_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO creatures (name, description, strength, weakness, habitat, level, health, damage_range, behavior_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (creature.name, creature.description, creature.strength, creature.weakness,
         creature.habitat, creature.level, creature.health, creature.damage_range, creature.behavior_type)
    )
    conn.commit()
    conn.close()

def generate_sample_creatures():
    behavior_types = ["aggressive", "passive", "ambusher", "fleeing", "territorial"]
    creatures = [
        Creature(
            name="Wilkor Cmentarny",
            description="Cień przeszłości, wyje w księżycowe noce przy starych mogiłach.",
            strength="Szybki atak, odporność na magię cienia",
            weakness="Słaby pancerz",
            habitat="Cmentarze, stare ruiny",
            level=3,
            health=180,
            damage_range="25-40",
            behavior_type=random.choice(behavior_types)
        ),
        Creature(
            name="Bagienna Czała",
            description="Mokradłowa bestia o jadowitym oddechu i twardym pancerzu.",
            strength="Zatrucie, wytrzymałość",
            weakness="Ogień",
            habitat="Bagna",
            level=5,
            health=350,
            damage_range="40-60",
            behavior_type=random.choice(behavior_types)
        ),
        Creature(
            name="Kruczy Pasterz",
            description="Zakonny renegat, który przywołuje stada kruków przeciw wrogom.",
            strength="Magia ciemności, przyzwanie",
            weakness="Silne światło",
            habitat="Zamglone wzgórza",
            level=7,
            health=260,
            damage_range="30-55",
            behavior_type=random.choice(behavior_types)
        ),
    ]
    for c in creatures:
        add_creature(c)

if __name__ == "__main__":
    create_table()
    generate_sample_creatures()
    print("Dodano przykładowe potwory do bazy danych.")
