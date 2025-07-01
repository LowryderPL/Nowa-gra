# arena.py

import random
import time
from core_ranking import update_player_ranking
from core_save_load import save_game_state
from enemy import generate_enemy
from xp_system import grant_xp
from inventory import reward_loot
from guilds import update_guild_score

ARENA_TYPES = ["PvP", "PvE", "Frakcyjna", "Turniejowa"]
ARENA_LOCATIONS = [
    "Ruiny Zamku Eldur",
    "Kryształowa Dolina",
    "Arena Czaszek",
    "Sanktuarium Ognia",
    "Zatopione Podziemia",
    "Twierdza Mgły"
]

class ArenaBattle:
    def __init__(self, player, arena_type="PvE", is_ranked=False):
        self.player = player
        self.arena_type = arena_type
        self.is_ranked = is_ranked
        self.enemy = self.generate_opponent()
        self.battle_log = []

    def generate_opponent(self):
        if self.arena_type == "PvP":
            return self.find_online_opponent()
        else:
            return generate_enemy(level=self.player.level, boss=self.arena_type == "Turniejowa")

    def find_online_opponent(self):
        # Placeholder — replace with real player pool
        fake_enemy = generate_enemy(level=self.player.level)
        fake_enemy.name = "Cień Gracza"
        return fake_enemy

    def start_battle(self):
        self.battle_log.append(f"Arena: {random.choice(ARENA_LOCATIONS)}")
        self.battle_log.append(f"{self.player.name} vs {self.enemy.name}")
        turn = 0
        while self.player.is_alive() and self.enemy.is_alive():
            turn += 1
            self.battle_log.append(f"--- Tura {turn} ---")
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
            time.sleep(0.2)
        return self.resolve_battle()

    def resolve_battle(self):
        if self.player.is_alive():
            self.battle_log.append("Zwycięstwo!")
            reward_loot(self.player, difficulty="arena")
            grant_xp(self.player, amount=50 + self.enemy.level * 10)
            if self.is_ranked:
                update_player_ranking(self.player, result="win")
            if self.arena_type == "Frakcyjna":
                update_guild_score(self.player.guild, points=10)
        else:
            self.battle_log.append("Porażka.")
            if self.is_ranked:
                update_player_ranking(self.player, result="loss")
        save_game_state(self.player)
        return self.battle_log

# Optional GUI launcher for arena
def launch_arena_menu(player):
    print("=== ARENA ===")
    for idx, arena in enumerate(ARENA_TYPES):
        print(f"{idx+1}. {arena}")
    choice = int(input("Wybierz typ areny: ")) - 1
    arena_type = ARENA_TYPES[choice]
    battle = ArenaBattle(player, arena_type=arena_type, is_ranked=True)
    result = battle.start_battle()
    for line in result:
        print(line)

# Arena daily quest
def arena_daily_challenge(player):
    print("Codzienne wyzwanie Areny!")
    enemy = generate_enemy(level=player.level + 2, boss=True)
    battle = ArenaBattle(player, arena_type="Turniejowa", is_ranked=False)
    battle.enemy = enemy
    result = battle.start_battle()
    for line in result:
        print(line)
    print("Zakończono wyzwanie.")
