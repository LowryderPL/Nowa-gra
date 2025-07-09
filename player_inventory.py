
class PlayerInventory:
    def __init__(self):
        self.items = []
        self.nfts = []
        self.rfn = 0

    def add_item(self, item):
        self.items.append(item)
        print(f"📦 Dodano przedmiot: {item['name']} ({item['type']})")

    def add_nft(self, nft):
        self.nfts.append(nft)
        print(f"🖼️ Otrzymano NFT: {nft['name']} [{nft['rarity']}]")

    def add_rfn(self, amount):
        self.rfn += amount
        print(f"💰 Dodano {amount} RFN. Aktualny stan: {self.rfn}")

    def show_inventory(self):
        print("🎒 Ekwipunek gracza:")
        print(f"💰 RFN: {self.rfn}")
        print("📦 Przedmioty:")
        for item in self.items:
            print(f"  - {item['name']} ({item['type']}) → {item['effect']}")
        print("🖼️ NFT:")
        for nft in self.nfts:
            print(f"  - {nft['name']} [{nft['rarity']} – {nft['type']}]")
