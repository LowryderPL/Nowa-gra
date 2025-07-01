import pygame
import sys
from guilds import GuildsManager

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("FIROS: System Gildii")
clock = pygame.time.Clock()

font = pygame.font.SysFont("timesnewroman", 24)
manager = GuildsManager()
input_box = pygame.Rect(50, 50, 300, 40)
input_text = ''
info_message = ''
selected_guild_id = None

def draw_text(surface, text, pos, color=(255, 255, 255)):
    render = font.render(text, True, color)
    surface.blit(render, pos)

def draw_button(surface, text, rect, color, text_color=(0, 0, 0)):
    pygame.draw.rect(surface, color, rect)
    draw_text(surface, text, (rect.x + 10, rect.y + 10), text_color)

def render_guild_list(surface, guilds, selected):
    y = 150
    for guild in guilds:
        color = (180, 180, 255) if guild['id'] == selected else (100, 100, 100)
        pygame.draw.rect(surface, color, (50, y, 400, 40))
        draw_text(surface, f"{guild['name']} (Lv: {guild['level']}, Leader: {guild['leader']})", (60, y + 10))
        y += 50

def render_guild_details(surface, guild):
    if not guild:
        return
    draw_text(surface, f"--- GILDIA: {guild.name} ---", (500, 150))
    draw_text(surface, f"Poziom: {guild.guild_level}", (500, 180))
    draw_text(surface, f"Lider: {guild.leader_id}", (500, 210))
    draw_text(surface, f"Punkty: {guild.points}", (500, 240))
    draw_text(surface, f"Członkowie: {len(guild.members)}", (500, 270))
    draw_text(surface, f"Złoto: {guild.gold}", (500, 300))

    draw_text(surface, f"Ulepszenia:", (500, 330))
    for i, up in enumerate(guild.upgrades[-3:]):
        draw_text(surface, f"- {up}", (520, 360 + i * 20))

    draw_text(surface, f"Logi:", (500, 430))
    for i, log in enumerate(guild.logs[-4:]):
        draw_text(surface, f"- {log[-50:]}", (520, 460 + i * 20))

def main_loop():
    global input_text, info_message, selected_guild_id
    running = True

    while running:
        screen.fill((30, 30, 30))
        draw_text(screen, "Nowa Gildia:", (50, 20))
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)
        draw_text(screen, input_text, (input_box.x + 10, input_box.y + 10))

        draw_button(screen, "Utwórz", pygame.Rect(370, 50, 100, 40), (100, 255, 100))
        draw_button(screen, "Ulepsz", pygame.Rect(500, 360, 100, 40), (255, 200, 100))
        draw_button(screen, "Walka z bossem", pygame.Rect(620, 360, 180, 40), (255, 100, 100))

        if info_message:
            draw_text(screen, info_message, (50, 100), (255, 255, 0))

        guild_list = manager.list_guilds()
        render_guild_list(screen, guild_list, selected_guild_id)

        guild = manager.get_guild(selected_guild_id) if selected_guild_id else None
        render_guild_details(screen, guild)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                manager.save_guilds()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    pass
                elif pygame.Rect(370, 50, 100, 40).collidepoint(event.pos):
                    if input_text.strip():
                        gid = manager.create_guild(input_text.strip(), leader_id="Gracz#1")
                        selected_guild_id = gid
                        info_message = f"Utworzono gildię: {input_text.strip()}"
                        input_text = ''
                elif pygame.Rect(500, 360, 100, 40).collidepoint(event.pos):
                    if selected_guild_id:
                        manager.upgrade_guild(selected_guild_id, "Wieża Magii", 50)
                        info_message = "Ulepszono gildię!"
                elif pygame.Rect(620, 360, 180, 40).collidepoint(event.pos):
                    if selected_guild_id:
                        manager.run_guild_boss_battle(selected_guild_id, "Cień Smoka")
                        info_message = "Pokonano gildyjnego bossa!"

                y = 150
                for g in guild_list:
                    if pygame.Rect(50, y, 400, 40).collidepoint(event.pos):
                        selected_guild_id = g['id']
                    y += 50

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    input_text += event.unicode

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()
