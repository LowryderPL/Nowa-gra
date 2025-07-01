from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from inventory import get_user_inventory
from crafting_logic import attempt_craft
from marketplace_logic import list_market_items
InlineKeyboardButton("🛒 Marketplace", callback_data="menu_market")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Witaj w świecie Firos: Magic & Magic!",
        reply_markup=main_menu()
    )

def main_menu():
    buttons = [
        [InlineKeyboardButton("📦 Inventory", callback_data="inventory")],
        [InlineKeyboardButton("🛠️ Crafting", callback_data="craft")],
        [InlineKeyboardButton("🏪 Marketplace", callback_data="market")],
    ]
    return InlineKeyboardMarkup(buttons)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = str(query.from_user.id)

    if query.data == "inventory":
        inventory = get_user_inventory(user_id)
        items = inventory.get("items", [])
        text = "📦 Twoje przedmioty:\n" + "\n".join([f"- {item}" for item in items]) if items else "📭 Ekwipunek jest pusty."
        await query.edit_message_text(text=text, reply_markup=main_menu())

    elif query.data == "craft":
        result = attempt_craft(user_id)
        await query.edit_message_text(text=f"🛠️ {result}", reply_markup=main_menu())

    elif query.data == "market":
        items = list_market_items()
        text = "🏪 Dostępne przedmioty:\n" + "\n".join(items) if items else "🔒 Brak aktywnych ofert."
        await query.edit_message_text(text=text, reply_markup=main_menu())

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CallbackQueryHandler(handle_button))
