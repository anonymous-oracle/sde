package dp10

// Glyph holds only intrinsic state (the rune); position is extrinsic.
type Glyph struct{ R rune }

// Factory hands out one shared Glyph per rune.
type Factory struct{ pool map[rune]*Glyph }

func (f *Factory) Get(r rune) *Glyph {
	if f.pool == nil {
		f.pool = map[rune]*Glyph{}
	}
	g, ok := f.pool[r]
	if !ok {
		g = &Glyph{R: r}
		f.pool[r] = g
	}
	return g
}

func (f *Factory) Distinct() int { return len(f.pool) }
