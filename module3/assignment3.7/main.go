package main

import "fmt"

type NodeStatus int

const (
	StatusOffline = iota
	StatusOnline
	StatusMaintenance
	StatusDecommissioned
)

func RouteCommand(cmd string) string {
	switch cmd {
	case "START":
		return "Initializing subsystem components"
	case "STOP":
		return "Halting active system node tracks"
	case "DRAIN":
		return "Draining processing queues"
	default:
		return "Command unknown: operational rejection"
	}
}

func EvaluateMetric(cpuLoad float64) string {
	switch {
	case cpuLoad < 30.0:
		return "Optimal Utilization Profile"
	case cpuLoad >= 30.0 && cpuLoad <= 75.0:
		return "Standard Load Profile"
	case cpuLoad > 75.0:
		return "Critical Saturation Threshold"
	default:
		return "Well, that's not a healthy profile now, is it?"
	}
}

func SystemAlert(tier int) {
	switch tier {
	case 3:
		fmt.Println("Threat Level: Red alert")
		fallthrough
	case 4:
		fmt.Println("Automated protocol: Activating defense arrays")
	default:
		fmt.Println("Nothing suspicious...")
	}
}

func main() {
	fmt.Printf("StatusMaintenance:\n\ttype -> %T\n\tvalue -> %v\n", StatusMaintenance, StatusMaintenance)
	SystemAlert(3)
	const (
		PriorityLow = iota
		_
		_
		PriorityHigh
	)
	fmt.Println(PriorityHigh)
}
