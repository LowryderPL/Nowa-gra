import json
import os
import random

MARKET_FILE = "market_data.json"
INVENTORY_FOLDER = "inventories"
OWNER_ADDRESS = "UQAnzg088aqSorf2rYteBGw6duFLYTR8VlxJv3QsXcALOKjP"
MARKET_FEE = 0.15  # 15% prowizji

def load_market():
    if not os.path.exists(MARKET_FILE):
        return []
    with open(MARKET_FILE, "r") as f:
        return json.load(f)

def save_market(market_data):
    with open(MARKET_FILE, "w") as f:
        json.dump(market_data, f, indent=2)

def list_market_items():
    market = load_market()
    return [f"{item['item']} - {item['price']} TON (sprzedawca: {item['user']})" for item in market]

def add_item_to_market(user_id, item, price):
    market = load_market()
    market.append({
        "user": user_id,
        "item": item,
        "price": round(price, 2)
    })
    save_market(market)

def purchase_item(buyer_id, item_name):
    market = load_market()
    for item in market:
        if item["item"].lower() == item_name.lower():
            price = item["price"]
            seller = item["user"]

            # Prowizja
            fee = round(price * MARKET_FEE, 2)
            seller_gain = price - fee

            # Dodaj do inventory kupującego
            add_item_to_inventory(buyer_id, item_name)

            # Drop bonusowy za zakup (losowy)
            if random.random() < 0.25:
                add_item_to_inventory(buyer_id, "🎁 Losowy bonus")

            # Usuwamy z marketu
            market.remove(item)
            save_market(market)

            return f"✅ Zakupiono {item_name} za {price} TON.\n💰 Sprzedawca otrzymał {seller_gain} TON\n💎 Prowizja: {fee} TON dla właściciela."

    return "❌ Przedmiot niedostępny."

def add_item_to_inventory(user_id, item):
    inventory_path = os.path.join(INVENTORY_FOLDER, f"{user_id}.json")
    if not os.path.exists(inventory_path):
        data = {"items": []}
    else:
        with open(inventory_path, "r") as f:
            data = json.load(f)

    data["items"].append(item)
    with open(inventory_path, "w") as f:
        json.dump(data, f, indent=2)

def get_user_inventory(user_id):
    inventory_path = os.path.join(INVENTORY_FOLDER, f"{user_id}.json")
    if not os.path.exists(inventory_path):
        return {"items": []}
    with open(inventory_path, "r") as f:
        return json.load(f)
