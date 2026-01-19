class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Shape:
    def __init__(self, points):
        self.points = points

    def display(self):
        for i in self.points:
            print(i.x, i.y)

    def move_shape(self, dx, dy):
        for i in self.points:
            i.move(dx, dy)

# Creating Point objects
p1 = Point(1, 2)
p2 = Point(4, 2)
p3 = Point(3, 5)

# Creating Shape object
s1 = Shape([p1, p2, p3])

print("Shape: Triangle")
print("Before moving:")
s1.display()

s1.move_shape(5, 5)

print("After moving:")
s1.display()

