package dp06

import "testing"

func TestAdapter(t *testing.T) {
	var c Celsius = Adapter{LegacyThermometer{F: 212}}
	if c.C() != 100 {
		t.Fatalf("C() = %v, want 100", c.C())
	}
}
