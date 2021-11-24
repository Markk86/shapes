import sys
import os
from math import pi


class Circle:
    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius
        self.fill = fill
        self.stroke = stroke





    def calculate_area(self):
        return pi * self._radius ** 2

    @property
    def radius(self):  # Public access for_radius: read only
        return self._radius

    def __call__(self):
        return "I am a circle"


def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")
    print(f"area = {circle.area}")
    print(circle())
    circle2 = Circle(8.0)

    return 0


if __name__ == "__main__":
    sys.exit(main())
