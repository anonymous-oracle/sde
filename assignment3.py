character_name = "Ashborn - The Shadow Monarch (The greatest fragment of the brilliant light)"

class Hunter:
    # The Setup (Constructor)
    def __init__(self, name, rank):
        self.name = name       # Attribute
        self.rank = rank       # Attribute
        self.hp = 100          # Default Attribute
        self.inventory = []    # Each Hunter gets their own backpack!

    # An Action (Method)
    def show_stats(self):
        print(f"Hunter: {self.name} | Rank: {self.rank} | HP: {self.hp}")

    def take_damage(self):
        self.hp -= 20
        print(f"{self.name} took damage! HP is now {self.hp}")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} obtained {item}!")

player = Hunter("Ashborn", "The Shadow Monarch")
player.take_damage()
player.pick_up_item("Demon King's Dagger")
print(player.inventory)

