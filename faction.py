# faction.py — Rozbudowany system frakcji w grze FIROS

class Faction:
    def __init__(self, name, bonus, talents, description):
        self.name = name
        self.bonus = bonus
        self.talents = talents
        self.description = description
        self.members = []
        self.leader = None
        self.officers = []
        self.level = 1
        self.prestige = 0
        self.missions = []

    def add_member(self, player_id):
        if player_id not in self.members:
            self.members.append(player_id)

    def remove_member(self, player_id):
        if player_id in self.members:
            self.members.remove(player_id)
            if player_id == self.leader:
                self.leader = None
            if player_id in self.officers:
                self.officers.remove(player_id)

    def promote_to_officer(self, player_id):
        if player_id in self.members and player_id not in self.officers:
            self.officers.append(player_id)

    def set_leader(self, player_id):
        if player_id in self.members:
            self.leader = player_id

    def add_prestige(self, amount):
        self.prestige += amount
        if self.prestige >= self.level * 100:
            self.level += 1
            self.prestige = 0

    def add_mission(self, mission_text):
        self.missions.append(mission_text)

    def get_summary(self):
        return {
            "name": self.name,
            "bonus": self.bonus,
            "level": self.level,
            "members_count": len(self.members),
            "leader": self.leader,
            "officers": self.officers,
            "missions": self.missions,
        }

class FactionManager:
    def __init__(self):
        self.factions = {
            "Cienie": Faction(
                "Cienie",
                "+10% obrażeń nocą",
                ["Skrytobójstwo", "Iluzje", "Cisza"],
                "Frakcja sabotażystów i morderców działających w cieniu."
            ),
            "Krwawe Ostrza": Faction(
                "Krwawe Ostrza",
                "+20% obrażeń przy <50% HP",
                ["Szał", "Zemsta", "Wściekłość"],
                "Berserkerzy, którzy zyskują moc, gdy są ranni."
            ),
            "Lodowi Jeźdźcy": Faction(
                "Lodowi Jeźdźcy",
                "Zamrażają przeciwników co 5 ataków",
                ["Lodowy Mur", "Frostbite", "Spowolnienie"],
                "Kawaleria mrozu z dalekiej północy."
            ),
            "Zakon Wiedzy": Faction(
                "Zakon Wiedzy",
                "+15% moc czarów",
                ["Płonący Pocisk", "Bariery", "Teleportacja"],
                "Mistyczny zakon run, magii i wiedzy pradawnej."
            )
        }
        self.player_faction = None

    def choose_faction(self, player_id):
        print("🏰 Wybierz swoją frakcję:")
        for idx, (name, faction) in enumerate(self.factions.items(), 1):
            print(f"{idx}. {name} - {faction.bonus} | {faction.description}")
        choice = input(">> ")
        keys = list(self.factions.keys())
        try:
            selected = keys[int(choice) - 1]
            self.player_faction = self.factions[selected]
            self.player_faction.add_member(player_id)
            print(f"✅ Dołączono do frakcji: {self.player_faction.name}")
        except (IndexError, ValueError):
            print("❌ Nieprawidłowy wybór.")
            self.choose_faction(player_id)

    def get_player_bonus(self):
        return self.player_faction.bonus if self.player_faction else None

    def get_faction_summary(self):
        if self.player_faction:
            return self.player_faction.get_summary()
        return "Brak przypisanej frakcji."
