# npc_dialogue.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

npc_dialogues = {
    "znachorka": {
        "intro": "🌿 *Znachorka*: Witaj, podróżniku. Pachniesz... krwią i czarcim zielem. Czego szukasz w tej zapomnianej puszczy?",
        "options": [
            {"text": "🔮 Szukam wiedzy o eliksirach.", "response": "Mądry wybór. Wiedza to potęga. Przynieś mi korzeń mandragory..."},
            {"text": "⚔️ Słyszałem, że znasz drogę do artefaktu.", "response": "Tylko głupiec szuka artefaktu bez ofiary. Przynieś mi czaszkę wilkołaka."},
            {"text": "🚪 Żegnam.", "response": "Niech cie drzewa strzegą, dziecko mgły."}
        ]
    },
    "kuglarz": {
        "intro": "🎭 *Kuglarz*: Hej ho! Kiedyś byłem rycerzem, dziś jestem błaznem. Chcesz posłuchać pieśni... czy wolisz ukraść mi sakiewkę?",
        "options": [
            {"text": "🎵 Pieśń!", "response": "Był raz mag, co z błota tworzył złoto..."},
            {"text": "👜 Sakiewka!", "response": "Sprytny, ale głupi! Oto twoja kara: *-2 punkty akcji*"},
            {"text": "🚪 Odejście", "response": "Błazna się nie zapomina. Do zobaczenia!"}
        ]
    }
}

def start_npc_dialogue(update: Update, context: CallbackContext, npc_name: str):
    npc = npc_dialogues.get(npc_name)
    if npc:
        keyboard = [
            [InlineKeyboardButton(option["text"], callback_data=f"npc:{npc_name}:{idx}")]
            for idx, option in enumerate(npc["options"])
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_markdown(npc["intro"], reply_markup=reply_markup)
    else:
        update.message.reply_text("Nie rozpoznano tej postaci NPC.")

def handle_npc_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    _, npc_name, option_idx = query.data.split(":")
    option = npc_dialogues[npc_name]["options"][int(option_idx)]
    query.edit_message_text(f"{option['response']}")
