package dp12

import "strings"

// Handler is the component; decorators take one and return one.
type Handler func(string) string

func Upper(next Handler) Handler {
	return func(s string) string { return strings.ToUpper(next(s)) }
}

func Exclaim(next Handler) Handler {
	return func(s string) string { return next(s) + "!" }
}
