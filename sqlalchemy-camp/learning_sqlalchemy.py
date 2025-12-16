# learning_sqlalchemy.py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- 1. Define the Model Registry ---
class Base(DeclarativeBase):
    pass

# --- 2. Define a Table (Model) ---
class User(Base):
    __tablename__ = "users"
    
    # New 2.0 syntax: Type hints are enforced!
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, default="")
    email: Mapped[str] = mapped_column(nullable=False, default="")
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"

# --- 3. Setup the Engine ---
# "echo=True" prints the raw SQL to the terminal (Great for learning!)
engine = create_engine("sqlite:///:memory:", echo=True)

# Create all tables defined in Base (runs CREATE TABLE...)
Base.metadata.create_all(engine)

# --- 4. The Session (Unit of Work) ---
# We use a context manager ('with') to auto-close the session
with Session(engine) as session:
    print("\n--- INSERTING ---")
    alice = User(name="Alice", email="alice@example.com")
    bob = User(name="Bob", email="bob@example.com")
    
    # Add to the "Holding Zone"
    session.add(alice)
    session.add(bob)
    
    # Commit: "Make it so" (This executes the INSERT SQL)
    session.commit()

    print("\n--- SELECTING ---")
    # New 2.0 Syntax: select(Model).where(...)
    stmt = select(User).where(User.name == "Alice")
    
    # execute(stmt).scalar_one() gets a single object
    fetched_user = session.execute(stmt).scalar_one()
    print(f"Found: {fetched_user}")

    print("\n--- UPDATING ---")
    # We modify the Python object directly
    fetched_user.email = "super_alice@example.com"
    
    # The session is watching! It knows the object is 'dirty'.
    # Commit will auto-generate the UPDATE statement.
    session.commit()
    
    print("\n--- YOUR TURN: DELETE ---")
    # TODO: 
    # 1. Select "Alice" again.
    # 2. Call session.delete(alice_obj)
    # 3. Commit.
    # 4. Try to select her again to prove she is gone.

    stmt = select(User).where(User.name == "Alice")

    fetched_user = session.execute(stmt).scalar_one_or_none()
    if fetched_user is not None:
        print(f"Found: {fetched_user}")
    else:
        print("User not found")

    session.delete(fetched_user)
    print(f"Deleted: {fetched_user}")

    session.commit()
    
    stmt = select(User).where(User.name == "Alice")

    fetched_user = session.execute(stmt).scalar_one_or_none()
    if fetched_user is not None:
        print(f"Found: {fetched_user}")
    else:
        print("User not found") 