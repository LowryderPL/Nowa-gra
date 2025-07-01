# xp_system.py – System levelowania gracza w grze Firos: Magic & Magic

class PlayerStats:
    def __init__(self, name, level=1, exp=0, exp_to_next=100):
        self.name = name
        self.level = level
        self.exp = exp
        self.exp_to_next = exp_to_next
        self.skill_points = 0
        self.total_exp = 0

    def gain_exp(self, amount):
        print(f"\n📈 {self.name} zdobywa {amount} EXP!")
        self.exp += amount
        self.total_exp += amount

        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level_up()

        self.show_exp()

    def level_up(self):
        self.level += 1
        self.skill_points += 3
        self.exp_to_next = int(self.exp_to_next * 1.25)
        print(f"\n🎉 {self.name} awansował na poziom {self.level}!")
        print(f"🎁 Otrzymujesz 3 punkty umiejętności (razem: {self.skill_points})")

    def spend_point(self, stat):
        if self.skill_points <= 0:
            print("❌ Brak punktów do rozdania.")
            return

        print(f"🧬 Dodano 1 punkt do: {stat}")
        self.skill_points -= 1

    def show_exp(self):
        print(f"📊 EXP: {self.exp}/{self.exp_to_next} | Poziom: {self.level} | Skill Points: {self.skill_points}")

    def show_stats(self):
        print(f"\n=== POSTAĆ: {self.name} ===")
        print(f"Poziom: {self.level}")
        print(f"EXP: {self.exp}/{self.exp_to_next} (łącznie: {self.total_exp})")
        print(f"Punkty umiejętności: {self.skill_points}")

# Test lokalny
if __name__ == "__main__":
    player = PlayerStats("Geralt")
    player.show_stats()

    # Symulacja zdobywania EXP
    player.gain_exp(50)
    player.gain_exp(70)
    player.gain_exp(100)

    # Rozdawanie punktów (testowe)
    player.spend_point("siła")
    player.spend_point("magia")
    player.show_stats()
