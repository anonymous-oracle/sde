import sqlite3

class DatabaseManager:
    def __init__(self):
        # Connect to the file 'game_data.db'
        self.conn = sqlite3.connect('game_data.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create the table if it doesn't exist yet
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                name TEXT PRIMARY KEY,
                rank TEXT,
                hp INTEGER
            )
        ''')
        self.conn.commit() # Save changes

    def save_player(self, player):
        # "Upsert": Insert if new, Replace if exists
        self.cursor.execute('''
            INSERT OR REPLACE INTO players (name, rank, hp)
            VALUES (?, ?, ?)
        ''', (player.name, player.rank, player.hp))
        
        self.conn.commit()
        print(f"--- GAME SAVED: {player.name} ---")

    def load_player(self, name):
        self.cursor.execute("SELECT * FROM players WHERE name = ?", (name, ))
        data = self.cursor.fetchone() # get the first result
        return data # # Returns a tuple: (name, rank, hp) or None

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
    
    def __str__(self):
        return f"Hunter: {self.name} | Rank: {self.rank} | HP: {self.hp}"


class Monster(Character):
    pass

db = DatabaseManager()
player_data = db.load_player("Ashborn")

if player_data:
    print("--- WELCOME BACK, MONARCH ---")
    player = Hunter(player_data[0], player_data[1])
    player.hp = player_data[2]
    print(player)
else:
    print("--- NEW GAME STARTED ---")
    player = Hunter("Ashborn", "The Shadow Monarch")
boss = Monster("Igris - The Red", 200, 15)

while True:
    player.attack(boss)
    print("You hit the boss!")
    boss.attack(player)
    if player.hp <= 0 or boss.hp <= 0:
        break

db.save_player(player)
