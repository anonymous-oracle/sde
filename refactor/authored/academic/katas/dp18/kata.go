package dp18

// Handler handles a request or passes it on.
type Handler func(req string) string

// Link wraps next with one check; the chain is built by nesting.
type Link func(next Handler) Handler

func RejectAnonymous(next Handler) Handler {
	return func(req string) string {
		if req == "anon" {
			return "401"
		}
		return next(req)
	}
}

func RejectBlocked(next Handler) Handler {
	return func(req string) string {
		if req == "blocked" {
			return "403"
		}
		return next(req)
	}
}

// Chain applies links so that the first one runs first.
func Chain(final Handler, links ...Link) Handler {
	for i := len(links) - 1; i >= 0; i-- {
		final = links[i](final)
	}
	return final
}
