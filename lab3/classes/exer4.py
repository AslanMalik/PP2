class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def distance(self, x2, y2):
        return ((y2-self.y)**2 + (x2-self.x)**2)**0.5
    
p = Point()

p.move(2, 3)
p.show()
print(p.distance(5, 7))