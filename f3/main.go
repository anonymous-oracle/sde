package main

import "fmt"

var scope_map map[string]string
// var scope_map map[string]string = map[string]string{
// 	"gce_vm": "zonal",
// 	"zonal_pd": "zonal",
// 	"cloud_run": "regional",
// 	"us-central1-a": "zone",
// 	"us-central1": "region",
// 	"US": "multi-region",
// 	"nam4": "dual-region",
// }

func classify(identifier string) (string, error) {
	val, ok := scope_map[identifier]
	if !ok {
		return "", fmt.Errorf("The %s is an unknown scope\n", identifier)
	}
	return val, nil
}

func main(){
	scope, _ := classify("us-central1-a")
	fmt.Printf("For us-central1-a, the classification is %v\n", scope)
}