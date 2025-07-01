import random
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

user_crafting_attempts = {}

SPELLS = {
    "Ognista Kula": {
        "ingredients": ["Pył Feniksa", "Esencja Ognia", "Zwoje Runiczne"],
        "rarity": "epicka",
        "effect": "Zadaje 100 obrażeń obszarowych"
    },
    "Lodowa Zbroja": {
        "ingredients": ["Kryształ Lodu", "Skóra Trolla", "Esencja Tarczy"],
        "rarity": "rzadka",
        "effect": "Zwiększa obronę o 50%"
    },
    "Mroczna Więź": {
        "ingredients": ["Krew Upiora", "Mgła Zatracenia", "Kamień Cienia"],
        "rarity": "legendarna",
        "effect": "Przywołuje ducha zmarłego"
    }
}

COST_TON = 0.9
COOLDOWN = 2 * 24 * 60 * 60  # 2 dni
MAX_ATTEMPTS = 3
SUCCESS_RATE = 60  # %

def can_craft(user_id):
    now = time.time()
    attempts = user_crafting_attempts.get(user_id, [])
    attempts = [t for t in attempts if now - t < COOLDOWN]
    user_crafting_attempts[user_id] = attempts
    return len(attempts) < MAX_ATTEMPTS

def craft_spell(user_id, spell_name):
    if not can_craft(user_id):
        return "⚠️ Przekroczono limit 3 craftów na 2 dni."

    user_crafting_attempts[user_id].append(time.time())
    chance = random.randint(1, 100)

    if chance <= SUCCESS_RATE:
        bonus = ""
        if SPELLS[spell_name]["rarity"] == "legendarna":
            bonus = "🎁 BONUS: Losowy artefakt z FIROS!"
        return f"✅ Stworzono zaklęcie: {spell_name}\nEfekt: {SPELLS[spell_name]['effect']}\n{bonus}"
    else:
        fail_reward = random.choice(["Złom", "Złamany Zwój", "Resztki Magii", "Skręt Pająka"])
        return f"❌ Crafting nieudany. Otrzymano: {fail_reward}"

def show_crafting_menu(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton(f"{name} ({data['rarity']})", callback_data=f"craft_{name}")]
        for name, data in SPELLS.items()
    ]
    markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("🧪 Wybierz zaklęcie do stworzenia:", reply_markup=markup)

def handle_spell_crafting_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()
    if query.data.startswith("craft_"):
        spell_name = query.data[6:]
        result = craft_spell(user_id, spell_name)
        query.edit_message_text(result)
