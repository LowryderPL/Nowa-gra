
"""
🏰 GUILD SYSTEM – SYSTEM GILDII W GRZE FIROS

Ten moduł pozwala graczom tworzyć, dołączać i opuszczać gildie.
- Każda gildia ma lidera, członków, poziom, opis i bank.
- Gildie mogą rywalizować w wojnach gildii i zdobywać nagrody.
- Bank gildii służy do wspólnego rozwoju i odblokowywania bonusów.

Dane przechowywane są w guilds.json
"""
import json
import os

GUILD_DATA_FILE = "guilds.json"

class Guild:
    def __init__(self, name, leader, members=None, description="", level=1):
        self.name = name
        self.leader = leader
        self.members = members if members else [leader]
        self.description = description
        self.level = level
        self.bank = 0

    def to_dict(self):
        return {
            "name": self.name,
            "leader": self.leader,
            "members": self.members,
            "description": self.description,
            "level": self.level,
            "bank": self.bank
        }

    @staticmethod
    def from_dict(data):
        return Guild(
            name=data["name"],
            leader=data["leader"],
            members=data["members"],
            description=data.get("description", ""),
            level=data.get("level", 1)
        )

class GuildSystem:
    def __init__(self):
        self.guilds = {}
        self.load_guilds()

    def load_guilds(self):
        if os.path.exists(GUILD_DATA_FILE):
            with open(GUILD_DATA_FILE, 'r') as f:
                data = json.load(f)
                for name, gdata in data.items():
                    self.guilds[name] = Guild.from_dict(gdata)

    def save_guilds(self):
        with open(GUILD_DATA_FILE, 'w') as f:
            json.dump({name: guild.to_dict() for name, guild in self.guilds.items()}, f, indent=4)

    def create_guild(self, name, leader, description=""):
        if name in self.guilds:
            return False, "Guild already exists"
        self.guilds[name] = Guild(name, leader, description=description)
        self.save_guilds()
        return True, f"Guild '{name}' created successfully"

    def join_guild(self, name, player):
        if name not in self.guilds:
            return False, "Guild does not exist"
        guild = self.guilds[name]
        if player in guild.members:
            return False, "Player already in guild"
        guild.members.append(player)
        self.save_guilds()
        return True, f"{player} joined guild '{name}'"

    def leave_guild(self, name, player):
        if name not in self.guilds:
            return False, "Guild does not exist"
        guild = self.guilds[name]
        if player not in guild.members:
            return False, "Player not in this guild"
        guild.members.remove(player)
        self.save_guilds()
        return True, f"{player} left guild '{name}'"

    def deposit_to_guild_bank(self, name, amount):
        if name not in self.guilds:
            return False, "Guild does not exist"
        self.guilds[name].bank += amount
        self.save_guilds()
        return True, f"{amount} deposited to guild bank"

    def get_guild_info(self, name):
        if name not in self.guilds:
            return None
        return self.guilds[name].to_dict()
