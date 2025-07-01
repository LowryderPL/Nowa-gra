# states/market_states.py

from aiogram.dispatcher.filters.state import State, StatesGroup

class MarketStates(StatesGroup):
    SelectingItem = State()
    SettingPrice = State()
    ConfirmingListing = State()
