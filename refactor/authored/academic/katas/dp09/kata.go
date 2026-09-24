package dp09

import "errors"

// Subsystems is what the facade hides; each step is recorded in Log.
type Subsystems struct {
	Log        []string
	CardDenied bool
}

func (s *Subsystems) reserve(item string) { s.Log = append(s.Log, "reserve "+item) }
func (s *Subsystems) release(item string) { s.Log = append(s.Log, "release "+item) }
func (s *Subsystems) ship(item string)    { s.Log = append(s.Log, "ship "+item) }

func (s *Subsystems) charge(cents int) error {
	s.Log = append(s.Log, "charge")
	if s.CardDenied {
		return errors.New("card denied")
	}
	return nil
}

// Buy is the facade: one call, the right order, and the undo on failure.
func (s *Subsystems) Buy(item string, cents int) error {
	s.reserve(item)
	if err := s.charge(cents); err != nil {
		s.release(item)
		return err
	}
	s.ship(item)
	return nil
}
