
class MountGUI:
    def __init__(self, player):
        self.player = player
        self.current_mount = None
        self.mounts = []

    def load_mounts_from_inventory(self):
        self.mounts = [item for item in self.player.inventory if item.get("type") == "Mount"]

    def display_mount_menu(self):
        print("🐎 Your Mounts:")
        for idx, mount in enumerate(self.mounts):
            print(f"{idx+1}. {mount['name']} ({mount['rarity']}) – {mount['bonus']}")
        print("0. Unequip current mount")

    def select_mount(self, choice):
        if choice == 0:
            self.current_mount = None
            print("❌ Mount unequipped.")
        elif 0 < choice <= len(self.mounts):
            self.current_mount = self.mounts[choice - 1]
            print(f"✅ Equipped mount: {self.current_mount['name']} – {self.current_mount['bonus']}")
        else:
            print("Invalid choice.")

    def get_active_bonus(self):
        return self.current_mount["bonus"] if self.current_mount else "No active mount bonus."

    def show_current(self):
        if self.current_mount:
            print(f"🧭 Current mount: {self.current_mount['name']} – Bonus: {self.current_mount['bonus']}")
        else:
            print("🚶 No mount equipped.")
