import socket
import threading # for concurrency
import queue # used for queueing actions from client events
import json

boss_hp = 500 # shared game state, multiple players can join in to attack the boss
game_events = queue.Queue() # holds game events as a buffer
connected_clients = set()

def process_game_events():
    global boss_hp
    while boss_hp >= 0:
        event_data = game_events.get()
        attack_damage = event_data.get("damage", 10)
        player = event_data.get("player", "Ashborn")
        boss_hp -= attack_damage
        if boss_hp <= 0:
            break
        broadcast({"type": "update", "hp": boss_hp, "message":f"{player} hit the Boss! HP: {boss_hp}\n"})
    broadcast({"type": "update", "hp": boss_hp, "message":f"VICTORY! Boss Down.\n{player} hit the Boss! HP: {boss_hp}\n"})

def broadcast(message_payload: dict):
    for client_socket in connected_clients.copy():
        try:
            client_socket.send(bytes(json.dumps(message_payload), "utf-8"))
        except:
            pass

def handle_client(client_socket: socket.socket, address):
    print(f"New connection from {address}")
    global game_events
    try:
        while True:
            try:
                client_data_raw = client_socket.recv(1024).decode("utf-8")
                client_data = json.loads(client_data_raw)
                player, command = client_data.get("player", "Ashborn"), client_data.get("command", "attack")

                if not command or command == "quit":
                    connected_clients.discard(client_socket)
                    break
                response = ""
                if command == "attack":
                    game_events.put(
                        {
                            "player": player,
                            "damage": 10
                        }
                    )
                else:
                    response = "Unknown command."
                
            except:
                print(f"Connection to {address} shut down unexpectedly")
                connected_clients.discard(client_socket)
                break

        print(f"Player {address} disconnected.")
        client_socket.close()
    except:
        print("Unexpected failure. Shutting down the client connection.")
        connected_clients.discard(client_socket)

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
