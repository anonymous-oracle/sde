from typing import Optional
from infrastructure.orm import LineItemModel, OrderModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from domain.entities import Order, LineItem

# engine = create_engine("sqlite:///:memory:", echo=True)

class SqlAlchemyOrderRepository():

    def __init__(self, session: Session):
        # Initialising the engine
        self._session = session
    
    def save(self, order: Order) -> None:
        db_order = OrderModel(id=order.id, is_paid=order.is_paid)
        db_order.items = [LineItemModel(order_id=db_order.id, sku=item.sku, price=item.price, quantity=item.quantity) for item in order.items]
        
        # add to session
        self._session.merge(db_order)
    
    def get(self, order_id: str) -> Optional[Order]:
        db_order = self._session.get(OrderModel, order_id)
        if db_order is None:
            return None
        
        return Order(id=db_order.id, items=[LineItem(quantity=db_item.quantity, price=db_item.price, sku=db_item.sku) for db_item in db_order.items], is_paid=db_order.is_paid)
