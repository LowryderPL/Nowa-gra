
import pygame
import sys
import spellbook  # Importuj swój plik z czarami

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spellbook GUI")

font = pygame.font.SysFont('timesnewroman', 20)
big_font = pygame.font.SysFont('timesnewroman', 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class_names = list(spellbook.spells_data.keys())
selected_class_index = 0

def draw_class_menu(selected_index):
    screen.fill(BLACK)
    title = big_font.render("Wybierz klasę postaci", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    for i, cls in enumerate(class_names):
        color = (255, 215, 0) if i == selected_index else WHITE
        text = font.render(cls, True, color)
        screen.blit(text, (WIDTH // 2 - 100, 80 + i * 30))

    pygame.display.flip()

def draw_spell_list(class_name, selected_index):
    screen.fill(BLACK)
    spells = spellbook.get_spells_for_class(class_name)
    title = big_font.render(f"Czary klasy: {class_name}", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    for i, spell in enumerate(spells):
        color = (255, 215, 0) if i == selected_index else WHITE
        text = font.render(f"{spell['name']} (lv {spell['level']})", True, color)
        screen.blit(text, (50, 80 + i * 30))

    if spells:
        selected_spell = spells[selected_index]
        desc = font.render(f"Opis: {selected_spell['description']}", True, WHITE)
        mana = font.render(f"Mana: {selected_spell['mana']}, Moc: {selected_spell['power']}", True, WHITE)
        screen.blit(desc, (50, HEIGHT - 80))
        screen.blit(mana, (50, HEIGHT - 50))

    pygame.display.flip()

def main():
    mode = "class_select"
    selected_index = 0
    clock = pygame.time.Clock()

    while True:
        if mode == "class_select":
            draw_class_menu(selected_index)
        elif mode == "spell_list":
            class_name = class_names[selected_class_index]
            draw_spell_list(class_name, selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % (len(class_names) if mode == "class_select" else len(spellbook.get_spells_for_class(class_names[selected_class_index])))
                elif event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % (len(class_names) if mode == "class_select" else len(spellbook.get_spells_for_class(class_names[selected_class_index])))
                elif event.key == pygame.K_RETURN:
                    global selected_class_index
                    if mode == "class_select":
                        selected_class_index = selected_index
                        selected_index = 0
                        mode = "spell_list"
                    else:
                        mode = "class_select"
                        selected_index = 0

        clock.tick(15)

if __name__ == "__main__":
    main()
