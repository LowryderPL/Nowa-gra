spells_data.py – Pełna baza zaklęć dla klas w Firos: Magic & Magic

Struktura: lista słowników z zaklęciami, podzielona na klasy postaci

Każde zaklęcie zawiera nazwę, poziom, typ, koszt many, moc, opis, klasę oraz wymagany poziom gracza

spells = [ # 🔥 Mag Ognia {"name": "Iskra Żarwena", "level": 1, "type": "ogień", "mana": 10, "power": 15, "description": "Pierwszy płomień Żarwena, który rani i podpala.", "class": "Mag", "required_level": 1}, {"name": "Płomień Swaroża", "level": 2, "type": "ogień", "mana": 12, "power": 20, "description": "Czysty ogień Swarożyca – wybuchowy i nieujarzmiony.", "class": "Mag", "required_level": 3}, {"name": "Żagiew Welesowa", "level": 3, "type": "ogień", "mana": 15, "power": 30, "description": "Ognista siła Welesa atakująca wielu przeciwników.", "class": "Mag", "required_level": 5}, {"name": "Cień Swaroga", "level": 10, "type": "ogień", "mana": 30, "power": 70, "description": "Ostateczna forma ognia – spopiela duszę.", "class": "Mag", "required_level": 10},

# ❄️ Mag Lodu
{"name": "Szron Dziadosza", "level": 1, "type": "lód", "mana": 9, "power": 12, "description": "Pierwszy chłód duchów puszczy.", "class": "Mag", "required_level": 1},
{"name": "Zlodź Opółca", "level": 3, "type": "lód", "mana": 14, "power": 22, "description": "Zatrzymuje wroga w lodzie.", "class": "Mag", "required_level": 4},

# ☠️ Nekromanta
{"name": "Krzyk Wołchwów", "level": 1, "type": "nekro", "mana": 11, "power": 18, "description": "Dźwięk śmierci, który osłabia żywych.", "class": "Nekromanta", "required_level": 1},
{"name": "Zgoniec", "level": 5, "type": "nekro", "mana": 20, "power": 35, "description": "Przywołanie upiora, który atakuje wroga.", "class": "Nekromanta", "required_level": 6},

# 🧪 Alchemik
{"name": "Wybuch Wiary", "level": 1, "type": "chemia", "mana": 10, "power": 17, "description": "Alchemiczny ogień – wybuch eliksiru.", "class": "Alchemik", "required_level": 1},
{"name": "Zatruta Mgła", "level": 2, "type": "chemia", "mana": 13, "power": 23, "description": "Otacza wroga trucizną, która go dusi.", "class": "Alchemik", "required_level": 3},

# 🐺 Mutant
{"name": "Skórka Żelazna", "level": 1, "type": "mutacja", "mana": 8, "power": 15, "description": "Mutacja skóry – zamienia się w żelazną powłokę.", "class": "Mutant", "required_level": 1},
{"name": "Szał Mięśni", "level": 3, "type": "mutacja", "mana": 14, "power": 28, "description": "Mięśnie pęcznieją, zwiększając atak.", "class": "Mutant", "required_level": 4},

# 🗡️ Wojownik
{"name": "Ryk Chwata", "level": 1, "type": "fizyczny", "mana": 6, "power": 14, "description": "Wydobywa krzyk, który osłabia przeciwnika.", "class": "Wojownik", "required_level": 1},
{"name": "Gromostrzał", "level": 2, "type": "fizyczny", "mana": 10, "power": 25, "description": "Przebijający cios z siłą błyskawicy.", "class": "Wojownik", "required_level": 3},

# 🏹 Łucznik
{"name": "Strzała Mokoszy", "level": 1, "type": "wiatr", "mana": 7, "power": 16, "description": "Natchniona strzała – nie chybia celu.", "class": "Łucznik", "required_level": 1},
{"name": "Widmowy Bełt", "level": 3, "type": "cień", "mana": 12, "power": 24, "description": "Niewidoczny pocisk – rani i dezorientuje.", "class": "Łucznik", "required_level": 4},

# 🧙 Wiedzący / Szeptun
{"name": "Modlitwa Kraka", "level": 1, "type": "duchowy", "mana": 9, "power": 12, "description": "Cisza i światło – leczy rany.", "class": "Szeptun", "required_level": 1},
{"name": "Dotyk Białobożki", "level": 2, "type": "duchowy", "mana": 13, "power": 22, "description": "Uzdrowienie duszy i ciała.", "class": "Szeptun", "required_level": 3}

]

Można rozszerzyć do pełnych 10 poziomów dynamicznie w grze na podstawie tej bazy.

