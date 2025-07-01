# keyboards/inline/market_buttons.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Główne menu rynku
market_menu = InlineKeyboardMarkup(row_width=2)
market_menu.add(
    InlineKeyboardButton(text="🛒 Przeglądaj rynek", callback_data="market_view"),
    InlineKeyboardButton(text="📤 Wystaw przedmiot", callback_data="market_sell")
)

# Przycisk powrotu
back_to_menu = InlineKeyboardMarkup()
back_to_menu.add(InlineKeyboardButton(text="↩️ Wróć", callback_data="back_to_market"))

# Potwierdzenie wystawienia
confirm_listing = InlineKeyboardMarkup(row_width=2)
confirm_listing.add(
    InlineKeyboardButton(text="✅ Tak", callback_data="confirm_yes"),
    InlineKeyboardButton(text="❌ Nie", callback_data="confirm_no")
)
