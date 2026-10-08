class Tag:
    prefix = "x"

    def __init__(self):
        pass

m = Tag()
n = Tag()

Tag.prefix = "y"
n.prefix = "z" # creates attribute on the classes

print(m.prefix)
print(n.prefix)