# mana_system.py – System many gracza w grze Firos: Magic & Magic

class ManaManager:
    def __init__(self, max_mana=50):
        self.max_mana = max_mana
        self.current_mana = max_mana

    def spend_mana(self, cost):
        if self.current_mana >= cost:
            self.current_mana -= cost
            print(f"🔵 Zużyto {cost} many. Pozostało: {self.current_mana}/{self.max_mana}")
            return True
        else:
            print("❌ Nie masz wystarczającej ilości many!")
            return False

    def regenerate(self, amount):
        self.current_mana = min(self.max_mana, self.current_mana + amount)
        print(f"🔄 Zregenerowano {amount} many. Aktualnie: {self.current_mana}/{self.max_mana}")

    def show(self):
        print(f"🔷 MANA: {self.current_mana}/{self.max_mana}")
