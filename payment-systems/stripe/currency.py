# currency.py
ZERO_DECIMAL = {
    "bif","clp","djf","gnf","jpy","kmf","krw","mga","pyg","rwf","ugx","vnd","vuv","xaf","xof","xpf"
}

def to_minor_units(amount_major: float, currency: str) -> int:
    """Convert e.g. 12.99 USD -> 1299 (minor units).
       For zero-decimal, 12 -> 12."""
    c = currency.lower()
    return int(round(amount_major if c in ZERO_DECIMAL else amount_major * 100))

def is_valid_min(amount_minor: int, min_minor: int) -> bool:
    return amount_minor >= min_minor