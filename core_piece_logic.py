core_piece_logic.py - logika pionków i klas

import pygame

TILE_SIZE = 80

class Piece: def init(self, team, type, pos): self.team = team self.type = type  # np. "Wiedźmograd", "Zjomistrz" self.row, self.col = pos self.image = self.load_image()

def load_image(self):
    # Tymczasowa grafika pionków w zależności od typu
    surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
    if self.team == 0:
        surface.fill((0, 100, 200))
    else:
        surface.fill((200, 0, 0))
    return surface

def draw(self, screen):
    screen.blit(self.image, (self.col * TILE_SIZE, self.row * TILE_SIZE))

def can_move(self, dest_row, dest_col, board):
    # Prosta logika ruchu (przód i bicie na skos)
    dr = dest_row - self.row
    dc = dest_col - self.col
    if self.team == 0 and dr == 1 and abs(dc) <= 1:
        return True
    if self.team == 1 and dr == -1 and abs(dc) <= 1:
        return True
    return False

def cast_spell(self, spell, board):
    # Przykładowa obsługa czaru (tylko w trybie magicznym)
    print(f"{self.type} rzuca czar: {spell.name}")
    spell.apply_effect(self, board)

