
import json
from marketplace_logic import Marketplace

class NFTManager:
    def __init__(self, player_id, collection_file="nft_cards.json"):
        self.player_id = player_id
        self.collection_file = collection_file
        self.load_collection()
        self.marketplace = Marketplace()

    def load_collection(self):
        try:
            with open(self.collection_file, "r", encoding="utf-8") as f:
                self.collection = json.load(f).get(self.player_id, [])
        except FileNotFoundError:
            self.collection = []

    def save_collection(self):
        try:
            with open(self.collection_file, "r", encoding="utf-8") as f:
                all_data = json.load(f)
        except FileNotFoundError:
            all_data = {}
        all_data[self.player_id] = self.collection
        with open(self.collection_file, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)

    def add_nft(self, nft):
        self.collection.append(nft)
        self.save_collection()

    def list_nfts(self):
        return self.collection

    def show_marketplace(self, rarity_filter=None):
        if rarity_filter:
            return self.marketplace.filter_by_rarity(rarity_filter)
        return self.marketplace.list_offers()

    def buy_nft(self, nft_id, currency="TON"):
        result = self.marketplace.purchase_nft(nft_id, self.player_id, currency)
        return result
