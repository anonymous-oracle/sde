class Bag:
    items = []

    def __init__(self):
        self.items = []


m = Bag()
n = Bag()

n.items.append(1)

print(m.items)