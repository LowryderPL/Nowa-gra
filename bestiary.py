bestiary.py – rozszerzona wersja z poziomami, HP i zakresem obrażeń

import sqlite3 import random

class Creature: def init(self, name, description, strength, weakness, habitat, level, health, damage_range): self.name = name self.description = description self.strength = strength self.weakness = weakness self.habitat = habitat self.level = level self.health = health self.damage_range = damage_range

class Bestiary: def init(self, db_path="firos_game_database.db"): self.conn = sqlite3.connect(db_path) self.create_table()

def create_table(self):
    self.conn.execute("""
    CREATE TABLE IF NOT EXISTS creatures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        strength TEXT,
        weakness TEXT,
        habitat TEXT,
        level INTEGER,
        health INTEGER,
        damage_range TEXT
    )
    """)
    self.conn.commit()

def add_creature(self, creature):
    self.conn.execute("""
        INSERT INTO creatures (name, description, strength, weakness, habitat, level, health, damage_range)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (creature.name, creature.description, creature.strength,
         creature.weakness, creature.habitat, creature.level,
         creature.health, f"{creature.damage_range[0]}-{creature.damage_range[1]}"))
    self.conn.commit()

def get_all_creatures(self):
    return self.conn.execute("SELECT * FROM creatures").fetchall()

Przykladowe dane potworów

creatures_data = [ ("Złowrogi Wilk", "Wilk nocy z krwistymi oczami", "Szybkość", "Ogień", "Lasy", 2, 150, (10, 25)), ("Upiorna Wiedźma", "Magini rzucająca klątwy i wiry ognia", "Magia", "Stal", "Bagna", 5, 230, (20, 40)), ("Kruk Krwi", "Latający zwiadowca śmierci", "Skrzydła", "Pociski", "Ruiny", 3, 90, (5, 20)), # Dodaj więcej... ]

if name == "main": bestiary = Bestiary() for data in creatures_data: creature = Creature(*data) bestiary.add_creature(creature) print("Zaktualizowano bazę potworów z poziomami, zdrowiem i obrażeniami.")

