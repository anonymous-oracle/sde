# run.py
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from http import cookies
from app.users import InMemoryUserStore
from app.session import SessionStore

user_store = InMemoryUserStore()
session_store = SessionStore()

# Pre-register a demo user 

if __name__ == "__main__":
    print("Auth Lab — run hooks will live here soon.")