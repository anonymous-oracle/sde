from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    name: Optional[str] = None

print(User(id=1, email="a@example.com"))

