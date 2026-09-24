package dp17

import "testing"

func TestCommand(t *testing.T) {
	var e Editor
	e.Run(Append{"hello"})
	e.Run(Append{" world"})
	e.Undo()
	if e.Doc.Text != "hello" {
		t.Fatalf("text = %q", e.Doc.Text)
	}
	e.Undo()
	e.Undo()
	if e.Doc.Text != "" {
		t.Fatalf("text = %q", e.Doc.Text)
	}
}
