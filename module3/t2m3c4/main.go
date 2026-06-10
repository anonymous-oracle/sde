package main

import "fmt"

type ClusterState int

const (
	StateHalted = iota
	StateOperational
	StateOverloaded
)

type MetricEnvelope[T any] struct {
	SystemState ClusterState
	Payload     T
}

type SubsystemRegistry[K comparable, V any] struct {
	MetricEnvelopes map[K]MetricEnvelope[V]
}

func (sr *SubsystemRegistry[K, V]) RegisterAndAudit(key K, data V, state ClusterState) (V, bool) {
	var returnPayload V
	var boolVal bool
	if val, ok := sr.MetricEnvelopes[key]; ok {
		returnPayload = val.Payload
		boolVal = false
	} else if !ok {
		sr.MetricEnvelopes[key] = MetricEnvelope[V]{SystemState: state, Payload: data}
		returnPayload = data
		boolVal = true
	}
	if state == StateOverloaded {
		var zeroVal V
		returnPayload = zeroVal
		boolVal = false
	}
	return returnPayload, boolVal
}

func main() {
	var registry SubsystemRegistry[string, int] = SubsystemRegistry[string, int]{MetricEnvelopes: (make(map[string]MetricEnvelope[int]))}
	res, _ := registry.RegisterAndAudit("core-01", 4096, StateOperational)
	fmt.Println(res)
	res, _ = registry.RegisterAndAudit("core-01", 8192, StateOperational)
	fmt.Println(res)
	res, _ = registry.RegisterAndAudit("core-overflow", 9999, StateOverloaded)
	fmt.Println(res)
}
