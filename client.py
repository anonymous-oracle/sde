import socket

# 1. Create the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server
client.connect(("localhost", 9999))

# 3. Receive the message (buffer size 1024 bytes)
message = client.recv(1024)
print(message.decode("utf-8"))
