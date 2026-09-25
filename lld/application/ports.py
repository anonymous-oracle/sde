# application/ports.py
from typing import Optional, Protocol

from domain.entities import Order
from typing import Optional, Protocol

from domain.entities import Order

class EmailSender(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> bool:
        """Sends an email and returns True if successful."""

class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        """Persist the order."""
        ...

    def get(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        ...

class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        """Persist the order."""
        ...

    def get(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        ...