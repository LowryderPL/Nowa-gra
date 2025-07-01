# battle_chess.py — Pełny system Szachów Królewskich FIROS

# Obsługuje tryby 1v1, 2v2, 4v4, 10v10, klasyczne szachy i szachy magiczne

import pygame
import sys
from core.game_board import Board
from core.piece_logic import Piece
from core.magic_system import SpellManager
from core.lobby import LobbyManager
from core.chat import ChatSystem
from core.replay import ReplayManager
from core.rankings import RankingSystem
from core.tournament import TournamentSystem
from core.save_load import SaveSystem

# Inicjalizacja
pygame.init()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("FIROS: Royal Chess")
clock = pygame.time.Clock()

# Kolory i czcionki
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("timesnewroman", 24)

# Zmienne globalne
lobby = LobbyManager()
chat = ChatSystem(quick_messages=["GG", "Potężne zaklęcie!", "Dobra zagrywka", "Cofnij się!", "Twoja tura."])
spellbook = SpellManager()
rankings = RankingSystem()
tournaments = TournamentSystem()
save_system = SaveSystem()

# Tryby gry
GAME_MODES = ["Classic", "Magic"]
TEAM_SIZES = [2, 4, 8, 20]  # np. 1v1, 2v2, 4v4, 10v10

# Menu wyboru gry
def show_menu():
    print("=== FIROS: Royal Chess ===")
    print("Wybierz tryb gry:")
    for i, mode in enumerate(GAME_MODES):
        print(f"{i + 1}. {mode} szachy")
    mode = GAME_MODES[int(input("Tryb (1-2): ")) - 1]

    print("Wybierz typ rozgrywki:")
    for i, ts in enumerate(TEAM_SIZES):
        print(f"{i + 1}. {ts//2}v{ts//2}")
    team_size = TEAM_SIZES[int(input("Zespoły: ")) - 1]

    lobby.create_lobby(team_size)
    return mode, team_size

# Główna pętla gry
def run_game(mode, team_size):
    board = Board(mode, team_size)
    running = True
    replay = ReplayManager()

    while running:
        screen.fill(BLACK)
        board.draw(screen)
        chat.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_system.save(board)
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.handle_click(event.pos)
                chat.handle_click(event.pos)

            elif event.type == pygame.KEYDOWN:
                chat.handle_key(event.key)
                if event.key == pygame.K_r:
                    replay.start(board)
                elif event.key == pygame.K_e:
                    board.end_turn()
                elif event.key == pygame.K_q:
                    chat.send_quick_message("GG")
                elif event.key == pygame.K_t:
                    tournaments.start_tournament()

        board.update()
        replay.update(screen)
        chat.update()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

# Start gry
if __name__ == "__main__":
    selected_mode, selected_team_size = show_menu()
    run_game(selected_mode, selected_team_size)
