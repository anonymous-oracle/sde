package dp16

// State decides the next state for an event; unknown events keep the state.
type State interface {
	Name() string
	On(event string) State
}

type Pending struct{}
type Paid struct{}
type Shipped struct{}

func (Pending) Name() string { return "pending" }
func (Paid) Name() string    { return "paid" }
func (Shipped) Name() string { return "shipped" }

func (s Pending) On(e string) State {
	if e == "pay" {
		return Paid{}
	}
	return s
}

func (s Paid) On(e string) State {
	if e == "ship" {
		return Shipped{}
	}
	return s
}

func (s Shipped) On(string) State { return s }
