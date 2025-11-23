from wsgiref.simple_server import make_server
import http.cookies
import secrets
import time

from load_dotenv import load_dotenv

# ---------------------------------------------------------
# 1. IN-MEMORY SESSION STORE (Global State)
# ---------------------------------------------------------
# Mapping: session_id -> username
SESSIONS = {}

def application(environ, start_response):
    """
    Raw WSGI Application.
    environ: Contains HTTP request headers (like COOKIE).
    start_response: Function to send HTTP response headers.
    """
    
    # -----------------------------------------------------
    # 2. PARSE INCOMING COOKIES
    # -----------------------------------------------------
    # The browser sends: "Cookie: session_id=abc; theme=dark"
    cookie_header = environ.get('HTTP_COOKIE', '')
    
    # Python's stdlib cookie parser
    server_cookies = http.cookies.SimpleCookie(cookie_header)
    
    # Check if user sent a session_id
    session_id = None
    if 'session_id' in server_cookies:
        session_id = server_cookies['session_id'].value

    # -----------------------------------------------------
    # 3. AUTH LOGIC (Mock)
    # -----------------------------------------------------
    path = environ.get('PATH_INFO')
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    response_body = ""

    if path == '/login':
        # SIMULATE: User passed correct credentials.
        # Generate new session
        new_sess_id = secrets.token_urlsafe(16)
        SESSIONS[new_sess_id] = "user_alice"
        
        # CONSTRUCT SECURE COOKIE
        # We use SimpleCookie to format the string correctly
        c = http.cookies.SimpleCookie()
        c['session_id'] = new_sess_id
        
        # SECURITY FLAGS (The Core Lesson)
        c['session_id']['path'] = '/'
        c['session_id']['httponly'] = True  # No JS access
        c['session_id']['secure'] = False   # False only for localhost dev!
        c['session_id']['samesite'] = 'Lax' 
        c['session_id']['max-age'] = 360     # Expires in 360 seconds
        
        # Add Set-Cookie header
        # output string looks like: "Set-Cookie: session_id=...; HttpOnly; ..."
        headers.append(('Set-Cookie', c['session_id'].OutputString()))
        
        response_body = f"Logged in! Session created: {new_sess_id}"

    elif path in {"/profile", "/favicon.ico"}:
        # AUTHZ CHECK
        if session_id and session_id in SESSIONS:
            user = SESSIONS[session_id]
            response_body = f"Welcome back, {user}. This is private data."
        else:
            status = '401 Unauthorized'
            response_body = "Who are you? Go to /login"
            
    elif path == '/logout':
        # INVALIDATE SESSION
        if session_id in SESSIONS:
            del SESSIONS[session_id]
            
        # Tell browser to delete cookie (Max-Age=0)
        c = http.cookies.SimpleCookie()
        c['session_id'] = ''
        c['session_id']['path'] = '/'
        c['session_id']['max-age'] = 0
        
        headers.append(('Set-Cookie', c['session_id'].OutputString()))
        response_body = "Logged out."

    else:
        response_body = "Visit /login, /profile, or /logout"

    start_response(status, headers)
    return [response_body.encode('utf-8')]

if __name__ == '__main__':
    load_dotenv()
    print("Serving on http://localhost:8000...")
    # Single-threaded dev server
    with make_server('', 8000, application) as httpd:
        httpd.serve_forever()