
from grubobrzuch_story_arc_full import GrubobrzuchStoryArc

class StoryQuestDialogInterface:
    def __init__(self, player):
        self.arc = GrubobrzuchStoryArc(player)

    def show_intro(self):
        lines = [
            "🐖 Grubobrzuch: Ty! Ty z mordą jak z runicznego zadka – masz chwilę?",
            "🐖 Grubobrzuch: W stajni dzieją się dziwne rzeczy. Ktoś kurwa coś nawiedza moje konie.",
            "🐖 Grubobrzuch: Chcesz się dorobić? Albo zginąć z siodłem w ryju? To posłuchaj.",
            "🐖 Grubobrzuch: Mam dla ciebie misję. Fabułę. Pieprzoną legendę.",
            "📖 [1] Rozpocznij fabularne zadania",
            "📖 [2] Sprawdź, co już zrobiłeś",
            "📖 [0] Spierdalaj z powrotem do karczmy"
        ]
        for line in lines:
            print(line)

    def handle_input(self, action):
        if action == "1":
            print("🐖 Grubobrzuch: Dobrze. Nie mów, że cię nie ostrzegałem...")
            self.arc.start_main_arc()
        elif action == "2":
            print("📘 Grubobrzuch: No dobra, sprawdźmy co już odjebałeś...")
            self.arc.check_progress()
        else:
            print("🐖 Grubobrzuch: Hah! I dobrze, mniej trupów do zakopania.")
