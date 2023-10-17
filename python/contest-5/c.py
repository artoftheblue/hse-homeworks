import sys

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    @staticmethod
    def dist(one, two):
        return (abs(one.x - two.x) ** 2 + abs(one.y - two.y) ** 2 + abs(one.z - two.z) ** 2) ** 0.5

exec(sys.stdin.read())