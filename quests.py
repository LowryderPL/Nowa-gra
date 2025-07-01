class Quest:
    def __init__(self, title, description, quest_type, reward, completed=False):
        self.title = title
        self.description = description
        self.quest_type = quest_type  # 'główna', 'poboczna', 'klasowa', 'dzienna'
        self.reward = reward
        self.completed = completed

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title} [{self.quest_type}] – {self.description} (Nagroda: {self.reward})"

class QuestLog:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)
        print(f"\n📘 Nowa misja: {quest.title}")

    def complete_quest(self, title):
        for q in self.quests:
            if q.title == title and not q.completed:
                q.completed = True
                print(f"\n🎉 Ukończono: {q.title} (Nagroda: {q.reward})")
                return
        print("❗ Nie znaleziono nieukończonej misji o tej nazwie.")

    def list_quests(self):
        print("\n📜 Twoje misje:")
        if not self.quests:
            print("Brak aktywnych misji.")
            return
        for i, q in enumerate(self.quests, 1):
            print(f"{i}. {q}")

# Przykład testowy:
if __name__ == "__main__":
    log = QuestLog()
    log.add_quest(Quest("Wyprawa do lasu", "Zbadaj mroczny las na wschodzie", "główna", "500 EXP + artefakt"))
    log.add_quest(Quest("Polowanie na wilki", "Zabij 3 wilki", "dzienna", "50 RFM"))
    log.list_quests()
    log.complete_quest("Polowanie na wilki")
    log.list_quests()
