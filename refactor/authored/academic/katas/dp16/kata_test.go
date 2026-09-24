package dp16

import "testing"

func TestState(t *testing.T) {
	var s State = Pending{}
	for _, e := range []string{"ship", "pay", "pay", "ship", "pay"} {
		s = s.On(e)
	}
	if s.Name() != "shipped" {
		t.Fatalf("state = %s, want shipped", s.Name())
	}
	if (Pending{}).On("ship").Name() != "pending" {
		t.Fatal("cannot ship before paying")
	}
}
