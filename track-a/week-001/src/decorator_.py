import functools, logging

logging.basicConfig(level=logging.INFO)
def log_call(fn):
    @functools.wraps(fn)
    def wrapper(*a, **kw):
        logging.info(f"Calling {fn.__name__} with {a}")
        return fn(*a, **kw)
    return wrapper

@log_call
def add(x, y): return x + y

print(add(2, 3))