import random

def attempt_craft(rarity, user_wallet, player_inventory):
    config = crafting_config.get(rarity)
    if not config:
        return "Nieznana rzadkość"

    if user_wallet["TON"] < config["cost"]["amount"]:
        return "Brak wystarczających środków"

    # Odejmij koszt
    user_wallet["TON"] -= config["cost"]["amount"]

    # Próba craftingu
    success = random.random() < config["success_chance"]

    if success:
        bonus = config.get("success_bonus")
        crafted_item = f"{rarity}_crafted_item"
        player_inventory.append(crafted_item)
        result = f"Crafting udany! Otrzymano: {crafted_item}"
        if bonus:
            player_inventory.append(bonus)
            result += f" + bonus: {bonus}"
        return result
    else:
        fallback = config.get("failure_reward")
        result = "Crafting nieudany."
        if fallback:
            player_inventory.append(fallback)
            result += f" Nagroda pocieszenia: {fallback}"
        # Losowe zdarzenie
        events = config.get("random_events_on_failure", [])
        if events:
            triggered = random.choice(events)
            result += f" Wydarzenie specjalne: {triggered}"
        return result
