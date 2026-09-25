character_name = "Ashborn - The Shadow Monarch (The greatest fragment of the brilliant light)"

class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.damage)
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} took {damage} damage! HP: {self.hp}")
        
class Hunter(Character):
    def __init__(self, name, rank):
        super().__init__(name, 100, 30)
        self.rank = rank
        self.inventory = []

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} obtained {item}!")


class Monster(Character):
    pass

player = Hunter("Ashborn", "The Shadow Monarch")
boss = Monster("Igris - The Red", 200, 15)

while player.hp > 0 and boss.hp > 0:
    player.attack(boss)
    print("You hit the boss!")
    boss.attack(player)
