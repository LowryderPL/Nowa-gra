
import json
from game_engine_nft import NFTManager

class NFTMarketplaceUI:
    def __init__(self, player_id):
        self.manager = NFTManager(player_id)

    def display_nft_collection(self):
        print(f"Twoja kolekcja NFT:")
        for nft in self.manager.list_nfts():
            print(f"- {nft['name']} ({nft['rarity']})")

    def show_marketplace(self, rarity=None):
        offers = self.manager.show_marketplace(rarity_filter=rarity)
        print("Marketplace NFT:")
        for offer in offers:
            print(f"[{offer['id']}] {offer['name']} - {offer['rarity']} - {offer['price_ton']} TON / {offer['price_rfn']} RFN")

    def buy_nft(self, nft_id, currency="TON"):
        result = self.manager.buy_nft(nft_id, currency)
        print(result)

    def list_equipment_for_sale(self, equipment_item, rarity, ton=None, rfn=None):
        new_offer = {
            "id": equipment_item["id"],
            "name": equipment_item["name"],
            "rarity": rarity,
            "price_ton": ton,
            "price_rfn": rfn,
            "seller": self.manager.player_id
        }
        try:
            with open("marketplace_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(new_offer)
        with open("marketplace_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Dodano ofertę: {equipment_item['name']}")

    def drop_reward_from_quest(self, quest_id):
        # Przykład dropu NFT po wykonaniu misji
        reward_nft = {
            "id": f"quest_{quest_id}_nft",
            "name": f"Relikt z zadania {quest_id}",
            "rarity": "Epic"
        }
        self.manager.add_nft(reward_nft)
        print(f"Zdobyto NFT z zadania: {reward_nft['name']}")
