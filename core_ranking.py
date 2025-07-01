core/ranking.py

import json from datetime import datetime

class RankingSystem: def init(self, path="ranking.json"): self.path = path self.rankings = {}  # {player_id: {"score": int, "wins": int, "losses": int, "last_active": str}}

def load(self):
    try:
        with open(self.path, "r", encoding="utf-8") as f:
            self.rankings = json.load(f)
        print("✅ Ranking wczytany.")
    except FileNotFoundError:
        print("ℹ️ Nie znaleziono pliku rankingu, tworzę nowy.")
        self.rankings = {}

def save(self):
    try:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.rankings, f, indent=4)
        print("✅ Ranking zapisany.")
    except Exception as e:
        print(f"❌ Błąd zapisu rankingu: {e}")

def register_player(self, player_id):
    if player_id not in self.rankings:
        self.rankings[player_id] = {
            "score": 0,
            "wins": 0,
            "losses": 0,
            "last_active": datetime.utcnow().isoformat()
        }

def record_match(self, winner_id, loser_id, points=10):
    self.register_player(winner_id)
    self.register_player(loser_id)

    self.rankings[winner_id]["score"] += points
    self.rankings[winner_id]["wins"] += 1
    self.rankings[winner_id]["last_active"] = datetime.utcnow().isoformat()

    self.rankings[loser_id]["score"] = max(0, self.rankings[loser_id]["score"] - points // 2)
    self.rankings[loser_id]["losses"] += 1
    self.rankings[loser_id]["last_active"] = datetime.utcnow().isoformat()

def get_top_players(self, limit=10):
    return sorted(self.rankings.items(), key=lambda x: x[1]["score"], reverse=True)[:limit]

def export_leaderboard(self):
    leaderboard = self.get_top_players(100)
    return [
        {
            "player": player_id,
            "score": data["score"],
            "wins": data["wins"],
            "losses": data["losses"],
            "last_active": data["last_active"]
        } for player_id, data in leaderboard
    ]

