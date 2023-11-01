#manim -pqm "vector space test.py" transformation

from manim import *
from math import sin, cos

class Base(LinearTransformationScene):
    def construct(self):
        self.apply_nonlinear_transformation(self.func)
        self.wait(1)

class FiveA(Base):
    def func(self, dot):
        x, y, z = dot
        return np.array((x + y, x ** 2 + y, z))

class FiveB(Base):
    def func(self, dot):
        x, y, z = dot
        return np.array((x * sin(y), x * cos(y), z))

class Two(Base):
    def func(self, dot):
        x, y, z = dot
        if x < 0:
            x = -1
        return np.array((x, 0, z))

class Three(Base):
    def func(self, dot):
        x, y, z = dot
        return np.array((x ** 2, 0, z))

class FourA(Base):
    def func(self, dot):
        x, y, z = dot
        return np.array((x - 2 * y, 0, z))

class FourB(Base):
    def func(self, dot):
        x, y, z = dot
        res = (x / y) if y != 0 else 10
        return np.array((res, 0., z))

class FourC(Base):
    def func(self, dot):
        x, y, z = dot
        return (max(x, y), 0, z)
