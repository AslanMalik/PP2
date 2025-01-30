class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle area with {self.length} and {self.width} equal {self.area()}"
    
length = int(input())
width = int(input())

rectangle_area = Rectangle(length, width)

print(rectangle_area)