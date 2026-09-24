package dp11

import "testing"

func TestProxy(t *testing.T) {
	b := &Backend{}
	var f Fetcher = &CachingProxy{Real: b}
	f.Fetch("k")
	if f.Fetch("k") != "value:k" || b.Calls != 1 {
		t.Fatalf("backend calls = %d, want 1", b.Calls)
	}
}
