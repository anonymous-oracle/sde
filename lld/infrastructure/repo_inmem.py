# infrastructure/repo_inmem.py
from typing import Optional
from domain.entities import Order

class InMemoryOrderRepository:
    def __init__(self):
        # The "Database" is just a dictionary
        self._storage = {}

    def save(self, order: Order) -> None:
        # We store by ID so we can look it up later
        self._storage[order.id] = order
        print(f"   [DB] Saved Order {order.id} with Paid={order.is_paid}")

    def get(self, order_id: str) -> Optional[Order]:
        # Return the object if found, else None
        return self._storage.get(order_id)