package dp22

import "testing"

func TestVisitor(t *testing.T) {
	e := Add{Num{1}, Add{Num{2}, Num{3}}}
	var ev Eval
	var pr Print
	e.Accept(&ev)
	e.Accept(&pr)
	if ev.Result != 6 || pr.Out != "(1 + (2 + 3))" {
		t.Fatalf("eval=%d print=%s", ev.Result, pr.Out)
	}
}
