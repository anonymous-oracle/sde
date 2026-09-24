package dp06

// LegacyThermometer is the adaptee: it reports Fahrenheit.
type LegacyThermometer struct{ F float64 }

func (l LegacyThermometer) ReadF() float64 { return l.F }

// Celsius is the interface the client expects.
type Celsius interface{ C() float64 }

// Adapter makes a LegacyThermometer satisfy Celsius.
type Adapter struct{ L LegacyThermometer }

func (a Adapter) C() float64 { return (a.L.ReadF() - 32) * 5 / 9 }
