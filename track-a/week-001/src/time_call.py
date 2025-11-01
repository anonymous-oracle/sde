import functools, time, logging

logging.basicConfig(level=logging.INFO)

def time_call(fn):
    @functools.wraps(fn)
    def time_wrapper(*a, **kw):
        _a = time.time_ns()
        val = fn(*a, **kw)
        logging.info(f"{fn.__name__} took {time.time_ns() - _a} nanoseconds to execute")
        return val
    return time_wrapper

@time_call
def pow(x, y): return x ** y

print(pow(131, 7))