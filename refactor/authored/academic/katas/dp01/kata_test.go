package dp01

import (
	"sync"
	"testing"
)

func TestConfigOnce(t *testing.T) {
	var wg sync.WaitGroup
	got := make([]*Settings, 50)
	for i := range got {
		wg.Add(1)
		go func() {
			defer wg.Done()
			got[i] = Config()
		}()
	}
	wg.Wait()
	for _, s := range got {
		if s != got[0] {
			t.Fatal("two different instances")
		}
	}
	if loads != 1 {
		t.Fatalf("loads = %d, want 1", loads)
	}
}
