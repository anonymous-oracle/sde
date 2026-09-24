package dp23

import (
	"fmt"
	"strings"
)

// Grammar:  expr := term { "AND" term } ;  term := "NOT" term | name
// Eval parses and evaluates in one recursive-descent pass.
func Eval(src string, env map[string]bool) (bool, error) {
	toks := strings.Fields(src)
	pos := 0
	var term func() (bool, error)
	term = func() (bool, error) {
		if pos >= len(toks) {
			return false, fmt.Errorf("unexpected end")
		}
		t := toks[pos]
		pos++
		if t == "NOT" {
			v, err := term()
			return !v, err
		}
		v, ok := env[t]
		if !ok {
			return false, fmt.Errorf("unknown name %q", t)
		}
		return v, nil
	}
	v, err := term()
	for err == nil && pos < len(toks) {
		if toks[pos] != "AND" {
			return false, fmt.Errorf("want AND, got %q", toks[pos])
		}
		pos++
		var r bool
		r, err = term()
		v = v && r
	}
	return v, err
}
