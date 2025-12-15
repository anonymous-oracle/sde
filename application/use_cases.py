from dataclasses import dataclass
from domain.entities import Order
from application.ports import OrderRepository

@dataclass
class CreateOrderDTO:
    """Data Transfer Object: Simple data container for input."""
    items: list[tuple[str, int, int]]  # list of (sku, price, qty)

class CreateOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, data: CreateOrderDTO) -> str:
        # 1. Orchestrate the Entity
        order = Order()
        
        for sku, price, qty in data.items:
            order.add_item(sku, price, qty)

        # 2. Persist using the Port
        self.repo.save(order)
        
        # 3. Return the result (ID)
        return order.id

class PayOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str):
        # 1. Fetch
        order = self.repo.get(order_id)
        
        # Guard clause: Fail fast if data is missing
        if order is None:
            raise ValueError(f"Order {order_id} not found")

        # 2. Act (Domain Logic)
        order.accept_payment()

        # 3. Save
        self.repo.save(order)
        return True