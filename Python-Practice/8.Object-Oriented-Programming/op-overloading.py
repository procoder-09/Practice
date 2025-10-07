class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# p1 = Point(4, 8)
# p2 = Point(4, 5)
# print(p1 - p2)  # (6, 8)

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lets_fly(flyer):
    flyer.fly()

lets_fly(Bird())      # Bird is flying
lets_fly(Airplane())  # Airplane is flying