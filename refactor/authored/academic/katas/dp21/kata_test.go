package dp21

import "testing"

func TestMemento(t *testing.T) {
	e := &Editor{Text: "v1"}
	snap := e.Save()
	e.Text = "v2"
	e.Restore(snap)
	if e.Text != "v1" {
		t.Fatalf("text = %q", e.Text)
	}
}
