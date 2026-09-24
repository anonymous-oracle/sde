package dp15

import (
	"errors"
	"testing"
)

type squares struct{}

func (squares) Fetch() ([]int, error) { return []int{1, 2, 3}, nil }
func (squares) Transform(x int) int   { return x * x }

type broken struct{ squares }

func (broken) Fetch() ([]int, error) { return nil, errors.New("down") }

func TestTemplate(t *testing.T) {
	if got, err := Run(squares{}); err != nil || got != 14 {
		t.Fatalf("got %d, %v", got, err)
	}
	if _, err := Run(broken{}); err == nil {
		t.Fatal("fetch error must stop the skeleton")
	}
}
