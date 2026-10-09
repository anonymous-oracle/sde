class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, value):
        return self.cents == value.cents


money1 = Money(100)
money2 = Money(100)

print(money1 == money2)