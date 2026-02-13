import socket
import threading

def receive_messages(sock: socket.socket):
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8")
            print(msg)
            if "victory" in msg.lower():
                break
        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

print("Connected! Type 'attack' to fight.")

while True:
    # 1. Get user input
    action = input("Your Move: ")

    # 2. Send it to server
    client.send(bytes(action, "utf-8"))

    if "quit" in action.lower() or not action:
        break
client.close()