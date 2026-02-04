import socket
import threading # for concurrency
import queue # used for queueing actions from client events

boss_hp = 500 # shared game state, multiple players can join in to attack the boss
game_events = queue.Queue() # holds game events as a buffer
connected_clients = set()

def process_game_events():
    global game_events
    global boss_hp
    while boss_hp >= 0:
        event = game_events.get()
        attack_damage = event if isinstance(event, int) else 0
        boss_hp -= attack_damage
        print(boss_hp)

def broadcast(message: str):
    global connected_clients
    for client_socket in connected_clients:
        client_socket.send(bytes(message, "utf-8"))

def handle_client(client_socket: socket.socket, address):
    global connected_clients
    print(f"New connection from {address}")
    global game_events
    while True:
        try:
            command = client_socket.recv(1024).decode("utf-8").lower()
            if not command or command == "quit":
                break
            response = ""
            if command == "attack":
                game_events.put(10)
                client_socket.send(bytes("Attack queued", "utf-8"))
            else:
                response = "Unknown command."
            
            client_socket.send(bytes(response if response else f"BOSS HP - {boss_hp}", "utf-8"))

            if boss_hp <= 0:
                client_socket.send(bytes("\nBOSS DEFEATED! Everyone wins! VICTORY!!!", "utf-8"))
                break

        except:
            print(f"Connection to {address} shut down unexpectedly")
            connected_clients.remove(client_socket)
            break

    print(f"Player {address} disconnected.")
    client_socket.close()

# --- Main Server Setup ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()
print("Raid Server Started! Waiting for party members...")

game_event_thread = threading.Thread(target=process_game_events)
game_event_thread.start()

while True:
    # 1. Accept a new player
    client_socket, address = server.accept()
    connected_clients.add(client_socket)

    # 2. Create a specific thread just for them
    # target = the function to run
    # args = the inputs for that function
    thread = threading.Thread(target=handle_client, args=(client_socket, address))

    # 3. Start the thread (The assistant starts working)
    thread.start()

    # 4. The main loop immediately loops back to accept the NEXT player
    print(f"Active connections: {threading.active_count() - 2}")
