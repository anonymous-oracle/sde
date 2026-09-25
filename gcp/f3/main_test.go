package main

import "testing"

func TestClassify(t *testing.T) {
	tests := []struct {
		name    string
		input   string
		want    string
		wantErr bool
	}{
		{name: "gce vm", input: "gce_vm", want: "zonal"},
		{name: "zonal pd", input: "zonal_pd", want: "zonal"},
		{name: "cloud run", input: "cloud_run", want: "regional"},
		{name: "zone label", input: "us-central1-a", want: "zone"},
		{name: "region label", input: "us-central1", want: "region"},
		{name: "multi region", input: "US", want: "multi-region"},
		{name: "dual region", input: "nam4", want: "dual-region"},
		{name: "unknown", input: "made-up-scope", wantErr: true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := classify(tt.input)
			if tt.wantErr {
				if err == nil {
					t.Fatalf("classify(%q) returned nil error, want error", tt.input)
				}
				return
			}
			if err != nil {
				t.Fatalf("classify(%q) returned error: %v", tt.input, err)
			}
			if got != tt.want {
				t.Fatalf("classify(%q) = %q, want %q", tt.input, got, tt.want)
			}
		})
	}
}
