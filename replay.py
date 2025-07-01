import json import os from datetime import datetime

class ReplayManager: def init(self, replay_dir="replays"): self.replay_data = [] self.replay_dir = replay_dir self.current_replay = [] if not os.path.exists(replay_dir): os.makedirs(replay_dir)

def record_action(self, player_id, action_type, details):
    event = {
        "timestamp": datetime.now().isoformat(),
        "player": player_id,
        "action": action_type,
        "details": details
    }
    self.current_replay.append(event)

def save_replay(self, match_id=None):
    if not self.current_replay:
        return None

    if not match_id:
        match_id = datetime.now().strftime("replay_%Y%m%d_%H%M%S")

    filepath = os.path.join(self.replay_dir, f"{match_id}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(self.current_replay, f, indent=2)
    self.current_replay = []
    return filepath

def load_replay(self, match_id):
    filepath = os.path.join(self.replay_dir, f"{match_id}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.replay_data = json.load(f)
        return True
    return False

def get_events(self):
    return self.replay_data

def display_replay(self):
    if not self.replay_data:
        print("Brak powtórki do wyświetlenia.")
        return

    print("=== Powtórka rozgrywki ===")
    for event in self.replay_data:
        timestamp = event.get("timestamp")
        player = event.get("player")
        action = event.get("action")
        details = event.get("details")
        print(f"[{timestamp}] Gracz {player} wykonał akcję '{action}': {details}")

def list_replays(self):
    return [f for f in os.listdir(self.replay_dir) if f.endswith(".json")]

