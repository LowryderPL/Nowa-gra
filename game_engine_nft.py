
# --- NFT SYSTEM INTEGRATION START ---
import json

class NFTManager:
    def __init__(self, nft_file='nft_cards.json'):
        with open(nft_file, 'r', encoding='utf-8') as f:
            self.nfts = json.load(f)

    def get_player_nfts(self, player_id):
        return [nft for nft in self.nfts if nft["rarity"] in ["Legendary", "Epic"]]

    def get_nft_by_type(self, nft_type):
        return [nft for nft in self.nfts if nft["type"] == nft_type]

    def get_boost_from_nfts(self, nfts):
        boost = {"power": 0, "magic": 0, "defense": 0}
        for nft in nfts:
            boost["power"] += nft.get("power", 0)
            boost["magic"] += nft.get("magic", 0)
            boost["defense"] += nft.get("defense", 0)
        return boost
# --- NFT SYSTEM INTEGRATION END ---
