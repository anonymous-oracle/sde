character_name = "Ashborn - The Shadow Monarch (The greatest fragment of the brilliant light)"

class Hunter:
    # The Setup (Constructor)
    def __init__(self, name, rank):
        self.name = name       # Attribute
        self.rank = rank       # Attribute
        self.hp = 100          # Default Attribute
        self.inventory = []    # Each Hunter gets their own backpack!
        self.damage = 30

    # An Action (Method)
    def show_stats(self):
        print(f"Hunter: {self.name} | Rank: {self.rank} | HP: {self.hp}")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} damage! HP is now {self.hp}")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} obtained {item}!")
    
    def attack(self, target):
        # target is going to be our Player object!
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.damage)

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        # target is going to be our Player object!
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} damage! HP is now {self.hp}")

player = Hunter("Ashborn", "The Shadow Monarch")
boss = Monster("Igris - The Red", 200, 15)

while player.hp > 0 and boss.hp > 0:
    player.attack(boss)
    print("You hit the boss!")
    boss.attack(player)
