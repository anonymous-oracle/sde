class HashMap:

    def __init__(self, m=8, resizing=False):
        self.m = m
        self.buckets = [[] for i in range(self.m)]
        self.resizing = resizing
        self.n = 0

    @property
    def resize(self):
        return self.n/self.m > 0.75

    @property
    def len(self):
        return self.n
    
    def put(self, key, value):
        bucket = hash(key) % self.m
        exists = False
        for k, v in self.buckets[bucket]:
            if k==key:
                idx = self.buckets[bucket].index((k, v))
                self.buckets[bucket][idx] = (key, value)
                exists = True
                break
        if not exists:
            self.buckets[bucket].append((key, value))
            self.n += 1
        if self.resize and self.resizing:
            new_m = self.m * 2
            new_buckets = [[] for i in range(new_m)]
            for bucket in self.buckets:
                for k, v in bucket:
                    new_bucket = hash(k) % new_m
                    new_buckets[new_bucket].append((k, v))
            self.buckets = new_buckets
            self.m = new_m

    def get(self, key):
        bucket = hash(key) % self.m
        for k, v in self.buckets[bucket]:
            if k==key:
                return v
        return None

    def delete(self, key):
        bucket = hash(key) % self.m 
        key_found = False
        value = None
        for k, v in self.buckets[bucket]:
            if k==key:
                key_found = True
                value = v
                break
        if key_found:
            idx=self.buckets[bucket].index((key, value))
            self.buckets[bucket].pop(idx)
            self.n -= 1

if __name__ == "__main__":
    from week1.bench import percentile
    import time
    hm = HashMap(resizing=True)
    for i in range(10000):
        hm.put(i, i)
    print(f"""Buckets: {hm.m}\t Number of entries: {hm.len}""")
    lookup_durations = []
    for i in range(10000):
        t0 = time.perf_counter_ns()
        hm.get(i)
        t1 = time.perf_counter_ns() - t0
        lookup_durations.append(t1 / 1000)
    lookup_durations = sorted(lookup_durations)
    for p in [50, 95, 99]:
        print(f"""Percentile for p: {percentile(lookup_durations, p)}""")

    hm = HashMap()
    for i in range(10000):
        hm.put(i, i)
    print(f"""Buckets: {hm.m}\t Number of entries: {hm.len}""")
    lookup_durations = []
    for i in range(10000):
        t0 = time.perf_counter_ns()
        hm.get(i)
        t1 = time.perf_counter_ns() - t0
        lookup_durations.append(t1 / 1000)
    lookup_durations = sorted(lookup_durations)
    for p in [50, 95, 99]:
        print(f"""Percentile for p: {percentile(lookup_durations, p)}""")