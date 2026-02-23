import socket
import threading
import json

def receive_messages(sock: socket.socket):
    while True:
        try:
            server_data_raw = sock.recv(1024)
            if isinstance(server_data_raw, bytes):
                server_data_raw = server_data_raw.decode("utf-8")
            if not server_data_raw:
                break
            server_data_chunks = server_data_raw.split("\n")
            break_while = False
            for server_data in server_data_chunks:
                if server_data:
                    if isinstance(server_data, str):
                        server_data = json.loads(server_data)
                    msg = server_data.get("message", "")
                    print(msg)
                    if "victory" in msg.lower():
                        break_while = True
                        break
            if break_while:
                break
        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

print("Connected! Type 'attack' to fight.")

while True:
    # # 1. Get user input
    action = str(input("Your Move: "))
    if not action:
        continue
    if "quit" in action.lower():
        break
    payload = {"player": "Ashborn", "command":action}
    serialized_payload = json.dumps(payload) + "\n"
    # 2. Send it to server
    client.send(bytes(serialized_payload, "utf-8"))

    
client.close()