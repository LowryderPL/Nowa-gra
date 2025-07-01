
from nft_ui_marketplace import NFTMarketplaceUI
import random

class Enemy:
    def __init__(self, name, hp, attack, rarity="Common"):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.rarity = rarity

class BattleSystem:
    def __init__(self, player_id):
        self.player_id = player_id
        self.nft_ui = NFTMarketplaceUI(player_id)

    def start_battle(self, enemy):
        print(f"⚔️ Rozpoczynasz walkę z: {enemy.name}")
        # Prosty system walki (symulacja)
        player_hp = 100
        enemy_hp = enemy.hp

        while player_hp > 0 and enemy_hp > 0:
            dmg_to_enemy = random.randint(10, 30)
            dmg_to_player = random.randint(5, enemy.attack)
            enemy_hp -= dmg_to_enemy
            player_hp -= dmg_to_player
            print(f"💥 Zadajesz {dmg_to_enemy} dmg. 🩸 Otrzymujesz {dmg_to_player} dmg.")

        if player_hp > 0:
            print(f"🏆 Pokonałeś {enemy.name}!")
            self.drop_nft_after_battle(enemy)
        else:
            print("💀 Zostałeś pokonany...")

    def drop_nft_after_battle(self, enemy):
        print(f"🎁 Z potwora {enemy.name} wypadła karta NFT!")
        self.nft_ui.drop_reward_from_battle(enemy.name, rarity=enemy.rarity)
