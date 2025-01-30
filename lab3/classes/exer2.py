class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

    def __str__(self):
        return f"Square {self.length} equal {self.area()}"
        
length = int(input())

square = Square(length)

print(square)