package dp20

import "iter"

// Countdown yields n, n-1, ..., 1 and stops early when the consumer stops.
func Countdown(n int) iter.Seq[int] {
	return func(yield func(int) bool) {
		for i := n; i > 0; i-- {
			if !yield(i) {
				return
			}
		}
	}
}
