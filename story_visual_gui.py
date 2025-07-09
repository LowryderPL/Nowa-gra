
class VisualQuestGUI:
    def __init__(self):
        self.portrait = "🧟‍♂️ [Grubobrzuch: mistrz stajni przeklętych]"
        self.background = "🌒 Zgniła stajnia pod Głuchym Lasem"

    def show_welcome(self):
        print(self.background)
        print(self.portrait)
        print("""
🐖 Grubobrzuch: Ej ty, z ryjem jak koń po ognistym galopie!
Mam dla ciebie coś więcej niż obornik i siano...

📖 Fabuła – wybierz opcję:
[1] 🔥 Zaczynam swoją przygodę
[2] 📘 Sprawdź co już odjebałeś
[0] 🚪 Wypierdalaj z powrotem
""")

    def respond(self, action):
        if action == "1":
            print("📜 [System]: Fabuła uruchomiona. Ruszasz w piekielną jazdę...")
        elif action == "2":
            print("📜 [System]: Otwieram księgę twoich grzechów...")
        else:
            print("🐖 Grubobrzuch: I dobrze. Zdychaj gdzieś indziej.")
