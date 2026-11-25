from week1.units import to_seconds
import math

def validate_stage_ms(stage_ms):
    if not isinstance(stage_ms, list):
        raise ValueError("Invalid input")
    for ms in stage_ms:
        if not isinstance(ms, (int, float)):
            raise ValueError("Invalid input")
        if float(ms) < 0:
            raise ValueError("Invalid input")

def pipeline_latency_s(stage_ms):
    validate_stage_ms(stage_ms=stage_ms)
    return sum(stage_ms) / 1000

def pipeline_throughput_per_s(stage_ms):
    validate_stage_ms(stage_ms=stage_ms)
    max_latency = max(stage_ms)
    return (1 / max_latency) * 1000

def in_flight(rate_per_s, time_s):
    validate_stage_ms[rate_per_s, time_s]
    return rate_per_s * time_s

def servers_needed(rate_per_s, latency_s, per_server_limit):
    validate_stage_ms([rate_per_s, latency_s, per_server_limit])
    L = in_flight(rate_per_s=rate_per_s, latency_s=latency_s)
    return math.ceil(L / per_server_limit)


if __name__ == "__main__":
    def close(a, b):
        return abs(a - b) < 1e-9

    def raises(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return True
        return False

    checks = [
        ("latency 10+20+10 ms = 0.04 s", close(pipeline_latency_s([10, 20, 10]), 0.04)),
        ("throughput, bottleneck 20 ms = 50/s", close(pipeline_throughput_per_s([10, 20, 10]), 50.0)),
        ("in flight 50/s x 0.04 s = 2", close(in_flight(50, 0.04), 2.0)),
        ("in flight 500/s x 0.04 s = 20", close(in_flight(500, 0.04), 20.0)),
        ("servers: 2000/s, 80 ms, 50 each = 4", servers_needed(2000, 0.08, 50) == 4),
        ("servers: 2000/s, 160 ms, 50 each = 7", servers_needed(2000, 0.16, 50) == 7),
        ("servers: exact multiple (50.0 in flight) = 1", servers_needed(1000, 0.05, 50) == 1),
        ("servers: exact multiple (300 in flight) = 3", servers_needed(3000, 0.1, 100) == 3),
        ("servers returns an int", isinstance(servers_needed(2000, 0.08, 50), int)),
        ("tail k=3 = 0.029701", close(tail_fraction(0.01, 3), 0.029701)),
        ("tail k=5 = 0.04901", close(tail_fraction(0.01, 5), 0.0490099501)),
        ("tail k=1 equals p", close(tail_fraction(0.01, 1), 0.01)),
        ("tail p=0 is 0", close(tail_fraction(0, 10), 0.0)),
        ("ValueError: empty stage list", raises(pipeline_latency_s, [])),
        ("ValueError: empty stage list (throughput)", raises(pipeline_throughput_per_s, [])),
        ("ValueError: zero stage time", raises(pipeline_latency_s, [10, 0])),
        ("ValueError: negative rate", raises(in_flight, -1, 0.1)),
        ("ValueError: zero time", raises(in_flight, 10, 0)),
        ("ValueError: zero per-server limit", raises(servers_needed, 100, 0.1, 0)),
        ("ValueError: probability above 1", raises(tail_fraction, 1.5, 3)),
        ("ValueError: k below 1", raises(tail_fraction, 0.01, 0)),
    ]
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    print(sum(ok for _, ok in checks), "of", len(checks), "passed")