package dp23

import "testing"

func TestInterpreter(t *testing.T) {
	env := map[string]bool{"adult": true, "banned": false}
	if v, err := Eval("adult AND NOT banned", env); err != nil || !v {
		t.Fatalf("got %v, %v", v, err)
	}
	if v, _ := Eval("NOT adult", env); v {
		t.Fatal("NOT adult should be false")
	}
	if _, err := Eval("adult OR banned", env); err == nil {
		t.Fatal("OR is not in the grammar")
	}
}
