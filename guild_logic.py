guilds_logic.py – Rozszerzony system logiki gildii w grze Firos: Magic & Magic

import json import os

class Guild: def init(self, name, leader): self.name = name self.leader = leader self.members = [leader] self.level = 1 self.exp = 0 self.resources = {"gold": 0, "rfm": 0, "ton": 0} self.structures = [] self.quests = [] self.alliances = [] self.wars = []

def add_member(self, player):
    if player not in self.members:
        self.members.append(player)

def remove_member(self, player):
    if player in self.members:
        self.members.remove(player)

def gain_exp(self, amount):
    self.exp += amount
    while self.exp >= self.required_exp():
        self.level_up()

def required_exp(self):
    return self.level * 1000

def level_up(self):
    self.level += 1
    self.exp = 0
    self.unlock_structure(f"Sala gildii Lv.{self.level}")

def unlock_structure(self, structure):
    if structure not in self.structures:
        self.structures.append(structure)

def declare_war(self, other_guild):
    if other_guild.name not in self.wars:
        self.wars.append(other_guild.name)

def form_alliance(self, other_guild):
    if other_guild.name not in self.alliances:
        self.alliances.append(other_guild.name)

def assign_quest(self, quest_id):
    if quest_id not in self.quests:
        self.quests.append(quest_id)

def add_resources(self, kind, amount):
    if kind in self.resources:
        self.resources[kind] += amount

def spend_resources(self, kind, amount):
    if kind in self.resources and self.resources[kind] >= amount:
        self.resources[kind] -= amount
        return True
    return False

class GuildManager: def init(self, filepath="guilds.json"): self.guilds = {} self.filepath = filepath self.load()

def create_guild(self, name, leader):
    if name not in self.guilds:
        self.guilds[name] = Guild(name, leader)
        self.save()
        return True
    return False

def delete_guild(self, name):
    if name in self.guilds:
        del self.guilds[name]
        self.save()

def get_guild(self, name):
    return self.guilds.get(name, None)

def save(self):
    data = {name: guild.__dict__ for name, guild in self.guilds.items()}
    with open(self.filepath, "w") as f:
        json.dump(data, f, indent=4)

def load(self):
    if os.path.exists(self.filepath):
        with open(self.filepath, "r") as f:
            data = json.load(f)
            for name, info in data.items():
                guild = Guild(info['name'], info['leader'])
                guild.members = info['members']
                guild.level = info['level']
                guild.exp = info['exp']
                guild.resources = info['resources']
                guild.structures = info['structures']
                guild.quests = info['quests']
                guild.alliances = info['alliances']
                guild.wars = info['wars']
                self.guilds[name] = guild

