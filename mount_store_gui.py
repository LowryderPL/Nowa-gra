
class MountStore:
    def __init__(self, player):
        self.player = player
        self.mount_shop = [
            {"id": "mnt_shadow", "name": "Shadowmane", "rarity": "Epic", "bonus": "+15% stealth", "price_rfn": 2400},
            {"id": "mnt_elk", "name": "Runic Elk", "rarity": "Rare", "bonus": "+10% forest speed", "price_rfn": 1750},
            {"id": "mnt_bone", "name": "Bonecharger", "rarity": "Legendary", "bonus": "+20% terror", "price_rfn": 5000}
        ]
        self.horse_equipment = [
            {"id": "armor_iron", "name": "Iron Horseplate", "bonus": "+3 armor", "price_rfn": 400},
            {"id": "armor_rune", "name": "Runed Barding", "bonus": "+15 magic resist", "price_rfn": 2500},
            {"id": "saddle_elf", "name": "Elven Saddlecloth", "bonus": "+5 stamina", "price_rfn": 650}
        ]
        self.purchase_log = []

    def show_store_menu(self):
        print("🐎 Mount & Horse Equipment Store")
        print("1. View Mounts")
        print("2. View Horse Equipment")
        print("3. View Purchase History")
        print("0. Exit")

    def list_mounts(self):
        print("🐴 Mounts Available:")
        for idx, mnt in enumerate(self.mount_shop, 1):
            print(f"{idx}. {mnt['name']} [{mnt['rarity']}] – {mnt['bonus']} | 💰 {mnt['price_rfn']} RFN")

    def list_equipment(self):
        print("🛡️ Horse Equipment Available:")
        for idx, eq in enumerate(self.horse_equipment, 1):
            print(f"{idx}. {eq['name']} – {eq['bonus']} | 💰 {eq['price_rfn']} RFN")

    def buy_mount(self, idx):
        if 0 < idx <= len(self.mount_shop):
            mnt = self.mount_shop[idx - 1]
            if self.player.rfn >= mnt["price_rfn"]:
                self.player.rfn -= mnt["price_rfn"]
                self.player.inventory.append(mnt)
                self.purchase_log.append(mnt["name"])
                print(f"✅ Purchased mount: {mnt['name']}")
            else:
                print("❌ Not enough RFN.")
        else:
            print("Invalid mount ID.")

    def buy_equipment(self, idx):
        if 0 < idx <= len(self.horse_equipment):
            eq = self.horse_equipment[idx - 1]
            if self.player.rfn >= eq["price_rfn"]:
                self.player.rfn -= eq["price_rfn"]
                self.player.inventory.append(eq)
                self.purchase_log.append(eq["name"])
                print(f"✅ Purchased equipment: {eq['name']}")
            else:
                print("❌ Not enough RFN.")
        else:
            print("Invalid equipment ID.")

    def show_log(self):
        print("📜 Purchase History:")
        if self.purchase_log:
            for item in self.purchase_log:
                print(f"- {item}")
        else:
            print("No purchases yet.")
