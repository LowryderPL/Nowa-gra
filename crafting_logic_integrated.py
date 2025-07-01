# coding: utf-8
# Rozszerzony system Craftingu dla Firos: Magic & Magic – zintegrowany

import random
import time

class CraftingSystem:
    def __init__(self, user_data):
        self.user_data = user_data
        self.crafting_log = {}
        self.daily_craft_limit = 3

    def can_craft(self, user_id):
        today = time.strftime("%Y-%m-%d")
        if user_id not in self.crafting_log:
            self.crafting_log[user_id] = {}
        if today not in self.crafting_log[user_id]:
            self.crafting_log[user_id][today] = 0
        return self.crafting_log[user_id][today] < self.daily_craft_limit

    def register_craft(self, user_id):
        today = time.strftime("%Y-%m-%d")
        self.crafting_log[user_id][today] += 1

    def get_crafting_cost(self, rarity):
        return {
            'common': 0.2,
            'uncommon': 0.4,
            'rare': 0.6,
            'epic': 0.8,
            'legendary': 1.0,
            'mythic': 3.0
        }.get(rarity, 1.0)

    def get_success_chance(self, rarity):
        return {
            'common': 95,
            'uncommon': 85,
            'rare': 70,
            'epic': 55,
            'legendary': 40,
            'mythic': 25
        }.get(rarity, 50)

    def get_random_failure_reward(self):
        loot = ['Złom magiczny', 'Mikstura losowa', 'Fragment artefaktu', 'Tajemniczy składnik']
        return random.choice(loot)

    def attempt_craft(self, user_id, materials, rarity):
        if not self.can_craft(user_id):
            return {"success": False, "message": "Limit craftów dziennych osiągnięty."}

        self.register_craft(user_id)
        chance = self.get_success_chance(rarity)
        roll = random.randint(1, 100)

        if roll <= chance:
            crafted_item = f"Przedmiot ({rarity.title()})"
            return {"success": True, "item": crafted_item, "cost": self.get_crafting_cost(rarity)}
        else:
            fallback = self.get_random_failure_reward()
            return {"success": False, "message": "Crafting nieudany. Otrzymano w zamian: " + fallback, "fallback": fallback}
