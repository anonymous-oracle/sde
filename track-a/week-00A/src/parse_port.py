def parse_port(s: str) -> int:
    try:
        v = int(s)
    except ValueError:
        raise ValueError("Port must be an integer")

    else:
        if not (0 < v < 65536): raise ValueError("Port out of range")
        return v
    finally:
        pass

print(parse_port("8080"))