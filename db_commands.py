# utils/db_api/db_commands.py

from utils.db_api.database import db

# INVENTORY SYSTEM

async def get_user_items(user_id):
    items = await db.fetch_all("SELECT * FROM inventory WHERE user_id = :user_id", {"user_id": user_id})
    return items

async def add_item_to_inventory(user_id, item_id, name, rarity):
    await db.execute("INSERT INTO inventory (user_id, item_id, name, rarity) VALUES (:user_id, :item_id, :name, :rarity)", {
        "user_id": user_id,
        "item_id": item_id,
        "name": name,
        "rarity": rarity
    })

async def remove_item_from_inventory(user_id, item_id):
    await db.execute("DELETE FROM inventory WHERE user_id = :user_id AND item_id = :item_id", {
        "user_id": user_id,
        "item_id": item_id
    })

# MARKETPLACE SYSTEM

async def get_market_items():
    items = await db.fetch_all("SELECT * FROM market")
    return items

async def add_item_to_market(user_id, item_id, price):
    await db.execute("INSERT INTO market (user_id, item_id, price) VALUES (:user_id, :item_id, :price)", {
        "user_id": user_id,
        "item_id": item_id,
        "price": price
    })

async def remove_item_from_market(item_id):
    await db.execute("DELETE FROM market WHERE item_id = :item_id", {"item_id": item_id})

async def buy_item_from_market(buyer_id, item_id):
    item = await db.fetch_one("SELECT * FROM market WHERE item_id = :item_id", {"item_id": item_id})
    if not item:
        return None

    await db.execute("INSERT INTO inventory (user_id, item_id, name, rarity) VALUES (:user_id, :item_id, :name, :rarity)", {
        "user_id": buyer_id,
        "item_id": item["item_id"],
        "name": item["name"],
        "rarity": item.get("rarity", "unknown")
    })

    await remove_item_from_market(item_id)
    return item

# CRAFTING SYSTEM

async def save_crafted_item(user_id, item_id, name, rarity, crafted_at):
    await db.execute(
        "INSERT INTO inventory (user_id, item_id, name, rarity, crafted_at) VALUES (:user_id, :item_id, :name, :rarity, :crafted_at)",
        {
            "user_id": user_id,
            "item_id": item_id,
            "name": name,
            "rarity": rarity,
            "crafted_at": crafted_at
        }
    )

# BOSS REWARDS

async def give_loot_from_boss(user_id, item_id, name, rarity):
    await db.execute("INSERT INTO inventory (user_id, item_id, name, rarity) VALUES (:user_id, :item_id, :name, :rarity)", {
        "user_id": user_id,
        "item_id": item_id,
        "name": name,
        "rarity": rarity
    })

# USER SYSTEM

async def get_user_balance(user_id):
    result = await db.fetch_one("SELECT balance FROM users WHERE user_id = :user_id", {"user_id": user_id})
    return result["balance"] if result else 0

async def update_user_balance(user_id, new_balance):
    await db.execute("UPDATE users SET balance = :balance WHERE user_id = :user_id", {
        "balance": new_balance,
        "user_id": user_id
    })
