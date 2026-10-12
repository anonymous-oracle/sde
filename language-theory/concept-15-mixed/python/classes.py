class Cart:
    tags = []

    def __init__(self, owner):
        self.owner = owner

a = Cart("sam")
b = Cart("sam")

a.tags.append("x")
print(b.tags is a.tags)