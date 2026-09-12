import socket

# set reusable address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8080))
s.listen(5)
print("Server listening on port 8080")

client_bytes = b""
while True:
    client_socket, client_address = s.accept()
    print(f"Connection from {client_address}")
    recv_data = client_socket.recv(1024)
    if b"\r\n\r\n" in recv_data:
        break
    client_bytes += recv_data

response = f"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\n{client_bytes.decode()}".encode()
client_socket.sendall(response)
client_socket.close()
s.close()
