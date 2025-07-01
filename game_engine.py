from map_system import Map
from faction import FactionManager
from inventory import Inventory
from quests import QuestLog
from bestiary import Bestiary
from battle_system import BattleSystem
from alchemy import AlchemySystem
from nft_system import NFTManager
from sqlite_db import DBHandler

class GameEngine:
    def __init__(self):
        self.map = Map()
        self.factions = FactionManager()
        self.inventory = Inventory()
        self.quest_log = QuestLog()
        self.bestiary = Bestiary()
        self.battle = BattleSystem(self.bestiary, self.inventory)
        self.alchemy = AlchemySystem()
        self.nft = NFTManager()
        self.db = DBHandler()

    def run(self):
        print("\n🔷 Start gry: Firos - Magic & Magic 🔷")
        self.factions.choose_faction()
        self.map.display_starting_area()
        self.main_menu()

    def main_menu(self):
        while True:
            print("\n📜 Główne Menu:")
            print("1. Mapa Świata")
            print("2. Inwentarz")
            print("3. Bestiariusz")
            print("4. Alchemia")
            print("5. Questy")
            print("6. Walka")
            print("7. NFT & Księga")
            print("0. Zakończ")
            choice = input(">> ")

            if choice == "1":
                self.map.show()
            elif choice == "2":
                self.inventory.display()
            elif choice == "3":
                self.bestiary.list_creatures()
            elif choice == "4":
                self.alchemy.menu()
            elif choice == "5":
                self.quest_log.show()
            elif choice == "6":
                self.battle.menu()
            elif choice == "7":
                self.nft.display_collection()
            elif choice == "0":
                print("👋 Do zobaczenia w świecie Firos!")
                break
            else:
                print("❌ Nieprawidłowy wybór.")
