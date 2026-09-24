package dp02

import "fmt"

// Store is the product interface.
type Store interface {
	Put(k, v string)
	Get(k string) (string, bool)
}

type memStore struct{ m map[string]string }

func (s *memStore) Put(k, v string) { s.m[k] = v }

func (s *memStore) Get(k string) (string, bool) {
	v, ok := s.m[k]
	return v, ok
}

// NewStore is the factory: the caller names a kind, never a concrete type.
func NewStore(kind string) (Store, error) {
	switch kind {
	case "memory":
		return &memStore{m: map[string]string{}}, nil
	default:
		return nil, fmt.Errorf("unknown store kind %q", kind)
	}
}
