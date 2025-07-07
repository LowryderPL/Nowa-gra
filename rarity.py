# rarity.py – System rzadkości dla przedmiotów Firos: Magic & Magic

def get_rarity_for_result(item_name):
    """
    Zwraca rzadkość danego przedmiotu na podstawie jego nazwy.
    Można tu zastosować bardziej złożone reguły lub bazę danych.
    """

    item_name = item_name.lower()

    if "miecz" in item_name or "zbroja" in item_name:
        if "cieni" in item_name or "demon" in item_name:
            return "legendarny"
        return "rzadki"

    if "eliksir" in item_name or "wywar" in item_name:
        if "krwi" in item_name or "chaosu" in item_name:
            return "epicki"
        return "rzadki"

    if "mikstura" in item_name:
        return "zwykły"

    return "zwykły"  # domyślna rzadkość
