from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# --- 1. Setup The World ---
# We use SQLite in memory for speed. echo=True prints the raw SQL to console (great for learning!)
engine = create_engine("sqlite:///:memory:", echo=True)

class Base(DeclarativeBase):
    pass

# --- 2. Define the Model ---
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, default="")
    email: Mapped[str] = mapped_column(nullable=False, default="")

    def __repr__(self):
        return f"<User {self.username}>"

# --- 3. Create Tables ---
Base.metadata.create_all(engine)

# --- 4. The Session Loop ---
# We use a context manager ('with') to ensure the session closes automatically.
with Session(engine) as session:
    print("\n--- STAGE 1: Adding Data ---")
    alice = User(username="alice", email="alice@example.com")
    bob = User(username="bob", email="bob@example.com")
    
    session.add(alice)
    session.add(bob)
    
    # NOTE: Look at the logs. No INSERT happens yet! Alice is 'pending'.
    print("   (Data is in session, but not committed)")
    
    session.commit()
    print("   (Data committed!)")

    print("\n--- STAGE 2: Reading Data ---")
    # Modern Select Syntax
    stmt = select(User).where(User.username == "alice")
    
    # scalar_one_or_none() gives us the object or None
    retrieved_user = session.execute(stmt).scalar_one_or_none()
    
    print(f"   Found: {retrieved_user}")