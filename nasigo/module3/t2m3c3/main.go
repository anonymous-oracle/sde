package main

import "fmt"

type ProcessorCore struct {
	CoreID         int
	LoadPercentage float64
}

func (core ProcessorCore) StatusTrace() string {
	return fmt.Sprintf("Core-%d running at capacity\n", core.CoreID)
}

type NetworkRadio struct {
	RadioID        int
	LoadPercentage float64
}

func (radio NetworkRadio) StatusTrace() string {
	return fmt.Sprintf("Radio-%d broadcasting packets\n", radio.RadioID)
}

type ComputeNode struct {
	ProcessorCore
	NetworkRadio
	LoadPercentage float64
}

type RoutingSwarm struct {
	Nodes map[string]ComputeNode
}

func (swarm *RoutingSwarm) ExecuteNodeAudit(nodeKey string) {
	if _, ok := swarm.Nodes[nodeKey]; !ok {
		return
	}
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Audit Panic Bypassed: - %v\n", r)
		}
	}()
	node, _ := swarm.Nodes[nodeKey]
	if node.LoadPercentage == 99.9 {
		panic("CRITICAL_NODE_OVERLOAD")
	}
	fmt.Printf("Top Level load - %v\n", node.LoadPercentage)
	fmt.Printf("Processor Core load - %v\n", node.ProcessorCore.LoadPercentage)
	fmt.Printf("Network Radio Load - %v\n", node.NetworkRadio.LoadPercentage)
	node.ProcessorCore.StatusTrace()
	node.NetworkRadio.StatusTrace()
}

func main() {
	var routingSwarm RoutingSwarm = RoutingSwarm{Nodes: make(map[string]ComputeNode)}
	node := ComputeNode{LoadPercentage: 45.2, ProcessorCore: ProcessorCore{CoreID: 808, LoadPercentage: 12.5}, NetworkRadio: NetworkRadio{RadioID: 909, LoadPercentage: 88.1}}
	routingSwarm.Nodes["node-alpha"] = node
	node2 := ComputeNode{LoadPercentage: 99.9, ProcessorCore: ProcessorCore{}, NetworkRadio: NetworkRadio{}}
	routingSwarm.Nodes["node-omega"] = node2

	routingSwarm.ExecuteNodeAudit("node-alpha")
	routingSwarm.ExecuteNodeAudit("node-omega")

}
