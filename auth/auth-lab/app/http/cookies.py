from wsgiref.simple_server import make_server # wsgi simple server for dev
from datetime import datetime, timedelta, timezone
import secrets

COOKIE_NAME = "__Host-authsid" # __Host- prefix enforces Secure + host-only in modern browsers
COOKIE_TTL = 1800 # cookie time-to-live in seconds (30 minutes

def fmt_http_date(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S GMT")

def app(environ, start_response):

    path = environ.get("PATH_INFO", "/") # request path
    headers = [] # we'll collect response headers here

    if path == "/login":
        # Simulate successful login -> mint a new random session id (opaque)
        sid = secrets.token_urlsafe(32) # ~256-bit randomness, URL-safe base64
        expires = datetime.now(timezone.utc) + timedelta(seconds=COOKIE_TTL) # absolute expiry time
        # Build Set-Cookie with strong flags:
        # - Secure: only sent over HTTPS
        # - HttpOnly: not readable by JS (mitigates XSS token theft)
        # - SameSite=Lax: 