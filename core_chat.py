core_chat_system.py - Rozszerzony system czatu dla Szachów Królewskich FIROS

import pygame import datetime

class ChatSystem: def init(self, quick_messages=None): self.messages = [] self.quick_messages = quick_messages or [] self.input_text = "" self.input_active = False self.scroll_offset = 0 self.max_messages = 15 self.rect = pygame.Rect(10, 10, 400, 220) self.font = pygame.font.SysFont(None, 24) self.username = "Gracz" self.chat_log_file = "chat_log.txt" self.color_player = (200, 255, 200) self.color_other = (255, 200, 200)

def draw(self, screen):
    pygame.draw.rect(screen, (10, 10, 10), self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    y_offset = self.rect.y + 5
    visible_messages = self.messages[-(self.max_messages + self.scroll_offset):-self.scroll_offset or None]
    for msg in visible_messages:
        color = self.color_player if msg.startswith("Ty:") else self.color_other
        msg_surface = self.font.render(msg, True, color)
        screen.blit(msg_surface, (self.rect.x + 5, y_offset))
        y_offset += 20

    if self.input_active:
        input_surface = self.font.render(self.input_text + "|", True, (255, 255, 255))
        screen.blit(input_surface, (self.rect.x + 5, y_offset))

def update(self):
    pass

def handle_click(self, pos):
    if self.rect.collidepoint(pos):
        self.input_active = True
    else:
        self.input_active = False

def handle_key(self, key):
    if not self.input_active:
        return

    if key == pygame.K_RETURN:
        self.send_message(self.input_text)
        self.input_text = ""
    elif key == pygame.K_BACKSPACE:
        self.input_text = self.input_text[:-1]
    elif key == pygame.K_UP:
        self.scroll_offset = min(self.scroll_offset + 1, len(self.messages))
    elif key == pygame.K_DOWN:
        self.scroll_offset = max(self.scroll_offset - 1, 0)
    else:
        name = pygame.key.name(key)
        if len(name) == 1:
            self.input_text += name

def send_message(self, text):
    if text.strip():
        formatted = f"Ty: {text}"
        self.messages.append(formatted)
        self.save_to_log(formatted)

def send_quick_message(self, text):
    formatted = f"(Szybko): {text}"
    self.messages.append(formatted)
    self.save_to_log(formatted)

def receive_message(self, text):
    formatted = f"{self.username}: {text}"
    self.messages.append(formatted)
    self.save_to_log(formatted)

def save_to_log(self, message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(self.chat_log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")

