import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen()
print("Waiting for a challenger...")

client_socket, address = server.accept()
print(f"Challenger connected from {address}")

# --- GAME STATE (Lives on Server) ---
boss_hp = 100

# --- THE GAME LOOP ---
while True:
    # 1. Wait for command from client
    # We use 1024 bytes buffer size
    try:
        command = client_socket.recv(1024).decode("utf-8").lower()
    except:
        break # Client disconnected unexpectedly

    if not command or command in {"quit"}:
        print("Client disconnected")
        break

    # 2. Process the command (Game Logic)
    response = ""
    if command=="attack":
        boss_hp -= 10
        response = f"You hit the boss! Boss HP: {boss_hp}"
    elif command == "heal":
        boss_hp += 5
        response = f"You healed the Boss (Why?!). Boss HP: {boss_hp}"
    else:
        pass