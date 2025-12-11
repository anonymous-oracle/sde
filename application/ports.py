# application/ports.py
from typing import Protocol

class EmailSender(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> bool:
        """Sends an email and returns True if successful."""