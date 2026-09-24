package dp03

// Logger and Metrics are the two products of one family.
type Logger interface{ Family() string }
type Metrics interface{ Family() string }

// Factory creates a matched family.
type Factory interface {
	NewLogger() Logger
	NewMetrics() Metrics
}

type fam string

func (f fam) Family() string { return string(f) }

// LocalFactory builds the local family.
type LocalFactory struct{}

func (LocalFactory) NewLogger() Logger   { return fam("local") }
func (LocalFactory) NewMetrics() Metrics { return fam("local") }

// CloudFactory builds the cloud family.
type CloudFactory struct{}

func (CloudFactory) NewLogger() Logger   { return fam("cloud") }
func (CloudFactory) NewMetrics() Metrics { return fam("cloud") }
