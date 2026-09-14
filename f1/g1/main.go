package main

import "fmt"

func main() {
	var a int8 = 127
	a = a + 1
	fmt.Println(a)

	var b uint8 = 0
	b = b - 1
	fmt.Println(b)

	var f float32 = 0.1
	var sum float32 = 0
	for i := 0; i < 10; i++ {
		sum += f
	}
	fmt.Println(sum)
	fmt.Println(sum == 1.0)
}