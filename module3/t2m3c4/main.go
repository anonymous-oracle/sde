package main

type ClusterState int 
const (
	StateHalted = iota
	StateOperational
	StateOverloaded
)

type MetricEnvelope[T any] struct {
	SystemState ClusterState
	Payload T
}

type SubsystemRegistry[K comparable, V any] struct {
	MetricEnvelopes map[K]MetricEnvelope[V]
}

func (sr *SubsystemRegistry[K, V]) RegisterAndAudit(key K, data V, state ClusterState) (V, bool) {
	if val, ok := sr.MetricEnvelopes[key]; ok {
		return val.Payload, false
	} else if !ok {
		sr.MetricEnvelopes[key] = MetricEnvelope[V]{SystemState: state, Payload: data}

	}
}