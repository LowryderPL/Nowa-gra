# spellbook.py - Zaktualizowana baza czarów do gry Firos: Magic & Magic

# Struktura: każda klasa posiada 6 czarów, w tym buffy.
# Buffy (healujące lub wzmacniające) są wliczone w odpowiednich klasach.

spells_data = {
    "Mag Ognia": [
        {"name": "Iskra Żarwena", "level": 1, "type": "ogień", "mana": 10, "power": 15, "description": "Wypuszcza iskrę ognia, która podpala wrogów."},
        {"name": "Kraśny Słońca", "level": 2, "type": "ogień", "mana": 12, "power": 22, "description": "Tworzy krąg ognia wokół przeciwników."},
        {"name": "Płomienny Pięść", "level": 3, "type": "ogień", "mana": 18, "power": 30, "description": "Rzuca ognistą kulą w przeciwnika, zadając mu poważne obrażenia."},
        {"name": "Złoty Opuszczacz", "level": 4, "type": "ogień", "mana": 25, "power": 35, "description": "Ognisty atak w odległość, ogień powoduje poparzenia."},
        {"name": "Płonące Serce", "level": 5, "type": "ogień", "mana": 35, "power": 50, "description": "Zwiększa siłę ognia wokół ciebie, tworząc strefę płomieni."},
        {"name": "Ognisty Sztorm", "level": 6, "type": "ogień", "mana": 45, "power": 60, "description": "Przywołuje sztorm ognia, zadając obrażenia wszystkim w okolicy."}
    ],
    "Mag Lodu": [
        {"name": "Szron Dziadosza", "level": 1, "type": "lód", "mana": 9, "power": 12, "description": "Zamraża wroga na chwilę, spowalniając go."},
        {"name": "Mgiełka Welesowa", "level": 2, "type": "lód", "mana": 12, "power": 18, "description": "Tworzy mgłę lodową, spowalniając wszystkich wrogów."},
        {"name": "Pazury Zimy", "level": 3, "type": "lód", "mana": 18, "power": 23, "description": "Wydaje zamrażający atak na przeciwników, zadając obrażenia."},
        {"name": "Zimny Krąg", "level": 4, "type": "lód", "mana": 25, "power": 30, "description": "Wytwarza wielki krąg lodu, który zamraża pobliskich wrogów."},
        {"name": "Sople Nawin", "level": 5, "type": "lód", "mana": 35, "power": 45, "description": "Wysyła kolce lodowe w kierunku wrogów."},
        {"name": "Sędzia Lodowej Otchłani", "level": 6, "type": "lód", "mana": 45, "power": 55, "description": "Zamraża wszystkich w okolicy, zadając im potężne obrażenia."}
    ],
    "Nekromanta": [
        {"name": "Krzyk Włochów", "level": 1, "type": "nekro", "mana": 10, "power": 18, "description": "Wzywa duchy przodków, aby zadały obrażenia wrogom."},
        {"name": "Zgoniec", "level": 2, "type": "nekro", "mana": 14, "power": 22, "description": "Wzywa umarłych, którzy atakują wrogów."},
        {"name": "Czarna Magia", "level": 3, "type": "nekro", "mana": 18, "power": 25, "description": "Zwiększa moc ciemnej magii, zadając obrażenia wszystkim wrogom."},
        {"name": "Zatruta Mgiełka", "level": 4, "type": "nekro", "mana": 22, "power": 30, "description": "Tworzy mgłę, która zmniejsza obronę wrogów."},
        {"name": "Nekrokscyzja", "level": 5, "type": "nekro", "mana": 30, "power": 35, "description": "Rozpoczyna nekrokscyzję, zwiększając siłę wszystkich martwych istot."},
        {"name": "Powstanie Cienia", "level": 6, "type": "nekro", "mana": 45, "power": 50, "description": "Wzywa całe armie cieni, które atakują wrogów."}
    ],
    "Alchemik": [
        {"name": "Wybuch Wiary", "level": 1, "type": "chemia", "mana": 10, "power": 15, "description": "Wybuch chemiczny powoduje obrażenia wrogom."},
        {"name": "Wróżka Płomienia", "level": 2, "type": "chemia", "mana": 15, "power": 20, "description": "Wysypuje materiały wybuchowe, które powodują poważne obrażenia."},
        {"name": "Tarcza Złotej Wiary", "level": 3, "type": "chemia", "mana": 20, "power": 25, "description": "Tworzy ochronną tarczę z chemicznych materiałów."},
        {"name": "Skrzynka Wiatrów", "level": 4, "type": "chemia", "mana": 30, "power": 40, "description": "Przywołuje burzę, która atakuje wrogów."},
        {"name": "Zatruta Mikstura", "level": 5, "type": "chemia", "mana": 35, "power": 45, "description": "Używa mikstur, które zatruwają wrogów."},
        {"name": "Tajemne Reagent", "level": 6, "type": "chemia", "mana": 45, "power": 50, "description": "Tworzy rzadką substancję alchemiczną."}
    ],
    "Mutant": [
        {"name": "Skórka Zelżona", "level": 1, "type": "mutacja", "mana": 10, "power": 12, "description": "Skórka zmutowana, pochłania obrażenia."},
        {"name": "Szal Misjonizmu", "level": 2, "type": "mutacja", "mana": 15, "power": 20, "description": "Zwiększa odporność na czary."},
        {"name": "Przemiana Ciała", "level": 3, "type": "mutacja", "mana": 20, "power": 25, "description": "Zmieniasz ciało, zyskując lepszą siłę."},
        {"name": "Zwiększenie Mocy", "level": 4, "type": "mutacja", "mana": 30, "power": 35, "description": "Zwiększa maksymalną moc w danym czasie."},
        {"name": "Ognisty Skórka", "level": 5, "type": "mutacja", "mana": 40, "power": 45, "description": "Twoja skórka przyjmuje postać ognia, zadając obrażenia."},
        {"name": "Zjednoczenie Umysłu", "level": 6, "type": "mutacja", "mana": 50, "power": 60, "description": "Twój umysł łączy się z innymi umysłami."}
    ],
    "Wojownik": [
        {"name": "Ryk Chwały", "level": 1, "type": "fizyczny", "mana": 5, "power": 12, "description": "Odzyskuje zdrowie poprzez jego siłę."},
        {"name": "Gniew Ziemi", "level": 2, "type": "fizyczny", "mana": 8, "power": 15, "description": "Przywołuje siłę ziemi do walki."},
        {"name": "Zmasowane Uderzenie", "level": 3, "type": "fizyczny", "mana": 12, "power": 20, "description": "Tworzy potężny atak z masy uderzeń."},
        {"name": "Uderzenie Gromu", "level": 4, "type": "fizyczny", "mana": 15, "power": 25, "description": "Atakuje wroga z piorunem."},
        {"name": "Berserker", "level": 5, "type": "fizyczny", "mana": 20, "power": 30, "description": "Niszczy wroga całkowicie."},
        {"name": "Wyciągnięcie Złota", "level": 6, "type": "fizyczny", "mana": 25, "power": 35, "description": "Zwiększa swoją moc na długie godziny."}
    ]
}

# Można dodać inne klasy, a także dynamicznie dodawać nowe czary na podstawie wymagania gry.
