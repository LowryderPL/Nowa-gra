
class QuestLogic:
    def __init__(self):
        pass

    def is_quest_available(self, quest, faction_reputation, completed_quests):
        # Sprawdź, czy quest wymaga reputacji
        required_rep = quest.get("required_reputation", 0)
        faction = quest.get("faction", None)
        if faction and faction_reputation.get_reputation(faction) < required_rep:
            return False
        if quest["id"] in completed_quests:
            return False
        return True

    def process_quest(self, quest):
        # Tutaj byłby system walki, zbierania itp.
        print(f"🎯 Processing quest: {quest['title']}")

        # Collection-type check
        if quest["type"] == "collection":
            print(f"📦 Required item: {quest['objective_item']} x{quest['required_amount']}")
            return True

        # Boss battle-type
        if quest["type"] == "boss_battle":
            boss = quest["boss"]
            print(f"⚔️ Boss Encounter: {boss['name']} – HP: {boss['hp']}, ATK: {boss['atk']}, DEF: {boss['def']}")
            return True

        # Escort, sabotage, etc. – simplified
        print(f"🔍 Quest Type: {quest['type']} – Auto-complete simulated.")
        return True
