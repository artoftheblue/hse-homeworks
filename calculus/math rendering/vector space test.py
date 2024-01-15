#manim -pqm "vector space test.py" transformation

from manim import *
from math import sin, cos, exp

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

class Seminar(Base):
    def func(self, dot):
        x, y, z = dot
        k = 0.1
        return (k * (x + y), k * (x ** 2 + y ** 2), k * z)

class Test(LinearTransformationScene, ThreeDScene):
    def construct(self, **kwargs):
        LinearTransformationScene.__init__(
                    self,
                    show_basis_vectors = False,
                    *kwargs
                    )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.apply_nonlinear_transformation(self.func)
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=-0.30)
        self.wait(10)
        self.stop_ambient_camera_rotation()

    def func(self, dot):
        x, y, z = dot
        if (y == z == 0):
            return (x, x ** 2, x ** 3)
        return (x, y, z)

class Lab(Base):
    def func(self, dot):
        x, y, z = dot
        return (x + sin(y), y + sin(x), z)

class another(Base):
    def func(self, dot):
        x, y, z = dot
        return (x + y, x * y, z)


class SizingAndSpacing(Scene):
    def construct(self):
        print(UR, LEFT)
        #func = lambda pos: (np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT)
        func = lambda pos: RIGHT * np.exp(pos[0]) + UP
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()
