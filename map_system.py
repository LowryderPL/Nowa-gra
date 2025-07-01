# map_system.py – Rozszerzony system mapy FIROS

import random

class Location:
    def __init__(self, name, description, coordinates, region, faction, danger_level=1, boss=None, loot=None, visible=False, special_type=None):
        self.name = name
        self.description = description
        self.coordinates = coordinates  # (x, y)
        self.region = region
        self.faction = faction
        self.danger_level = danger_level
        self.boss = boss
        self.loot = loot or []
        self.visible = visible
        self.explored = False
        self.connected_paths = []
        self.special_type = special_type  # np. zamek, młyn, loch

    def add_path(self, other_location):
        if other_location not in self.connected_paths:
            self.connected_paths.append(other_location)

    def reveal(self):
        self.visible = True
        self.explored = True

    def get_info(self):
        return {
            "Nazwa": self.name,
            "Opis": self.description,
            "Region": self.region,
            "Frakcja": self.faction,
            "Typ": self.special_type,
            "Poziom zagrożenia": self.danger_level,
            "Boss": self.boss,
            "Łup": self.loot,
            "Widoczność": self.visible,
            "Zwiedzony": self.explored
        }

class MapSystem:
    def __init__(self):
        self.locations = []
        self.weather = "Bezchmurnie"

    def add_location(self, location):
        self.locations.append(location)

    def get_location_by_name(self, name):
        for loc in self.locations:
            if loc.name == name:
                return loc
        return None

    def connect_locations(self, loc1, loc2):
        loc1.add_path(loc2)
        loc2.add_path(loc1)

    def reveal_location(self, name):
        loc = self.get_location_by_name(name)
        if loc:
            loc.reveal()

    def generate_weather(self):
        self.weather = random.choice(["Bezchmurnie", "Deszcz", "Burza", "Mgła", "Śnieżyca", "Słonecznie"])

    def get_weather(self):
        return self.weather

    def trigger_random_event(self, location):
        events = [
            f"Zasadzka bandytów w {location.name}!",
            f"Znaleziona magiczna księga w {location.name}.",
            f"Tajemniczy portal pojawił się w {location.name}.",
            f"Spotkano wędrownego kupca w {location.name}.",
            f"Nagły atak potwora w {location.name}!"
        ]
        return random.choice(events)

def generate_full_firos_map():
    ms = MapSystem()

    sample_locations = [
        Location("Wiedźmograd", "Starożytna twierdza mutantów.", (0, 0), "Ziemie Centralne", "Wiedźminy", 5, boss="Arcyliszek", loot=["Miecz z Żył"], special_type="Zamek"),
        Location("Krypta Zjomistrza", "Zapomniane ruiny zaklętego maga.", (1, 1), "Doliny Cienia", "Zjomistrze", 4, boss="Zjomistrz", loot=["Zwoje Złowróżbne"], special_type="Loch"),
        Location("Port Krwistych Elfów", "Ośrodek handlu i piractwa.", (2, -1), "Wybrzeże Południa", "Krwistostrzelcy", 2, special_type="Port"),
        Location("Ruiny Mgłomistrza", "Mgła spowija pozostałości zamku.", (-1, 2), "Mgławice", "Mgłomistrzowie", 3, boss="Mgłowy Lich", special_type="Ruiny"),
        Location("Młyn Duszołowcy", "Opuszczony młyn zamieniony w sanktuarium.", (-2, 0), "Pola Żalu", "Duszołowcy", 1, special_type="Młyn"),
        Location("Szlak Handlowy Cierniojadów", "Bezpieczna trasa między regionami.", (3, 1), "Trakt Północy", "Cierniojady", 1, special_type="Szlak"),
        Location("Aglomeracja Żarogniewu", "Wielkie miasto frakcji ognia.", (-1, -2), "Ziemie Żaru", "Żarogniewcy", 4, special_type="Miasto"),
        Location("Katedra Runokultanów", "Miejsce rytuałów i mocy.", (2, 2), "Ziemie Zaklęte", "Runokultanowie", 5, special_type="Katedra")
    ]

    for loc in sample_locations:
        ms.add_location(loc)

    # Połączenia między lokacjami
    ms.connect_locations(sample_locations[0], sample_locations[1])
    ms.connect_locations(sample_locations[1], sample_locations[2])
    ms.connect_locations(sample_locations[2], sample_locations[3])
    ms.connect_locations(sample_locations[3], sample_locations[4])
    ms.connect_locations(sample_locations[4], sample_locations[5])
    ms.connect_locations(sample_locations[5], sample_locations[6])
    ms.connect_locations(sample_locations[6], sample_locations[7])

    return ms

def display_map_ascii(map_system):
    print("\n🗺️  Mapa świata FIROS (Odkryte lokacje):")
    for loc in map_system.locations:
        if loc.visible:
            print(f"[{loc.name}] — {loc.region}, frakcja: {loc.faction} ({loc.special_type})")
        else:
            print("[???]")

def move_to_location(map_system, from_name, to_name):
    from_loc = map_system.get_location_by_name(from_name)
    to_loc = map_system.get_location_by_name(to_name)
    if from_loc and to_loc and to_loc in from_loc.connected_paths:
        to_loc.reveal()
        map_system.generate_weather()
        event = map_system.trigger_random_event(to_loc)
        print(f"\n➡️  Przeniesiono z {from_loc.name} do {to_loc.name}")
        print(f"🌦️  Pogoda: {map_system.get_weather()}")
        print(f"📜  Zdarzenie: {event}")
    else:
        print("❌ Nie można przejść do tej lokacji.")
