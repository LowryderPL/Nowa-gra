import pygame import sys

Inicjalizacja Pygame

pygame.init() screen = pygame.display.set_mode((1280, 720)) pygame.display.set_caption("FIROS: System Craftingu") font = pygame.font.SysFont("timesnewroman", 24) clock = pygame.time.Clock()

WHITE = (255, 255, 255) BLACK = (0, 0, 0) GRAY = (50, 50, 50) GOLD = (212, 175, 55)

Kategorie craftingu

CATEGORIES = ["Broń", "Zbroja", "Mikstura", "Runa", "Artefakt", "Specjalne"] selected_category = 0 selected_recipe = None

Przykladowe przepisy

RECIPES = { "Broń": [ {"name": "Miecz Płomienia", "materials": ["Stal", "Esencja Ognia"], "level": 3}, {"name": "Topór Runiczny", "materials": ["Drewno", "Runa Mocy"], "level": 2} ], "Zbroja": [ {"name": "Pancerz Cieni", "materials": ["Skóra", "Pył Cienia"], "level": 4}, {"name": "Hełm Trolla", "materials": ["Kość", "Skóra"], "level": 1} ], "Mikstura": [ {"name": "Mikstura Leczenia", "materials": ["Ziele", "Woda"], "level": 1}, {"name": "Eliksir Szybkości", "materials": ["Czerwony Grzyb", "Krew Wilka"], "level": 2} ], "Runa": [ {"name": "Runa Wzmocnienia", "materials": ["Kryształ", "Energia Runiczna"], "level": 2} ], "Artefakt": [ {"name": "Amulet Krwi", "materials": ["Rubin", "Krew Upiora"], "level": 5} ], "Specjalne": [ {"name": "Klejnot Wieczności", "materials": ["Diament", "Esencja Duszy", "Złoto"], "level": 10} ] }

Funkcja rysująca przyciski kategorii

def draw_categories(): y = 30 for i, category in enumerate(CATEGORIES): color = GOLD if i == selected_category else WHITE txt = font.render(category, True, color) screen.blit(txt, (30, y)) y += 35

Funkcja rysująca listę przepisów

def draw_recipes(): y = 30 recipes = RECIPES[CATEGORIES[selected_category]] for i, recipe in enumerate(recipes): name = recipe["name"] txt = font.render(f"{name} (Lvl {recipe['level']})", True, WHITE) screen.blit(txt, (300, y)) y += 40

Funkcja rysująca szczegóły przepisu

def draw_recipe_details(): if selected_recipe: txt = font.render(f"Tworzenie: {selected_recipe['name']}", True, GOLD) screen.blit(txt, (600, 100)) mat_txt = font.render("Materiały:", True, WHITE) screen.blit(mat_txt, (600, 140)) for i, mat in enumerate(selected_recipe["materials"]): m = font.render(f"- {mat}", True, WHITE) screen.blit(m, (600, 170 + i * 30))

Główna pętla gry

running = True while running: screen.fill(BLACK) draw_categories() draw_recipes() draw_recipe_details()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if 30 <= x <= 200:
            index = (y - 30) // 35
            if 0 <= index < len(CATEGORIES):
                selected_category = index
                selected_recipe = None
        elif 300 <= x <= 600:
            index = (y - 30) // 40
            recipes = RECIPES[CATEGORIES[selected_category]]
            if 0 <= index < len(recipes):
                selected_recipe = recipes[index]

pygame.display.flip()
clock.tick(30)

pygame.quit() sys.exit()

