# marketplace.py — logika handlu w grze Firos

class Item:
    def __init__(self, name, description, rarity, price_rfn, price_ton):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.price_rfn = price_rfn  # cena w RFN (waluta gry)
        self.price_ton = price_ton  # cena w TON (kryptowaluta)

    def __repr__(self):
        return f"<Item: {self.name} ({self.rarity}) - {self.price_rfn} RFN / {self.price_ton} TON>"


class Player:
    def __init__(self, name, balance_rfn, balance_ton):
        self.name = name
        self.balance_rfn = balance_rfn
        self.balance_ton = balance_ton
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def __repr__(self):
        return f"<Player: {self.name} - {self.balance_rfn} RFN / {self.balance_ton} TON>"


class Marketplace:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def buy_item(self, item_name, player: Player, currency="RFN"):
        for item in self.items:
            if item.name == item_name:
                if currency == "RFN" and player.balance_rfn >= item.price_rfn:
                    player.balance_rfn -= item.price_rfn
                    player.add_item(item)
                    self.items.remove(item)
                    return f"{player.name} kupił {item.name} za {item.price_rfn} RFN."

                elif currency == "TON" and player.balance_ton >= item.price_ton:
                    player.balance_ton -= item.price_ton
                    player.add_item(item)
                    self.items.remove(item)
                    return f"{player.name} kupił {item.name} za {item.price_ton} TON."

                else:
                    return "Za mało środków!"

        return "Przedmiot nie znaleziony."

    def sell_item(self, item_name, player: Player, currency="RFN"):
        for item in player.inventory:
            if item.name == item_name:
                if currency == "RFN":
                    player.balance_rfn += item.price_rfn
                else:
                    player.balance_ton += item.price_ton

                self.items.append(item)
                player.inventory.remove(item)
                return f"{player.name} sprzedał {item.name}."

        return "Przedmiot nie znaleziony w ekwipunku."

    def list_items(self):
        return [str(item) for item in self.items]
