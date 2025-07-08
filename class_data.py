import json

def load_classes(path="class.json"):
    """Wczytuje dane klas postaci z pliku JSON."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Nie znaleziono pliku class.json.")
        return []
    except json.JSONDecodeError:
        print("❌ Błąd dekodowania JSON w class.json.")
        return []

# Przykładowe użycie:
if __name__ == "__main__":
    classes = load_classes()
    for cls in classes:
        print(f"🛡 Klasa: {cls['name']}")
        print(f"   🧭 Frakcja: {cls['faction']}")
        print(f"   📜 Specjalizacja: {cls['specialization']}")
        print(f"   ✨ Umiejętności: {', '.join(cls['skills'])}")
        print("-" * 40)
