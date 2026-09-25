package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net"
)

type Response struct {
	Data   string `json:"data"`
	Status string `json:"status"`
}

func main() {
	delimiter := []byte("\r\n\r\n")
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer ln.Close() // Ensure the listener is closed when the main function exits
	fmt.Println("Server listening on port 8080")

	clientConn, err := ln.Accept()
	if err != nil {
		fmt.Println("Error accepting connection:", err)
		return
	}
	defer clientConn.Close() // Ensure the client connection is closed when done
	fmt.Println("Accepted connection from", clientConn.RemoteAddr())
	buffer := make([]byte, 4096)
	clientData := make([]byte, 0, 4096)
	for {
		n, err := clientConn.Read(buffer)
		fmt.Println("Received data of", n, "bytes: ", string(buffer[:n]))
		if err != nil {
			fmt.Println("Error reading from connection:", err)
			break
		}
		if n == 0 {
			fmt.Println("Connection closed by client")
			break
		}
		clientData = append(clientData, buffer[:n]...)
		if bytes.Contains(clientData, delimiter) == true {
			fmt.Println("Received complete message:", string(clientData))
			fmt.Println("Total bytes:", len(clientData))
			break
		}
	}

	response := Response{
		Data:   string(clientData),
		Status: "ok",
	}
	fmt.Println("Response prepared:", response)
	responseVal, err := json.Marshal(response)
	if err != nil {
		fmt.Println("Error marshaling response:", err)
		return
	}

	// build the response
	fullResponse := fmt.Sprintf("HTTP/1.1 200 OK\r\nContent-Length: %v\r\nContent-Type: application/json\r\n\r\n%v", len(responseVal), string(responseVal))

	fmt.Println("Response JSON:", fullResponse)
	_, err = clientConn.Write([]byte(fullResponse))
	if err != nil {
		fmt.Println("Error writing response to client:", err)
		return
	}

}
