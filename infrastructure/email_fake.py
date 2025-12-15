# infrastructure/email_fake.py
# Note: We do NOT import the protocol here explicitly if using structural typing (Protocol),
# but adhering to it allows polymorphism.

class FakeEmailSender:
    def __init__(self):
        self.outbox = []

    def send(self, recipient: str, subject: str, body: str) -> bool:
        print(f"STUB: Sending email to {recipient}")
        self.outbox.append((recipient, subject, body))
        return True