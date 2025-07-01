from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Przyciski do menu ekwipunku

inventory_menu = InlineKeyboardMarkup(row_width=2) inventory_menu.add( InlineKeyboardButton(text="⚡ Ulepsz przedmiot", callback_data="upgrade_item"), InlineKeyboardButton(text="↩ Powrót", callback_data="back_to_main_menu") )

Potwierdzenie ulepszania

confirm_upgrade = InlineKeyboardMarkup(row_width=2) confirm_upgrade.add( InlineKeyboardButton(text="✅ Tak", callback_data="confirm_upgrade_yes"), InlineKeyboardButton(text="❌ Nie", callback_data="confirm_upgrade_no") )

Powrót do menu ekwipunku

back_to_inventory = InlineKeyboardMarkup() back_to_inventory.add( InlineKeyboardButton(text="↩ Powrót do ekwipunku", callback_data="back_to_inventory") )

