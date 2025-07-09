
import random

class RewardSystem:
    def __init__(self):
        self.nft_collection = ["Sword of the Forgotten", "Banner of Ebonhill", "Orb of the Deep"]
        self.currency_reward_range = (5, 50)  # RFN
        self.unlocked_features = []

    def give_reward(self, quest):
        reward = quest["reward"]
        exp = reward.get("exp", 0)
        fame = reward.get("fame", 0)
        item = reward.get("item", "Unknown Relic")
        rfn = random.randint(*self.currency_reward_range)
        nft = random.choice(self.nft_collection) if fame >= 10 else None

        print(f"🎁 Nagroda za questa:")
        print(f"✨ EXP: +{exp}, Sława: +{fame}")
        print(f"📦 Przedmiot: {item}")
        print(f"💰 RFN zdobyte: +{rfn}")
        if nft:
            print(f"🖼️ NFT zdobyte: {nft}")
        if fame >= 15:
            unlock = "New Dungeon Access"
            self.unlocked_features.append(unlock)
            print(f"🗺️ Odblokowano: {unlock}")
