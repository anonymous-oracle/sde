package dp01

import "sync"

// Settings is the one shared configuration value.
type Settings struct{ Region string }

var loads int

// Config returns the same *Settings on every call; the loader runs once.
var Config = sync.OnceValue(func() *Settings {
	loads++
	return &Settings{Region: "europe-west2"}
})
