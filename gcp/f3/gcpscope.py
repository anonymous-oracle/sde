IDENTIFIER_SCOPES = {
    "gce_vm": "zonal",
    "zonal_pd": "zonal",
    "cloud_run": "regional",
    "us-central1-a": "zone",
    "us-central1": "region",
    "US": "multi-region",
    "nam4": "dual-region",
}


def classify(identifier: str) -> str:
    try:
        return IDENTIFIER_SCOPES[identifier]
    except KeyError:
        raise ValueError(f"Unknown identifier: {identifier}") from None