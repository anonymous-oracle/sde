package main

import "fmt"

func main (){
	var agentRegistry = map[string]bool {"Alpha": true, "Bravo": false}
	delete(agentRegistry, "Bravo")
	_, ok := agentRegistry["Alpha"]
	if ok {
		fmt.Printf("Alpha is online\n")
	} else {
		fmt.Printf("Alpha is offline\n")
	}
	delete(agentRegistry, "Alpha")
	_, ok = agentRegistry["Bravo"]
	if ok {
		fmt.Printf("Bravo is online\n")
	} else {
		fmt.Printf("Bravo not found\n")
	}
	delete(agentRegistry, "Bravo")
	for agt, item := range agentRegistry {
		if item {
			fmt.Printf("%s is online\n", agt)
		} else {
			fmt.Printf("%s is offline\n", agt)
		}
	}
}