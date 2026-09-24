package dp09

import (
	"slices"
	"testing"
)

func TestFacade(t *testing.T) {
	ok := &Subsystems{}
	if err := ok.Buy("book", 1200); err != nil {
		t.Fatal(err)
	}
	if !slices.Equal(ok.Log, []string{"reserve book", "charge", "ship book"}) {
		t.Fatal(ok.Log)
	}
	bad := &Subsystems{CardDenied: true}
	if err := bad.Buy("book", 1200); err == nil {
		t.Fatal("want an error")
	}
	if !slices.Equal(bad.Log, []string{"reserve book", "charge", "release book"}) {
		t.Fatal(bad.Log)
	}
}
