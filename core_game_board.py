core/game_board.py - Pełna wersja z rozszerzeniami

import pygame from core.piece_logic import Piece from core.magic_system import SpellManager

TILE_SIZE = 80 ROWS, COLS = 8, 8

Kolory

WHITE = (255, 255, 255) BLACK = (0, 0, 0) GRAY = (100, 100, 100) GREEN = (0, 255, 0) RED = (255, 0, 0) BLUE = (0, 0, 255)

class Board: def init(self, mode="Classic", team_size=2): self.mode = mode self.team_size = team_size self.tiles = [[None for _ in range(COLS)] for _ in range(ROWS)] self.selected_piece = None self.turn = 0 self.font = pygame.font.SysFont("timesnewroman", 18) self.init_board() self.spellbook = SpellManager()

def init_board(self):
    # Tymczasowe ustawienie pionków, zgodnie z trybem i drużynami
    for row in range(2):
        for col in range(COLS):
            self.tiles[row][col] = Piece(team=0, type="pawn", pos=(row, col))
    for row in range(6, 8):
        for col in range(COLS):
            self.tiles[row][col] = Piece(team=1, type="pawn", pos=(row, col))

def draw(self, screen):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, rect)
            piece = self.tiles[row][col]
            if piece:
                piece.draw(screen)
    # Wyświetlanie aktualnej tury
    turn_text = self.font.render(f"Tura: {self.turn + 1}", True, RED)
    screen.blit(turn_text, (10, 660))

def handle_click(self, pos):
    col = pos[0] // TILE_SIZE
    row = pos[1] // TILE_SIZE
    if row >= ROWS or col >= COLS:
        return
    clicked = self.tiles[row][col]
    if self.selected_piece:
        if self.selected_piece.can_move(row, col, self.tiles):
            self.tiles[self.selected_piece.row][self.selected_piece.col] = None
            self.selected_piece.row = row
            self.selected_piece.col = col
            self.tiles[row][col] = self.selected_piece
            self.end_turn()
        self.selected_piece = None
    elif clicked:
        self.selected_piece = clicked

def end_turn(self):
    self.turn += 1
    if self.mode == "Magic":
        self.spellbook.apply_passive_effects(self.tiles)

def update(self):
    # Można dodać efekty czarów lub inne animacje
    pass

