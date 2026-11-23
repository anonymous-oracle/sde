from week1.bench import percentile

def summarize(durations):
    durations.sort()
    return {p: percentile(durations, p) for p in (50, 95, 99)}

if __name__ == "__main__":
    data = [5, 3, 9, 1, 7, 2, 8, 4, 6, 10]
    print(summarize(data))