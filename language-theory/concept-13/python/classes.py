class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, value):
        return self.cents == value.cents

    def __str__(self):
        return f"{self.cents // 100} dollars {self.cents % 100} cents"

print(Money(1234))