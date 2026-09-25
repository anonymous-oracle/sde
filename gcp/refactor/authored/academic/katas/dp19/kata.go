package dp19

// Room is the mediator: users talk to it, never to each other.
type Room struct{ users map[string]*User }

type User struct {
	Name  string
	Inbox []string
	room  *Room
}

func (r *Room) Join(name string) *User {
	if r.users == nil {
		r.users = map[string]*User{}
	}
	u := &User{Name: name, room: r}
	r.users[name] = u
	return u
}

func (u *User) Say(msg string) { u.room.broadcast(u.Name, msg) }

func (r *Room) broadcast(from, msg string) {
	for name, u := range r.users {
		if name != from {
			u.Inbox = append(u.Inbox, from+": "+msg)
		}
	}
}
