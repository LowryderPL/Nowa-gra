# guilds.py – System gildii FIROS: Magia i Miecz

class Guild:
    def __init__(self, name, founder):
        self.name = name
        self.founder = founder
        self.members = [founder]
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.honor = 0
        self.territory = []
        self.upgrades = []
        self.guild_points = 0
        self.chat_log = []
        self.bosses_defeated = []
        self.faction = None
        self.history = []
        self.active_missions = []
        self.guild_hall = "Drewniana Sala"
        self.wars = []

    def add_member(self, player):
        if player not in self.members:
            self.members.append(player)
            self.history.append(f"{player} dołączył do gildii {self.name}.")

    def remove_member(self, player):
        if player in self.members:
            self.members.remove(player)
            self.history.append(f"{player} opuścił gildię {self.name}.")

    def send_message(self, player, message):
        self.chat_log.append(f"[{player}]: {message}")

    def contribute_gold(self, player, amount):
        self.gold += amount
        self.history.append(f"{player} przekazał {amount} sztuk złota do gildii.")

    def start_mission(self, mission_name):
        self.active_missions.append(mission_name)
        self.history.append(f"Gildia rozpoczęła misję: {mission_name}")

    def finish_mission(self, mission_name, success=True):
        if mission_name in self.active_missions:
            self.active_missions.remove(mission_name)
            if success:
                self.experience += 50
                self.guild_points += 1
                self.history.append(f"Misja zakończona sukcesem: {mission_name}")
            else:
                self.history.append(f"Misja nie powiodła się: {mission_name}")

    def declare_war(self, other_guild):
        self.wars.append(other_guild)
        self.history.append(f"Wypowiedziano wojnę gildii {other_guild.name}")

    def defeat_boss(self, boss_name):
        self.bosses_defeated.append(boss_name)
        self.experience += 100
        self.history.append(f"Gildia pokonała bossa: {boss_name}")

    def level_up(self):
        required_exp = self.level * 150
        if self.experience >= required_exp:
            self.level += 1
            self.experience -= required_exp
            self.history.append(f"Gildia awansowała na poziom {self.level}!")

    def set_faction(self, faction_name):
        self.faction = faction_name
        self.history.append(f"Gildia dołączyła do frakcji: {faction_name}")

    def get_summary(self):
        return {
            "Nazwa": self.name,
            "Założyciel": self.founder,
            "Poziom": self.level,
            "Złoto": self.gold,
            "Honor": self.honor,
            "Frakcja": self.faction,
            "Misje aktywne": self.active_missions,
            "Pokonani bossowie": self.bosses_defeated,
            "Terytorium": self.territory,
            "Członkowie": self.members,
            "Wojny": [g.name for g in self.wars]
        }
