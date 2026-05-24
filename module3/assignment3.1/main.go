package main

import "fmt"

type AgentCard struct {
	ID         int
	Name       string
	PowerLevel float64
}

type ControlPlane struct {
	ActiveAgent AgentCard
}

func main() {
	var myAgent AgentCard = AgentCard{ID: 101, Name: "Nasiko-01", PowerLevel: 9.5}
	var controlPlane ControlPlane = ControlPlane{ActiveAgent: myAgent}

	fmt.Printf("%+v\n", controlPlane)
}
