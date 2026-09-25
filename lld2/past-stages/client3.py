import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

print("Connected! Type 'attack' to fight.")

while True:
    # 1. Get user input
    action = input("Your Move: ")

    # 2. Send it to server
    client.send(bytes(action, "utf-8"))

    # 3. Wait for reply
    response = client.recv(1024).decode("utf-8")
    print(f"Server says: {response}")

    if "VICTORY" in response:
        break
    if action == "quit":
        break

client.close()