package main

import "fmt"

func main() {
	activeAgents := []string {"Alpha", "Bravo", "Charlie"}
	activeAgents = append(activeAgents, "Delta")

	for i, name := range activeAgents {
		fmt.Printf("Agent %d: %s\n", i, name)
	}
}