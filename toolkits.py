# tooltips.py – generowanie opisów przedmiotów

def generate_tooltip(item):
    """
    Tworzy opis (tooltip) dla danego przedmiotu.
    Wspiera pola: name, type, rarity, effect, level_required, special.
    """
    lines = [f"{item.get('name', 'Nieznany przedmiot')}"]

    if 'rarity' in item:
        lines.append(f"Rzadkość: {item['rarity'].capitalize()}")

    if 'effect' in item:
        lines.append(f"Efekt: {item['effect']}")

    if 'level_required' in item:
        lines.append(f"Wymagany poziom: {item['level_required']}")

    if item.get('special'):
        lines.append("✨ Przedmiot specjalny")

    return "\n".join(lines)
