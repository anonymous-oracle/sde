# domain/entities.py
from dataclasses import dataclass, field
from typing import List
import uuid
import logging


logging.getLogger().setLevel(logging.WARNING)

@dataclass
class LineItem:
    sku: str
    price: int  # Storing money as integers (cents) avoids floating point errors!
    quantity: int

@dataclass
class Order:
    # This is our "King". It holds data and rules.
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[LineItem] = field(default_factory=list)
    is_paid: bool = False
    
    def add_item(self, sku: str, price: int, quantity: int):
        # RULE: Logic lives here, not in the database, not in the view.

        # exercise - add invariant check
        if not self.is_paid:
            item = LineItem(sku=sku, price=price, quantity=quantity)
            self.items.append(item)
        else:
            raise ValueError("Paid orders cannot be modified")
    
    @property
    def total_amount(self) -> int:
        return sum(item.price * item.quantity for item in self.items)

    def accept_payment(self):
        self.is_paid = True
        return True

# --- Test Script (Simulating a Unit Test) ---
if __name__ == "__main__":
    # 1. Create the King
    order = Order()
    
    # 2. Add some items
    order.add_item("KEYBOARD-001", 5000, 1)  # $50.00
    order.add_item("MOUSE-002", 2500, 2)     # $25.00 x 2
    
    # 3. Ask the King a question
    print(f"Order ID: {order.id}")
    print(f"Is Paid?: {order.is_paid}")
    print(f"Total: ${order.total_amount / 100:.2f}")

    # 4. Exercise ops:
    order.accept_payment()
    try:
        order.add_item("MONITOR-003", 2500, 1)
    except Exception as e:
        logging.info(e)
