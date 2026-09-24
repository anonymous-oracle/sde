package dp14

import "testing"

func TestObserver(t *testing.T) {
	var b Bus
	var a, c []string
	stopA := b.Subscribe(func(m string) { a = append(a, m) })
	b.Subscribe(func(m string) { c = append(c, m) })
	b.Publish("one")
	stopA()
	b.Publish("two")
	if len(a) != 1 || len(c) != 2 {
		t.Fatalf("a=%v c=%v", a, c)
	}
}
