package dp03

import "testing"

func TestFamiliesNeverMix(t *testing.T) {
	for _, f := range []Factory{LocalFactory{}, CloudFactory{}} {
		if f.NewLogger().Family() != f.NewMetrics().Family() {
			t.Fatalf("%T produced a mixed family", f)
		}
	}
	if (LocalFactory{}).NewLogger().Family() == (CloudFactory{}).NewLogger().Family() {
		t.Fatal("the two families must differ")
	}
}
