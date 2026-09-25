package dp10

import "testing"

func TestFlyweight(t *testing.T) {
	var f Factory
	var gs []*Glyph
	for _, r := range "banana" {
		gs = append(gs, f.Get(r))
	}
	if f.Distinct() != 3 {
		t.Fatalf("Distinct = %d, want 3", f.Distinct())
	}
	if gs[1] != gs[3] {
		t.Fatal("the two 'a' glyphs must be one shared value")
	}
}
