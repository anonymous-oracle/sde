# main.py
import sys
import os

# Boilerplate to ensure Python finds your modules
sys.path.append(os.getcwd())

from domain.entities import Order
from application.use_cases import CreateOrderUseCase, CreateOrderDTO, PayOrderUseCase
# Import the adapter we just wrote
from infrastructure.repo_inmem import InMemoryOrderRepository

if __name__ == "__main__":
    print("🚀 System Starting...")

    # --- A. Setup Infrastructure (The "Toaster") ---
    repo = InMemoryOrderRepository()

    # --- B. Setup Application (The "Socket") ---
    # We inject the concrete 'repo' into the Use Cases.
    create_uc = CreateOrderUseCase(repo)
    pay_uc = PayOrderUseCase(repo)

    # --- C. Execute Flow (The "User") ---
    
    # 1. User creates an order
    print("\n1️⃣  Creating Order...")
    dto = CreateOrderDTO(items=[
        ("LAPTOP", 100000, 1), # $1000.00
        ("MOUSE", 5000, 2)     # $50.00 x 2
    ])
    
    try:
        new_order_id = create_uc.execute(dto)
        print(f"✅ Created Order ID: {new_order_id}")
    except Exception as e:
        print(f"❌ Creation Failed: {e}")
        exit(1)

    # 2. User pays for the order
    print("\n2️⃣  Paying for Order...")
    try:
        # EXECUTE THE PAY USE CASE
        pay_uc.execute(new_order_id)
        print(f"✅ Payment Processed for: {new_order_id}")
    except ValueError as e:
        print(f"❌ Payment Failed: {e}")

    # 3. Verification: Peek into the DB
    saved_order = repo.get(new_order_id)
    print(f"\n🔎 Verification: Order Paid Status = {saved_order.is_paid}")