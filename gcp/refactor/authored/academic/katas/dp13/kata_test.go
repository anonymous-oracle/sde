package dp13

import "testing"

func TestStrategy(t *testing.T) {
	items := []int{1000, 500}
	if (Checkout{Full}).Total(items) != 1500 {
		t.Fatal("full price")
	}
	if (Checkout{TenOff}).Total(items) != 1350 {
		t.Fatal("ten percent off")
	}
}
