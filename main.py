
"""
🎮 FIROS: MAGIC & MAGIC – GRA TERMINALOWA (main.py)
Zintegrowana z systemami gildii, małżeństw, handlu i łowienia ryb.
"""

from extended.guild_system import GuildSystem
from extended.marriage_system import MarriageSystem
from extended.trading_stalls import TradingStallsSystem
from extended.fishing_system import FishingSystem

# Inicjalizacja systemów
guilds = GuildSystem()
marriages = MarriageSystem()
stalls = TradingStallsSystem()
fishing = FishingSystem()

def main_menu():
    while True:
        print("\n🌍 Główne Menu:")
        print("1. Gildie")
        print("2. Małżeństwo")
        print("3. Handel (Szafki)")
        print("4. Łowienie ryb")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            guild_menu()
        elif choice == "2":
            marriage_menu()
        elif choice == "3":
            trading_menu()
        elif choice == "4":
            fishing_menu()
        elif choice == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór!")

def guild_menu():
    print("\n--- GILDIE ---")
    print("1. Stwórz Gildię")
    print("2. Dołącz do Gildii")
    print("3. Opuść Gildię")
    name = input("Nazwa gildii: ")
    if name:
        result = guilds.create_guild(name, "Gracz1")
        print(result[1])

def marriage_menu():
    print("\n--- MAŁŻEŃSTWO ---")
    print("1. Pobierz partnera")
    print("2. Weź ślub")
    print("3. Rozwiedź się")
    choice = input("Wybór: ")
    if choice == "1":
        partner = marriages.get_partner("Gracz1")
        print(f"Partner: {partner}" if partner else "Nie jesteś w związku.")
    elif choice == "2":
        p2 = input("Z kim chcesz się ożenić?: ")
        print(marriages.marry("Gracz1", p2)[1])
    elif choice == "3":
        print(marriages.divorce("Gracz1")[1])

def trading_menu():
    print("\n--- SZAFKA HANDLOWA ---")
    print("1. Wystaw przedmiot")
    print("2. Pokaż szafkę gracza")
    print("3. Usuń przedmiot")
    choice = input("Wybór: ")
    if choice == "1":
        item = input("Nazwa: ")
        price = int(input("Cena: "))
        qty = int(input("Ilość: "))
        print(stalls.add_stall("Gracz1", item, price, qty))
    elif choice == "2":
        owner = input("Gracz: ")
        offers = stalls.get_stalls(filter_by_owner=owner)
        for o in offers:
            print(o)
    elif choice == "3":
        item = input("Nazwa do usunięcia: ")
        print(stalls.remove_stall("Gracz1", item))

def fishing_menu():
    print("\n--- ŁOWIENIE RYB ---")
    location = input("Lokalizacja (Village Lake / Mystic River / Haunted Swamp / Frozen Fjord / Depths of Firos): ")
    result = fishing.fish("Gracz1", location)
    print(result[1])

if __name__ == "__main__":
    main_menu()
