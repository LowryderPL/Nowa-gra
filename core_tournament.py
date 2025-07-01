core/tournament.py — system turniejów FIROS: Królewskie Szachy

import random from collections import defaultdict

class Player: def init(self, player_id, name): self.id = player_id self.name = name self.points = 0 self.wins = 0 self.losses = 0 self.reported = False self.gui_data = {}

class Match: def init(self, player1, player2): self.p1 = player1 self.p2 = player2 self.result = None  # 'p1', 'p2', 'draw'

def resolve(self, result):
    self.result = result
    if result == "p1":
        self.p1.wins += 1
        self.p2.losses += 1
        self.p1.points += 3
    elif result == "p2":
        self.p2.wins += 1
        self.p1.losses += 1
        self.p2.points += 3
    else:
        self.p1.points += 1
        self.p2.points += 1

class Tournament: def init(self, name, mode="Classic", max_players=16): self.name = name self.mode = mode  # Classic, Magic, 2v2, BossRush itd. self.max_players = max_players self.players = [] self.matches = [] self.current_round = 1 self.completed = False self.leaderboard = defaultdict(list) self.rewards_distributed = False

def register_player(self, player_id, name):
    if len(self.players) < self.max_players:
        player = Player(player_id, name)
        self.players.append(player)
        self._update_gui(player)
        return True
    return False

def _update_gui(self, player):
    player.gui_data = {
        "status": "Zarejestrowany",
        "team": None,
        "icon": "default_icon.png",
    }

def report_issue(self, player_id, issue):
    for p in self.players:
        if p.id == player_id:
            p.reported = True
            print(f"⚠️ Gracz {p.name} zgłosił problem: {issue}")

def generate_round(self):
    print(f"\n=== Runda {self.current_round} ===")
    random.shuffle(self.players)
    self.matches = []
    for i in range(0, len(self.players), 2):
        if i + 1 < len(self.players):
            match = Match(self.players[i], self.players[i + 1])
            self.matches.append(match)
        else:
            self.players[i].points += 3
            self.players[i].wins += 1

def play_round(self, results):
    for match, result in zip(self.matches, results):
        match.resolve(result)
    self.current_round += 1

def show_table(self):
    print("\n=== Tabela Turnieju ===")
    ranked = sorted(self.players, key=lambda p: p.points, reverse=True)
    for i, p in enumerate(ranked, 1):
        print(f"{i}. {p.name} | Pkt: {p.points} | W: {p.wins} | L: {p.losses}")

def distribute_rewards(self):
    if not self.rewards_distributed:
        ranked = sorted(self.players, key=lambda p: p.points, reverse=True)
        for i, p in enumerate(ranked):
            rfm = max(50 - i * 5, 10)
            print(f"🎁 {p.name} otrzymuje {rfm} RFM!")
        self.rewards_distributed = True

def end(self):
    self.completed = True
    print(f"\n🎉 Turniej {self.name} zakończony!")
    self.show_table()
    self.distribute_rewards()
    print("🏆 Zwycięzca:", max(self.players, key=lambda p: p.points).name)
    print("📊 Ranking zapisany do globalnej tablicy wyników.")

