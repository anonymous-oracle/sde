package dp08

// Node is the component: a leaf and a composite answer the same call.
type Node interface{ Size() int }

type File struct{ N int }

func (f File) Size() int { return f.N }

type Dir struct{ Children []Node }

func (d Dir) Size() int {
	total := 0
	for _, c := range d.Children {
		total += c.Size()
	}
	return total
}
