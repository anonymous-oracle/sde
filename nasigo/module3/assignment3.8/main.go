package main

import "fmt"

type ClusterRank int

const (
	RankUnknown = iota
	RankPrimary
	RankSecondary
	RankBackup
)

type Celsius float64
type Fahrenheit float64

type NodeIdentity struct {
	ID    int
	Name  string
	Class ClusterRank
}

type ComputeCore struct {
	CoreID   int
	CoreTemp Celsius
	Load     float64
}

type DataNode struct {
	Meta      NodeIdentity
	Processor ComputeCore
	Online    bool
}

type EngineCluster struct {
	nodeMap map[string]DataNode
}

func (engineClusterMap *EngineCluster) IngestTelemetry(key string, updatedLoad float64, tempCelsius float64) {
	if cluster, ok := engineClusterMap.nodeMap[key]; ok {
		cluster.Processor.Load = updatedLoad
		cluster.Processor.CoreTemp = Celsius(tempCelsius)
		updatedLoad := 999.9
		fmt.Println("Updated Load inside if block", updatedLoad)
	}
	fmt.Println("Updated Load outside if block", updatedLoad)
}

func (engineClusterMap EngineCluster) CalculateHeatIndex(key string) (Fahrenheit, error) {
	if cluster, ok := engineClusterMap.nodeMap[key]; ok {
		coreTemp := cluster.Processor.CoreTemp
		return Fahrenheit((float64(coreTemp) * 1.9) + 32), nil
	} else {
		return 0.0, fmt.Errorf("node identity %s missing from telemetry trace", key)
	}
}

func RouteAlert(load float64) {
	switch {
	case load > 85.0:
		fmt.Println("CRITICAL ISOLATION PROTOCOL ENGAGED")
		fallthrough
	case load > 60.0:
		fmt.Println("ALERT LEVEL MODERATE: EXPANDING QUEUE LIMITS")
	default:
		fmt.Println("Subsystem matrix running within baseline limits.")
	}
}

func SafeExecute(cluster *EngineCluster) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("Catastrophic fault isoldated cleanly. Message: %v\n", r)
		}
	}()
	cluster.IngestTelemetry("Node-Alpha", 92.5, 45.0)
	panic("HARDWARE_THERMAL_MELTDOWN")
}

func main() {
	var engineCluster EngineCluster
	engineCluster.nodeMap = make(map[string]DataNode)

	nodeName := "Node-Alpha"
	node := DataNode{Meta: NodeIdentity{ID: 77, Name: nodeName, Class: RankPrimary}, Processor: ComputeCore{CoreID: 1, CoreTemp: 22.5, Load: 10.0}, Online: true}
	engineCluster.nodeMap[nodeName] = node
	SafeExecute(&engineCluster)

	heatTemp, err := engineCluster.CalculateHeatIndex(nodeName)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("The temperature is", heatTemp, "Fahrenheit")
	}

	RouteAlert(node.Processor.Load)

}
