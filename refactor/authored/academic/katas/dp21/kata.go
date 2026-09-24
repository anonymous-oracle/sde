package dp21

// Memento is opaque outside the package: its field is unexported.
type Memento struct{ text string }

// Editor is the originator.
type Editor struct{ Text string }

func (e *Editor) Save() Memento     { return Memento{text: e.Text} }
func (e *Editor) Restore(m Memento) { e.Text = m.text }
