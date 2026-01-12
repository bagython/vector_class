# implement a `class Vector` that has two attributes
# - x: double
# - y: double

# and add the following methods
# - getFromPolar(length: double, angle: double) -> Vector: returns a Vector with the given length and angle, it computes the x,y coordinates from the length and angle
# - length() -> double: returns the length
# - angle() -> double: computes the angle the vector forms with the X axis
# - dot(other: 'Vector') -> double: computes the dot product with `other`
# - __add__(other: 'Vector') -> Vector: add the two vectors
# - __mul__(scalar: double) -. Vector: multiply by scalar
# - __neg__() -> Vector: multiplies the vector by -1

# note: if it says double, it means float of double precision (in your programming language it might be just float)

# ADD TESTS!!!


from math import atan2, cos, degrees, pi, pow, sin, sqrt
from random import uniform
from typing import Self

import matplotlib.pyplot as plt
import pytest


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def getFromPolar(cls, length: float, angle: float) -> Self:
        """return a Vector with x,y coords matching given angle and length; alternative constructor for Vector"""
        x = length * cos(angle)
        y = length * sin(angle)
        return cls(x, y)

    def length(self) -> float:
        """return the length"""
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def angle(self) -> float:
        """compute the angle the vector forms with the X axis"""
        return degrees(atan2(self.y, self.x))  # atan2 considers signs (?)

    def dot(self, other_vector: "Vector") -> float:
        """compute the dot product with other_vector"""
        return (self.x * other_vector.x) + (self.y * other_vector.y)

    def __add__(self, other_vector: "Vector") -> "Vector":
        """add the two vectors"""
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __mul__(self, scalar: float) -> "Vector":
        """multiply by scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __neg__(self) -> "Vector":
        """multiply the vector by -1"""
        return self * -1


# dawg idk how to do python tests
# uv run pytest main.py
# me when im too lazy to make a folder?
class TestVector:
    @pytest.mark.parametrize(  # waow cool
        "length, radians, expected_x, expected_y",
        [
            (sqrt(2), -(pi / 4), 1.0, -1.0),
            (10, pi, -10.0, 0.0),
            (0, 0, 0.0, 0.0),
        ],
    )
    def test_getFromPolar(self, length, radians, expected_x, expected_y):
        v = Vector.getFromPolar(length, radians)
        assert v.x == pytest.approx(expected_x)
        assert v.y == pytest.approx(expected_y)

    @pytest.mark.parametrize(
        "x, y, expected_length",
        [
            (3, 4, 5.0),
            (-3, -4, 5.0),
            (0, 0, 0.0),
        ],
    )
    def test_length(self, x, y, expected_length):
        assert Vector(x, y).length() == pytest.approx(expected_length)

    @pytest.mark.parametrize(
        "x, y, expected_angle",
        [
            (1, 1, 45.0),
            (-1, 1, 135.0),
            (-1, -1, -135.0),
            (1, -1, -45.0),
            (0, 1, 90.0),
        ],
    )
    def test_angle(self, x, y, expected_angle):
        assert Vector(x, y).angle() == pytest.approx(expected_angle)

    def test_dot(self):
        v1 = Vector(3, 4)
        v2 = Vector(2, 1)
        assert v1.dot(v2) == 10
        assert Vector(1, 0).dot(Vector(0, 1)) == 0

    def test_neg(self):
        v1 = Vector(2, 4)
        v_neg = -v1
        assert (v_neg.x, v_neg.y) == (-2, -4)
        assert (v1.x, v1.y) == (2, 4)


def main():
    vecs = [Vector(uniform(-10, 10), uniform(-10, 10)) for _ in range(5)]
    plt.quiver(
        [0] * len(vecs),
        [0] * len(vecs),
        [v.x for v in vecs],
        [v.y for v in vecs],
        color="b",
        angles="xy",
        scale_units="xy",
        scale=1,
    )

    for v in vecs:
        txt = f"length: {v.length():.1f}, {v.angle():.0f} degrees"  # degrees from the x axis but like, it wont fit
        if v.x > 0:
            plt.text(v.x, v.y, txt, fontsize=8, ha="left", va="bottom")
        else:
            plt.text(v.x, v.y, txt, fontsize=8, ha="right", va="bottom")

    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.grid()
    plt.gca().set_aspect("equal")
    plt.show()
    # thanks internet


if __name__ == "__main__":
    main()
