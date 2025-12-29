# application/uow.py
from abc import ABC, abstractmethod
from application.ports import OrderRepository

class AbstractUnitOfWork(ABC):
    orders: OrderRepository

    def __enter__(self) -> "AbstractUnitOfWork":
        # Start the transaction
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Stop the transaction.
        # If an exception occurred (exc_type is not None), we rollback.
        self.rollback()

    @abstractmethod
    def commit(self):
        """Commit all changes."""
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        """Rollback all changes."""
        raise NotImplementedError