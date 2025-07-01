from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api.db_commands import get_user_inventory, remove_item, upgrade_item
from keyboards.inline.inventory_buttons import inventory_menu, upgrade_confirm_buttons
from states.inventory_states import InventoryStates
from random import randint, choice

@dp.message_handler(commands=["inventory"])
async def show_inventory(message: types.Message):
    inventory = await get_user_inventory(user_id=message.from_user.id)
    if not inventory:
        await message.answer("🧳 Twój ekwipunek jest pusty.")
        return

    msg = "🎒 Twoje przedmioty:\n\n"
    for item in inventory:
        rarity = item.get("rarity", "Zwykły")
        lvl = item.get("level", 1)
        msg += f"🔹 {item['name']} | 🧬 Rzadkość: {rarity} | 📈 Poziom: {lvl}\n"

    await message.answer(msg, reply_markup=inventory_menu)

@dp.callback_query_handler(lambda c: c.data.startswith("upgrade_"))
async def initiate_upgrade(call: types.CallbackQuery, state: FSMContext):
    item_id = call.data.split("_")[1]
    await state.update_data(item_id=item_id)
    await call.message.edit_text(
        "🛠️ Czy chcesz ulepszyć ten przedmiot?\n\n💸 Koszt: 0.9 TON\n🎯 Szansa: 60%\n\nPotwierdzasz?",
        reply_markup=upgrade_confirm_buttons
    )
    await state.set_state(InventoryStates.ConfirmUpgrade)

@dp.callback_query_handler(text="upgrade_yes", state=InventoryStates.ConfirmUpgrade)
async def perform_upgrade(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    item_id = data["item_id"]
    user_id = call.from_user.id

    roll = randint(1, 100)
    if roll <= 60:
        await upgrade_item(user_id, item_id)
        await call.message.edit_text("✅ Ulepszenie zakończone sukcesem! 🔥 Twój przedmiot został wzmocniony.")
    else:
        # Niepowodzenie z efektem
        fallback = choice([
            "🪓 Złamany młotek – ale znalazłeś inny przedmiot!",
            "💥 Eksplozja! Przedmiot zniszczony, ale zdobywasz odłamek!",
            "🧿 Przeklęty dym – nic nie dostałeś, ale czujesz się obserwowany...",
            "🪙 Przedmiot przepalił się – w zamian otrzymujesz losowy drop!",
        ])
        await remove_item(user_id, item_id)
        await call.message.edit_text(f"❌ Niepowodzenie! {fallback}")

    await state.finish()

@dp.callback_query_handler(text="upgrade_no", state=InventoryStates.ConfirmUpgrade)
async def cancel_upgrade(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("❎ Anulowano ulepszanie.")
    await state.finish()
