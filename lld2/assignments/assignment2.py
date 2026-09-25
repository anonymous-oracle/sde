character_name = "Ashborn - The Shadow Monarch (The greatest fragment of the brilliant light)"
inventory = []

def enter_dungeon_room():
    while True:
        direction = input("Do you want to go left or right? ").strip().lower()
        if direction == "left":
            print("You fell!")
            return "died"
        elif direction == "right":
            print("You found a sword!")
            return "survived"
        else:
            print("I do not understand")

if enter_dungeon_room() == "survived":
    print(inventory)