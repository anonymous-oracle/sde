package dp07

import "fmt"

// Renderer is the implementation side of the bridge.
type Renderer interface{ Circle(r float64) string }

type SVG struct{}

func (SVG) Circle(r float64) string { return fmt.Sprintf(`<circle r="%g"/>`, r) }

type Text struct{}

func (Text) Circle(r float64) string { return fmt.Sprintf("circle(r=%g)", r) }

// Circle is the abstraction side; it holds a Renderer instead of subclassing one.
type Circle struct {
	R   float64
	Ren Renderer
}

func (c Circle) Draw() string { return c.Ren.Circle(c.R) }
