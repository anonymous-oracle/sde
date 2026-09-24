package dp20

import (
	"slices"
	"testing"
)

func TestIterator(t *testing.T) {
	if got := slices.Collect(Countdown(3)); !slices.Equal(got, []int{3, 2, 1}) {
		t.Fatal(got)
	}
	seen := 0
	for v := range Countdown(10) {
		seen++
		if v == 8 {
			break
		}
	}
	if seen != 3 {
		t.Fatalf("seen = %d, want 3", seen)
	}
}
