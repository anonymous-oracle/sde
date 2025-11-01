from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from crypto import hash_password, verify_password
from config import AUTHLAB_SECRET

# # Ensure project root is on sys.path when running this file directly.
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

@dataclass(frozen=True, slots=True)
class User:
    id: str
    email: str
    pw_record: str # serialized password hash record

class InMemoryUserStore:

    """
    Naive in-memory user store to build flows. Will be swapped with a repository backed by a DB later.
    """

    def __init__(self) -> None:
        self._by_email: Dict[str, User] = dict()

    def create(self, email: str, password: str) -> User:
        if email in self._by_email:
            raise ValueError("email already registered")
        rec = hash_password(password=password, pepper=AUTHLAB_SECRET)
        user = User(id=email, email=email, pw_record=rec)
        self._by_email[email] = user
        return user
    
    def get_by_email(self, email: str) -> Optional[User]:
        return self._by_email.get(email)
    
    def verify_login(self, email: str, password: str) -> Optional[User]:
        user: User = self._by_email.get(email)
        if not user:
            return None
        if verify_password(password=password, record=user.pw_record, pepper=AUTHLAB_SECRET):
            return user
        return None


if __name__ == "__main__":
    store = InMemoryUserStore()
    store.create("alice@example.com", "correct horse")
    user = store.verify_login("alice@example.com", "correct horse")
    print(f"User for correct password case: {user}")
    store.verify_login("alice@example.com", "wrong")
    print(f"User for wrong password case...no pun intended: {user}")