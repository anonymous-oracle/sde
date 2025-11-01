import http.client

conn = http.client.HTTPSConnection("httpbin.org", timeout=3)
conn.request("GET", "/status/200")
res = conn.getresponse()
print(res.status, res.reason)