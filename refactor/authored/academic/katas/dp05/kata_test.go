package dp05

import "testing"

func TestCloneIsDeep(t *testing.T) {
	orig := Template{Name: "base", Tags: []string{"a", "b"}}
	c := orig.Clone()
	c.Tags[0] = "changed"
	if orig.Tags[0] != "a" {
		t.Fatal("clone shares its slice with the original")
	}
}
