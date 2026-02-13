import socket
import threading # for concurrency

boss_hp = 500 # shared game state, multiple players can join in to attack the boss

def handle_client(client_socket: socket.socket, address):
    global boss_hp # refer to global scope boss_hp
    print(f"New connection from {address}")

    while True:
        try:
            command = client_socket.recv(1024).decode("utf-8").lower()
            if not command or command == "quit":
                break
            response = ""
            if command == "attack":
                boss_hp -= 10
                response = f"You hit! Global Boss HP: {boss_hp}"
            else:
                response = "Unknown command."
            
            client_socket.send(bytes(response, "utf-8"))

            if boss_hp <= 0:
                client_socket.send(bytes("\nBOSS DEFEATED! Everyone wins!", "utf-8"))
                break

        except:
            print(f"Connection to {address} shut down unexpectedly")
            break

    print(f"Player {address} disconnected.")
    client_socket.close()

# --- Main Server Setup ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()
print("Raid Server Started! Waiting for party members...")

while True:
    # 1. Accept a new player
    client_socket, address = server.accept()

    # 2. Create a specific thread just for them
    # target = the function to run
    # args = the inputs for that function
    thread = threading.Thread(target=handle_client, args=(client_socket, address))

    # 3. Start the thread (The assistant starts working)
    thread.start()

    # 4. The main loop immediately loops back to accept the NEXT player
    print(f"Active connections: {threading.active_count() - 1}")
