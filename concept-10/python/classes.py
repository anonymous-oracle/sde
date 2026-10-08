class Counter():

    def __init__(self):
        self.count = 0

    def bump(self):
        self.count += 1

a = Counter()
b = a
c = Counter()
a.bump()
a.bump()
c.bump()
print(b.count)
print(c.count)