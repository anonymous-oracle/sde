package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := a[1:3]
	b[0] = 99
	fmt.Println("a:", a)
	fmt.Println("b:", b)

	c := append(b, 100)
	fmt.Println("a:", a)
	fmt.Println("b:", b)
	fmt.Println("c:", c)

	var m map[string]int
	fmt.Println("read from nil map:", m["missing"])
	m["key"] = 1
	fmt.Println("m:", m)
}