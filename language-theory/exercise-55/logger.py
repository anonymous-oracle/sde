total_calls = 0

def make_logger(prefix):
    counter = 0
    def log(message, *tags, level="INFO", **details):
        global total_calls
        nonlocal counter, prefix
        counter += 1
        total_calls += 1
        print(f"Count: {counter}\tPrefix: {prefix}\tLevel: {level}\tMessage: {message}\tTags: {len(tags)} tags - {list(tags)}\tDetails: {', '.join([f'{key}:{val}' for key, val in details.items()])}")

    return log

if __name__ == "__main__":
    app = make_logger("app")
    db = make_logger("db")

    app("started")
    app("user joined", "web", "new", level="DEBUG")
    db("query ran", rows=3, ms=12)
    app("stopped", level="WARN", reason="timeout")
    db("closed")
    print(total_calls)