
import json
import os

MARRIAGE_DATA_FILE = "marriages.json"

class MarriageSystem:
    def __init__(self):
        self.marriages = {}
        self.load_marriages()

    def load_marriages(self):
        if os.path.exists(MARRIAGE_DATA_FILE):
            with open(MARRIAGE_DATA_FILE, 'r') as f:
                self.marriages = json.load(f)

    def save_marriages(self):
        with open(MARRIAGE_DATA_FILE, 'w') as f:
            json.dump(self.marriages, f, indent=4)

    def marry(self, player1, player2):
        if player1 in self.marriages or player2 in self.marriages:
            return False, "One of the players is already married"
        self.marriages[player1] = player2
        self.marriages[player2] = player1
        self.save_marriages()
        return True, f"{player1} and {player2} are now married!"

    def divorce(self, player):
        if player not in self.marriages:
            return False, "Player is not married"
        partner = self.marriages[player]
        del self.marriages[player]
        del self.marriages[partner]
        self.save_marriages()
        return True, f"{player} and {partner} are now divorced"

    def get_partner(self, player):
        return self.marriages.get(player, None)

    def is_married(self, player):
        return player in self.marriages
