package dp11

// Fetcher is the subject interface.
type Fetcher interface{ Fetch(key string) string }

// Backend is the real subject; it counts its calls.
type Backend struct{ Calls int }

func (b *Backend) Fetch(key string) string { b.Calls++; return "value:" + key }

// CachingProxy has the same interface and controls access to the backend.
type CachingProxy struct {
	Real  Fetcher
	cache map[string]string
}

func (p *CachingProxy) Fetch(key string) string {
	if v, ok := p.cache[key]; ok {
		return v
	}
	if p.cache == nil {
		p.cache = map[string]string{}
	}
	v := p.Real.Fetch(key)
	p.cache[key] = v
	return v
}
