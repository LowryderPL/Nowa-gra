
import json
import os

# Ścieżka do zaktualizowanego pliku z lokacjami
LOCATION_DATA_PATH = os.path.join(os.path.dirname(__file__), "locations_firos_extended_final_cleaned.json")

def load_locations():
    with open(LOCATION_DATA_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Przykładowe użycie
if __name__ == "__main__":
    locations = load_locations()
    for loc in locations[:10]:  # Podgląd 10 pierwszych lokacji
        print(f"{loc['name']} - {loc['type']} - {loc['region']}")
