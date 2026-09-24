package dp22

import "strconv"

// Expr is the element hierarchy; each node accepts a visitor.
type Expr interface{ Accept(Visitor) }

type Num struct{ V int }
type Add struct{ L, R Expr }

func (n Num) Accept(v Visitor) { v.VisitNum(n) }
func (a Add) Accept(v Visitor) { v.VisitAdd(a) }

// Visitor is one operation over the whole hierarchy (double dispatch).
type Visitor interface {
	VisitNum(Num)
	VisitAdd(Add)
}

type Eval struct{ Result int }

func (e *Eval) VisitNum(n Num) { e.Result = n.V }
func (e *Eval) VisitAdd(a Add) {
	var l, r Eval
	a.L.Accept(&l)
	a.R.Accept(&r)
	e.Result = l.Result + r.Result
}

type Print struct{ Out string }

func (p *Print) VisitNum(n Num) { p.Out = strconv.Itoa(n.V) }
func (p *Print) VisitAdd(a Add) {
	var l, r Print
	a.L.Accept(&l)
	a.R.Accept(&r)
	p.Out = "(" + l.Out + " + " + r.Out + ")"
}
