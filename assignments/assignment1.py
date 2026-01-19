character_name = "Ashborn - The Shadow Monarch (The greatest fragment of the brilliant light)"

while True:
    direction = input("Do you want to go left or right? ").strip().lower()
    if direction == "left":
        print("You fell in a hole! Game over.")
        break
    elif direction == "right":
        print("You found a treasure!")
        break
    else:
        print("I do not understand")