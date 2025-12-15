from typing import Protocol, Optional
from domain.entities import Order

# From Module 1
class EmailSender(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> bool:
        ...

# From Module 2
class OrderRepository(Protocol):
    def save(self, order: Order) -> None:
        """Persist the order."""
        ...

    def get(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        ...