# inventory_system.py – FIROS: Magic & Magic (Telegram + logika)

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

RARITY_COLORS = {
    "zwykły": "⚪",
    "rzadki": "🔵",
    "epicki": "🟣",
    "legendarny": "🟡"
}

class InventorySystem:
    def __init__(self, player):
        self.player = player
        self.inventory = player.get("inventory", [])
        self.max_size = 30

    def add_item(self, item):
        if len(self.inventory) >= self.max_size:
            return "❌ Brak miejsca w plecaku."
        self.inventory.append(item)
        return f"✅ Dodano: {item['name']}"

    def remove_item(self, item_name):
        for item in self.inventory:
            if item["name"].lower() == item_name.lower():
                self.inventory.remove(item)
                return f"🗑️ Usunięto: {item_name}"
        return "❌ Przedmiot nie znaleziony."

    def use_item(self, item_name):
        for item in self.inventory:
            if item["name"].lower() == item_name.lower():
                if self.player["class"] not in item.get("allowed_classes", ["All"]):
                    return "🚫 Twoja klasa nie może używać tego przedmiotu."
                if "mikstura" in item_name.lower():
                    self.player["health"] = min(self.player["max_health"], self.player["health"] + 30)
                elif "mana" in item_name.lower():
                    self.player["mana"] = min(self.player["max_mana"], self.player["mana"] + 20)
                elif "runa" in item_name.lower():
                    self.player.setdefault("active_runes", []).append(item_name)
                elif "zwój" in item_name.lower():
                    return f"📜 Zwój {item_name} gotowy do użycia w alchemii."
                else:
                    return f"🪙 {item_name} nie może być użyty."
                self.inventory.remove(item)
                return f"✅ Użyto: {item_name}"
        return "❌ Przedmiot nie znaleziony."

    def show_inventory_text(self):
        if not self.inventory:
            return "🎒 Twój plecak jest pusty."
        msg = "🎒 **Twoje przedmioty:**\n"
        for item in self.inventory:
            icon = RARITY_COLORS.get(item.get('rarity', "zwykły"), "⚪")
            msg += f"{icon} {item['name']} — lvl {item['level']} ({item['rarity']})\n"
        return msg

    def inventory_menu(self):
        buttons = []
        for item in self.inventory:
            label = f"{RARITY_COLORS.get(item['rarity'], '⚪')} {item['name']} (lvl {item['level']})"
            buttons.append([InlineKeyboardButton(text=label, callback_data=f"use_{item['name']}")])
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    async def upgrade_item(self, item_name):
        item = next((i for i in self.inventory if i["name"] == item_name), None)
        if not item:
            return "❌ Przedmiot nie znaleziony."

        ton_cost = 0.2
        success_chance = 80 - (item["level"] * 5)

        if self.player.get("ton", 0) < ton_cost:
            return "❌ Brak wystarczającej ilości TON."
        self.player["ton"] -= ton_cost

        if random.randint(1, 100) <= success_chance:
            item["level"] += 1
            # Upgrade rzadkości
            lvl = item["level"]
            if lvl >= 10:
                item["rarity"] = "legendarny"
            elif lvl >= 7:
                item["rarity"] = "epicki"
            elif lvl >= 4:
                item["rarity"] = "rzadki"
            return f"⬆️ Ulepszono {item['name']} do lvl {item['level']} ({item['rarity']})"
        else:
            self.inventory.remove(item)
            return f"💥 Ulepszanie nie powiodło się. {item_name} zniszczony."
