
from core import player_state
from core import game_loop
from modes.heroes import heroes_mode

def main():
    print("=== Firos: Magic & Magic – Tryb Heroes ===")
    player = player_state.Player()
    heroes_map = heroes_mode.HeroesMap(player)
    game_loop.start_game_loop(player, heroes_map)

if __name__ == "__main__":
    main()
