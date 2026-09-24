package dp12

import "testing"

func TestDecorators(t *testing.T) {
	base := Handler(func(s string) string { return "hi " + s })
	if got := Exclaim(Upper(base))("ann"); got != "HI ANN!" {
		t.Fatal(got)
	}
	if got := Upper(Exclaim(base))("ann"); got != "HI ANN!" {
		t.Fatal(got)
	}
	if got := Exclaim(Exclaim(base))("ann"); got != "hi ann!!" {
		t.Fatal(got)
	}
}
