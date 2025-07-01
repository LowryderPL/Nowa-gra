# core/save_load.py

import json
from datetime import datetime

class SaveSystem:
    def __init__(self, path="savegame.json"):
        self.path = path

    def save(self, board_state):
        try:
            data = {
                "timestamp": datetime.utcnow().isoformat(),
                "board": board_state.export_state(),
                "players": board_state.export_players(),
                "chat": board_state.chat.export(),
                "spells": board_state.spells.export(),
                "turn": board_state.current_turn
            }

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print("✅ Gra zapisana.")
        except Exception as e:
            print(f"❌ Błąd zapisu: {e}")

    def load(self, board_state):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            board_state.import_state(data["board"])
            board_state.import_players(data["players"])
            board_state.chat.import_data(data["chat"])
            board_state.spells.import_data(data["spells"])
            board_state.current_turn = data.get("turn", 0)
            print("✅ Gra wczytana.")
        except Exception as e:
            print(f"❌ Błąd wczytywania: {e}")
