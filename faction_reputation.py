
class FactionReputation:
    def __init__(self):
        self.reputation = {
            "Order of Flame": 5,
            "Elven Watchers": 2,
            "Dwarven Kin": 0,
            "Shadow Covenant": -3,
            "Free Folk": 1,
            "Firos Order": 4
        }

    def get_reputation(self, faction):
        return self.reputation.get(faction, 0)

    def change_reputation(self, faction, amount):
        if faction in self.reputation:
            self.reputation[faction] += amount
        else:
            self.reputation[faction] = amount
        print(f"📈 Reputation with {faction} is now {self.reputation[faction]}")

    def list_factions(self):
        print("🏳️ Faction Reputation:")
        for f, val in self.reputation.items():
            print(f"- {f}: {val}")

    def faction_status(self, faction):
        rep = self.get_reputation(faction)
        if rep >= 10:
            return "Ally"
        elif rep >= 5:
            return "Friendly"
        elif rep >= 0:
            return "Neutral"
        elif rep >= -5:
            return "Suspicious"
        else:
            return "Hostile"
