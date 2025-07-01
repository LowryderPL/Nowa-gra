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

def draw_spell_list(class_name, selected_index):
    screen.fill(BLACK)
    spells = spellbook.get_spells_for_class(class_name)
    title = big_font.render(f"Czary klasy: {class_name}", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    for i, spell in enumerate(spells):
        color = (255, 215, 0) if i == selected_index else WHITE
        text = font.render(f"{spell['name']} (lvl {spell['level']})", True, color)
        screen.blit(text, (50, 80 + i * 30))

    if spells:
        selected_spell = spells[selected_index]
        desc = font.render(f"Opis: {selected_spell['description']}", True, WHITE)
        mana = font.render(f"Mana: {selected_spell['mana']}, Moc: {selected_spell['power']}", True, WHITE)
        screen.blit(desc, (50, HEIGHT - 80))
        screen.blit(mana, (50, HEIGHT - 50))

    pygame.display.flip()

def main():
    print("Wybierz klasę gracza spośród:")
    print(" - Wiedźmograd\n - Zjomistrz\n - Krwistostrzelec\n - Duszołowca")
    print(" - Runokultan\n - Cierniojad\n - Żarogniew\n - Mgłomistrz")
    class_name = input("Wpisz nazwę klasy gracza: ").strip()
    selected = 0
    clock = pygame.time.Clock()

    while True:
        draw_spell_list(class_name, selected)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(spellbook.get_spells_for_class(class_name))
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(spellbook.get_spells_for_class(class_name))

        clock.tick(15)

if __name__ == "__main__":
    main()
