# run.py
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from http import cookies
from app.users import InMemoryUserStore
from app.session import SessionStore

user_store = InMemoryUserStore()
session_store = SessionStore()

# Pre-register a demo user 
user_store.create("alice@example.com", "wonderland")

def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ.get("REQUEST_METHOD", "GET")
    headers = []

    def respond(status: str, body: str, content_type="text/html"):
        headers.append(("Content-Type", content_type))
        start_response(status, headers)
        return [body.encode("utf-8")]
    
    # Parse cookies
    cookie_header = environ.get("HTTP_COOKIE", "")
    jar = cookies.SimpleCookie()
    jar.load(cookie_header)
    sid = jar.get("__Host-sessionid")
    session = session_store.get(sid.value) if sid else None

    # Routes
    if path == "/" and method == "GET":
        if session:
            return respond("200 OK", f"<h1>Welcome, {session.user_id}!</h1><a href='/logout'>Logout</a>")
        else:
            return respond("200 OK", "<h1>Login</h1><form method='POST' action='/login'>Email: <input name='email'><br>Password: <input name='password' type='password'><br><button>Login</button></form>")
        
    elif path == "/login" and method == "POST":
        try:
            size = int(environ.get("CONTENT_LENGTH", 0))
        except ValueError:
            size = 0
        
        body = environ["wsgi.input"].read(size).decode()
        data = parse_qs(body)
        email = data.get("email", [""])[0]
        password = data.get("password", [""])[0]

        user = user_store.verify_login(email, password)
        if not user:
            return respond("403 FORBIDDEN", "<h1>Invalid credentials</h1>")

        sid = session_store.create(user.id)
        c = cookies.SimpleCookie()
        c[""]
        

        



if __name__ == "__main__":
    print("Auth Lab — run hooks will live here soon.")