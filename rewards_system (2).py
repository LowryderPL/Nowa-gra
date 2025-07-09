
import random

class RewardSystem:
    def __init__(self):
        self.item_pool = ["Iron Sword", "Wolfblade", "Elven Helm", "Health Potion"]
        self.nft_pool = ["NFT_Card_001", "NFT_Banner_Elf", "NFT_Boss_Trophy"]
        self.mount_pool = [
            {"name": "Shadowmane", "rarity": "Epic", "bonus": "+15% stealth"},
            {"name": "Runic Elk", "rarity": "Rare", "bonus": "+10% forest travel speed"},
            {"name": "Bonecharger", "rarity": "Legendary", "bonus": "+20% terror radius"}
        ]

    def get_reward(self, quest_type="normal"):
        reward = {"rfn": random.randint(10, 150)}
        reward["item"] = random.choice(self.item_pool)
        reward["nft"] = random.choice(self.nft_pool) if random.random() < 0.25 else None

        # Mounty tylko dla trudnych questów lub bossów
        if quest_type in ["boss", "epic", "hard"] and random.random() < 0.4:
            reward["mount"] = random.choice(self.mount_pool)

        return reward

    def show_reward(self, reward):
        print(f"🎁 Nagroda:")
        print(f"💰 RFN: {reward['rfn']}")
        print(f"📦 Przedmiot: {reward['item']}")
        if reward.get("nft"):
            print(f"🖼️ NFT: {reward['nft']}")
        if reward.get("mount"):
            print(f"🐎 Wierzchowiec: {reward['mount']['name']} ({reward['mount']['rarity']}) → {reward['mount']['bonus']}")
