package dp18

import "testing"

func TestChain(t *testing.T) {
	h := Chain(func(string) string { return "200" }, RejectAnonymous, RejectBlocked)
	for req, want := range map[string]string{"anon": "401", "blocked": "403", "ann": "200"} {
		if got := h(req); got != want {
			t.Fatalf("%s: got %s, want %s", req, got, want)
		}
	}
}
