class NFTItem:
    def __init__(self, id, name, item_type, rarity, power, magic, description):
        self.id = id
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.power = power
        self.magic = magic
        self.description = description

    def display(self):
        return f"[{self.rarity.upper()}] {self.name} | Power: {self.power}, Magic: {self.magic} — {self.description}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: NFTItem):
        self.items.append(item)

    def remove_item_by_id(self, id):
        self.items = [item for item in self.items if item.id != id]

    def list_inventory(self):
        if not self.items:
            return "📦 Twój ekwipunek jest pusty."
        return "\n".join(f"{idx + 1}. {item.display()}" for idx, item in enumerate(self.items))

    def get_items_by_rarity(self, rarity):
        return [item for item in self.items if item.rarity == rarity]

    def get_by_type(self, item_type):
        return [item for item in self.items if item.item_type == item_type]

# TEST

if __name__ == "__main__":
    inv = Inventory()
    inv.add_item(NFTItem(1, "Miecz Cienia", "broń", "epicki", 120, 0, "Przeklęty miecz wykuty z czarnego kamienia."))
    inv.add_item(NFTItem(2, "Zbroja Wędrowca", "zbroja", "rzadka", 0, 10, "Zbroja starego maga-wojownika."))
    inv.add_item(NFTItem(3, "Karta Bohatera: Eldrin", "karta klasowa", "unikatowa", 50, 150, "Elfi mag, obrońca Lasy Firowej."))

    print("\nTwój ekwipunek:\n")
    print(inv.list_inventory())
