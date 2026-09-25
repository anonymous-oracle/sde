package dp17

// Doc is the receiver the commands act on.
type Doc struct{ Text string }

// Command is a request as an object: it can be stored and undone.
type Command interface {
	Do(*Doc)
	Undo(*Doc)
}

type Append struct{ S string }

func (a Append) Do(d *Doc)   { d.Text += a.S }
func (a Append) Undo(d *Doc) { d.Text = d.Text[:len(d.Text)-len(a.S)] }

// Editor is the invoker; it keeps the history.
type Editor struct {
	Doc     Doc
	history []Command
}

func (e *Editor) Run(c Command) { c.Do(&e.Doc); e.history = append(e.history, c) }

func (e *Editor) Undo() {
	if n := len(e.history); n > 0 {
		e.history[n-1].Undo(&e.Doc)
		e.history = e.history[:n-1]
	}
}
