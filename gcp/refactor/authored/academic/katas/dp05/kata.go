package dp05

import "slices"

// Template is the prototype that new values are copied from.
type Template struct {
	Name string
	Tags []string
}

// Clone is a deep copy: the clone's slice has its own backing array.
func (t Template) Clone() Template {
	return Template{Name: t.Name, Tags: slices.Clone(t.Tags)}
}
