from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

req = Request("https://httpbin.org/get", headers={"User-Agent": "week0a/1.0"})
try:
    with urlopen(req, timeout=3) as r:
        print(r.status, r.read(60).decode("utf-8","ignore"))
except HTTPError as e:
    print("HTTPError", e.code)
except URLError as e:
    print("URLError", e.reason)