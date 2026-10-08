class Rectangle():

    def __init__(self, height: float = 0.0, width: float = 0.0):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

print(Rectangle(5, 4).area())
print(Rectangle(25, 20).area())