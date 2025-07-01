import random

MAX_UPGRADE_LEVEL = 15

class Blacksmith:
    def __init__(self, inventory, player_stats):
        self.inventory = inventory
        self.player_stats = player_stats

    def upgrade_item(self, item_name):
        item = self.inventory.get(item_name)
        if not item:
            return f"Przedmiot '{item_name}' nie istnieje w ekwipunku."

        if item.get("level", 0) >= MAX_UPGRADE_LEVEL:
            return f"{item_name} osiągnął maksymalny poziom ulepszenia ({MAX_UPGRADE_LEVEL})."

        if not self._check_class_restriction(item):
            return f"{item_name} nie może być ulepszany przez Twoją klasę ({self.player_stats['class']})."

        upgrade_cost = self._calculate_upgrade_cost(item["level"])
        if not self._has_resources(upgrade_cost):
            return "Brak zasobów: potrzebujesz więcej RFN, złota, materiałów lub zwojów."

        success = self._attempt_upgrade(item["level"])
        if success:
            item["level"] += 1
            self._apply_cost(upgrade_cost)
            return f"{item_name} ulepszono do poziomu {item['level']}!"
        else:
            self.inventory.remove(item_name)
            return f"Ulepszanie nie powiodło się. {item_name} został zniszczony!"

    def _calculate_upgrade_cost(self, level):
        return {
            "rfn": 10 * (level + 1),
            "gold": 100 * (level + 1),
            "materials": 1 + (level // 3),
            "scrolls": 1 if level >= 5 else 0
        }

    def _has_resources(self, cost):
        stats = self.player_stats
        return (
            stats["rfn"] >= cost["rfn"]
            and stats["gold"] >= cost["gold"]
            and stats["materials"] >= cost["materials"]
            and stats["scrolls"] >= cost["scrolls"]
        )

    def _apply_cost(self, cost):
        for key in cost:
            self.player_stats[key] -= cost[key]

    def _attempt_upgrade(self, level):
        # Szansa na sukces maleje wraz z poziomem
        success_rate = max(90 - level * 4, 25)  # np. 90% na 0 lvl, 50% na 10 lvl
        return random.randint(1, 100) <= success_rate

    def _check_class_restriction(self, item):
        # Przykład ograniczeń klasowych
        restricted_items = {
            "Wojownik": ["Miecz", "Zbroja", "Hełm"],
            "Mag": ["Różdżka", "Szata", "Amulet"],
            "Łucznik": ["Łuk", "Płaszcz", "Rękawice"]
        }
        item_type = item.get("type")
        return item_type in restricted_items.get(self.player_stats["class"], [])

# Przykład testowy (do usunięcia w finalnej integracji):
if __name__ == "__main__":
    inventory = {
        "Miecz Runiczny": {"level": 2, "type": "Miecz"}
    }
    stats = {"rfn": 500, "gold": 3000, "materials": 10, "scrolls": 2, "class": "Wojownik"}
    bs = Blacksmith(inventory, stats)
    print(bs.upgrade_item("Miecz Runiczny"))
