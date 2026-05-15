package main

import "fmt"

func main() {
	SafeWrapper()
	fmt.Println("System remains operational.")
}

func StartAgent(){
	defer fmt.Println("Cleaning up agent resources")
	panic("AGENT_CRITICAL_FAILURE")
}

func SafeWrapper(){
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Recovered from %v\n", r)
		}
	}()
	StartAgent()
}