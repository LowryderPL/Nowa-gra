
from nft_ui_marketplace import NFTMarketplaceUI

class QuestSystem:
    def __init__(self, player_id):
        self.player_id = player_id
        self.nft_ui = NFTMarketplaceUI(player_id)
        self.active_quests = []

    def accept_quest(self, quest):
        print(f"🧭 Nowe zadanie przyjęte: {quest['title']}")
        self.active_quests.append(quest)

    def complete_quest(self, quest_id):
        for quest in self.active_quests:
            if quest["id"] == quest_id:
                self.active_quests.remove(quest)
                print(f"✅ Zadanie ukończone: {quest['title']}")
                self.give_rewards(quest_id)
                return
        print("❌ Nie znaleziono zadania.")

    def give_rewards(self, quest_id):
        print(f"🎁 Otrzymujesz nagrodę za wykonanie zadania {quest_id}!")
        self.nft_ui.drop_reward_from_quest(quest_id)

    def list_active_quests(self):
        if not self.active_quests:
            print("Brak aktywnych zadań.")
            return
        print("📜 Twoje aktywne zadania:")
        for quest in self.active_quests:
            print(f"- {quest['title']}: {quest['description']}")
