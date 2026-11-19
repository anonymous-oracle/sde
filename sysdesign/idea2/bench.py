import time
from math import ceil

to_seconds = 1000

def measure(fn, n):
    if n==0:
        return []
    durations = []
    for i in range(n):
        t0 = time.perf_counter_ns()
        fn()
        durations.append((time.perf_counter_ns() - t0) * to_seconds)
    return durations

def percentile(sorted_values, p):
    n = len(sorted_values)
    r = max(1, ceil((p*n)/100))
    return sorted_values[r - 1]
    
if __name__ == "__main__":
    for p in [50, 95, 99]:
        print(percentile(list(range(1, 101)), p))
    for _ in range(5):
        durations = measure(lambda: sum(range(100000)), 1000)
        max_call = durations.index(max(durations)) + 1
        durations = sorted(durations)
        if len(durations) > 0:
            mini, maxi = durations[0], durations[-1]
            median = durations[len(durations) // 2]
            # print(mini, maxi, median)
            # print(f"""Minimum: {mini}\t Maximum: {maxi}\t Median: {median}\t Maximum call: {max_call}\t Calls > 3*Median: {[True if n > 3 * median else False for n in durations].count(True)}""")
            # time.sleep(1)
            for p in [50, 95, 99]:
                print(percentile(durations, p))
    