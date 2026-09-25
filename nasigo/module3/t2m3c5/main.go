package main

var SystemEnvironmentSignature string

func init() {
	SystemEnvironmentSignature = "PRODUCTION-CORE-ACTIVE"
}

type NetworkMetaData struct {
	OriginNode string `json:"node_origin_id"`
	PayloadHash string `json:"crypto_hash_sig"`
}

type TelemetryEnvelope[T any] struct {
    Environment string
    DataContent T
}

func BuildNormalizer(tokens ...string) (TelemetryEnvelope[NetworkMetaData]) {


	
}