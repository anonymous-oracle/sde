package dp04

import (
	"errors"
	"time"
)

// Request is built step by step; Build validates the whole.
type Request struct {
	URL     string
	Timeout time.Duration
	Retries int
}

// Builder holds the request under construction.
type Builder struct{ r Request }

// NewRequest starts a builder with the defaults.
func NewRequest(url string) *Builder {
	return &Builder{r: Request{URL: url, Timeout: 30 * time.Second}}
}

func (b *Builder) WithTimeout(d time.Duration) *Builder { b.r.Timeout = d; return b }
func (b *Builder) WithRetries(n int) *Builder           { b.r.Retries = n; return b }

// Build returns the request or the first rule it breaks.
func (b *Builder) Build() (Request, error) {
	switch {
	case b.r.URL == "":
		return Request{}, errors.New("url is required")
	case b.r.Retries < 0:
		return Request{}, errors.New("retries must be >= 0")
	}
	return b.r, nil
}
