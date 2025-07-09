
class NPCGrubobrzuch:
    def __init__(self, player):
        self.player = player
        self.name = "Grubobrzuch"
        self.mount_shop = [
            {"id": "mnt_mule", "name": "Swamp Mule", "rarity": "Common", "bonus": "+5% carry weight", "price_rfn": 600},
            {"id": "mnt_storm", "name": "Stormcoat Mare", "rarity": "Uncommon", "bonus": "+10% speed in rain", "price_rfn": 1200},
            {"id": "mnt_blood", "name": "Bloodhoof", "rarity": "Rare", "bonus": "+5% combat speed", "price_rfn": 1900}
        ]
        self.dialog_intro = [
            "🐖 Grubobrzuch: Co, szukasz czegoś, co cię nie kopnie przy siodle?",
            "🐖 Grubobrzuch: Mam tu kilka bestii. Nie wszystkie są oswojone...",
            "🐖 Grubobrzuch: Pokaż mi RFN, a pokażę ci potwory ze stajni."
        ]

    def greet(self):
        for line in self.dialog_intro:
            print(line)

    def show_mounts(self):
        print("🐎 Mounts from Grubobrzuch:")
        for idx, mnt in enumerate(self.mount_shop, 1):
            print(f"{idx}. {mnt['name']} [{mnt['rarity']}] – {mnt['bonus']} | 💰 {mnt['price_rfn']} RFN")

    def buy_mount(self, idx):
        if 0 < idx <= len(self.mount_shop):
            mnt = self.mount_shop[idx - 1]
            if self.player.rfn >= mnt["price_rfn"]:
                self.player.rfn -= mnt["price_rfn"]
                self.player.inventory.append(mnt)
                print(f"✅ Grubobrzuch: Masz to. Tylko nie wracaj z połamanym siodłem – {mnt['name']} jest twój!")
            else:
                print("❌ Grubobrzuch: To nie sklep z marzeniami, wracaj z pełnym sakiewką.")
        else:
            print("❌ Grubobrzuch: Nie znam takiego bydlęcia.")
