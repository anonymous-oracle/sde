package dp15

// Steps are the hooks; Run is the fixed skeleton.
type Steps interface {
	Fetch() ([]int, error)
	Transform(int) int
}

// Run fixes the order: fetch, transform each, sum. Callers vary only the steps.
func Run(s Steps) (int, error) {
	xs, err := s.Fetch()
	if err != nil {
		return 0, err
	}
	sum := 0
	for _, x := range xs {
		sum += s.Transform(x)
	}
	return sum, nil
}
