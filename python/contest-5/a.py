import sys

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(number * self.x, number * self.y)

    def __rmul__(self, number):
        return self * number

    def __str__(self):
        return f"({self.x}, {self.y})"

exec(sys.stdin.read())