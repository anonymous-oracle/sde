from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class LineItem:
    sku: str
    price: int  # Storing money as integers (cents)
    quantity: int

@dataclass
class Order:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[LineItem] = field(default_factory=list)
    is_paid: bool = False
    
    def add_item(self, sku: str, price: int, quantity: int):
        # RULE: Invariant check - Cannot modify a paid order
        if self.is_paid:
            raise ValueError("Paid orders cannot be modified")
            
        item = LineItem(sku=sku, price=price, quantity=quantity)
        self.items.append(item)
    
    @property
    def total_amount(self) -> int:
        return sum(item.price * item.quantity for item in self.items)

    def accept_payment(self):
        # State transition
        self.is_paid = True