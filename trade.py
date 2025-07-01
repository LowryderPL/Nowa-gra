trade.py - System handlu gracz-gracz i z rynkiem w Firos: Magic & Magic

from inventory import Item

class TradeOffer: def init(self, seller, item, price, currency="RFN"): self.seller = seller  # nazwa gracza sprzedajacego self.item = item      # instancja Item self.price = price    # cena jednostkowa self.currency = currency  # RFN lub TON

def __str__(self):
    return f"{self.item.name} za {self.price} {self.currency} (sprzedawca: {self.seller})"

class Marketplace: def init(self): self.offers = []  # lista ofert TradeOffer

def list_offer(self, offer):
    self.offers.append(offer)
    print(f"📦 Dodano ofertę: {offer}")

def show_offers(self):
    if not self.offers:
        print("\n🕸️ Brak aktualnych ofert na rynku.")
    else:
        print("\n📜 Dostępne oferty na rynku:")
        for idx, offer in enumerate(self.offers):
            print(f"{idx + 1}. {offer}")

def buy_offer(self, idx, buyer_name, player_inventory, player_wallet):
    if idx < 0 or idx >= len(self.offers):
        print("❌ Niepoprawny numer oferty.")
        return

    offer = self.offers[idx]

    if player_wallet.get(offer.currency, 0) >= offer.price:
        player_wallet[offer.currency] -= offer.price
        player_inventory.add_item(offer.item)
        print(f"✅ Kupiono {offer.item.name} od {offer.seller} za {offer.price} {offer.currency}.")
        # tutaj można dodać logikę przekazania TON/RFN do sprzedawcy (np. logowanie)
        self.offers.pop(idx)
    else:
        print("❌ Nie masz wystarczająco środków.")

Przykładowe użycie

if name == "main": market = Marketplace() inv = [] wallet = {"RFN": 500, "TON": 10}

sword = Item("Miecz Runiczny", "broń", power=12, description="Stary miecz z runami")
potion = Item("Eliksir Many", "mikstura", power=25)

offer1 = TradeOffer("Gracz1", sword, 120, "RFN")
offer2 = TradeOffer("Gracz2", potion, 1, "TON")

market.list_offer(offer1)
market.list_offer(offer2)

market.show_offers()
market.buy_offer(0, "Ty", inv, wallet)
market.show_offers()

