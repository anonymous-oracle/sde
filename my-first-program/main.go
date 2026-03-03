package main

import "fmt"

func main() {
	productName := "Demon Monarch Dagger"
	stockCount := 2
	price := 500
	fmt.Println("Inventory report:", productName, "-", "Stock:", stockCount, "Price:", price)
	quantitySold := 1
	stockCount = stockCount - quantitySold

	revenue := (quantitySold * price)
	fmt.Println("Transaction complete. Revenue:", revenue, "Remaining Stock:", stockCount)

}