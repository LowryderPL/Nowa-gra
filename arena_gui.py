# arena_gui.py

import time
import sys
import random
from arena import ArenaBattle, ARENA_TYPES
from ui_elements import print_with_border, pause, clear_screen
from player_profile import load_player_profile
from core_save_load import save_game_state
from core_ranking import display_ranking

def slow_type(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_loading(text="Ładowanie Areny"):
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * (i + 1)}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def display_arena_menu(player):
    clear_screen()
    print_with_border("🛡️ ARENA BITEW 🛡️")
    print("Wybierz typ Areny:\n")
    for idx, arena_type in enumerate(ARENA_TYPES):
        print(f" {idx + 1}. {arena_type}")
    print(" 0. Powrót")

    choice = input("\nTwój wybór: ").strip()
    if choice == "0":
        return

    try:
        choice_index = int(choice) - 1
        if choice_index not in range(len(ARENA_TYPES)):
            raise ValueError
        selected_type = ARENA_TYPES[choice_index]
        handle_arena_battle(player, selected_type)
    except ValueError:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        pause(1.5)
        display_arena_menu(player)

def handle_arena_battle(player, arena_type):
    clear_screen()
    print_with_border(f"⚔️  Rozpoczynasz walkę na Arenie: {arena_type} ⚔️")
    animated_loading("Przywoływanie przeciwnika")
    arena = ArenaBattle(player, arena_type=arena_type, is_ranked=True)
    logs = arena.start_battle()

    for line in logs:
        slow_type(f" > {line}", delay=random.uniform(0.02, 0.06))
        time.sleep(0.3)

    print("\n🔥 Walka zakończona! 🔥")
    slow_type("🎁 Przydzielanie nagród...")
    save_game_state(player)
    pause(2)
    post_arena_menu(player)

def post_arena_menu(player):
    print_with_border("🏆 Co dalej?")
    print(" 1. Pokaż ranking")
    print(" 2. Wróć do Areny")
    print(" 0. Wyjście")

    choice = input("Twój wybór: ").strip()
    if choice == "1":
        display_ranking()
        post_arena_menu(player)
    elif choice == "2":
        display_arena_menu(player)
    else:
        slow_type("Powrót do gry...")

# Test lokalny
if __name__ == "__main__":
    player = load_player_profile("default_player")
    display_arena_menu(player)
