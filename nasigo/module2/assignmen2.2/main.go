package main

import "fmt"

func main() {
	result, err := CheckVersion(2, 3)
	if err != nil {
		fmt.Printf("Looks like it's an invalid version - %v\n", result)
	}

}

// Verb,Usage,Language Nuance
// %v,Default Value,"The ""universal"" verb. In Python/Java, you often need .toString(). In Go, %v figures it out."
// %T,Type,"Shows the variable's type (e.g., int). Critical for debugging types in a statically typed language."
// %t,Boolean,Specifically for true/false.
// %d,Decimal,Standard integer formatting (same as C/Java).
// %s,String,Standard string formatting.

func CheckVersion(version, minimum int) (bool, error) {
	if version < 0 {
		return false, fmt.Errorf("invalid version")
	}
	return version >= minimum, nil
}
