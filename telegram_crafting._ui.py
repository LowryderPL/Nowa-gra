coding: utf-8

=== Pełny system Craftingu UI dla Telegram Bota ===

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update from telegram.ext import CallbackContext, CallbackQueryHandler from crafting_logic import CraftingSystem

Przechowujemy dane użytkowników tymczasowo

user_data_global = {} crafting_system = CraftingSystem(user_data_global)

def start_crafting_ui(update: Update, context: CallbackContext): keyboard = [ [InlineKeyboardButton("Craft Przedmiot - Common (0.2 TON)", callback_data='craft_common')], [InlineKeyboardButton("Uncommon (0.4 TON)", callback_data='craft_uncommon')], [InlineKeyboardButton("Rare (0.6 TON)", callback_data='craft_rare')], [InlineKeyboardButton("Epic (0.8 TON)", callback_data='craft_epic')], [InlineKeyboardButton("Legendary (1 TON)", callback_data='craft_legendary')], [InlineKeyboardButton("Mythic (3 TON)", callback_data='craft_mythic')], ] reply_markup = InlineKeyboardMarkup(keyboard) update.message.reply_text("Wybierz rzadkość przedmiotu do craftingu:", reply_markup=reply_markup)

def handle_crafting(update: Update, context: CallbackContext): query = update.callback_query query.answer() user_id = str(query.from_user.id)

rarity = query.data.replace('craft_', '')
result = crafting_system.attempt_craft(user_id, materials=None, rarity=rarity)

if result["success"]:
    msg = f'✅ Sukces! Stworzono: {result["item"]}\nKoszt: {result["cost"]} TON.'
else:
    msg = f'❌ {result["message"]}\nCraft nie powiódł się. Możesz spróbować ponownie jutro.'

query.edit_message_text(text=msg)

Rejestracja handlera:

dispatcher.add_handler(CommandHandler("craft", start_crafting_ui))

dispatcher.add_handler(CallbackQueryHandler(handle_crafting, pattern=r"^craft_"))

