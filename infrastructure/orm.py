# infrastructure/orm.py
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

class Base(DeclarativeBase):
    pass

class OrderModel(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    is_paid: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # One-to-Many relationship (One Order -> Many Items)
    items: Mapped[List["LineItemModel"]] = relationship(
        back_populates="order", 
        cascade="all, delete-orphan"  # If Order is deleted, delete items too
    )

class LineItemModel(Base):
    __tablename__ = "order_lines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"))
    sku: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)

    order: Mapped["OrderModel"] = relationship(back_populates="items")