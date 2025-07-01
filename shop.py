
import random
from inventory import add_item_to_inventory
from currencies import get_player_rfm, deduct_player_rfm
from items_data import get_available_items
from nft_marketplace import list_nft_for_sale, buy_nft
from gui_framework import display_shop_gui

# Stałe
MAX_SHOP_ITEMS = 12

# Przedmioty dostępne do zakupu
def generate_shop_inventory():
    all_items = get_available_items()
    return random.sample(all_items, min(MAX_SHOP_ITEMS, len(all_items)))

# Zakup przedmiotu za RFM
def purchase_item(player_id, item):
    player_rfm = get_player_rfm(player_id)
    if player_rfm >= item['price']:
        deduct_player_rfm(player_id, item['price'])
        add_item_to_inventory(player_id, item)
        return f"✔ Zakupiono: {item['name']}"
    else:
        return "❌ Brak wystarczających środków (RFM)"

# Główna funkcja sklepu
def open_shop(player_id):
    shop_inventory = generate_shop_inventory()
    result = display_shop_gui(player_id, shop_inventory)
    if result:
        return purchase_item(player_id, result)
    return "❌ Nie wybrano przedmiotu"

# Handel NFT
def handle_nft_transaction(buyer_id, seller_id, nft_id, price):
    success = buy_nft(buyer_id, seller_id, nft_id, price)
    return "✔ NFT zakupione" if success else "❌ Zakup NFT nie powiódł się"

# Funkcja testowa
if __name__ == "__main__":
    sample_player = "test_player_001"
    print(open_shop(sample_player))
