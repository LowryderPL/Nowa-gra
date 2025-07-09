
from grubobrzuch_story_arc_full import GrubobrzuchStoryArc

class StoryQuestInterface:
    def __init__(self, player):
        self.arc = GrubobrzuchStoryArc(player)

    def show_main_menu(self):
        print("📖 Fabuła: Grubobrzuch")
        print("1. Rozpocznij fabularną linię zadań")
        print("2. Sprawdź postęp")
        print("3. Opuść")

    def run(self, action):
        if action == "1":
            self.arc.start_main_arc()
        elif action == "2":
            self.arc.check_progress()
        else:
            print("👋 Zamykasz interfejs fabularny.")
