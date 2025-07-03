
import json
import os
from datetime import datetime

STALLS_FILE = "trading_stalls.json"

class TradingStall:
    def __init__(self, owner, item_name, price, quantity, timestamp=None):
        self.owner = owner
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "owner": self.owner,
            "item_name": self.item_name,
            "price": self.price,
            "quantity": self.quantity,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return TradingStall(
            owner=data["owner"],
            item_name=data["item_name"],
            price=data["price"],
            quantity=data["quantity"],
            timestamp=data.get("timestamp")
        )

class TradingStallsSystem:
    def __init__(self):
        self.stalls = []
        self.load_stalls()

    def load_stalls(self):
        if os.path.exists(STALLS_FILE):
            with open(STALLS_FILE, 'r') as f:
                data = json.load(f)
                self.stalls = [TradingStall.from_dict(entry) for entry in data]

    def save_stalls(self):
        with open(STALLS_FILE, 'w') as f:
            json.dump([stall.to_dict() for stall in self.stalls], f, indent=4)

    def add_stall(self, owner, item_name, price, quantity):
        stall = TradingStall(owner, item_name, price, quantity)
        self.stalls.append(stall)
        self.save_stalls()
        return f"{owner} listed {quantity}x {item_name} for {price} each."

    def remove_stall(self, owner, item_name):
        self.stalls = [s for s in self.stalls if not (s.owner == owner and s.item_name == item_name)]
        self.save_stalls()
        return f"{owner}'s listing for {item_name} removed."

    def get_stalls(self, filter_by_owner=None):
        if filter_by_owner:
            return [s.to_dict() for s in self.stalls if s.owner == filter_by_owner]
        return [s.to_dict() for s in self.stalls]
