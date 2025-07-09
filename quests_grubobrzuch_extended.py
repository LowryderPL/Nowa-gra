
class GrubobrzuchQuests:
    def __init__(self, player):
        self.player = player
        self.completed = []

    def show_available(self):
        print("📜 Zadania od Grubobrzucha:")
        for idx, quest in enumerate(self.quest_descriptions(), 1):
            print(f"{idx}. {quest['title']} – {quest['type']}")

    def complete_quest(self, quest_id):
        quests = self.quest_descriptions()
        if 1 <= quest_id <= len(quests) and quest_id not in self.completed:
            q = quests[quest_id - 1]
            self.player.rfn += q["reward_rfn"]
            self.player.inventory.append(q["reward_item"])
            self.completed.append(quest_id)
            print(f"✅ Zadanie wykonane! {q['dialog']}")
            print(f"💰 Otrzymano: {q['reward_rfn']} RFN, 📦 {q['reward_item']}")
        else:
            print("❌ To zadanie już wykonane lub nie istnieje.")

    def quest_descriptions(self):
        return [
            {"title": "Dostarcz siano do stajni", "type": "Fetch", "reward_rfn": 150, "reward_item": "Horse Feed", "dialog": "Koń się najadł. Zadowolony."},
            {"title": "Uspokój Bonechargera", "type": "Combat", "reward_rfn": 500, "reward_item": "Bone Reins", "dialog": "Nie każdy wraca z takiej jazdy."},
            {"title": "Odnajdź runiczne siodło", "type": "Explore", "reward_rfn": 400, "reward_item": "Runic Saddle", "dialog": "Działa, ale szeptało nocą."},
            {"title": "Zbierz 3 końskie artefakty", "type": "Collect", "reward_rfn": 600, "reward_item": "Artifact Bridle", "dialog": "Stare, magiczne, działa."},
            {"title": "Wygraj wyścig w Umbra", "type": "PvE", "reward_rfn": 750, "reward_item": "Legendary Whip", "dialog": "Gratulacje, łobuzie."},
            {"title": "Wyczyszczenie stajni", "type": "Explore", "reward_rfn": 512, "reward_item": "Witch Amulet", "dialog": "No to był rajd!"},
            {"title": "Polowanie na rumaka", "type": "Combat", "reward_rfn": 531, "reward_item": "Healing Potion", "dialog": "No to był rajd!"},
            {"title": "Transport beczki wody", "type": "Fetch", "reward_rfn": 324, "reward_item": "Healing Potion", "dialog": "Grubobrzuch kiwa z uznaniem."},
            {"title": "Rozmowa z wiedźmą", "type": "Collect", "reward_rfn": 494, "reward_item": "Golden Spur", "dialog": "Nie pytaj, ale to się przyda."},
            {"title": "Zbieranie podków", "type": "Collect", "reward_rfn": 780, "reward_item": "Elven Rope", "dialog": "No to był rajd!"},
            {"title": "Teleportacja konia", "type": "Combat", "reward_rfn": 316, "reward_item": "Shadow Saddle", "dialog": "Nie pytaj, ale to się przyda."},
            {"title": "Zagadka czarnego siodła", "type": "Puzzle", "reward_rfn": 569, "reward_item": "Healing Potion", "dialog": "Grubobrzuch kiwa z uznaniem."},
            {"title": "Ucieczka przed magiem", "type": "Explore", "reward_rfn": 784, "reward_item": "Healing Potion", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Czyszczenie boksów", "type": "Fetch", "reward_rfn": 690, "reward_item": "Runed Bit", "dialog": "Nie pytaj, ale to się przyda."},
            {"title": "Obrona stajni", "type": "Combat", "reward_rfn": 754, "reward_item": "Magic Whip", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Zbieranie nawozu", "type": "Combat", "reward_rfn": 570, "reward_item": "Runed Bit", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Zbieranie piór feniksa", "type": "Magic", "reward_rfn": 844, "reward_item": "Elven Rope", "dialog": "No to był rajd!"},
            {"title": "Skok przez przepaść", "type": "Fetch", "reward_rfn": 860, "reward_item": "Healing Potion", "dialog": "No to był rajd!"},
            {"title": "Tropienie złodziei", "type": "Fetch", "reward_rfn": 814, "reward_item": "Shadow Saddle", "dialog": "Nie pytaj, ale to się przyda."},
            {"title": "Zebranie błota z bagien", "type": "Fetch", "reward_rfn": 545, "reward_item": "Runed Bit", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Test miecza w siodle", "type": "Fetch", "reward_rfn": 606, "reward_item": "Golden Spur", "dialog": "No to był rajd!"},
            {"title": "Ukrycie przed mutantami", "type": "Collect", "reward_rfn": 666, "reward_item": "Magic Whip", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Wyprawa po smoczego konia", "type": "Collect", "reward_rfn": 364, "reward_item": "Healing Potion", "dialog": "Nie pytaj, ale to się przyda."},
            {"title": "Skrytka pod mostem", "type": "Explore", "reward_rfn": 941, "reward_item": "Witch Amulet", "dialog": "No to był rajd!"},
            {"title": "Trening w karczmie", "type": "Combat", "reward_rfn": 343, "reward_item": "Elven Rope", "dialog": "No to był rajd!"},
            {"title": "Zbieranie włosia", "type": "Fetch", "reward_rfn": 470, "reward_item": "Elven Rope", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Runiczna próba", "type": "Combat", "reward_rfn": 831, "reward_item": "Healing Potion", "dialog": "No to był rajd!"},
            {"title": "Próba siodła chaosu", "type": "Magic", "reward_rfn": 422, "reward_item": "Shadow Saddle", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Dostarczenie magicznych uzd", "type": "Collect", "reward_rfn": 314, "reward_item": "Elven Rope", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
            {"title": "Uleczenie konia czarami", "type": "Collect", "reward_rfn": 591, "reward_item": "Healing Potion", "dialog": "Koń już nie wróci... ale zadanie zrobione."},
        ]
