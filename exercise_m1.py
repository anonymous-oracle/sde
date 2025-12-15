from typing import Protocol

# --- 1. The Port (The "Socket") ---
# The logic says: "I need something that has a 'send' method."
class EmailSender(Protocol):
    def send(self, recipient: str, body: str) -> bool:
        ...

# --- 2. The Logic (The "Electricity") ---
# This function ONLY knows about the Protocol. 
# It does not know about "FakeEmailSender".
def welcome_user(service: EmailSender, username: str):
    email_address = f"{username}@example.com"
    msg = f"Welcome, {username}!"
    
    # We use the service here. We trust it fits the shape.
    success = service.send(email_address, msg)
    
    if success:
        print(f"✅ Logic: Successfully welcomed {username}")
    else:
        print(f"❌ Logic: Failed to welcome {username}")

# --- 3. The Adapter (The "Toaster") ---
class FakeEmailSender:
    def send(self, recipient: str, body: str) -> bool:
        print(f"   [FakeEmailSender] >> Written to log: {recipient} - {body}")
        return True

# exercise
class SillyEmailSender:
    def send(self, recipient: str, body: str) -> bool:
        print(f"EVERYTHINGS'S IN CAPS - To {recipient} - {body}")
        return True

class BrokenSender:
    def deliver(self, recipient: str, body: str) -> bool:
        print(f"EVERYTHINGS'S IN CAPS - To {recipient} - {body}")
        return True

# --- Execution ---
if __name__ == "__main__":
    # We plug the toaster (FakeEmailSender) into the socket (service argument)
    # my_sender = FakeEmailSender()
    # my_sender = SillyEmailSender()
    my_sender = BrokenSender()
    welcome_user(my_sender, "Alice")