package dp04

import (
	"testing"
	"time"
)

func TestBuilder(t *testing.T) {
	r, err := NewRequest("https://example.com").WithRetries(3).Build()
	if err != nil || r.Timeout != 30*time.Second || r.Retries != 3 {
		t.Fatalf("got %+v, %v", r, err)
	}
	if _, err := NewRequest("").Build(); err == nil {
		t.Fatal("empty URL must fail")
	}
	if _, err := NewRequest("x").WithRetries(-1).Build(); err == nil {
		t.Fatal("negative retries must fail")
	}
}
