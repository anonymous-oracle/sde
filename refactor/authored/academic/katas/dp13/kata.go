package dp13

// Pricing is the strategy: a function value is the lightest Go form.
type Pricing func(cents int) int

func Full(c int) int   { return c }
func TenOff(c int) int { return c * 90 / 100 }

// Checkout holds a strategy and never branches on which one it is.
type Checkout struct{ Price Pricing }

func (c Checkout) Total(items []int) int {
	sum := 0
	for _, it := range items {
		sum += c.Price(it)
	}
	return sum
}
