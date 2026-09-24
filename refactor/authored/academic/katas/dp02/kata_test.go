package dp02

import "testing"

func TestNewStore(t *testing.T) {
	s, err := NewStore("memory")
	if err != nil {
		t.Fatal(err)
	}
	s.Put("a", "1")
	if v, ok := s.Get("a"); !ok || v != "1" {
		t.Fatalf("Get(a) = %q, %v", v, ok)
	}
	if _, err := NewStore("tape"); err == nil {
		t.Fatal("unknown kind must be an error")
	}
}
