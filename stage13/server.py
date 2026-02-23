import socket
import threading # for concurrency
import queue # used for queueing actions from client events
import json



class RaidServer:
    def __init__(self):
        self.boss_hp = 500
        self.connected_clients = set()
        self.game_events = queue.Queue()
        self.broadcast_queue = queue.Queue()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 9999))
        self.server.listen()


    def process_game_events(self):
        while self.boss_hp >= 0:
            event_data = self.game_events.get()
            attack_damage = event_data.get("damage", 10)
            player = event_data.get("player", "Ashborn")
            self.boss_hp -= attack_damage
            if self.boss_hp <= 0:
                break
            self.broadcast_queue.put({"type": "update", "hp": self.boss_hp, "message":f"{player} hit the Boss! HP: {self.boss_hp}"})
        self.broadcast_queue.put({"type": "update", "hp": self.boss_hp, "message":f"VICTORY! Boss Down.\n{player} hit the Boss! HP: {self.boss_hp}\n"})

    def broadcast_dispatcher(self):
        while True:
            broadcast_event = self.broadcast_queue.get()
            if broadcast_event:
                self.broadcast(broadcast_event)

    def broadcast(self, message_payload: dict):
        payload = json.dumps(message_payload) + "\n"
        for client_socket in self.connected_clients.copy():
            try:
                client_socket.send(bytes(payload, "utf-8"))
            except:
                pass

    def handle_client(self, client_socket: socket.socket, address):
        print(f"New connection from {address}")
        try:
            while True:
                try:
                    client_data_raw = client_socket.recv(1024)
                    client_data_obj = {}
                    if not client_data_raw:
                        break
                    if isinstance(client_data_raw, bytes):
                        client_data_raw = client_data_raw.decode("utf-8")
                    client_data_chunks = client_data_raw.split("\n")
                    break_while = False
                    for client_data in client_data_chunks:
                        if not client_data:
                            continue
                        if isinstance(client_data, str):
                            client_data_obj = json.loads(client_data)
                        player, command = client_data_obj.get("player"), client_data_obj.get("command")

                        if not command or command == "quit":
                            self.connected_clients.discard(client_socket)
                            break_while = True
                        response = ""
                        if command == "attack":
                            self.game_events.put(
                                {
                                    "player": player,
                                    "damage": 10
                                }
                            )
                        else:
                            response = "Unknown command."
                    if break_while:
                        break
                    
                except:
                    print(f"Connection to {address} shut down unexpectedly")
                    self.connected_clients.discard(client_socket)
                    break

            print(f"Player {address} disconnected.")
            client_socket.close()
            self.connected_clients.discard(client_socket)
        except:
            print("Unexpected failure. Shutting down the client connection.")
            self.connected_clients.discard(client_socket)


    def start(self):
        game_event_thread = threading.Thread(target=self.process_game_events)
        game_event_thread.start()
        broadcast_thread = threading.Thread(target=self.broadcast_dispatcher)
        broadcast_thread.start()

        while True:
            # 1. Accept a new player
            client_socket, address = self.server.accept()
            self.connected_clients.add(client_socket)

            # 2. Create a specific thread just for them
            # target = the function to run
            # args = the inputs for that function
            thread = threading.Thread(target=self.handle_client, args=(client_socket, address))

            # 3. Start the thread (The assistant starts working)
            thread.start()

            # 4. The main loop immediately loops back to accept the NEXT player
            print(f"Active connections: {threading.active_count() - 2}")

if __name__ == "__main__":
    raid = RaidServer()
    print("Raid Server Started! Waiting for party members...")
    raid.start()