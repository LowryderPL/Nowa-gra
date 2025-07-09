
import json
import os
import random

class LocationManager:
    def __init__(self, file_path="lokacje_firos_full_extended.json"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Location file not found: {self.file_path}")
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_all(self):
        locations = []
        for group in self.data.values():
            locations.extend(group)
        return list(set(locations))

    def get_by_category(self, category):
        return self.data.get(category, [])

    def get_categories(self):
        return list(self.data.keys())

    def get_random(self, category=None):
        if category and category in self.data:
            return random.choice(self.data[category])
        return random.choice(self.get_all())

    def search(self, keyword):
        keyword = keyword.lower()
        return [loc for loc in self.get_all() if keyword in loc.lower()]

    def add_location(self, category, location_name):
        if category not in self.data:
            self.data[category] = []
        if location_name not in self.data[category]:
            self.data[category].append(location_name)
            self._save_data()

    def remove_location(self, category, location_name):
        if category in self.data and location_name in self.data[category]:
            self.data[category].remove(location_name)
            self._save_data()

    def rename_location(self, old_name, new_name):
        changed = False
        for category in self.data:
            if old_name in self.data[category]:
                idx = self.data[category].index(old_name)
                self.data[category][idx] = new_name
                changed = True
        if changed:
            self._save_data()

    def _save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
