import sys

class Point3D:
    axes = {"x": (1, -1, -1),
            "y": (-1, 1, -1),
            "z": (-1, -1, 1)}
    
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

    def axial_symmetric(self, axis, inplace=False):
        if not isinstance(axis, str):
            raise Point3DError(f"invalid axis type: {type(axis)}")
        elif axis not in ["x", "y", "z"]:
            raise Point3DError(f"invalid axis name: {axis}")
        
        if not inplace:
            return Point3D(self.x * Point3D.axes[axis][0],
                           self.y * Point3D.axes[axis][1],
                           self.z * Point3D.axes[axis][2])
        
        self.x = self.x * Point3D.axes[axis][0]
        self.y = self.y * Point3D.axes[axis][1]
        self.z = self.z * Point3D.axes[axis][2]
        return self

class Point3DError(TypeError):
    def __init__(self, e):
        self.e = e

exec(sys.stdin.read())