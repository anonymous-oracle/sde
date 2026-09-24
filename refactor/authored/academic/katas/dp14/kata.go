package dp14

// Bus is the subject; observers are functions.
type Bus struct {
	next int
	subs map[int]func(string)
}

// Subscribe registers f and returns the function that removes it.
func (b *Bus) Subscribe(f func(string)) (unsubscribe func()) {
	if b.subs == nil {
		b.subs = map[int]func(string){}
	}
	id := b.next
	b.next++
	b.subs[id] = f
	return func() { delete(b.subs, id) }
}

func (b *Bus) Publish(msg string) {
	for _, f := range b.subs {
		f(msg)
	}
}
