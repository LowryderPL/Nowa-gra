
class GrubobrzuchQuests:
    def __init__(self, player):
        self.player = player
        self.completed = []

    def show_available(self):
        print("📜 Zadania od Grubobrzucha:")
        quests = [
            "1. Dostarcz siano do stajni (łatwe)",
            "2. Uspokój Bonechargera (walka)",
            "3. Odnajdź runiczne siodło (eksploracja)",
            "4. Zbierz 3 końskie artefakty (zbieractwo)",
            "5. Wygraj wyścig w dolinie Umbra (PvE)"
        ]
        for q in quests:
            print(q)

    def complete_quest(self, quest_id):
        rewards = {
            1: {"rfn": 150, "item": "Horse Feed", "msg": "Dobre siano, koń podziękuje."},
            2: {"rfn": 500, "item": "Bone Reins", "msg": "Nieźle, nie każdy wraca żywy."},
            3: {"rfn": 400, "item": "Runic Saddle", "msg": "Siodło działa. Ale coś szeptało nocą..."},
            4: {"rfn": 600, "item": "Artifact Bridle", "msg": "Stare gówno, ale magiczne."},
            5: {"rfn": 750, "item": "Legendary Whip", "msg": "Najszybszy łobuz w dolinie. Masz to."}
        }
        if quest_id in rewards and quest_id not in self.completed:
            reward = rewards[quest_id]
            self.player.rfn += reward["rfn"]
            self.player.inventory.append(reward["item"])
            self.completed.append(quest_id)
            print(f"✅ Zadanie wykonane! {reward['msg']}")
            print(f"💰 Otrzymano: {reward['rfn']} RFN, 📦 {reward['item']}")
        else:
            print("❌ To zadanie już wykonane lub nie istnieje.")
