package main

import (
    "fmt"
    "net"
)

func main() {
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	fmt.Println("Server listening on port 8080")

	clientConn, err := ln.Accept()
	if err != nil {
		fmt.Println("Error accepting connection:", err)
		return
	}
	fmt.Println("Accepted connection from", clientConn.RemoteAddr())
	buffer := make([]byte, 4096)
	n, err := clientConn.Read(buffer)
	if err != nil {
		fmt.Println("Error reading from connection:", err)
		return
	}
	fmt.Println("Received data of", n, "bytes: ", string(buffer[:n]))



	defer clientConn.Close() // Ensure the client connection is closed when done

	defer ln.Close() // Ensure the listener is closed when the main function exits
}