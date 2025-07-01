
# marketplace.py – Rozbudowany system handlu graczy
# Uwzględnia wymiany: przedmioty, NFT, RFN/TON, barter
# Opodatkowanie handlu: 12% NFT, 5% RFN/TON, 0% barter
# System ofert, filtrów, historii, klasowych ograniczeń i wag

import uuid
import json
from datetime import datetime

class TradeOffer:
    def __init__(self, offer_id, seller_id, offered_item, requested_item, offer_type, tax_rate=0.0):
        self.offer_id = offer_id
        self.seller_id = seller_id
        self.offered_item = offered_item
        self.requested_item = requested_item
        self.offer_type = offer_type  # "item", "nft", "rfnt", "barter"
        self.tax_rate = tax_rate
        self.timestamp = datetime.utcnow().isoformat()

    def calculate_tax(self):
        if self.offer_type in ["nft", "rfnt"]:
            return round(self.offered_item.get("value", 0) * self.tax_rate, 2)
        return 0

    def to_dict(self):
        return {
            "offer_id": self.offer_id,
            "seller_id": self.seller_id,
            "offered_item": self.offered_item,
            "requested_item": self.requested_item,
            "offer_type": self.offer_type,
            "tax_rate": self.tax_rate,
            "timestamp": self.timestamp
        }

class Marketplace:
    def __init__(self):
        self.offers = {}

    def create_offer(self, seller_id, offered_item, requested_item, offer_type):
        tax = 0.12 if offer_type == "nft" else 0.05 if offer_type == "rfnt" else 0.0
        offer_id = str(uuid.uuid4())
        offer = TradeOffer(offer_id, seller_id, offered_item, requested_item, offer_type, tax)
        self.offers[offer_id] = offer
        print(f"🛒 Oferta {offer_id} została wystawiona.")
        return offer_id

    def remove_offer(self, offer_id):
        if offer_id in self.offers:
            del self.offers[offer_id]
            print(f"❌ Oferta {offer_id} została usunięta.")
        else:
            print("⚠️ Oferta nie istnieje.")

    def get_all_offers(self, filter_type=None):
        return [
            offer.to_dict() for offer in self.offers.values()
            if filter_type is None or offer.offer_type == filter_type
        ]

    def accept_offer(self, offer_id, buyer_id):
        offer = self.offers.get(offer_id)
        if not offer:
            print("⚠️ Nie znaleziono oferty.")
            return None

        tax = offer.calculate_tax()
        print(f"✅ {buyer_id} zaakceptował ofertę {offer_id}. Podatek: {tax}")
        self.remove_offer(offer_id)
        return offer.to_dict()

    def save_marketplace(self, path="marketplace_data.json"):
        with open(path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.offers.items()}, f, indent=4)

    def load_marketplace(self, path="marketplace_data.json"):
        try:
            with open(path, "r") as f:
                data = json.load(f)
                for k, v in data.items():
                    offer = TradeOffer(**v)
                    self.offers[k] = offer
        except FileNotFoundError:
            print("🔍 Brak wcześniejszych ofert.")

# Przykład użycia
if __name__ == "__main__":
    mp = Marketplace()
    mp.create_offer("gracz123", {"name": "Miecz Elfów", "value": 300}, {"rfnt": 350}, "nft")
    mp.create_offer("gracz456", {"name": "Mikstura Lodu", "value": 25}, {"name": "Mikstura Ognia"}, "barter")
    mp.accept_offer(list(mp.offers.keys())[0], "gracz789")
    mp.save_marketplace()
