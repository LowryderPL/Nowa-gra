from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import TON_OWNER_WALLET
from utils.db_api.db_commands import (
    get_user_items, get_market_items,
    remove_item_from_inventory, add_item_to_market,
    remove_item_from_market, transfer_item_to_buyer
)
from keyboards.inline.market_buttons import market_menu, back_to_menu, confirm_listing, confirm_purchase
from states.market_states import MarketStates

@dp.message_handler(commands=['market'])
async def open_market_menu(message: types.Message):
    await message.answer("🏪 Witaj na Rynku NFT!\n\nWybierz, co chcesz zrobić:", reply_markup=market_menu)

@dp.callback_query_handler(text='market_view')
async def view_market(call: types.CallbackQuery):
    items = await get_market_items()
    if not items:
        await call.message.edit_text("⚠️ Brak przedmiotów na rynku.", reply_markup=back_to_menu)
        return

    msg = "🛒 Przedmioty na rynku:\n\n"
    for item in items:
        msg += f"🔹 {item['name']} – {item['price']} TON\n"
        msg += f"/buy_{item['id']}\n\n"

    await call.message.edit_text(msg, reply_markup=back_to_menu)

@dp.callback_query_handler(lambda c: c.data.startswith("buy_"))
async def handle_buy_request(call: types.CallbackQuery, state: FSMContext):
    item_id = call.data.split("_")[1]
    await state.update_data(item_id=item_id, buyer_id=call.from_user.id)
    await call.message.answer("✅ Czy na pewno chcesz kupić ten przedmiot?", reply_markup=confirm_purchase)
    await state.set_state(MarketStates.ConfirmingPurchase)

@dp.callback_query_handler(text='buy_yes', state=MarketStates.ConfirmingPurchase)
async def finalize_purchase(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    item_id = data['item_id']
    buyer_id = data['buyer_id']

    item = await remove_item_from_market(item_id)
    if not item:
        await call.message.edit_text("❌ Przedmiot został już sprzedany.", reply_markup=market_menu)
        await state.finish()
        return

    tax = round(item['price'] * 0.12, 2)
    final_price = item['price']
    seller_amount = round(final_price - tax, 2)

    ton_url = f"https://tonkeeper.com/transfer/{TON_OWNER_WALLET}?amount={final_price}&text=NFT%20market"

    await transfer_item_to_buyer(buyer_id, item['id'])
    await call.message.edit_text(
        f"✅ Zakup zakończony sukcesem!\n\n💸 Zapłać: {final_price} TON\n"
        f"🏷️ Przedmiot: {item['name']}\n📲 [Kliknij, aby zapłacić TON]({ton_url})",
        reply_markup=market_menu,
        parse_mode='Markdown'
    )
    await state.finish()

@dp.callback_query_handler(text='buy_no', state=MarketStates.ConfirmingPurchase)
async def cancel_purchase(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("❌ Anulowano zakup.", reply_markup=market_menu)
    await state.finish()

@dp.callback_query_handler(text='market_sell')
async def sell_item_step1(call: types.CallbackQuery, state: FSMContext):
    items = await get_user_items(user_id=call.from_user.id)
    if not items:
        await call.message.edit_text("🧳 Brak przedmiotów w ekwipunku!", reply_markup=back_to_menu)
        return

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for item in items:
        keyboard.add(types.InlineKeyboardButton(text=item['name'], callback_data=f"sell_{item['id']}"))
    keyboard.add(types.InlineKeyboardButton(text="↩️ Wróć", callback_data="back_to_market"))

    await call.message.edit_text("📦 Wybierz przedmiot do wystawienia:", reply_markup=keyboard)
    await state.set_state(MarketStates.SelectingItem)

@dp.callback_query_handler(lambda c: c.data.startswith("sell_"), state=MarketStates.SelectingItem)
async def sell_item_step2(call: types.CallbackQuery, state: FSMContext):
    item_id = call.data.split("_")[1]
    await state.update_data(item_id=item_id)
    await call.message.edit_text("💰 Podaj cenę w TON:")
    await state.set_state(MarketStates.SettingPrice)

@dp.message_handler(state=MarketStates.SettingPrice)
async def sell_item_confirm(message: types.Message, state: FSMContext):
    try:
        price = float(message.text.replace(",", "."))
        if price <= 0:
            raise ValueError
    except ValueError:
        await message.answer("❌ Błędna cena. Spróbuj ponownie (np. 1.2).")
        return

    await state.update_data(price=price)
    data = await state.get_data()
    item_id = data['item_id']

    await message.answer(
        f"✅ Czy chcesz wystawić przedmiot ID {item_id} za {price} TON?",
        reply_markup=confirm_listing
    )
    await state.set_state(MarketStates.ConfirmingListing)

@dp.callback_query_handler(text='confirm_yes', state=MarketStates.ConfirmingListing)
async def finalize_listing(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await remove_item_from_inventory(call.from_user.id, data['item_id'])
    await add_item_to_market(call.from_user.id, data['item_id'], data['price'])
    await call.message.edit_text("✅ Przedmiot został wystawiony!", reply_markup=market_menu)
    await state.finish()

@dp.callback_query_handler(text='confirm_no', state=MarketStates.ConfirmingListing)
async def cancel_listing(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("❌ Wystawianie anulowane.", reply_markup=market_menu)
    await state.finish()

@dp.callback_query_handler(text='back_to_market')
async def back_to_market(call: types.CallbackQuery):
    await call.message.edit_text("↩️ Powrót do rynku:", reply_markup=market_menu)
