# application/use_cases.py
from dataclasses import dataclass
from domain.entities import Order
from application.ports import OrderRepository

@dataclass
class CreateOrderDTO:
    """Data Transfer Object: Simple data container for input."""
    items: list[tuple[str, int, int]]  # list of (sku, price, qty)

class CreateOrderUseCase:
    def __init__(self, repo: OrderRepository):
        # We DEPEND on the Port, not the Adapter (SQLAlchemy).
        self.repo = repo

    def execute(self, data: CreateOrderDTO) -> str:
        # 1. Orchestrate the Entity
        order = Order()
        
        for sku, price, qty in data.items:
            # The Entity enforces the rules (e.g., can't add if paid)
            order.add_item(sku, price, qty)

        # 2. Persist using the Port
        self.repo.save(order)
        
        # 3. Return the result (ID)
        return order.id

class PayOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str):
        order: Order = self.repo.get(order_id)
        if order is None:
            raise ValueError("order not found")

        order.accept_payment()

        self.repo.save(order)

        return True
    

# application/use_cases.py
from dataclasses import dataclass
from domain.entities import Order
from application.ports import OrderRepository

@dataclass
class CreateOrderDTO:
    """Data Transfer Object: Simple data container for input."""
    items: list[tuple[str, int, int]]  # list of (sku, price, qty)

class CreateOrderUseCase:
    def __init__(self, repo: OrderRepository):
        # We DEPEND on the Port, not the Adapter (SQLAlchemy).
        self.repo = repo

    def execute(self, data: CreateOrderDTO) -> str:
        # 1. Orchestrate the Entity
        order = Order()
        
        for sku, price, qty in data.items:
            # The Entity enforces the rules (e.g., can't add if paid)
            order.add_item(sku, price, qty)

        # 2. Persist using the Port
        self.repo.save(order)
        
        # 3. Return the result (ID)
        return order.id

class PayOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str):
        order: Order = self.repo.get(order_id)
        if order is None:
            raise ValueError("order not found")

        order.accept_payment()

        self.repo.save(order)

        return True
    
