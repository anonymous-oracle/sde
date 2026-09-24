package dp19

import "testing"

func TestMediator(t *testing.T) {
	var r Room
	a, b, c := r.Join("a"), r.Join("b"), r.Join("c")
	a.Say("hi")
	if len(a.Inbox) != 0 || len(b.Inbox) != 1 || len(c.Inbox) != 1 || b.Inbox[0] != "a: hi" {
		t.Fatalf("a=%v b=%v c=%v", a.Inbox, b.Inbox, c.Inbox)
	}
}
