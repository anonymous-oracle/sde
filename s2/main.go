package main

import (
	"errors"
	"fmt"
	"os"
	"pkg/greet"
)

func returnErr() error {
	// err := fmt.Errorf("context: %w", os.ErrNotExist)
	err := fmt.Errorf("context: %v", os.ErrNotExist)
	return err
}

func Add(i1, i2 int) int {
	return i1 + i2
}

func main() {
	fmt.Println(greet.Hello())

	// S2: scalar types & conversions
	var a int32 = 5
	var b int64 = 10
	// c := a+b // will fail
	c := int64(a) + b // explicit conversion works
	fmt.Println(c)
	// fmt.Println(string(65)) // comment out when testing

	// S2: control flow
	i := 0
	for {
		if i == 3 {
			break
		}
		fmt.Println(i)
		i++
	}

	switch i := 2; i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	default:
		fmt.Println("other")
	}

	// S2: arrays/slices/maps
	aNew := make([]int, 3, 5)
	aNew[0], aNew[1], aNew[2] = 1, 2, 3
	bNew := aNew[0:2]
	bNew = append(bNew, 99)
	fmt.Println(aNew)
	fmt.Println(bNew)

	m := map[string]int{}
	v, ok := m["x"]
	fmt.Println(v, ok)

	// S2: strings/bytes/runes
	s := "h\u00e9llo"
	fmt.Println(len(s))
	for i, r := range s {
		fmt.Println(i, string(r))
	}

	// S2: structs & zero values
	type Info struct {
		Tags []string
		Meta map[string]int
	}
	var iNew Info
	iNew.Tags = append(iNew.Tags, "x")
	// iNew.Meta["k"] = 1 // panics
	iNew.Meta = make(map[string]int)
	iNew.Meta["k"] = 1 // works now

	// S2: errors & wrapping
	err := returnErr()
	fmt.Println(errors.Is(err, os.ErrNotExist))
}
