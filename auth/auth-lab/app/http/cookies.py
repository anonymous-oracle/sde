# app/cookies.py
from __future__ import annotations  # enable future annotations for clarity
from datetime import datetime, timezone  # for UTC timestamps
from http import cookies  # stdlib cookie utilities
from typing import Optional  # type hints for optional params

def format_http_date(dt: datetime) -> str:
    # convert a timezone-aware datetime to RFC 7231 IMF-fixdate string
    return dt.astimezone(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")


def set_session_cookie(
    name: str,  # cookie name; prefer "__Host-session" when on HTTPS with path="/"
    value: str,  # opaque session id value
    *,
    max_age: Optional[int] = None,  # optional Max-Age in seconds
    expires: Optional[datetime] = None,  # optional Expires absolute time
    samesite: str = "Lax",  # SameSite policy: "Lax" or "Strict" or "None"
    secure: bool = True,  # Secure flag; must be True in production
    httponly: bool = True,  # HttpOnly flag to block JS access
    path: str = "/",  # restrict cookie to a path; "/" is typical for session
    domain: Optional[str] = None,  # omit for __Host- cookies; otherwise set explicitly
) -> tuple[str, str]:
    # build a Set-Cookie header value using SimpleCookie for basic formatting
    c = cookies.SimpleCookie()  # container for cookies
    c[name] = value  # assign name=value pair
    morsel = c[name]  # obtain the underlying morsel object
    morsel["path"] = path  # set the Path attribute
    if domain:  # add Domain only if provided (not for __Host- prefix)
        morsel["domain"] = domain  # set Domain attribute to scope subdomains
    if secure:  # apply Secure attribute when requested
        morsel["secure"] = True  # mark cookie to be sent only over HTTPS
    if httponly:  # apply HttpOnly attribute
        morsel["httponly"] = True  # disallow document.cookie access in JS
    if samesite:  # set SameSite policy
        morsel["samesite"] = samesite  # assign policy value as provided
    if max_age is not None:  # optionally set Max-Age
        morsel["max-age"] = str(max_age)  # seconds until expiry
    if expires is not None:  # optionally set Expires
        morsel["expires"] = format_http_date(expires)  # HTTP-date string
    
    # return the header name and header value to add into the response
    return "Set-Cookie", morsel.OutputString()