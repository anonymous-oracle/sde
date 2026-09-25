package dp08

import "testing"

func TestComposite(t *testing.T) {
	root := Dir{[]Node{File{10}, Dir{[]Node{File{5}, File{7}}}, Dir{}}}
	if root.Size() != 22 {
		t.Fatalf("Size = %d, want 22", root.Size())
	}
}
