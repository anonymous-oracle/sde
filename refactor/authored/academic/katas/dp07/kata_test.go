package dp07

import "testing"

func TestBridge(t *testing.T) {
	if got := (Circle{2, SVG{}}).Draw(); got != `<circle r="2"/>` {
		t.Fatal(got)
	}
	if got := (Circle{2, Text{}}).Draw(); got != "circle(r=2)" {
		t.Fatal(got)
	}
}
