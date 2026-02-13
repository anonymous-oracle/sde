import socket

# 1. Create the socket (AF_INET = Internet, SOCK_STREAM = TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to an address (localhost means "this computer", 9999 is the "door" number)
server.bind(("localhost", 9999))

# 3. Start listening
server.listen()
print("Server is listening on port 9999...")

# 4. Accept a connection (This halts the code until someone connects!)
client_socket, address = server.accept()
print(f"Connection from {address} has been established!")

# 5. Send a welcome message
client_socket.send(bytes("Welcome to the Hunter Association Server!", "utf-8"))