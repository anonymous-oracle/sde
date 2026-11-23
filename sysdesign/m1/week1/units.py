BYTE_MAP = {
        "B": 1,
        "KB": 10**3,
        "MB": 10**6,
        "GB": 10**9,
        "TB": 10**12,
        "PB": 10**15
    }

SECOND_MAP = {
    "s": 1,
    "ns": 1 / (10**9),
    "us": 1 / (10**6),
    "ms": 1 / (10**3)
}

def to_bytes(value, unit):
    if str(unit).upper() not in BYTE_MAP:
        raise ValueError("Invalid Unit specification")
    return float(value) * BYTE_MAP[str(unit).upper()]

def human_bytes(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Invalid input")
    n = float(n)
    if n<=0:
        return "0.0 B"
    if n > 0 and n <= 1:
        return f"{n} B"
    byte_string = ""
    for unit in BYTE_MAP.keys():
        result = n / BYTE_MAP[unit]
        if result < 1:
            break
        byte_string = f"""{result:0.1f} {unit}"""
    return byte_string


def to_seconds(value, unit):
    if str(unit).lower() not in SECOND_MAP:
        raise ValueError("Invalid Unit specification")
    return float(value) * SECOND_MAP[str(unit).lower()]

def link_bytes_per_s(gbps):
    if not isinstance(gbps, (int, float)):
        raise ValueError("Invalid input")
    return to_bytes(gbps / 8, "GB")

if __name__ == "__main__":
    print(human_bytes(1234567))
    print(human_bytes(0))
    print(link_bytes_per_s(1))
    print(human_bytes(0.5))
    print(human_bytes(-5))