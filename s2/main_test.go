package main

import "testing"

func TestAdd(t *testing.T) {
	cases := []struct {
		name     string
		a, b     int
		expected int
	}{
		{"positive", 2, 3, 5},
		{"negative", -1, -1, -2},
		{"zero", 0, 0, 0},
		{"neg-cancel", -5, 5, 0},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := Add(c.a, c.b)
			if got != c.expected {
				t.Errorf("Add(%d,%d) = %d, want %d", c.a, c.b, got, c.expected)
			}
		})
	}
}
